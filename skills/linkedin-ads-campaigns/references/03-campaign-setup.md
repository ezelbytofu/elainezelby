# 03 - Campaign setup (Campaign Manager)

## Hierarchy

**Campaign** (folder / funnel stage) > **Ad set** (objective, audience, budget, bid,
format) > **Ad** (creative + copy). Most decisions live at the **ad set** level. Use the
**Classic** builder, not Accelerate/AI, for control.

(Legacy names: "campaign group" = today's Campaign; "campaign" = today's Ad set.)

## Objectives by stage

- **Engagement** - Stage 1 thought-leadership (optimizes for likes/comments/clicks that
  build retargeting audiences).
- **Lead generation** - Stage 2 native lead-gen forms.
- **Website visits** - Stage 3 conversion traffic (also the CPRM hack objective for video
  and document ads).
- **Video views** - charges per 2-sec view; only cheap with high completion.

Note: the definition of a "click" varies by objective and ad type, so do **not** compare
CTR across objectives blindly. A low CTR on one objective is not automatically bad.

## Targeting

### Two ad sets, always test both
1. **By job title** - type the exact titles (e.g. HR Director, VP of HR, Head of HR).
   Titles are a free-text field on profiles, and the ad manager only offers a fixed list,
   so unusual titles (e.g. "Director of People Operations") get missed.
2. **By job function AND seniority** (plus an optional qualifier like a skill/interest) -
   catches the people that title targeting misses.

**Use AND, not OR.** "Function = HR AND Seniority = Director" = HR directors. "Function =
HR OR Seniority = Director" = every director on the platform plus the HR intern who started
Tuesday. The classic account-killing mistake is an accidental OR blowing the audience into
the millions and wasting months of spend.

One will usually outperform the other. Test, do not guess. Do not run too many ad sets
though, or you spread spend too thin.

### Deriving the ICP with AI (do this before targeting)
1. Pull the LinkedIn profiles of leads who have **already closed** on this exact offer
   (real paying clients, not hoped-for buyers).
2. For each, record what LinkedIn shows: exact job title, company industry, company size,
   location. Dump into a sheet.
3. Feed it to Claude and ask "who is our ICP?" It returns the company sizes, titles,
   industries to target.
4. Apply the **Pareto (80/20) rule**: only target the majority segments that show up
   repeatedly. If 20 records are "construction" and 2 are "retail," go after construction
   and ignore the anomalies (test them later). Anomalies throw off campaigns.

### Matched audiences (ABM) and list enrichment
- You can upload a **company list** (ABM) or **contact list** and target it directly.
  Precise but small, which limits scale and can raise cost. Use as a precision tool, not
  the default.
- **Match rates are a black box and often low.** Raw B2B work emails match poorly because
  people signed up for LinkedIn with a personal/old email, not their work address. Tactics
  that raise match rate dramatically:
  - **Enrich** the list: link the B2B identifier (LinkedIn URL / work email) to personal
    identifiers (personal emails, address). This pushes match rates from ~40% to **90%+**.
    A real case went 40% to ~100%, letting the client spend 2x+ against the same audience
    with the same CTR/conversion, at a slightly **lower** CPC/CPM (bigger audience =
    cheaper distribution). Tools: Evaboot (clean a Sales Navigator rip), Clay (enrich /
    verify tech stack etc.), contact-data enrichment services.
  - **Cartesian product / explode records:** create many variations of one person (name
    variants, several email permutations from the base data, multiple locations) so
    something matches. More records of the same person beats one "perfect" record.
  - **Split the record:** upload one row with just name+title+company and another row with
    just email. Separate pieces often match better than a full combined row. Experiment
    heavily; there is no published matching logic.

### Audience size, geography
- **Size:** target 50k-500k (AJ Wilcox's sweet spot is 20k-100k). Millions = too broad or
  an OR error. A few thousand exhausts fast (early results, then it dies). Preview size in
  the ad set builder before launch.
- **Geography:** set to **permanent** location, not "recent." Costs vary a lot by region:
  US is most expensive; Australia and South Africa are the cheapest English-speaking
  markets; Western Europe is solid. Budget-limited + global? Start in a cheaper market.
- **Company size** now has granular buckets between 1k-5k (1k-2k, 2k-3k, etc.), but only
  as accurate as company-page admins declaring their size.
- **Device** targeting exists (iOS/Android/desktop/tablet). Desktop is ~20% of traffic and
  runs ~20-30% pricier.

## Settings to change from default (they exist to spend your money)

- **Audience expansion:** OFF, always. Shows ads outside your specified audience.
- **LinkedIn Audience Network (LAN):** OFF. Puts ads on third-party sites; inflates
  impressions/clicks with low-quality and bot traffic. **Exception:** for a small,
  high-value audience you can turn LAN ON with a **strict publisher allow-list** (e.g. WSJ,
  NYT only) to keep nurturing them off-platform at a controlled cost.
- Leaving either on produces fake-good stats (CTR ~3%, CPC ~$0.50) that never convert.

## Bidding

- **Manual CPC** beats Maximum Delivery >95% of the time. Max delivery is the most
  expensive way to buy attention and tends to overspend the daily budget by ~50%.
- **Ignore LinkedIn's recommended bid range** (it may suggest $20-80/click). Start around
  **$7 in North America** and adjust up or down from there.
- **Uncheck "enable bid adjustment for high-value clicks."** It lets LinkedIn bid up to 45%
  over your bid and routinely drives ~40% higher CPCs and daily overspend. On by default.
- **Remarketing:** bid **high**. Counterintuitively, low bids do not deliver on LinkedIn;
  you get poor placements and lower-quality segments. High bids get prioritized delivery,
  better placements, and often a lower cost per result.
- **Engagement campaigns when starting out:** automatic bidding usually wins; simple and
  effective. For static thought-leader ads specifically, bidding ~$1/engagement is a
  sensible starting point.
- **Ad rotation:** keep the default **Optimize for performance**. "Rotate ads evenly"
  enters weak ads into the auction evenly, so they lose impressions and win only at higher
  cost ("charge me more, show me less").

## Budget and pacing

- Minimum **$50/day per engagement campaign**; minimum **$3-5k/month** total.
- **Consolidate** budget: one high-budget campaign beats many low-budget ad sets.
- LinkedIn overspends daily budgets by ~50%/day and does not catch up. On manual bidding,
  if you are overspending, just **lower your bid** (bid just high enough to spend what you
  want, which is not the same as the daily budget).
- **Lifetime budget + end date** flip the campaign to "Completed" status, which needs
  manual restart, bad for evergreen monthly budgets.
- **Avoid campaign-group budget optimization** - it only works if every ad set shares one
  objective (rare). Deselect the group objective at creation to keep ad sets flexible.
- Pacing tool: **shape.io** can auto-pause at a monthly cap and auto-unpause next month,
  and auto-add new campaigns to the tracked budget. Best insurance against overspend.

## Multi-format ad set structure (per stage)

- Stage 1: one Campaign, two ad sets (job title / function+seniority), each with ~5 ad
  variations replicated across both.
- Stage 3: one Campaign, multiple ad sets by format (single image, video, message ads,
  text ads), consolidated spend.
