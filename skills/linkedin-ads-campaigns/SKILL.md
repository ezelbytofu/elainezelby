---
name: linkedin-ads-campaigns
description: >
  End-to-end playbook for planning, building, launching, optimizing, and scaling
  B2B LinkedIn Ads campaigns and lead-gen funnels. Use whenever a user wants to
  run a new LinkedIn campaign, design a LinkedIn ad funnel, fix or audit an
  existing account, choose objectives/targeting/bidding, write ad creative or
  thought-leadership content, set benchmarks, or build the retargeting +
  outreach system that turns cold audiences into booked calls. Trigger on
  phrases like "LinkedIn ads", "LinkedIn campaign", "LinkedIn funnel", "thought
  leader ads", "LinkedIn lead gen", "retargeting on LinkedIn", "should we run
  LinkedIn ads", or any B2B paid-social work aimed at decision-makers.
---

# LinkedIn Ads Campaigns (B2B, 2026)

A distilled, opinionated playbook for running LinkedIn Ads that actually book
meetings. Synthesized from practitioners who have spent $6M+ (agency growth
operators) and $200M+ (AJ Wilcox / B2Linked) on the platform, plus LinkedIn's
own startup thought-leadership research and Neil Patel's guide.

## Core thesis (read this first)

LinkedIn is a **distribution channel, not magic**. It scales an already-proven
offer to a known audience. It will not fix a broken offer, unproven product-market
fit, or the wrong ICP. Before spending a cent, run the qualification gate
(reference `01-qualification.md`). If the offer only sells warm (network and
referrals), LinkedIn will burn budget.

Four principles thread through everything:

1. **Nobody buys on the first touch.** Plan for the ~7-hour / multiple-touch trust
   curve. Never ask a cold audience for a sales call. Warm first, then convert.
2. **Ads that look like ads lose.** Organic-looking, pain-led, scrappy creative
   beats polished corporate creative, often by 3x. Speak at a grade-5 level.
3. **LinkedIn does not self-optimize like Meta.** It is human-optimized: launch,
   read the data, cut losers, feed winners. Expect a stable state around month 3.
4. **It is a pyramid, not a funnel.** Invest more per person as intent grows, and
   **intent-gate** the retargeting: do not push demo/trial offers to someone just
   because they clicked or watched. Wait for a real signal (a website / high-intent
   page visit). People click on anything. Details in `02-funnel-strategy.md`.

## The standard workflow (run a new campaign)

Do these in order. Each step links to a reference doc for depth.

1. **Qualify** the offer and ICP. Is LinkedIn even right? → `01-qualification.md`
2. **Design the funnel.** Pick the 2- or 3-stage structure, decide what warms and
   what converts, and how retargeting audiences get built. → `02-funnel-strategy.md`
3. **Set up campaigns** in Campaign Manager: objectives, ad sets, targeting,
   matched audiences, the default settings to kill, bidding, budget, pacing.
   → `03-campaign-setup.md`
4. **Build creative + messaging:** thought-leadership posts, ad style rules,
   verticalized social proof, content ratios, post structure.
   → `04-creative-messaging.md`
5. **Set benchmarks + tracking**, then run the iteration loop (CPRM/RMR, demographics,
   attribution, the "don't turn off a winner" rule). → `05-benchmarks-optimization.md`
6. **Convert leads** with the human layer: profile, DMs, message ads (not conversation
   ads), voice/Loom, post-call remarketing. → `06-outreach-conversion.md`

When a user asks for something narrower (just creative, just targeting, just
"why isn't this working"), jump straight to the relevant reference but sanity-check
against the qualification gate and the funnel logic first.

## Quick reference: settings to change from default

LinkedIn's defaults are tuned to spend your money, not perform. On every new ad set:

| Setting | Default | Do this instead |
|---|---|---|
| Audience expansion | ON | **Turn OFF** always |
| LinkedIn Audience Network (LAN) | ON | **Turn OFF** (exception: tiny high-value audiences with a strict publisher allow-list) |
| Geographic targeting | Recent or permanent | Set to **permanent** location |
| Bidding | Maximum delivery | **Manual CPC**, ignore LinkedIn's recommended bid range |
| Bid adjustment for high-value clicks | ON | **Uncheck** (it bids up to 45% over your bid) |
| Campaign group budget optimization | prompts an objective | Deselect the group objective; keep ad sets flexible |
| Ad rotation | Optimize for performance | **Keep default** (rotate evenly = "charge me more, show me less") |
| Conversion tracking | page views tempting | Track a **meaningful action** (form, booking, download), never a page view |

Suspiciously good stats on a brand-new account (CTR ~3%, CPC ~$0.50) almost always
mean audience expansion or LAN was left on. That is a red flag, not a win.

## Benchmarks at a glance (baselines, vary by offer/region/seniority)

- CPM: ~$30 global (can exceed $100 on senior/enterprise audiences)
- CPC: ~$4-5 avg (can be $10-20+ when CPMs are high); AJ Wilcox starts manual CPC bids ~$7 in North America
- Cost per lead: mostly $30-50 (full range $15-300)
- Cost per acquisition (full cycle): ~$3,000 +/- $1,500
- CTR (website-visit/conversion campaigns): avg 0.4%, **aim 0.8%+**
- Target audience size: 50k-500k (AJ Wilcox: 20k-100k is the sweet spot). Millions = too broad or an "OR" error. A few thousand = exhausts fast.
- Connection-request acceptance: ~66% with **no note** vs ~34% with a note
- CPRM (cost per retargetable member) on video thought-leader ads: **$0.50-$1** is the target
- Budget split across stages: **60% TOFU / 25% MOFU / 15% BOFU**

Full benchmark set, the CTR-by-format table, and enterprise-leaning per-stage benchmarks
(CPC $8-22, CPM $50-90, CPL $75-600 by audience warmth, creative fatigue windows) are in
`05-benchmarks-optimization.md`.

## Terminology note (2025 rename)

LinkedIn renamed the account hierarchy. This skill uses the **current** names:

- **Campaign** (was "campaign group") = the folder / funnel-stage organizer
- **Ad set** (was "campaign") = where objective, audience, budget, bid, and format live
- **Ad / creative** = what people see in the feed

Older tutorials and some LinkedIn UI may still say "campaign group" and "campaign."
When a user quotes old terminology, map it forward.

## Money math (the decision rule)

If you make **2x or more** over your cost of acquisition, spend more. Average ROAS
runs ~3x, unicorns hit 10x, and even 2x is excellent and predictable. Do **not** turn
off a profitable campaign on a gut feeling. The hardest part of LinkedIn is not finding
what works, it is knowing it works so you keep doing it. Track leads to closed revenue
in a simple sheet (a VA + spreadsheet beats over-engineered dashboards).

## Provenance / sources

Built from: the 6M-spend agency growth videos (funnel, creative, outreach, human
touch), AJ Wilcox / B2Linked "LinkedIn Ads Show" episodes (CPRM, message vs
conversation ads, bidding/pacing, list enrichment, best practices), LinkedIn's
founder-led thought-leadership research (Ruby James), Neil Patel's LinkedIn Ads
guide, the SpeedworkSocial "pyramid" full-funnel strategy (intent-gating, persona
segmentation, demand-gen vs demand-capture, matching funnel length to sales cycle),
and Impactable's funnel benchmarks (per-stage CTR/CPC/CPM/CPL/SQL, budget split,
audience efficiency ladder, creative fatigue windows). Where sources disagree (e.g.
audience-size range, image dimensions, CPC/CPM by audience warmth), both figures are
noted in the reference docs.
