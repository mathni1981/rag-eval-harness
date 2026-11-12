# Held-out set review: h001–h050

Drafted by Claude; review every question before the held-out run. Once `baseline` or `final` has
been run on this set, it's frozen (see docs/preregistration.md). For each question, check that it's
unambiguous, the gold answer is correct and complete, and the evidence supports it. Fix anything
in `heldout.jsonl` (use `tools.find_quote` for new evidence), then tick the box.

## h001 · single_fact · medium · table

- [ ] **Q:** Per BlackRock's market risk disclosure, how much would its equity-price-sensitive investments lose in a 10% market decline at year-end 2025?
- **Gold:** $108 million, on a net exposure of $1,084 million (versus $190 million on $1,899 million a year earlier).
- **Key points:** $108 million; net exposure $1,084 million
- **Evidence** `BLK_FY2025_10K` Item 7A [398383:398438]: Investments | $ | 1,084 | $ | 108 | $ | 1,899 | $ | 190

## h002 · single_fact · easy · narrative

- [ ] **Q:** What quarterly dividend did BlackRock's board approve in January 2026, and when will it be paid?
- **Gold:** $5.73 per share, payable March 24, 2026, to holders of record at the close of business on March 6, 2026.
- **Key points:** $5.73 per share; paid March 24, 2026
- **Evidence** `BLK_FY2025_10K` Item 5 [241642:241842]: On January 15, 2026, the Board of Directors approved BlackRock’s quarterly dividend of $5.73 per share to be paid on March 24, 2026 to stockholders of record at the close of business on March 6, 2026.

## h003 · single_fact · medium · narrative

- [ ] **Q:** In which cities does BlackRock say a large share of its key operations is located?
- **Gold:** Atlanta, Belgrade, Budapest, Edinburgh, Gurgaon, London, Mumbai, New York and San Francisco.
- **Key points:** Atlanta; Belgrade; Budapest; Edinburgh; Gurgaon; London; Mumbai; New York; San Francisco
- **Evidence** `BLK_FY2025_10K` Item 1A [142919:143154]: Moreover, a significant portion of BlackRock’s critical business operations is concentrated in a limited number of geographic areas, including Atlanta, Belgrade, Budapest, Edinburgh, Gurgaon, London, Mumbai, New York ...

## h004 · single_fact · easy · narrative

- [ ] **Q:** Where is T. Rowe Price's current headquarters, how large is it, and when did the firm move there?
- **Gold:** In the Harbor Point area of Baltimore, Maryland, in about 550,000 square feet of leased space; the firm moved there in early 2025.
- **Key points:** Harbor Point, Baltimore; about 550,000 square feet, leased; moved in early 2025
- **Evidence** `TROW_FY2025_10K` Item 2 [117524:117709]: Our new corporate headquarters, which we moved to in early 2025, is located in the Harbor Point area of Baltimore, Maryland, in approximately 550,000 square feet of leased office space.

## h005 · single_fact · easy · table

- [ ] **Q:** How many shares did T. Rowe Price buy back in the fourth quarter of 2025, and at what average price?
- **Gold:** 1,366,531 shares at an average price of $103.06.
- **Key points:** 1,366,531 shares; $103.06 average
- **Evidence** `TROW_FY2025_10K` Item 5 [123245:123287]: Total | 1,366,531 | $ | 103.06 | 1,366,531

## h006 · single_fact · easy · narrative

- [ ] **Q:** What does T. Rowe Price expect to spend on capital expenditures in 2026, and on what mainly?
- **Gold:** About $270 million, including internal labor capitalization, with more than three-quarters planned for technology initiatives.
- **Key points:** about $270 million; more than three-quarters for technology
- **Evidence** `TROW_FY2025_10K` Item 7 [190246:190484]: We anticipate property, equipment, software and other capital expenditures, including internal labor capitalization, for the full-year 2026 to be about $270 million, of which more than three-quarters is planned for te...

## h007 · single_fact · medium · narrative

- [ ] **Q:** If Franklin's average AUM had been 10% higher or lower in fiscal 2026, how much would operating revenues have changed?
- **Gold:** About $838.4 million, assuming effective fee rates and asset mix stayed the same (excluding performance fees and asset-based distribution fees).
- **Key points:** $838.4 million
- **Evidence** `BEN_FY2026_10K` Item 7A [239279:239425]: Such a change for the fiscal year ended September 30, 2026 would have resulted in an increase or decrease in operating revenues of $838.4 million.

## h008 · single_fact · medium · narrative

- [ ] **Q:** What was Franklin's effective income tax rate in fiscal 2026, and why did it drop?
- **Gold:** 21.0%, down from 30.2% in fiscal 2025, mainly due to lower foreign earnings, higher net income attributable to noncontrolling interests, and the release of a valuation allowance on capital losses.
- **Key points:** 21.0%; down from 30.2%; lower foreign earnings
- **Evidence** `BEN_FY2026_10K` Item 7 [191392:191726]: Our effective income tax rate for fiscal year 2026 was 21.0% as compared to 30.2% in fiscal year 2025. The rate decrease in fiscal year 2026 was primarily due to a reduction in foreign earnings, an increase in net inc...

## h009 · single_fact · easy · narrative

- [ ] **Q:** How many stockholders of record did Franklin have at the end of October 2026?
- **Gold:** 2,132 stockholders of record at October 31, 2026.
- **Key points:** 2,132
- **Evidence** `BEN_FY2026_10K` Item 5 [154004:154085]: At October 31, 2026, there were 2,132 stockholders of record of our common stock.

## h010 · single_fact · easy · narrative

- [ ] **Q:** How many holders of record did MetLife's common stock have in February 2026?
- **Gold:** 69,355 stockholders of record at February 12, 2026.
- **Key points:** 69,355
- **Evidence** `MET_FY2025_10K` Item 5 [198542:198625]: At February 12, 2026, there were 69,355 stockholders of record of our common stock.

## h011 · single_fact · easy · narrative

- [ ] **Q:** Since when has MetLife's stock been listed on the NYSE?
- **Gold:** Since April 5, 2000, under the symbol MET.
- **Key points:** April 5, 2000
- **Evidence** `MET_FY2025_10K` Item 5 [198398:198540]: MetLife, Inc.’s common stock, par value $0.01 per share, began trading on the New York Stock Exchange under the symbol “MET” on April 5, 2000.

## h012 · single_fact · medium · narrative

- [ ] **Q:** What was MetLife's 2025 effective tax rate, and how did it compare with the statutory rate?
- **Gold:** 27%, versus the 21% U.S. statutory rate, mainly due to tax charges from foreign earnings taxed at higher rates (and foreign losses at lower rates), prior-year tax adjustments and non-deductible losses.
- **Key points:** 27%; statutory rate 21%; foreign earnings taxed at higher rates
- **Evidence** `MET_FY2025_10K` Item 7 [271641:271793]: •2025 effective tax rate on income before provision for income tax was 27% compared to the U.S. statutory rate of 21% primarily due to tax charges from:

## h013 · single_fact · medium · narrative

- [ ] **Q:** Which reinsurers does Lincoln identify as its largest reinsurance exposures?
- **Gold:** Fortitude Re, Protective Life Insurance Company, Security Life of Denver (Resolution Life), Commonwealth Annuity and Life (Global Atlantic), Hannover Life Reassurance Company of America (Bermuda), and Athene Holding.
- **Key points:** Fortitude Re; Protective Life; Security Life of Denver; Commonwealth Annuity; Hannover; Athene
- **Evidence** `LNC_FY2025_10K` Item 1 [58512:58888]: Fortitude Reinsurance Company Ltd. (“Fortitude Re”), Protective Life Insurance Company, Security Life of Denver Insurance Company (a subsidiary of Resolution Life), Commonwealth Annuity and Life Insurance Company (a s...

## h014 · single_fact · easy · narrative

- [ ] **Q:** How many shareholders of record did Lincoln have in February 2026?
- **Gold:** 4,732 as of February 12, 2026.
- **Key points:** 4,732
- **Evidence** `LNC_FY2025_10K` Item 5 [220146:220238]: As of February 12, 2026, the number of shareholders of record of our common stock was 4,732.

## h015 · single_fact · medium · narrative

- [ ] **Q:** How strong was Lincoln's consolidated risk-based capital position at the end of 2025?
- **Gold:** The consolidated RBC ratio of LNC's statutory insurance companies was more than four times the company action level.
- **Key points:** more than four times the company action level
- **Evidence** `LNC_FY2025_10K` Item 8 [839529:839693]: As of December 31, 2025, the consolidated RBC ratio for LNC’s statutory insurance companies was in excess of four times the aforementioned company action level RBC.

## h016 · single_fact · easy · narrative

- [ ] **Q:** On which exchange does Principal's stock trade, and when did it move there?
- **Gold:** The Nasdaq Global Select Market, since December 15, 2017; it originally listed on the NYSE on October 23, 2001.
- **Key points:** Nasdaq; December 15, 2017
- **Evidence** `PFG_FY2025_10K` Item 5 [161053:161184]: Effective December 15, 2017, we changed our listing to the Nasdaq Global Select Market and continue trading under the symbol “PFG”.

## h017 · single_fact · easy · narrative

- [ ] **Q:** Where is Principal headquartered, and does it own or lease that property?
- **Gold:** Des Moines, Iowa; Principal owns its world headquarters complex (and leases other offices in the U.S. and abroad).
- **Key points:** Des Moines, Iowa; owned
- **Evidence** `PFG_FY2025_10K` Item 2 [155053:155238]: As of December 31, 2025, we owned properties at our world headquarters complex in Des Moines, Iowa, and leased space for various offices located throughout the U.S. and internationally.

## h018 · single_fact · medium · narrative

- [ ] **Q:** What developments in Mexico and Chile does Principal flag as risks for its international business?
- **Gold:** In Mexico, recent judicial and regulatory reforms may create uncertainty about the rule of law; in Chile, the government is starting to reform the pension system, including a proposed contribution increase and changes to pension fund administration.
- **Key points:** Mexico: judicial and regulatory reforms, rule-of-law uncertainty; Chile: pension system reform
- **Evidence** `PFG_FY2025_10K` Item 1A [134207:134522]: For example, recent judicial and regulatory reforms in Mexico may create uncertainty for investors regarding the rule of law. The Chilean government is taking its first steps to reform the country’s pension system, wh...

## h019 · multi_passage · hard · narrative

- [ ] **Q:** How large was BlackRock's seed capital hedge at year-end 2025 compared with its net economic stake in its own corporate investments?
- **Gold:** Futures in the seed capital hedging program had about $1.7 billion of notional value, against $4.9 billion of economic exposure to the investment portfolio (excluding hedged seed investments and certain other items).
- **Key points:** about $1.7 billion notional; $4.9 billion economic exposure
- **Evidence** `BLK_FY2025_10K` Item 7A [396864:397068]: The Company had outstanding futures related to its seed capital hedging program with an aggregate notional value of approximately $1.7 billion and $1.8 billion at December 31, 2025 and 2024, respectively.
- **Evidence** `BLK_FY2025_10K` Item 7A [397545:397684]: the Company’s economic exposure to its investment portfolio at December 31, 2025 and 2024 were $4.9 billion and $3.9 billion, respectively.

## h020 · multi_passage · medium · mixed

- [ ] **Q:** How has BlackRock's quarterly dividend changed from 2024 through its January 2026 declaration?
- **Gold:** $5.10 per quarter in 2024, $5.21 in 2025, and $5.73 declared in January 2026, roughly a 10% increase over 2025.
- **Key points:** $5.10 in 2024; $5.21 in 2025; $5.73 in January 2026
- **Evidence** `BLK_FY2025_10K` Item 5 [241330:241466]: 2025 First Quarter | $ | 5.21 Second Quarter | $ | 5.21 Third Quarter | $ | 5.21 Fourth Quarter | $ | 5.21 2024 First Quarter | $ | 5.10
- **Evidence** `BLK_FY2025_10K` Item 5 [241642:241744]: On January 15, 2026, the Board of Directors approved BlackRock’s quarterly dividend of $5.73 per share

## h021 · multi_passage · medium · mixed

- [ ] **Q:** How far above the federal statutory rate was T. Rowe Price's 2025 effective tax rate, and what lowered it from 2024?
- **Gold:** 23.2% versus the 21.0% statutory rate (about 2.2 points higher). It fell from 24.3% in 2024 mainly because of lower state taxes from prior-period settlements.
- **Key points:** 23.2% effective; 21.0% statutory; lower state taxes from prior-period settlements
- **Evidence** `TROW_FY2025_10K` Item 7 [172329:172400]: Statutory U.S. federal income tax rate | 21.0 | % | 21.0 | % | 21.0 | %
- **Evidence** `TROW_FY2025_10K` Item 7 [173083:173309]: Our effective tax rate for 2025 was 23.2%, compared to 24.3% for 2024 and 26.3% for 2023. The decrease in our effective tax rate in 2025 from 2024 was primarily due to lower state taxes resulting from prior period set...

## h022 · multi_passage · hard · narrative

- [ ] **Q:** How does T. Rowe Price manage and measure the market risk on its seed capital investments?
- **Gold:** It doesn't actively hedge seed capital market risk. It measures potential loss using the lower of each investment's lowest 2025 net asset value per share or its year-end NAV, reduced by 10%, before tax benefits.
- **Key points:** does not actively hedge; lower of lowest 2025 NAV or year-end NAV, reduced by 10%
- **Evidence** `TROW_FY2025_10K` Item 7A [221801:221882]: We do not actively hedge the market risk related to our seed capital investments.
- **Evidence** `TROW_FY2025_10K` Item 7A [222276:222556]: The potential future loss of value, before any income tax benefits, of these investments at December 31, 2025 was determined by using the lower of each investment's lowest net asset value per share during 2025 or its ...

## h023 · multi_passage · hard · mixed

- [ ] **Q:** Roughly what share of Franklin's fiscal 2026 operating revenues would swing with a 10% change in average AUM?
- **Gold:** About 9%: a 10% AUM change moves operating revenues by $838.4 million, against total operating revenues of $9,415.3 million.
- **Key points:** $838.4 million; $9,415.3 million total; about 9%
- **Evidence** `BEN_FY2026_10K` Item 7A [239279:239425]: Such a change for the fiscal year ended September 30, 2026 would have resulted in an increase or decrease in operating revenues of $838.4 million.
- **Evidence** `BEN_FY2026_10K` Item 7 [173721:173803]: Total Operating Revenues | $ | 9,415.3 | $ | 8,770.7 | $ | 8,478.0 | 7 | % | 3 | %
- **Notes:** Reuses the total-revenue table row also used by dev question q017.

## h024 · multi_passage · medium · mixed

- [ ] **Q:** How many shares did Franklin repurchase in the last quarter of fiscal 2026, and how much room is left under its buyback program?
- **Gold:** 2,521,966 shares in July–September 2026, leaving 23,047,084 shares available. The program has no expiration date; the board added 20.8 million shares in December 2025, bringing the total available then to 40.0 million.
- **Key points:** 2,521,966 shares; 23,047,084 remaining; 20.8 million added December 2025
- **Evidence** `BEN_FY2026_10K` Item 5 [154592:154675]: September 2026 | 30,447 | 32.41 | 30,447 | 23,047,084 Total | 2,521,966 | 2,521,966
- **Evidence** `BEN_FY2026_10K` Item 5 [155182:155490]: In December 2025, our Board of Directors authorized the repurchase of up to an additional 20.8 million shares of our common stock in either open market or private transactions, for a total of up to 40.0 million shares...

## h025 · multi_passage · medium · mixed

- [ ] **Q:** How many shares did MetLife repurchase in the fourth quarter of 2025, and how much authorization remained at year-end?
- **Gold:** 5,443,831 shares (none in December); $2.1 billion of authorization remained at December 31, 2025, after a $3.0 billion authorization announced in April 2025.
- **Key points:** 5,443,831 shares; none in December; $2.1 billion remaining
- **Evidence** `MET_FY2025_10K` Item 5 [199417:199506]: December 1 - December 31, 2025 | — | — | — | $2,072,488,851 Total | 5,443,831 | 5,443,831
- **Evidence** `MET_FY2025_10K` Item 5 [199696:199945]: In April 2025, MetLife, Inc. announced that its Board of Directors authorized an additional $3.0 billion of common stock repurchases. At December 31, 2025, MetLife, Inc. had $2.1 billion of common stock repurchases re...

## h026 · multi_passage · hard · narrative

- [ ] **Q:** What interest-rate shocks does MetLife's scenario analysis assume, and which holdings drive its interest rate exposure?
- **Gold:** Immediate 50 basis point declines or rises in U.S. rates from January 1, 2026 through 2028. Exposure comes mainly from fixed maturity securities AFS, mortgage loans, derivatives and interest-rate-sensitive liabilities.
- **Key points:** 50 basis points up or down; from January 1, 2026 through 2028; fixed maturity securities, mortgage loans, derivatives, liabilities
- **Evidence** `MET_FY2025_10K` Item 7 [216350:216480]: The Rising Interest Rate Scenario assumes U.S. interest rates rise immediately on January 1, 2026 by 50 basis points through 2028.
- **Evidence** `MET_FY2025_10K` Item 7A [459899:460089]: Our exposure to interest rate changes results most significantly from our holdings of fixed maturity securities AFS, mortgage loans, derivatives, and our interest rate sensitive liabilities.

## h027 · multi_passage · medium · narrative

- [ ] **Q:** How can both falling and rising interest rates hurt Lincoln?
- **Gold:** Falling or persistently low rates can reduce investment returns, make policy liabilities insufficient (requiring reserve strengthening) and make statutory asset adequacy tests harder to pass. Rising or persistently high rates can hurt profitability, capital and portfolio values, and increase contract withdrawals and surrenders.
- **Key points:** falling rates: reserves may need strengthening; rising rates: more withdrawals and surrenders
- **Evidence** `LNC_FY2025_10K` Item 1A [120706:120938]: During periods of sustained lower interest rates, our recorded policy liabilities may not be sufficient to meet future policy obligations and may need to be strengthened, thereby reducing net income in the affected re...
- **Evidence** `LNC_FY2025_10K` Item 1A [121618:121851]: Increases in interest rates and sustained higher interest rates may negatively affect our profitability, capital position and the value of our investment portfolio and may also result in increased contract withdrawals...

## h028 · multi_passage · medium · mixed

- [ ] **Q:** Did Lincoln buy back stock in the fourth quarter of 2025, and what repurchase authorization does it have?
- **Gold:** No shares were repurchased in the quarter. The authorization (raised to $1.5 billion total in November 2021) had $714 million remaining at year-end 2025, with no expiration date.
- **Key points:** no repurchases in Q4 2025; $714 million remaining; no expiration
- **Evidence** `LNC_FY2025_10K` Item 5 [221911:221947]: 12/1/25 – 12/31/25 | – | – | – | 714
- **Evidence** `LNC_FY2025_10K` Item 5 [222212:222557]: On November 10, 2021, our Board of Directors authorized an increase in our securities repurchase authorization, bringing the total aggregate repurchase authorization to $1.5 billion. As of December 31, 2025, our remai...

## h029 · multi_passage · hard · narrative

- [ ] **Q:** According to Principal, what would a 100 basis point drop in interest rates do to its operating earnings and to other comprehensive income?
- **Gold:** An immediate, parallel 100 bp drop in U.S. rates would change segment pre-tax operating earnings by between (1)% and 1% over twelve months. A 100 bp decrease in upper-medium grade yields would reduce OCI by about $2.4 billion, net of taxes.
- **Key points:** operating earnings: between (1)% and 1%; OCI: about $2.4 billion reduction
- **Evidence** `PFG_FY2025_10K` Item 7A [311564:311755]: We estimate a hypothetical 100 basis point immediate, parallel decrease in U.S. interest rates would impact segment pre-tax operating earnings between (1)% and 1% over the next twelve months.
- **Evidence** `PFG_FY2025_10K` Item 7 [187937:188129]: If the current upper-medium grade yields decrease 100 basis points, the reduction in OCI would be approximately $2.4 billion, net of income taxes, based on December 31, 2025, reported amounts.

## h030 · multi_passage · medium · narrative

- [ ] **Q:** How does Principal describe its foreign currency risk, and which specific countries does it flag for political or regulatory risk?
- **Gold:** It faces currency risk from international operations and local-currency investments, hedged or managed to specific risk tolerances; it flags Mexico (judicial and regulatory reforms) and Chile (pension reform).
- **Key points:** currency risk from international operations and local-currency investments; hedged or managed to risk tolerances; Mexico and Chile
- **Evidence** `PFG_FY2025_10K` Item 1A [93908:93999]: We face foreign currency risk from international operations and local currency investments.
- **Evidence** `PFG_FY2025_10K` Item 1A [134207:134332]: For example, recent judicial and regulatory reforms in Mexico may create uncertainty for investors regarding the rule of law.

## h031 · comparison · easy · narrative

- [ ] **Q:** Which had more stockholders of record in February 2026, Principal or MetLife?
- **Gold:** Principal, with 186,047 (February 11, 2026) versus MetLife's 69,355 (February 12, 2026).
- **Key points:** Principal 186,047; MetLife 69,355; Principal more
- **Evidence** `PFG_FY2025_10K` Item 5 [161185:161269]: On February 11, 2026, there were 186,047 stockholders of record of our common stock.
- **Evidence** `MET_FY2025_10K` Item 5 [198542:198625]: At February 12, 2026, there were 69,355 stockholders of record of our common stock.

## h032 · comparison · medium · mixed

- [ ] **Q:** In the fourth quarter of 2025, how did MetLife's share repurchases compare with Lincoln's?
- **Gold:** MetLife repurchased 5,443,831 shares; Lincoln repurchased none.
- **Key points:** MetLife 5,443,831; Lincoln none
- **Evidence** `MET_FY2025_10K` Item 5 [199417:199506]: December 1 - December 31, 2025 | — | — | — | $2,072,488,851 Total | 5,443,831 | 5,443,831
- **Evidence** `LNC_FY2025_10K` Item 5 [222086:222206]: For the quarter ended December 31, 2025, there were no shares purchased as part of publicly announced plans or programs.

## h033 · comparison · hard · table

- [ ] **Q:** Which raised its quarterly dividend by a larger percentage from 2024 to 2025, BlackRock or T. Rowe Price?
- **Gold:** T. Rowe Price, slightly: $1.24 to $1.27 (about 2.4%) versus BlackRock's $5.10 to $5.21 (about 2.2%).
- **Key points:** T. Rowe Price +2.4% ($1.24→$1.27); BlackRock +2.2% ($5.10→$5.21); T. Rowe Price larger
- **Evidence** `BLK_FY2025_10K` Item 5 [241330:241466]: 2025 First Quarter | $ | 5.21 Second Quarter | $ | 5.21 Third Quarter | $ | 5.21 Fourth Quarter | $ | 5.21 2024 First Quarter | $ | 5.10
- **Evidence** `TROW_FY2025_10K` Item 5 [122464:122561]: 2025 | $ | 1.27 | $ | 1.27 | $ | 1.27 | $ | 1.27 2024 | $ | 1.24 | $ | 1.24 | $ | 1.24 | $ | 1.24
- **Notes:** Requires computing two percentage changes.

## h034 · comparison · medium · narrative

- [ ] **Q:** Do BlackRock and T. Rowe Price hedge the market risk on their seed capital investments?
- **Gold:** BlackRock does, using futures with about $1.7 billion of notional value at year-end 2025; T. Rowe Price does not actively hedge it.
- **Key points:** BlackRock hedges with futures (~$1.7B notional); T. Rowe Price does not actively hedge
- **Evidence** `BLK_FY2025_10K` Item 7A [396864:397068]: The Company had outstanding futures related to its seed capital hedging program with an aggregate notional value of approximately $1.7 billion and $1.8 billion at December 31, 2025 and 2024, respectively.
- **Evidence** `TROW_FY2025_10K` Item 7A [221801:221882]: We do not actively hedge the market risk related to our seed capital investments.

## h035 · comparison · medium · narrative

- [ ] **Q:** Which had the lower effective tax rate in its latest fiscal year, T. Rowe Price or Franklin, and did each rise or fall?
- **Gold:** Franklin: 21.0% for fiscal 2026 (down from 30.2%). T. Rowe Price: 23.2% for 2025 (down from 24.3%). Franklin's is lower; both fell. Fiscal years differ.
- **Key points:** Franklin 21.0%; T. Rowe Price 23.2%; both declined; different fiscal years
- **Evidence** `BEN_FY2026_10K` Item 7 [191392:191494]: Our effective income tax rate for fiscal year 2026 was 21.0% as compared to 30.2% in fiscal year 2025.
- **Evidence** `TROW_FY2025_10K` Item 7 [173083:173172]: Our effective tax rate for 2025 was 23.2%, compared to 24.3% for 2024 and 26.3% for 2023.

## h036 · comparison · easy · narrative

- [ ] **Q:** Do Principal and MetLife list their stock on the same exchange?
- **Gold:** No: Principal trades on the Nasdaq Global Select Market; MetLife trades on the New York Stock Exchange.
- **Key points:** Principal: Nasdaq; MetLife: NYSE
- **Evidence** `PFG_FY2025_10K` Item 5 [161053:161184]: Effective December 15, 2017, we changed our listing to the Nasdaq Global Select Market and continue trading under the symbol “PFG”.
- **Evidence** `MET_FY2025_10K` Item 5 [198398:198540]: MetLife, Inc.’s common stock, par value $0.01 per share, began trading on the New York Stock Exchange under the symbol “MET” on April 5, 2000.

## h037 · comparison · easy · narrative

- [ ] **Q:** How do T. Rowe Price and Principal differ in how they hold their headquarters?
- **Gold:** T. Rowe Price leases its Harbor Point, Baltimore headquarters (about 550,000 square feet); Principal owns its world headquarters complex in Des Moines, Iowa.
- **Key points:** T. Rowe Price leases (Baltimore); Principal owns (Des Moines)
- **Evidence** `TROW_FY2025_10K` Item 2 [117524:117709]: Our new corporate headquarters, which we moved to in early 2025, is located in the Harbor Point area of Baltimore, Maryland, in approximately 550,000 square feet of leased office space.
- **Evidence** `PFG_FY2025_10K` Item 2 [155053:155151]: As of December 31, 2025, we owned properties at our world headquarters complex in Des Moines, Iowa

## h038 · comparison · medium · narrative

- [ ] **Q:** Which uses the larger interest rate shock in its sensitivity disclosures, MetLife or Principal?
- **Gold:** Principal: a 100 basis point immediate, parallel decrease, versus MetLife's 50 basis point rise or decline.
- **Key points:** Principal 100 bp; MetLife 50 bp; Principal larger
- **Evidence** `MET_FY2025_10K` Item 7 [216350:216480]: The Rising Interest Rate Scenario assumes U.S. interest rates rise immediately on January 1, 2026 by 50 basis points through 2028.
- **Evidence** `PFG_FY2025_10K` Item 7A [311564:311755]: We estimate a hypothetical 100 basis point immediate, parallel decrease in U.S. interest rates would impact segment pre-tax operating earnings between (1)% and 1% over the next twelve months.

## h039 · comparison · medium · table

- [ ] **Q:** In its most recent fiscal quarter, which repurchased more shares, T. Rowe Price or Franklin?
- **Gold:** Franklin: 2,521,966 shares (July–September 2026) versus T. Rowe Price's 1,366,531 (October–December 2025). The quarters differ.
- **Key points:** Franklin 2,521,966; T. Rowe Price 1,366,531; Franklin more; different quarters
- **Evidence** `BEN_FY2026_10K` Item 5 [154592:154675]: September 2026 | 30,447 | 32.41 | 30,447 | 23,047,084 Total | 2,521,966 | 2,521,966
- **Evidence** `TROW_FY2025_10K` Item 5 [123245:123287]: Total | 1,366,531 | $ | 103.06 | 1,366,531

## h040 · comparison · medium · narrative

- [ ] **Q:** Which has more holders of record, BlackRock or Lincoln, and what caveat applies to these counts?
- **Gold:** Lincoln: 4,732 (February 12, 2026) versus BlackRock's 216 (January 31, 2026). Record holders include institutional or omnibus accounts that hold shares for many underlying investors, so these counts understate actual shareholders.
- **Key points:** Lincoln 4,732; BlackRock 216; record holders include omnibus accounts
- **Evidence** `BLK_FY2025_10K` Item 5 [240947:241154]: At the close of business on January 31, 2026, there were 216 common stockholders of record. Common stockholders include institutional or omnibus accounts that hold common stock for many underlying investors.
- **Evidence** `LNC_FY2025_10K` Item 5 [220146:220238]: As of February 12, 2026, the number of shareholders of record of our common stock was 4,732.

## h041 · unanswerable · medium

- [ ] **Q:** What quarterly dividend did T. Rowe Price declare for the first quarter of 2026?
- **Gold:** This information is not in the documents. The 10-K reports 2024 and 2025 dividends but no 2026 declaration.
- **Key points:** States that the documents don't contain this information; Does not guess or invent a figure
- **Notes:** The 10-K reports 2024 and 2025 dividends but no 2026 declaration.

## h042 · unanswerable · medium

- [ ] **Q:** How many square feet is Principal's Des Moines headquarters complex?
- **Gold:** This information is not in the documents. Principal says it owns the complex but gives no square footage.
- **Key points:** States that the documents don't contain this information; Does not guess or invent a figure
- **Notes:** Principal says it owns the complex but gives no square footage.

## h043 · unanswerable · medium

- [ ] **Q:** What is the name of BlackRock's Chief Information Security Officer?
- **Gold:** This information is not in the documents. BlackRock describes the CISO's experience but not the person's name.
- **Key points:** States that the documents don't contain this information; Does not guess or invent a figure
- **Notes:** BlackRock describes the CISO's experience but not the person's name.

## h044 · unanswerable · medium

- [ ] **Q:** How many T. Rowe Price associates work in Colorado Springs?
- **Gold:** This information is not in the documents. The 10-K names Colorado Springs as an owned campus but gives no headcount there.
- **Key points:** States that the documents don't contain this information; Does not guess or invent a figure
- **Notes:** The 10-K names Colorado Springs as an owned campus but gives no headcount there.

## h045 · unanswerable · medium

- [ ] **Q:** What was Lincoln's CEO paid in total for 2025?
- **Gold:** This information is not in the documents. Executive compensation is incorporated by reference from the proxy statement.
- **Key points:** States that the documents don't contain this information; Does not guess or invent a figure
- **Notes:** Executive compensation is incorporated by reference from the proxy statement.

## h046 · unanswerable · medium

- [ ] **Q:** What earnings per share does Principal expect for 2026?
- **Gold:** This information is not in the documents. The 10-K gives no 2026 EPS guidance.
- **Key points:** States that the documents don't contain this information; Does not guess or invent a figure
- **Notes:** The 10-K gives no 2026 EPS guidance.

## h047 · unanswerable · medium

- [ ] **Q:** How many Franklin Templeton employees work in India?
- **Gold:** This information is not in the documents. Franklin gives a total headcount and office count only.
- **Key points:** States that the documents don't contain this information; Does not guess or invent a figure
- **Notes:** Franklin gives a total headcount and office count only.

## h048 · unanswerable · medium

- [ ] **Q:** What dividend payout ratio does BlackRock target?
- **Gold:** This information is not in the documents. BlackRock reports dividends declared but states no target payout ratio.
- **Key points:** States that the documents don't contain this information; Does not guess or invent a figure
- **Notes:** BlackRock reports dividends declared but states no target payout ratio.

## h049 · unanswerable · medium

- [ ] **Q:** How many people does BlackRock employ in Belgrade?
- **Gold:** This information is not in the documents. Belgrade is listed as an operations and office location, with no headcount.
- **Key points:** States that the documents don't contain this information; Does not guess or invent a figure
- **Notes:** Belgrade is listed as an operations and office location, with no headcount.

## h050 · unanswerable · medium

- [ ] **Q:** What share of MetLife's employees work remotely?
- **Gold:** This information is not in the documents. The 10-K gives total headcount but nothing on remote work.
- **Key points:** States that the documents don't contain this information; Does not guess or invent a figure
- **Notes:** The 10-K gives total headcount but nothing on remote work.
