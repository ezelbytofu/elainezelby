# 05 - Benchmarks, tracking, and the optimization loop

## Benchmarks (baselines, not gospel; vary by offer, region, seniority)

| Metric | Benchmark | Notes |
|---|---|---|
| CPM (cost/1,000 impressions) | ~$30 global | Can exceed $100 on senior/enterprise/competitive audiences. Little control; driven by auction demand. When CPM rises, everything below it rises. |
| CPC | ~$4-5 avg | $10-20+ when CPMs are high. Fine if AOV is high enough. Manual bids often start ~$7 (NA). |
| Cost per lead | mostly $30-50 | Full range $15-300. Senior/enterprise = higher end; broad universal-pain audiences = lower. |
| Cost per acquisition (full cycle) | ~$3,000 +/- $1,500 | This is why AOV must be >=$5k. |
| CTR (website-visit / conversion campaigns) | avg 0.4%, aim **0.8%+** | Below 0.4% = creative or offer not resonating. Measured differently for brand/engagement campaigns, so do not compare across objectives. |
| Landing page conversion | 2-5% of traffic | |
| Lead-magnet lead to customer | 1-5% | |
| Qualified sales call to close | 20-30% | |
| Connection-request acceptance | ~66% no note / ~34% with note | |
| CPRM (video thought-leader ads) | **$0.50-$1** | See below. |

### CTR by ad format (Neil Patel / B2BHouse benchmarks)
- Sponsored content, single image: 0.56%
- Carousel: 0.40%
- Video: 0.44%
- Document ad: 0.43%
- Event ad: 0.55%
- Message ads: ~3% CTR, ~30% open rate
- Conversion rate (form/click, varies by definition): 5-15%

### The red-flag benchmark
Brand-new account with stats that are *too* good (CTR ~3%, CPC ~$0.50) almost always means
audience expansion or LAN was left on. Investigate before celebrating.

## Funnel-stage benchmarks and budget split (Impactable, enterprise-leaning)

These are higher than the averages above because they reflect **senior/enterprise audiences
on manual bidding at higher bids**. The ~$30 CPM / ~$4-5 CPC figures above reflect broader
audiences. Treat both as directional and learn your own baseline.

**Budget split: 60% TOFU / 25% MOFU / 15% BOFU.**

| Stage | CTR | CPC | CPM / CPL / SQL | Goal | Best formats |
|---|---|---|---|---|---|
| TOFU | 0.45-0.9% | $8-15 | CPM $50-90 | Build awareness + retargeting pools | POV video, thought-leader ads, founder content |
| MOFU | 0.5-0.8% | $10-18 | CPL $120-250 (lead gen + document ads); form-fill 8-18% | Educate, qualify, nurture intent | Document ads, webinar clips, case stories |
| BOFU | 0.7-1.2% | $12-22 | SQL cost $200-450 (with CRM/1P retargeting); demo-booking 3-6% | Convert qualified prospects to SQLs | Case studies with ROI, competitive comparisons, testimonials |

**Audience efficiency ladder (cheapest CPL to most expensive):**
1. Warm 1P (BOFU) - CRM lists, demo visitors: $75-150 CPL
2. Warm 1P (MOFU) - content engagers, site visitors: $120-250 CPL
3. Intent/Fit (ABM) - ICP + intent signals: $250-400 CPL
4. Very cold native - broad title/seniority: $300-600+ CPL

**Creative fatigue lifespan (refresh before this):**
- Single image: 4-5 weeks (monitor weekly; fatigue peaks 4-8 weeks)
- Carousel: 7 weeks
- Video: 9 weeks
- Document: 11 weeks
- Thought-leader ads: 12 weeks (last longest because they look organic)

**Scaling rules:**
- Do **not** scale TOFU budget until MOFU-to-SQL conversion is validated.
- Scale BOFU only when the 30/90-day retargeting pools are actively fed.
- When MOFU produces strong SQLs, shift 5-10% more budget to BOFU.

## CPRM and RMR: how to build and calculate

**CPRM (Cost Per Retargetable Member)** = spend / people who took the retargetable action.
It tells you the cheapest way to graduate someone to the next funnel stage. See `02` for
the format ranking (video thought-leader ads best; document-ads-on-website-visits cheapest).

Build the retargeting audiences: **Plan > Audiences**, then create:
- **Video** retargeting audience: pick the video ad sets, capture 50% (or 25%) viewers. Use
  a **180-day** window for max size (can shorten to 90/30).
- **Static / thought-leader / document**: create a single-image or document engagers
  audience from the relevant ad sets.

Calculate:
- **CPRM (video)** = cost / number of 50% (or 25%) video views.
- **CPRM (static/document)** = cost / engagements.
- Export Campaign Manager data to Excel and run it as a formula across ad sets/ads.

**RMR (Retargetable Member Rate)** = % of impressions that become a retargetable member:
- Video = the 50% video-view rate.
- Static / thought-leader / document = the engagement rate (Columns > Engagement, the
  engagement-rate column).
RMR measures how good the creative is at driving the action you want.

Note: the audience count may be slightly below the reported viewers/engagers because repeat
viewers are deduplicated. That is normal.

## The optimization loop (LinkedIn is human-optimized)

LinkedIn does **not** self-optimize like Meta. Launch, read data, adjust. Expect a stable
state around **month 3** (faster with more spend to accelerate the feedback cycle). Do not
expect it to work optimally on day one.

1. **Cut losing ads by CTR.** Turn off the weak ones; over time spend gets more efficient.
2. **Read professional demographics** (industry, job title, company size, geography). If a
   segment gets many impressions but low CTR, remove or exclude it. Repeat.
3. **Testing budget:** once you have a proven audience + landing page, allocate ~10% of
   budget to testing new creatives. Promote winners into the core campaigns.
4. **Feed data back** continuously. Efficiency compounds.

## Tracking and attribution

1. **Install the Insight Tag** (Signals Manager) on the site.
2. **Conversion tracking:** create Insight Tag conversions on **meaningful actions** (form
   submit, booking, download, thank-you page), **never a raw page view**. Select the
   conversion at the ad set level to see cost per conversion per ad set.
3. **UTM parameters:** set them in account settings > URL parameters so every lead's source
   (LinkedIn > campaign > ad set) is visible in your CRM.
4. **Tracking sheet:** put every lead + source into a sheet, track through the pipeline to
   close value. Compute cost per lead / call / show / close and the full CPA. A VA + simple
   spreadsheet as source of truth beats over-engineered dashboards.
5. **Monthly rollups:** leads, calls, shows, closes, revenue. Even when you cannot
   attribute a specific close, an up-and-to-the-right trend in line with your actions
   confirms the path.
6. **First-party + third-party:** LinkedIn's Revenue Attribution Report and Conversions API
   (CAPI) are first-party (CAPI reports ~31% more attributed conversions and ~20% lower
   cost-per-action, and removes cookie reliance). Best-in-class adds a third-party tool
   (Dreamdata, Factors, RevSure, HockeyStack) so you see cross-channel lift without
   over-crediting LinkedIn.

## The "don't turn off a winner" rule (the most expensive mistake)

Multiple operators independently killed campaigns on gut feeling that were later found to be
returning **10x**. The hard part of LinkedIn is not finding what works, it is **knowing** it
works so you keep doing it.

Decision rule: if you make **2x+** over your cost of acquisition, spend more. Average ROAS
is ~3x, 2x is still excellent and predictable, unicorns hit 10x. If a campaign is at all
profitable, do not turn it off. Keep tweaking audience and testing creatives and returns
tend to improve over time.

## A note on what actually moves the needle

The ads are never the biggest factor. **Offer, messaging, and the lead-to-client conversion
system** matter more. A great funnel feeding a weak offer or a broken follow-up process
still fails. See `06` for the conversion system.

## Platform watch (things that change)

LinkedIn ships changes constantly (device targeting, granular company size, dynamic lead-form
UTMs, video-viewer optimization for thought-leader ads, ad personalization with dynamic
name/company fields, dwell-time redefinition, the campaign-group-to-campaign rename). Auction
backend changes can also temporarily wreck manual-bid delivery (e.g. a Sept-Oct 2025 episode
forced 3-4x bids). When delivery suddenly breaks account-wide with no targeting change,
suspect a platform-side change before blaming the account.
