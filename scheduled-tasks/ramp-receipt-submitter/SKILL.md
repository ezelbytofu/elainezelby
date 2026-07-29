---
name: ramp-receipt-submitter
description: >
  Daily job that finds open Ramp receipt requests in Gmail, locates the matching
  vendor receipt, submits it to receipts@ramp.com as a verified attachment, and
  archives the thread only after Ramp confirms the match. Use when the user wants
  to automate expense receipt submission, stop manually chasing "transaction needs
  a receipt" emails, or asks about Ramp receipt matching, expense automation, or
  monitoring an inbox for receipt requests.
---

# Ramp Receipt Submitter

A daily scheduled task. It finds open Ramp receipt requests, tracks down the matching
receipt, submits it, and confirms the match before calling anything done.

## Setup

Fill these in before first run:

| Placeholder | What to put there |
| --- | --- |
| `<YOUR_EMAIL>` | The Gmail account that receives Ramp receipt requests |
| `<AD_ACCOUNT_ID>` | Only if you expense LinkedIn Ads. See step 2. |
| `<INBOX_KEY>` | Your Gmail `ik` value. See step 3c for how to read it. |

Requires a Gmail connector with draft-creation and search, plus browser tools for the
vendor portals that do not email invoices.

## 1. Find open receipt requests

Use the Gmail connector. Search:

```
from:communications@ramp.com subject:receipt newer_than:14d
```

Look for subjects like `<Merchant> $<amount> transaction needs a receipt` or
`...needs a memo and receipt`. Note the merchant, amount, and transaction date from each.

Skip any request already handled. A request is handled if there is a message in
`in:sent to:receipts@ramp.com` referencing that invoice or amount, or a Ramp reply saying
"Receipt matched!" or "Receipt automatically matched via the Gmail Integration". Also search:

```
in:sent to:receipts@ramp.com newer_than:30d
```

## 2. Find the matching receipt

First search Gmail for a vendor receipt email matching the merchant, amount, and date.

Some vendors never email an invoice and require pulling it from their portal. LinkedIn Ads
is the common case:

- Go to `https://www.linkedin.com/campaignmanager/accounts`
- Open `https://www.linkedin.com/campaignmanager/accounts/<AD_ACCOUNT_ID>/billing`, then
  click the **Payment activity** tab.
- Find the row whose date and total amount match the Ramp request exactly. Click the
  download icon in that row. The PDF lands in `~/Downloads/<invoiceNumber>.pdf`.
- LinkedIn only exposes receipts issued within a limited recent window here. Older invoices
  have to come from accounting.

**Gotcha:** if a mail-client browser extension (Superhuman and similar) is installed, opening
`mail.google.com` can show a client chooser page. If a screenshot or JS call fails with
`Cannot access a chrome-extension:// URL of different extension`, screenshot the page and
click through to Gmail.

Verify the PDF genuinely matches on both amount and transaction date before using it. Read it
with PDF tools or text extraction. Do not trust the filename.

## 3. Send it to Ramp

The Gmail connector's `create_draft` supports attachments but there is no send tool, and the
browser's `file_upload` is sandboxed. So use this exact flow.

### a) Shrink the invoice to a small 1-bit PNG

A raw vendor PDF around 90KB is too large to base64-encode reliably. Convert it:

```python
import fitz, io
from PIL import Image
import numpy as np

d = fitz.open(SRC_PDF); p = d[0]
pm = p.get_pixmap(dpi=100, colorspace=fitz.csGRAY)
im = Image.open(io.BytesIO(pm.tobytes('png'))).convert('L')
a = np.array(im); rows = (a < 200).any(axis=1)
keep = []; run = 0
for i, r in enumerate(rows):
    if r:
        run = 0; keep.append(i)
    else:
        run += 1
        if run <= 12: keep.append(i)
a2 = a[keep, :]
cols = (a2 < 200).any(axis=0); idx = np.where(cols)[0]
a2 = a2[:, max(0, idx[0] - 10):min(a2.shape[1], idx[-1] + 10)]
Image.fromarray(a2).point(lambda x: 0 if x < 150 else 255).convert('1').save(OUT_PNG, optimize=True)
```

That collapses runs of blank rows and trims horizontal whitespace, yielding roughly 6-7KB.
Read the PNG back and confirm it is legible before continuing.

### b) Create the draft

```bash
base64 -i OUT_PNG | tr -d '\n'
```

Create a Gmail draft to `receipts@ramp.com` with that as an attachment (mimeType `image/png`).
The body should state the charge amount and date, a Memo line describing the spend, and the
invoice number, transaction ID, and payment method.

### c) Verify the attachment. Do not skip this.

Transcribing roughly 9000 base64 characters fails often, around two attempts in three, and
produces a **silently corrupt image**. The draft looks fine; the attachment is garbage.

The returned draft id is also the permmsgid. Download the stored attachment through the browser:

```
https://mail.google.com/mail/u/0?ui=2&ik=<INBOX_KEY>&attid=0.1&permmsgid=msg-a:<draftId>&view=att&zw&disp=attd
```

To find `<INBOX_KEY>`: open any Gmail message with an attachment and read the `ik=` parameter
off the attachment download link via `read_page`. It is stable per mailbox.

It saves to `~/Downloads/<filename>`. Compare `shasum -a256` against the local PNG.

- **Mismatch:** delete that draft and redo step (b). Repeat until the hashes match.
- Never send an unverified attachment.

### d) Send

Once the hashes match, open the draft in Gmail and click Send. Confirm with:

```
in:sent to:receipts@ramp.com newer_than:1d
```

## 4. Confirm the match, then archive

**Sending is not success.** This is the definition of done.

Ramp replies within a couple of minutes. Wait for it, then check:

```
from:communications@ramp.com newer_than:1d
```

- **Success** is a reply whose body says "Receipt matched!", for example
  "We added a receipt to 1 transaction $<amount> at <Merchant>". Only then is that receipt done.
- When you see it, archive the thread. The Gmail connector cannot change labels (it returns a
  permissions error), so archive through the Gmail web UI: search `in:inbox <invoiceNumber>`,
  tick the row checkbox, click Archive, and confirm the "Conversation archived." toast.
- If Ramp replies "Couldn't match your receipt", leave the thread in the inbox and flag it.
- If no reply has arrived after a few minutes, say so rather than claiming success.

Also archive the original `<Merchant> $<amount> transaction needs a receipt` request once its
receipt is confirmed matched.

## 5. Report

Summarize: which requests were found, which were submitted (with amounts and invoice numbers),
which came back confirmed and were archived, which were already handled, and which could not be
matched and why. Clean up failed drafts and any temp files downloaded for verification.

## Installing as a daily task

Copy into `~/.claude/scheduled-tasks/` and schedule it. A 9am daily cron (`0 9 * * *`) works
well, since Ramp sends requests overnight.
