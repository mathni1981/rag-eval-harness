# Eval set review: first 50 questions

Drafted by Claude; every question needs Mahesh's review before it counts. For each one, check:
the question is unambiguous, the gold answer is correct and complete, and the evidence actually supports it.
Fix anything in `questions.jsonl` (use `tools.find_quote` for new evidence), then tick the box.

Evidence is shown abbreviated; the full quote and offsets are in `questions.jsonl`.

## q001 · single_fact · easy · narrative

- [ ] **Q:** What percentage of T. Rowe Price's total managed assets sat in its target date retirement products at the close of 2025?
- **Gold:** 31.6% ($561.4 billion), up from 29.6% at the end of 2024.
- **Key points:** 31.6%; $561.4 billion
- **Evidence** `TROW_FY2025_10K` Item 1 [13627:13829]: The assets under management in our target date retirement products totaled $561.4 billion at December 31, 2025, or 31.6% of our managed assets at December 31, 2025, compared to 29.6% at the end of 2024.

## q002 · single_fact · easy · table

- [ ] **Q:** What was T. Rowe Price's net operating income for 2025?
- **Gold:** $2,188.8 million, down from $2,333.3 million in 2024.
- **Key points:** $2,188.8 million
- **Evidence** `TROW_FY2025_10K` Item 7 [145051:145113]: Net operating income | $ | 2,188.8 | $ | 2,333.3 | $ | 1,986.2

## q003 · single_fact · medium · narrative

- [ ] **Q:** What growth range does T. Rowe Price expect for its 2026 non-GAAP operating expenses, and from what 2025 base?
- **Gold:** 3% to 6% growth from the 2025 amount of $4,608.0 million, excluding non-GAAP accrued carried interest compensation.
- **Key points:** 3% to 6%; $4,608.0 million base; excludes accrued carried interest compensation
- **Evidence** `TROW_FY2025_10K` Item 7 [149725:149916]: We currently estimate our 2026 non-GAAP operating expenses, excluding non-GAAP accrued carried interest compensation, will grow in the range of 3%-6% from the 2025 amount of $4,608.0 million.

## q004 · single_fact · easy · narrative

- [ ] **Q:** How large was BlackRock's iShares business at the end of 2025, and how much new money did its ETFs attract during the year?
- **Gold:** $5.5 trillion of iShares ETF AUM at December 31, 2025, with ETF net inflows of $527 billion in 2025.
- **Key points:** $5.5 trillion iShares ETF AUM; $527 billion ETF net inflows
- **Evidence** `BLK_FY2025_10K` Item 1 [26974:27148]: BlackRock is the leading ETF provider in the world with $5.5 trillion of iShares ETF AUM as of December 31, 2025. BlackRock generated ETF net inflows of $527 billion in 2025.

## q005 · single_fact · easy · narrative

- [ ] **Q:** How much revenue did BlackRock's technology and subscription offerings generate in 2025, and how fast did it grow?
- **Gold:** $2.0 billion, up 24% year over year.
- **Key points:** $2.0 billion; 24% growth
- **Evidence** `BLK_FY2025_10K` Item 1 [57752:57839]: Technology services and subscription revenue of $2.0 billion was up 24% year-over-year.

## q006 · single_fact · easy · table

- [ ] **Q:** What was BlackRock's GAAP operating margin in 2025, and what was it the prior year?
- **Gold:** 29.1% in 2025, compared with 37.1% in 2024.
- **Key points:** 29.1%; 37.1% in 2024
- **Evidence** `BLK_FY2025_10K` Item 1 [12913:12984]: Operating margin | 29.1 | % | 37.1 | % | 35.1 | % | 35.7 | % | 38.5 | %

## q007 · single_fact · easy · narrative

- [ ] **Q:** On its adjusted (non-GAAP) basis, how much did MetLife earn for common shareholders in 2025?
- **Gold:** $5.9 billion, up from $5.8 billion in 2024.
- **Key points:** $5.9 billion
- **Evidence** `MET_FY2025_10K` Item 7 [266145:266311]: Adjusted earnings available to common shareholders was $5.9 billion, $5.8 billion and $5.5 billion for the years ended December 31, 2025, 2024 and 2023, respectively.

## q008 · single_fact · easy · table

- [ ] **Q:** In MetLife's consolidated results, what was GAAP net income available to common shareholders for 2025, in millions?
- **Gold:** $3,173 million, down from $4,226 million in 2024.
- **Key points:** $3,173 million
- **Evidence** `MET_FY2025_10K` Item 7 [267923:268025]: Net income (loss) available to MetLife, Inc.’s common shareholders | $ | 3,173 | $ | 4,226 | $ | 1,380

## q009 · single_fact · easy · narrative

- [ ] **Q:** Which four areas does MetLife's New Frontier strategy prioritize for growth?
- **Gold:** Extending leadership in Group Benefits; capitalizing on its retirement platform; accelerating growth in asset management; and expanding in high-growth international markets.
- **Key points:** Group Benefits; retirement platform; asset management; high-growth international markets
- **Evidence** `MET_FY2025_10K` Item 1 [14331:14517]: • Extend our leadership in Group Benefits; • Capitalize on our unique retirement platform; • Accelerate our growth in asset management; and • Expand in high growth international markets.

## q010 · single_fact · easy · narrative

- [ ] **Q:** How much capital did Lincoln raise from Bain Capital's minority investment in 2025, and how many shares did it issue?
- **Gold:** About $825 million for approximately 18.8 million common shares.
- **Key points:** $825 million; about 18.8 million shares
- **Evidence** `LNC_FY2025_10K` Item 7 [239220:239354]: Under the final terms, Lincoln sold approximately 18.8 million shares of its common stock for aggregate consideration of $825 million.

## q011 · single_fact · easy · table

- [ ] **Q:** What cash dividend per common share did Lincoln declare in 2025?
- **Gold:** $1.80 per share, the same as in 2024 and 2023.
- **Key points:** $1.80
- **Evidence** `LNC_FY2025_10K` Item 8 [477229:477302]: Cash Dividends Declared Per Common Share | $ | 1.80 | $ | 1.80 | $ | 1.80

## q012 · single_fact · easy · narrative

- [ ] **Q:** Where are Lincoln National's principal executive offices, and in which state was the company organized?
- **Gold:** Radnor, Pennsylvania; organized under Indiana law in 1968.
- **Key points:** Radnor, Pennsylvania; Indiana
- **Evidence** `LNC_FY2025_10K` Item 1 [8466:8610]: LNC was organized under the laws of the state of Indiana in 1968. We currently maintain our principal executive offices in Radnor, Pennsylvania.

## q013 · single_fact · easy · narrative

- [ ] **Q:** How much in client assets did Principal administer at the end of 2025, and how much of that did it manage?
- **Gold:** $1,814.6 billion in assets under administration, including $781.0 billion in assets under management.
- **Key points:** $1,814.6 billion AUA; $781.0 billion AUM
- **Evidence** `PFG_FY2025_10K` Item 1 [8225:8373]: We had $1,814.6 billion in assets under administration (“AUA”), including $781.0 billion in assets under management (“AUM”) as of December 31, 2025.

## q014 · single_fact · medium · narrative

- [ ] **Q:** What buyback did Principal's board approve in February 2025, and does it expire?
- **Gold:** Up to $1.5 billion of common stock, with no expiration date, in addition to the $696.5 million remaining under the 2024 authorization.
- **Key points:** $1.5 billion; no expiration date; in addition to $696.5 million remaining
- **Evidence** `PFG_FY2025_10K` Item 5 [163649:163918]: In February 2025, our Board authorized a share repurchase program of up to $1.5 billion of our outstanding common stock, which has no expiration date, and is in addition to the $696.5 million that remained under the t...

## q015 · single_fact · easy · narrative

- [ ] **Q:** How many of Principal's employees worked outside the United States at year-end 2025?
- **Gold:** About 8,100, out of roughly 19,700 employees globally (about 11,600 in the U.S.).
- **Key points:** about 8,100
- **Evidence** `PFG_FY2025_10K` Item 1 [65757:65947]: As of December 31, 2025, we employed approximately 19,700 people across the globe, including approximately 11,600 employees who work in the U.S. and 8,100 employees who work outside the U.S.

## q016 · single_fact · easy · narrative

- [ ] **Q:** When did Franklin Resources start using the corporate name Franklin Templeton, Inc.?
- **Gold:** Effective August 17, 2026.
- **Key points:** August 17, 2026
- **Evidence** `BEN_FY2026_10K` Item 1 [10190:10290]: We changed our corporate name to Franklin Templeton, Inc. effective August 17, 2026 (“Name Change”).

## q017 · single_fact · easy · table

- [ ] **Q:** What were Franklin's total operating revenues for fiscal year 2026?
- **Gold:** $9,415.3 million, up 7% from $8,770.7 million in fiscal 2025.
- **Key points:** $9,415.3 million
- **Evidence** `BEN_FY2026_10K` Item 7 [173721:173803]: Total Operating Revenues | $ | 9,415.3 | $ | 8,770.7 | $ | 8,478.0 | 7 | % | 3 | %

## q018 · single_fact · easy · narrative

- [ ] **Q:** What effective fee rate, excluding performance fees, did Franklin earn in fiscal 2026?
- **Gold:** 40.7 basis points, versus 40.5 basis points in fiscal 2025.
- **Key points:** 40.7 basis points
- **Evidence** `BEN_FY2026_10K` Item 7 [174457:174670]: Our effective investment management fee rate excluding performance fees (investment management fees excluding performance fees divided by average AUM) was 40.7 and 40.5 basis points for fiscal years 2026 and 2025.

## q019 · multi_passage · medium · narrative

- [ ] **Q:** T. Rowe Price's AUM grew in 2025 even though clients withdrew money. What explains the growth, and which strategies and client types drove the withdrawals?
- **Gold:** AUM rose $169.0 billion to $1,775.6 billion because $216.7 billion of market appreciation outweighed $56.9 billion of net cash outflows. Outflows came mainly from growth-oriented equity strategies, chiefly from financial intermediaries and institutional clients; fixed income, target date and alternatives saw inflows.
- **Key points:** market appreciation of $216.7 billion; net outflows of $56.9 billion; growth-oriented equity strategies; financial intermediaries and institutional clients
- **Evidence** `TROW_FY2025_10K` Item 1 [11581:11884]: At December 31, 2025, we had $1,775.6 billion in assets under management, an increase of $169.0 billion from the end of 2024. This increase in assets under management was driven by market appreciation, net of distribu...
- **Evidence** `TROW_FY2025_10K` Item 7 [135958:136281]: Our net cash outflows in 2025 were driven primarily by growth-oriented equity strategies. These outflows were partially offset by net cash inflows in fixed income, target date retirement products, and alternatives str...

## q020 · multi_passage · medium · narrative

- [ ] **Q:** T. Rowe Price ended 2025 with fewer people than a year earlier. How did its headcount and its GAAP operating expenses each change, and what pushed expenses up?
- **Gold:** Headcount fell 4.7% to 7,773 from 8,158, while GAAP operating expenses rose 7.7% to $5,126.0 million, driven mainly by a restructuring charge plus higher technology and facility, compensation, and distribution and servicing costs.
- **Key points:** 7,773 employees, down 4.7%; operating expenses up 7.7% to $5,126.0 million; restructuring charge; technology and facility costs
- **Evidence** `TROW_FY2025_10K` Item 1 [34592:34720]: As of December 31, 2025, we employed 7,773 associates, a decrease of 4.7% from the 8,158 associates employed at the end of 2024.
- **Evidence** `TROW_FY2025_10K` Item 7 [148921:149399]: Operating expenses on a U.S. GAAP basis were $5,126.0 million in 2025, an increase of 7.7% compared to $4,760.3 million in 2024. On a non-GAAP basis, operating expenses were $4,666.5 million, an increase of 3.7% compa...

## q021 · multi_passage · hard · narrative

- [ ] **Q:** What did BlackRock donate in December 2025, what did it cost, and how did it factor into the year's decline in GAAP operating income?
- **Gold:** BlackRock contributed part of its stake in Circle Internet Group to the BlackRock Charitable Fund, creating a $109 million operating expense (offset by a $29 million tax benefit). This noncash contribution, along with noncash acquisition-related expenses, drove the $529 million decline in GAAP operating income to $7.0 billion.
- **Key points:** part of its Circle stake; $109 million expense; $29 million tax benefit; contributed to the $529 million operating income decline
- **Evidence** `BLK_FY2025_10K` Item 7 [253610:253949]: On December 10, 2025, BlackRock contributed a portion of its stake in Circle Internet Group, Inc. ("Circle") to the BlackRock Charitable Fund, which BlackRock established in 2013 (the “Charitable Contribution”). The C...
- **Evidence** `BLK_FY2025_10K` Item 7 [271851:272354]: Operating income of $7.0 billion decreased $529 million and operating margin of 29.1% decreased 800 bps from 2024. Operating income and operating margin reflected higher revenue, driven by organic base fee growth, pos...

## q022 · multi_passage · hard · mixed

- [ ] **Q:** How did BlackRock pay for HPS Investment Partners, and how many of those instruments were outstanding at year-end 2025 compared with its common shares?
- **Gold:** Substantially all consideration was paid in Class B-2 common units of BlackRock Saturn Subco (Subco Units). At December 31, 2025 there were 7.7 million Subco Units outstanding versus 155.1 million common shares.
- **Key points:** Subco Units (Class B-2 common units); 7.7 million Subco Units; 155.1 million common shares
- **Evidence** `BLK_FY2025_10K` Item 1 [6567:6927]: On July 1, 2025, BlackRock completed the acquisition of 100% of the business and assets of HPS Investment Partners (the "HPS Transaction" or "HPS"), a leading global credit investment manager, with substantially all c...
- **Evidence** `BLK_FY2025_10K` Item 7 [271568:271681]: As of December 31, 2025, there were 155.1 million shares of common stock and 7.7 million Subco Units outstanding.

## q023 · multi_passage · medium · narrative

- [ ] **Q:** How did MetLife's 2025 reorganization change its segment reporting, and what changed in how MIM is paid for managing the general account?
- **Gold:** MetLife Investment Management (MIM) became a reportable segment (previously in Corporate & Other) and MetLife Holdings was removed as a segment, moving mostly into Corporate & Other. Effective January 1, 2025, agreements between MIM and other MetLife entities were amended so MIM manages general account investments at current market rate fees.
- **Key points:** MIM became a reportable segment; MetLife Holdings removed; market rate fees for general account; effective January 1, 2025
- **Evidence** `MET_FY2025_10K` Item 1 [14741:15034]: MetLife Investment Management, the Company’s institutional asset management business (“MIM”), which was previously reported in Corporate & Other, became a reportable segment. MetLife Holdings was removed as a reportab...
- **Evidence** `MET_FY2025_10K` Item 7 [265256:265498]: In conjunction with the Strategic Reorganization, effective January 1, 2025, the Company amended agreements between MIM and other MetLife entities to manage general account investments at current market rate fees, a c...

## q024 · multi_passage · medium · narrative

- [ ] **Q:** Why did MetLife buy PineBridge Investments, and how much cash did it pay at closing?
- **Gold:** To accelerate growth in asset management under New Frontier by adding scale and broadening global products and distribution. Preliminary cash consideration at closing on December 30, 2025 was $885 million ($800 million purchase price plus $85 million for excess cash and investments over liabilities).
- **Key points:** accelerate asset management growth / scale; $885 million at closing; $800 million plus $85 million
- **Evidence** `MET_FY2025_10K` Item 1 [31761:32073]: On December 30, 2025, MIM completed the acquisition of PineBridge Investments (“PineBridge”), a global asset manager. This acquisition supports MetLife’s New Frontier strategy to accelerate growth in asset management ...
- **Evidence** `MET_FY2025_10K` Item 8 [619333:619556]: The preliminary purchase consideration paid in cash at closing was $885 million, comprised of purchase consideration of $800 million plus $85 million for the excess of cash and investments acquired over liabilities as...

## q025 · multi_passage · hard · narrative

- [ ] **Q:** What minimum RBC ratio does one of LLANY's reinsurance arrangements require, and how does that compare with the RBC range that triggers the regulator's company action level?
- **Gold:** One arrangement requires LLANY to keep an RBC ratio of at least 185% (or an S&P capital adequacy ratio of 115%). The company action level applies when the RBC ratio is between 75% and 100%, so the contractual minimum is well above that regulatory trigger.
- **Key points:** at least 185%; company action level is 75%-100%; requirement is well above the regulatory trigger
- **Evidence** `LNC_FY2025_10K` Item 7 [395349:395478]: One of these arrangements also requires LLANY to maintain an RBC ratio of at least 185% or an S&P capital adequacy ratio of 115%.
- **Evidence** `LNC_FY2025_10K` Item 1 [80800:80974]: •“Company action level” – If the RBC ratio is between 75% and 100%, then the insurer must submit a plan to the regulator detailing corrective action it proposes to undertake;

## q026 · multi_passage · medium · narrative

- [ ] **Q:** Who does Lincoln's top information security executive report to, how often do they brief the board's Audit Committee, and how large is their team?
- **Gold:** The CISO reports directly to the Chief Information Officer (a Senior Management Committee member) and indirectly to the Audit Committee, briefing it twice a year (biannually). The CISO has a staff of more than 100 employees.
- **Key points:** reports to the CIO; briefs Audit Committee biannually; more than 100 staff
- **Evidence** `LNC_FY2025_10K` Item 1C [214415:214871]: The CISO reports directly to the Company’s Chief Information Officer (“CIO”), who is a member of the Company’s Senior Management Committee. As a result, all information security personnel report into the CISO, and ult...
- **Evidence** `LNC_FY2025_10K` Item 1C [215384:215550]: The CISO has a staff of more than 100 employees dedicated to protecting the data and systems belonging to the Company, our customers, business partners and consumers.

## q027 · multi_passage · medium · narrative

- [ ] **Q:** Why does Principal Financial Group's capacity to return capital hinge on Principal Life, and how much could Principal Life pay out in 2026 without asking the Iowa regulator?
- **Gold:** As a holding company, PFG's ability to pay dividends, repurchase shares and meet obligations depends on dividends and distributions from Principal Life, which Iowa law limits. Based on 2025 statutory results, Principal Life could pay about $1,234.0 million in ordinary dividends in 2026 without prior approval.
- **Key points:** depends on distributions from Principal Life; Iowa limits; about $1,234.0 million in 2026
- **Evidence** `PFG_FY2025_10K` Item 1A [115211:115449]: Our ability to pay dividends to our stockholders, make share repurchases and meet our obligations, including paying operating expenses and any debt service, depends upon the receipt of dividends or other distributions...
- **Evidence** `PFG_FY2025_10K` Item 8 [736521:736706]: Based on this limitation and 2025 statutory results, Principal Life could pay approximately $1,234.0 million in ordinary stockholder dividends in 2026 without prior regulatory approval.

## q028 · multi_passage · medium · mixed

- [ ] **Q:** How much did Principal's bottom line (attributable to the company) shrink in 2025, and what were the two biggest causes?
- **Gold:** It fell $385.9 million, from $1,571.0 million to $1,185.1 million. The biggest causes were a $654.5 million hit from the change in fair value of the funds withheld embedded derivative and $119.7 million of asset write-downs from exiting sponsor and trustee roles for Hong Kong MPF schemes.
- **Key points:** down $385.9 million to $1,185.1 million; $654.5 million funds withheld embedded derivative; $119.7 million Hong Kong MPF write-downs
- **Evidence** `PFG_FY2025_10K` Item 7 [203953:204059]: Net income attributable to Principal Financial Group, Inc. | | $ | 1,185.1 | | $ | 1,571.0 | | $ | (385.9)
- **Evidence** `PFG_FY2025_10K` Item 7 [204192:204578]: The most significant items that contributed to the decrease in net income attributable to Principal Financial Group, Inc. were a $654.5 million decrease due to the change in fair value of the funds withheld embedded d...

## q029 · multi_passage · hard · narrative

- [ ] **Q:** What drove Franklin's rise in general and administrative expenses in fiscal 2026, and how is the largest driver treated in its adjusted operating income?
- **Gold:** G&A rose $147.7 million, mainly from a $100.0 million regulatory settlement, plus a $33.2 million increase in contingent consideration fair value and $21.5 million in higher fund-related expenses. Charges for significant regulatory settlements are excluded from adjusted operating income.
- **Key points:** G&A up $147.7 million; $100.0 million regulatory settlement; excluded from adjusted operating income
- **Evidence** `BEN_FY2026_10K` Item 7 [186509:186853]: General, administrative and other operating expenses increased $147.7 million in fiscal year 2026, primarily due to a $100.0 million regulatory settlement, an increase of $33.2 million in the fair value of a contingen...
- **Evidence** `BEN_FY2026_10K` Item 7 [194590:194672]: •Charges related to significant regulatory settlements. Adjusted Operating Margin

## q030 · multi_passage · medium · narrative

- [ ] **Q:** Which firm did Franklin acquire at the start of fiscal 2026, and what part did it play in the change in investment management fees that year?
- **Gold:** Apera Asset Management, a pan-European private credit firm, acquired October 1, 2025. Investment management fees rose $497.1 million, driven by higher average equity, multi-asset and alternative AUM and the Apera acquisition, partly offset by lower performance fees and WAM outflows.
- **Key points:** Apera Asset Management; October 1, 2025; fees up $497.1 million; Apera contributed to the increase
- **Evidence** `BEN_FY2026_10K` Item 7 [159267:159368]: On October 1, 2025, we acquired Apera Asset Management (“Apera”), a pan-European private credit firm.
- **Evidence** `BEN_FY2026_10K` Item 7 [174191:174455]: Investment management fees increased $497.1 million in fiscal year 2026 primarily due to an increase in average equity, multi-asset and alternative AUM and the acquisition of Apera, partially offset by a decrease in p...

## q031 · comparison · easy · narrative

- [ ] **Q:** Which has the larger workforce, MetLife or Principal, and by roughly how many people?
- **Gold:** MetLife, with about 46,000 employees versus about 19,700 at Principal (both at December 31, 2025): roughly 26,300 more.
- **Key points:** MetLife ~46,000; Principal ~19,700; MetLife larger by ~26,300
- **Evidence** `MET_FY2025_10K` Item 1 [106357:106417]: At December 31, 2025, we had approximately 46,000 employees.
- **Evidence** `PFG_FY2025_10K` Item 1 [65757:65838]: As of December 31, 2025, we employed approximately 19,700 people across the globe

## q032 · comparison · easy · narrative

- [ ] **Q:** How does BlackRock's headcount compare with T. Rowe Price's at the end of 2025?
- **Gold:** BlackRock had about 24,900 employees versus T. Rowe Price's 7,773, a little over three times as many.
- **Key points:** BlackRock ~24,900; T. Rowe Price 7,773; about 3x
- **Evidence** `BLK_FY2025_10K` Item 1 [6301:6419]: With approximately 24,900 employees in more than 30 countries who serve clients in over 100 countries across the globe
- **Evidence** `TROW_FY2025_10K` Item 1 [34592:34645]: As of December 31, 2025, we employed 7,773 associates

## q033 · comparison · hard · narrative

- [ ] **Q:** Which manages more assets according to their latest annual reports, Franklin Templeton or T. Rowe Price?
- **Gold:** Franklin reports about $1.8 trillion (as of September 30, 2026) versus T. Rowe Price's $1,775.6 billion (as of December 31, 2025). The figures are close and measured at different dates, so the difference isn't meaningful; Franklin's is marginally higher as reported.
- **Key points:** Franklin ~$1.8 trillion at Sept 30, 2026; T. Rowe Price $1,775.6 billion at Dec 31, 2025; different dates; roughly comparable
- **Evidence** `BEN_FY2026_10K` Item 1 [11224:11368]: We are a global investment management organization with approximately $1.8 trillion in assets under management (“AUM”) as of September 30, 2026.
- **Evidence** `TROW_FY2025_10K` Item 1 [11581:11653]: At December 31, 2025, we had $1,775.6 billion in assets under management
- **Notes:** Fiscal periods differ (Franklin's year ends September 30). A good answer flags this.

## q034 · comparison · medium · narrative

- [ ] **Q:** At the end of 2025, how did Principal's assets under management compare with T. Rowe Price's?
- **Gold:** T. Rowe Price managed $1,775.6 billion versus Principal's $781.0 billion, more than twice as much (Principal's $1,814.6 billion is assets under administration, not management).
- **Key points:** T. Rowe Price $1,775.6 billion; Principal AUM $781.0 billion; T. Rowe Price more than double; don't confuse Principal's AUA with AUM
- **Evidence** `PFG_FY2025_10K` Item 1 [8225:8373]: We had $1,814.6 billion in assets under administration (“AUA”), including $781.0 billion in assets under management (“AUM”) as of December 31, 2025.
- **Evidence** `TROW_FY2025_10K` Item 1 [11581:11653]: At December 31, 2025, we had $1,775.6 billion in assets under management
- **Notes:** Trap: Principal's AUA ($1,814.6B) exceeds T. Rowe Price's AUM; the right comparison uses Principal's AUM.

## q035 · comparison · medium · table

- [ ] **Q:** Which earned more GAAP net income for common shareholders in 2025, MetLife or Lincoln, and did each improve or decline from 2024?
- **Gold:** MetLife: $3,173 million (down from $4,226 million). Lincoln: $1,086 million (down from $3,184 million). MetLife earned more; both declined.
- **Key points:** MetLife $3,173 million; Lincoln $1,086 million; both declined from 2024
- **Evidence** `MET_FY2025_10K` Item 7 [267923:268025]: Net income (loss) available to MetLife, Inc.’s common shareholders | $ | 3,173 | $ | 4,226 | $ | 1,380
- **Evidence** `LNC_FY2025_10K` Item 8 [477027:477115]: Net income (loss) available to common stockholders | $ | 1,086 | $ | 3,184 | $ | ( 834 )

## q036 · comparison · easy · narrative

- [ ] **Q:** How many reportable business segments do MetLife and Principal each have, and which has more?
- **Gold:** MetLife has six (Group Benefits; RIS; Asia; Latin America; EMEA; MIM); Principal has three (Retirement and Income Solutions; Principal Asset Management; Benefits and Protection). MetLife has more.
- **Key points:** MetLife six; Principal three; MetLife has more
- **Evidence** `MET_FY2025_10K` Item 1 [15502:15696]: As a result of the Strategic Reorganization, MetLife is organized into the following six segments: Group Benefits; RIS; Asia; Latin America; Europe, the Middle East and Africa (“EMEA”); and MIM.
- **Evidence** `PFG_FY2025_10K` Item 1 [9647:9817]: We organize our businesses into the following reportable segments: ● | Retirement and Income Solutions; ● | Principal Asset Management and ● | Benefits and Protection.

## q037 · comparison · easy · narrative

- [ ] **Q:** Which employs more people according to its latest 10-K, Lincoln or Franklin Templeton?
- **Gold:** Franklin Templeton, with about 9,900 employees (September 30, 2026), versus Lincoln's 9,423 (December 31, 2025). The dates differ.
- **Key points:** Franklin ~9,900; Lincoln 9,423; different dates
- **Evidence** `LNC_FY2025_10K` Item 1 [108755:108814]: As of December 31, 2025, we had a total of 9,423 employees.
- **Evidence** `BEN_FY2026_10K` Item 1 [76430:76497]: As of September 30, 2026, we employed approximately 9,900 employees

## q038 · comparison · medium · narrative

- [ ] **Q:** Whose chief information security officer has more experience, BlackRock's or Lincoln's?
- **Gold:** BlackRock's: over 31 years in information technology, including 25 years focused on information security, versus Lincoln's CISO with over 20 years in cybersecurity.
- **Key points:** BlackRock 31+ years (25 in security); Lincoln 20+ years; BlackRock more
- **Evidence** `BLK_FY2025_10K` Item 1C [238895:239039]: As of December 31, 2025, the CISO had over 31 years of experience in information technology with a 25-year concentration in information security
- **Evidence** `LNC_FY2025_10K` Item 1C [215228:215306]: Our current CISO has over 20 years of experience in the field of cybersecurity

## q039 · comparison · hard · mixed

- [ ] **Q:** Whose revenue grew faster in 2025, BlackRock's or T. Rowe Price's?
- **Gold:** BlackRock's: total revenue rose from $20,407 million to $24,216 million (about 18.7%), versus T. Rowe Price's net revenues up 3.1% to $7,314.8 million.
- **Key points:** BlackRock ~18.7% ($20,407M to $24,216M); T. Rowe Price 3.1%; BlackRock faster
- **Evidence** `BLK_FY2025_10K` Item 1 [12757:12835]: Total revenue | $ | 24,216 | $ | 20,407 | $ | 17,859 | $ | 17,873 | $ | 19,374
- **Evidence** `TROW_FY2025_10K` Item 7 [147456:147559]: Total net revenues were $7,314.8 million in 2025, a 3.1% increase compared to $7,093.6 million in 2024.
- **Notes:** Requires computing BlackRock's growth from the table.

## q040 · comparison · medium · narrative

- [ ] **Q:** In their latest fiscal years, did the effective fee rates (excluding performance fees) at Franklin and T. Rowe Price move in the same direction?
- **Gold:** No. Franklin's rose slightly, from 40.5 to 40.7 basis points (fiscal 2026 vs 2025). T. Rowe Price's average effective fee rate for 2025 declined from 2024, as flows shifted assets toward lower-fee strategies.
- **Key points:** Franklin up 40.5 to 40.7 bps; T. Rowe Price declined; opposite directions
- **Evidence** `BEN_FY2026_10K` Item 7 [174457:174670]: Our effective investment management fee rate excluding performance fees (investment management fees excluding performance fees divided by average AUM) was 40.7 and 40.5 basis points for fiscal years 2026 and 2025.
- **Evidence** `TROW_FY2025_10K` Item 7 [148396:148632]: The average annualized effective fee rate earned for 2025 declined from 2024 primarily due to client flows and transfers shifting assets under management toward lower-fee strategies and products, partially offset by m...
- **Notes:** Fiscal periods differ (Franklin FY ends September 30).

## q041 · unanswerable · medium

- [ ] **Q:** How much total compensation did BlackRock pay its CEO for 2025?
- **Gold:** This information is not in the documents. BlackRock's 10-K doesn't disclose CEO compensation; Item 11 incorporates it by reference from the proxy statement.
- **Key points:** States that the documents don't contain this information; Does not guess or invent a figure
- **Notes:** BlackRock's 10-K doesn't disclose CEO compensation; Item 11 incorporates it by reference from the proxy statement.

## q042 · unanswerable · medium

- [ ] **Q:** What were Franklin Templeton's assets under management on December 31, 2025?
- **Gold:** This information is not in the documents. Franklin's 10-K reports AUM at its September 30 fiscal year ends, not at December 31, 2025.
- **Key points:** States that the documents don't contain this information; Does not guess or invent a figure
- **Notes:** Franklin's 10-K reports AUM at its September 30 fiscal year ends, not at December 31, 2025.

## q043 · unanswerable · medium

- [ ] **Q:** How many of MetLife's employees work in Japan?
- **Gold:** This information is not in the documents. MetLife gives a total headcount (about 46,000) but no breakdown by country.
- **Key points:** States that the documents don't contain this information; Does not guess or invent a figure
- **Notes:** MetLife gives a total headcount (about 46,000) but no breakdown by country.

## q044 · unanswerable · medium

- [ ] **Q:** What was Principal Life's risk-based capital (RBC) ratio at the end of 2025?
- **Gold:** This information is not in the documents. The 10-K discusses RBC requirements but doesn't state Principal Life's RBC ratio.
- **Key points:** States that the documents don't contain this information; Does not guess or invent a figure
- **Notes:** The 10-K discusses RBC requirements but doesn't state Principal Life's RBC ratio.

## q045 · unanswerable · medium

- [ ] **Q:** How much stock does Lincoln plan to repurchase in 2026?
- **Gold:** This information is not in the documents. Lincoln discloses $714 million of remaining repurchase authorization at year-end 2025 with no expiration, but no planned 2026 repurchase amount; timing and amount depend on capital ratios and other factors.
- **Key points:** States that the documents don't contain this information; Does not guess or invent a figure
- **Notes:** Lincoln discloses $714 million of remaining repurchase authorization at year-end 2025 with no expiration, but no planned 2026 repurchase amount; timing and amount depend on capital ratios and other factors.

## q046 · unanswerable · medium

- [ ] **Q:** How many of Principal's employees are based in Brazil?
- **Gold:** This information is not in the documents. Principal splits headcount only into U.S. (~11,600) and non-U.S. (~8,100); no country breakdown.
- **Key points:** States that the documents don't contain this information; Does not guess or invent a figure
- **Notes:** Principal splits headcount only into U.S. (~11,600) and non-U.S. (~8,100); no country breakdown.

## q047 · unanswerable · medium

- [ ] **Q:** What were T. Rowe Price's ETF assets under management at the end of 2025?
- **Gold:** This information is not in the documents. T. Rowe Price mentions its ETFs but doesn't report ETF AUM separately.
- **Key points:** States that the documents don't contain this information; Does not guess or invent a figure
- **Notes:** T. Rowe Price mentions its ETFs but doesn't report ETF AUM separately.

## q048 · unanswerable · medium

- [ ] **Q:** How many clients use BlackRock's Aladdin platform?
- **Gold:** This information is not in the documents. BlackRock reports Aladdin revenue and ACV growth but no client count.
- **Key points:** States that the documents don't contain this information; Does not guess or invent a figure
- **Notes:** BlackRock reports Aladdin revenue and ACV growth but no client count.

## q049 · unanswerable · medium

- [ ] **Q:** What was MetLife's net income available to common shareholders in 2021?
- **Gold:** This information is not in the documents. MetLife's 10-K presents results for 2023 through 2025 only.
- **Key points:** States that the documents don't contain this information; Does not guess or invent a figure
- **Notes:** MetLife's 10-K presents results for 2023 through 2025 only.

## q050 · unanswerable · medium

- [ ] **Q:** What is the name of Lincoln's Chief Information Security Officer?
- **Gold:** This information is not in the documents. Lincoln describes the CISO's experience and reporting line but doesn't name the person.
- **Key points:** States that the documents don't contain this information; Does not guess or invent a figure
- **Notes:** Lincoln describes the CISO's experience and reporting line but doesn't name the person.
