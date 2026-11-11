# Hand-labeling packet: `baseline` (rubric v2)

30 questions. For each, read the excerpts and the answer, then record three grades
in `baseline_labels.csv` using the rubric below. Grade what you see; don't look at the judge's
verdicts until you're done.

Allowed values:
- correctness: correct, partial, incorrect, abstained
- faithfulness: faithful, unfaithful, n/a
- citations: accurate, inaccurate, none, n/a

## Rubric

```
CORRECTNESS (compare the answer with the gold answer and key points)
- correct: covers every key point and contradicts nothing in the gold answer.
- partial: covers some key points, or is right but missing a qualifier the key points require.
  A COMPARISON that gives the right facts for one side but not the other is "partial".
- incorrect: misses the main point, states a wrong figure or fact, or answers a different question.
- abstained: declines to answer the question asked, for example by saying the documents don't
  contain the answer. Use "abstained" even if the answer was in fact in the excerpts; the harness
  reports separately whether the evidence was retrieved. A decline that also offers related facts
  (for example, a figure for a different segment or period), clearly not answering the question
  asked, is still "abstained". If a related fact is presented AS the answer, grade it as
  "incorrect" instead.
For an UNANSWERABLE question (no gold evidence): "abstained" if the answer declines, and
"incorrect" if it gives a substantive answer anyway.

FAITHFULNESS (compare the answer with the numbered excerpts only, not with the gold answer)
Grade every factual claim the answer makes, including facts mentioned inside a decline.
- faithful: every factual claim is supported by the excerpts. Simple arithmetic on excerpt
  figures counts as supported.
- unfaithful: at least one factual claim is not supported by the excerpts (even if it happens
  to be true).
- n/a: the answer states no facts at all (for example, only "the documents don't contain this").
  A claim about what the excerpts do or don't contain is not a fact for this purpose.

CITATIONS (grade every factual claim, including facts mentioned inside a decline)
- accurate: the answer cites excerpts, and each cited excerpt supports the claim it's attached
  to; no major claim is left uncited.
- inaccurate: at least one citation points to an excerpt that doesn't support its claim, or a
  major claim is uncited.
- none: the answer states facts but cites nothing.
- n/a: the answer states no facts at all.
```

---

## q001 · single_fact

**Question:** What percentage of T. Rowe Price's total managed assets sat in its target date retirement products at the close of 2025?

**Gold answer:** 31.6% ($561.4 billion), up from 29.6% at the end of 2024.

**Key points:**
1. 31.6%
2. $561.4 billion

**System answer:**

> At December 31, 2025, target date retirement products made up 31.6% of T. Rowe Price's managed assets. That compares with 29.6% at the end of 2024 [1]. These products held $561.4 billion in assets under management at year-end 2025 [1][2].

<details><summary>Excerpts the system saw</summary>

```
[1] T. Rowe Price, fiscal year ended 2025-12-31 (TROW_FY2025_10K), Item 1
(4)Retail includes assets sourced through our direct-marketed business and financial intermediaries.

United States | U.S. Defined Contribution
APAC, EMEA, Canada | Other Retirement
Other Accounts

In 2025, our target date retirement products experienced net cash inflows of $5.2 billion. The assets under management in our target date retirement products totaled $561.4 billion at December 31, 2025, or 31.6% of our managed assets at December 31, 2025, compared to 29.6% at the end of 2024.

Additional information concerning our assets under management, results of operations, and financial condition during the past three years is contained in Part II, Item 7. Management’s Discussion and Analysis of Financial Condition and Results of Operations as well as our consolidated financial statements, which are included in Item 8. of this Form 10-K.

INVESTMENT MANAGEMENT SERVICES.

Investment Capabilities

We manage a broad range of investment strategies in equity, fixed income, multi-asset, and alternatives across sectors, styles and regions. Our strategies are designed to meet the varied and changing needs of investors and are delivered across a range of vehicles. We also offer specialized advisory services, including management of stable value investment contracts, customized multi-asset solutions, and a distribution management service for the disposition of equity securities our clients receive from third-party venture capital investment pools.

Page 4

Table of Contents

---

[2] T. Rowe Price, fiscal year ended 2025-12-31 (TROW_FY2025_10K), Item 7
8.6% at December 31, 2023.

The following table details our assets under management and net flows in our target date retirement products, which are included in the multi-asset column shown above:

(in billions) | 2025 | 2024 | 2023
Assets under management | $ | 561.4 | $ | 475.6 | $ | 408.4
Net cash flows | $ | 5.2 | $ | 16.3 | $ | 13.1

Page 33

Table of Contents

Our net cash outflows in 2025 were driven primarily by growth-oriented equity strategies. These outflows were partially offset by net cash inflows in fixed income, target date retirement products, and alternatives strategies. Financial intermediaries and institutional clients were the main sources of net outflows in 2025. From a geography perspective, net outflows were predominantly from U.S. clients invested in equity strategies, though all regions experienced net outflows. For 2024, net outflows were driven primarily by growth-oriented equity strategies and a multi-asset sub-advised variable annuity outflow. These outflows were partially offset by net cash inflows in our target date retirement products, fixed income and alternatives strategies. Financial intermediaries were the main sources of net outflows in 2024. Geographically, while the EMEA and APAC regions experienced net inflows, these were outweighed by outflows in the Americas. For 2023, net outflows were driven primarily by our growth-oriented equity strategies sourced from Americas financial intermediaries and institutional clients.

---

[3] T. Rowe Price, fiscal year ended 2025-12-31 (TROW_FY2025_10K), Item 1
assets under management at the end of 2025.

The following table outlines the five distribution channels and vehicles through which our assets under management are sourced as of December 31, 2025.

Vehicle | Retail | Institutional
Americas financial intermediaries | EMEA & APAC financial intermediaries | Individual U.S. investors on a direct basis | U.S. Defined Contribution | Institutional investors
U.S. Mutual Funds | x | x | x | x
Collective Investment Trusts | x | x | x
Exchange-Traded Funds | x | x | x
College Savings Plans | x | x
Model Portfolios | x | x | x (6)
Separately Managed Accounts (SMAs) (1) | x | x | x
Subadvised Accounts | x | x | x | x
Separate Accounts | x | x | x | x | x
SICAVs (2) / FCPs (3) | x | x | x
Canadian Pooled Funds | x | x
OEICs (4) | x | x
Japanese ITMs (5) | x | x
Australian Unit Trusts | x | x
Private Funds | x
Collateralized Loan Obligations | x
Business Development Company (BDC) | x | x
Interval Funds | x | x

Page 6

Table of Contents

(1) Includes both model delivery and manager traded SMAs,. (2)Société d'Investissement à Capital Variable (Luxembourg), (3)Fonds Commun de Placement (Luxembourg), (4)Open-Ended Investment Company (U.K.), (5)Japanese Investment Trust Management Funds, (6) Provided through our ActivePlus and Retirement Advisory Service Portfolios.

INVESTMENT ADVISORY FEES.

---

[4] T. Rowe Price, fiscal year ended 2025-12-31 (TROW_FY2025_10K), Item front matter
and Management and Related Stockholder Matters | 95
ITEM 13. | Certain Relationships and Related Transactions, and Director Independence | 95
ITEM 14. | Principal Accountant Fees and Services | 95
PART IV | 95
ITEM 15. | Exhibits, Financial Statement Schedules | 95
ITEM 16. | Form 10-K Summary | 98
SIGNATURES | 99

Page 1

Table of Contents

PART I

Item 1.Business.

T. Rowe Price Group, Inc. (T. Rowe Price Group, T. Rowe Price, the firm, we, us, or our) is a financial services holding company that provides global investment advisory services through its subsidiaries to investors worldwide. We identify and actively invest in opportunities to help people thrive in an evolving world. As a premier global asset management organization with more than 85 years of experience, we provide investment solutions and a broad range of equity, fixed income, multi-asset, and alternatives capabilities to individuals, advisors, institutions, and retirement plan sponsors. We also provide certain investment advisory clients with related administrative services, including distribution, mutual fund transfer agent, accounting, and shareholder services; participant recordkeeping and transfer agent services for defined contribution retirement plans; brokerage; trust services; and other advisory services. We take an active, independent approach to investing, offering our dynamic perspective and meaningful partnership, so our clients can feel more confident.

---

[5] T. Rowe Price, fiscal year ended 2025-12-31 (TROW_FY2025_10K), Item 7
mutual funds (across primary share classes) ended 2025 with an overall rating of 4 or 5 stars.

(1) The investment performance reflects that of T. Rowe Price U.S. mutual funds, ETFs, and composites.

(2) Source: © 2026 Morningstar, Inc. All rights reserved. The information contained herein: 1) is proprietary to Morningstar and/or its content providers; 2) may not be copied or distributed; and 3) is not warranted to be accurate, complete, or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

(3) Source: Morningstar. Primary share class only. Excludes money market mutual funds, funds with an operating history of less than one year, T. Rowe Price passive funds, and T. Rowe Price funds that are clones of other funds. The top chart reflects the percentage of T. Rowe Price funds with 1 year, 3 year, 5 year, and 10 year track record that outperformed the Morningstar category median. The bottom chart reflects the percentage of T. Rowe Price funds AUM that has outperformed for the time periods indicated. Total AUM included for this analysis includes $329B for 1 year, $319B for 3 years, $317B for 5 years, and $316B for 10 years.
```

</details>

---

## q003 · single_fact

**Question:** What growth range does T. Rowe Price expect for its 2026 non-GAAP operating expenses, and from what 2025 base?

**Gold answer:** 3% to 6% growth from the 2025 amount of $4,608.0 million, excluding non-GAAP accrued carried interest compensation.

**Key points:**
1. 3% to 6%
2. $4,608.0 million base
3. excludes accrued carried interest compensation

**System answer:**

> T. Rowe Price expects its 2026 non-GAAP operating expenses, excluding non-GAAP accrued carried interest compensation, to grow 3%–6% from a 2025 base of $4,608.0 million [1][2]. The company says it could adjust its expense growth if unforeseen circumstances arise, including significant market movements [1][2].
> 
> This base differs from the $4,666.5 million of total 2025 non-GAAP operating expenses [2], because the guidance excludes non-GAAP accrued carried interest compensation.

<details><summary>Excerpts the system saw</summary>

```
[1] T. Rowe Price, fiscal year ended 2025-12-31 (TROW_FY2025_10K), Item 7
will grow in the range of 3%-6% from the 2025 amount of $4,608.0 million. We could elect to adjust our expense growth should unforeseen circumstances arise, including significant market movements.

Operating margin was 29.9% in 2025 compared to 32.9% in 2024. The decrease is primarily driven by the restructuring charge recognized in 2025, which largely contributed to operating expense growth exceeding net revenue growth.

Diluted earnings per share was $9.24 in 2025 compared to $9.15 in 2024. The increase in GAAP basis diluted earnings per share was primarily due to higher non-operating income and fewer outstanding shares, partially offset by lower operating income.

On a non-GAAP basis, diluted earnings per share was $9.72 in 2025 compared to $9.33 in 2024. The increase was primarily due to fewer outstanding shares and higher net income.

See our non-GAAP reconciliations later in this Management's Discussion and Analysis section.

Results Overview - 2024 compared to 2023

---

[2] T. Rowe Price, fiscal year ended 2025-12-31 (TROW_FY2025_10K), Item 7
to accrued carried interest for the change in value of certain affiliated funds assuming the funds’ underlying investments were realized as of the end of the period.

Page 36

Table of Contents

Operating expenses on a U.S. GAAP basis were $5,126.0 million in 2025, an increase of 7.7% compared to $4,760.3 million in 2024. On a non-GAAP basis, operating expenses were $4,666.5 million, an increase of 3.7% compared to $4,498.8 million in 2024.

Compared to 2024, the increase in U.S. GAAP operating expenses was primarily due to the restructuring charge as well as higher technology and facility costs, compensation and related costs, and distribution and servicing costs. These increases were partially offset by lower advertising and promotion costs. The drivers of the increase in non-GAAP operating expenses were the same as those for the increase in U.S. GAAP operating expenses with the exception of the restructuring charge, which is excluded from our non-GAAP operating expenses measures.

We currently estimate our 2026 non-GAAP operating expenses, excluding non-GAAP accrued carried interest compensation, will grow in the range of 3%-6% from the 2025 amount of $4,608.0 million. We could elect to adjust our expense growth should unforeseen circumstances arise, including significant market movements.

---

[3] T. Rowe Price, fiscal year ended 2025-12-31 (TROW_FY2025_10K), Item 7
Additionally, 2023 included a $82.4 million reduction in operating expenses related to the remeasurement of the contingent consideration liability compared to a $13.4 million reduction in 2024.

On a non-GAAP basis, operating expenses were $4,498.8 million, an increase of 5.6% compared to 2023. The increase in our non-GAAP operating expenses was primarily driven by higher costs across compensation and benefits, distribution and servicing, advertising, professional fees, and a nonrecurring recovery of general and administrative costs recognized in 2023. These increases were partially offset by lower external research fees, lower accrued carried interest compensation, and higher capitalized labor. In 2024, the firm changed its approach to paying for external research, consistent with regulations and general industry practice.

Page 37

Table of Contents

Operating margin was 32.9% in 2024 compared to 30.7% in 2023. The increase is primarily driven by net revenue growth outpacing operating expense growth primarily due to higher average assets under management.

Diluted earnings per share was $9.15 in 2024 compared to $7.76 in 2023. The increase in GAAP basis diluted earnings per share was primarily due to higher operating income and a lower effective tax rate.

On a non-GAAP basis, diluted earnings per share was $9.33 in 2024 compared to $7.59 in 2023. The increase was primarily due to higher operating income and a lower effective tax rate.

---

[4] T. Rowe Price, fiscal year ended 2025-12-31 (TROW_FY2025_10K), Item 7
tax rate.

On a non-GAAP basis, diluted earnings per share was $9.33 in 2024 compared to $7.59 in 2023. The increase was primarily due to higher operating income and a lower effective tax rate.

See our non-GAAP reconciliations later in this Management's Discussion and Analysis section.

Net revenues

2025 compared to 2024 | 2024 compared to 2023
(in millions) | 2025 | 2024 | 2023 | $ Change | % Change (1) | $ Change | % Change (1)
Investment advisory fees
Equity | $ | 3,923.7 | $ | 3,864.7 | $ | 3,442.3 | $ | 59.0 | 1.5 | % | $ | 422.4 | 12.3 | %
Fixed income, including money market | 433.0 | 410.7 | 400.4 | 22.3 | 5.4 | % | 10.3 | 2.6 | %
Multi-asset | 1,910.6 | 1,814.1 | 1,583.4 | 96.5 | 5.3 | % | 230.7 | 14.6 | %
Alternatives | 335.0 | 310.2 | 283.4 | 24.8 | 8.0 | % | 26.8 | 9.5 | %
6,602.3 | 6,399.7 | 5,709.5 | 202.6 | 3.2 | % | 690.2 | 12.1 | %
Performance-based advisory fees | 37.4 | 59.3 | 38.2 | (21.9) | (36.9) | % | 21.1 | 55.2 | %
Capital allocation-based income
Change in accrued carried interest | 149.5 | 134.1 | 223.2 | 15.4 | n/m | (89.1) | n/m
Acquisition-related amortization and impairments | (68.3) | (87.5) | (61.3) | 19.2 | n/m | (26.2) | n/m
81.2 | 46.6 | 161.9 | 34.6 | n/m | (115.3) | n/m
Administrative, distribution, services, and other fees
Administrative and other fees | 506.3 | 498.8 | 467.5 | 7.5 | 1.5 | % | 31.3 | 6.7 | %
Distribution and servicing fees | 87.6 | 89.2 | 83.4 | (1.6) | (1.8) | % | 5.8 | 7.0 | %

---

[5] T. Rowe Price, fiscal year ended 2025-12-31 (TROW_FY2025_10K), Item 7
other investments, acquisition-related amortization and costs, impairment charges, and certain nonrecurring charges and gains, including the restructuring charges.

Page 35

Table of Contents

2025 compared to 2024 | 2024 compared to 2023
(in millions, except per-share data) | 2025 | 2024 | 2023 | $ Change | % Change (1) | $ Change | % Change (1)
U.S. GAAP basis
Investment advisory fees | $ | 6,602.3 | $ | 6,399.7 | $ | 5,709.5 | $ | 202.6 | 3.2 | % | $ | 690.2 | 12.1 | %
Capital allocation-based income (2) | $ | 81.2 | $ | 46.6 | $ | 161.9 | $ | 34.6 | n/m | $ | (115.3) | n/m
Net revenues | $ | 7,314.8 | $ | 7,093.6 | $ | 6,460.5 | $ | 221.2 | 3.1 | % | $ | 633.1 | 9.8 | %
Operating expenses | $ | 5,126.0 | $ | 4,760.3 | $ | 4,474.3 | $ | 365.7 | 7.7 | % | $ | 286.0 | 6.4 | %
Net operating income | $ | 2,188.8 | $ | 2,333.3 | $ | 1,986.2 | $ | (144.5) | (6.2) | % | $ | 347.1 | 17.5 | %
Non-operating income (loss) | $ | 686.7 | $ | 486.3 | $ | 504.1 | $ | 200.4 | 41.2 | % | $ | (17.8) | (3.5) | %
Net income to T. Rowe Price Group | $ | 2,087.1 | $ | 2,100.1 | $ | 1,788.7 | $ | (13.0) | (0.6) | % | $ | 311.4 | 17.4 | %
Diluted earnings per common share | $ | 9.24 | $ | 9.15 | $ | 7.76 | $ | 0.09 | 1.0 | % | $ | 1.39 | 17.9 | %
Weighted average common shares outstanding assuming dilution | 220.3 | 223.3 | 224.8 | (3.0) | (1.3) | % | (1.5) | (0.7) | %
Adjusted basis (3)
Operating expenses | $ | 4,666.5 | $ | 4,498.8 | $ | 4,260.7 | $ | 167.7 | 3.7 | % | $ | 238.1 | 5.6 | %
```

</details>

---

## q005 · single_fact

**Question:** How much revenue did BlackRock's technology and subscription offerings generate in 2025, and how fast did it grow?

**Gold answer:** $2.0 billion, up 24% year over year.

**Key points:**
1. $2.0 billion
2. 24% growth

**System answer:**

> BlackRock's technology services and subscription revenue was $2.0 billion in 2025, up 24% year-over-year [1]. In dollar terms, it rose $378 million from $1.6 billion in 2024 [2].
> 
> Two factors drove the increase. One was sustained demand for Aladdin technology offerings. The other was roughly $210 million of revenue from the Preqin Transaction [2]. Aladdin made up the majority of the segment's revenue for the year [1].
> 
> Annual contract value (ACV) increased 31% year-over-year including Preqin, and 16% excluding Preqin, driven by strong net sales of Aladdin [1].

<details><summary>Excerpts the system saw</summary>

```
[1] BlackRock, fiscal year ended 2025-12-31 (BLK_FY2025_10K), Item 1
official institutions, banks, asset servicers, corporations, law firms, consultants and other investors across North America, South America, Europe, the Middle East, Asia, Africa and Australia.

Technology services and subscription revenue of $2.0 billion was up 24% year-over-year. Annual contract value (“ACV”) increased 31% year-over-year including ACV related to Preqin, and increased 16% excluding ACV related to Preqin, driven by strong net sales of Aladdin in 2025. Aladdin assignments are typically long-term contracts that provide recurring revenue. At the end of any period, BlackRock generally has recurring revenue contracts in place for a large portion of total annual revenue. BlackRock measures the fees related to these agreements and refers to this as ACV. For further information on ACV, see Item 7. Management’s Discussion and Analysis of Financial Condition and Results of Operations — Non-GAAP Financial Measures.

Aladdin, which represented the majority of technology services and subscription revenue for the year, continues to benefit from trends favoring global platform and multi-asset risk solutions across public and private markets. In addition, while Aladdin is a multi-asset system, the majority of positions managed on the platform are fixed income. Revenue growth in 2025 reflected the successful onboarding of a number of new clients and expanding relationships with existing clients.

---

[2] BlackRock, fiscal year ended 2025-12-31 (BLK_FY2025_10K), Item 7
or 19%, from 2024, primarily reflecting the positive impact of markets, organic base fee growth, fees related to the GIP and HPS Transactions and higher technology services and subscription revenue.

Investment advisory, administration fees and securities lending revenue of $19.2 billion in 2025 increased $3.1 billion from $16.1 billion in 2024, primarily driven by organic base fee growth, the impact of market beta and foreign exchange movements on average AUM and the impact of the GIP and HPS Transactions. Securities lending revenue of $705 million increased $90 million from $615 million in 2024, primarily reflecting higher average balances of securities on loan and higher spreads.

Investment advisory performance fees of $1.4 billion in 2025 increased $217 million from $1.2 billion in 2024, primarily reflecting higher revenue from private markets, including the impact of the HPS Transaction, partially offset by lower revenue from liquid alternative products.

Technology services and subscription revenue of $2.0 billion in 2025 increased $378 million from $1.6 billion in 2024, reflecting the sustained demand for Aladdin technology offerings and approximately $210 million of revenue related to the Preqin Transaction.

Expense

The following table presents expense for 2025 and 2024.

---

[3] BlackRock, fiscal year ended 2025-12-31 (BLK_FY2025_10K), Item FS
$ | 1,783
Acquisition (1) | 1,441 | —
Net increase (decrease) in unrealized allocations | 706 | 364
Performance fee revenue recognized | ( 492 | ) | ( 287 | )
Ending balance | $ | 3,515 | $ | 1,860

(1)
Amount for 2025 includes deferred carried interest acquired in connection with the HPS Transaction. See Note 3, Acquisitions, for information on the HPS Transaction.

Technology Services and Subscription Revenue – Remaining Performance Obligation

The tables below present estimated technology services and subscription revenue expected to be recognized in the future related to the unsatisfied portion of the performance obligations at December 31, 2025 and 2024:

December 31, 2025

(in millions) | 2026 | 2027 | 2028 | Thereafter | Total
Technology services and subscription revenue (1)(2) | $ | 208 | $ | 121 | $ | 73 | $ | 95 | $ | 497

December 31, 2024

(in millions) | 2025 | 2026 | 2027 | Thereafter | Total
Technology services and subscription revenue (1)(2) | $ | 134 | $ | 81 | $ | 50 | $ | 69 | $ | 334

(1)
Technology services and subscription revenue includes upfront payments from customers, which the Company recognizes as services are performed. Revenue attributed to future periods could be subject to change due to a change in business activities and actual amounts could differ from amounts disclosed in the table above.

---

[4] BlackRock, fiscal year ended 2025-12-31 (BLK_FY2025_10K), Item 7
launched in the last five years. Active ETFs delivered $54 billion in net inflows in 2025, and BlackRock’s US equity factor rotation active ETF was the highest grossing active ETF in the industry. BlackRock fixed income ETFs generated a record $159 billion of net inflows, and the Company had both the highest net inflowing active and index fixed income ETFs in the industry. BlackRock will continue to innovate at the product and portfolio level and accelerate distribution capabilities to deliver differentiated investment solutions.

BlackRock continues to invest in technology services offerings, which enhance the ability to manage portfolios and risk, effectively serve clients and operate efficiently. Market volatility, growing cost pressures, and complexity in optimizing whole portfolios underscore the need for enterprise operating and risk management technology, and should continue to drive demand for holistic and flexible technology solutions. BlackRock continues to evolve and enable clients to further simplify their operating infrastructure with Aladdin. Clients increasingly want to tailor how they use Aladdin to meet their specific needs, and BlackRock is providing them with choice and flexibility. Through the integration of Aladdin and eFront, clients are able to better manage and analyze risk across their whole portfolio spanning public and private markets.

---

[5] BlackRock, fiscal year ended 2025-12-31 (BLK_FY2025_10K), Item 1
of positions managed on the platform are fixed income. Revenue growth in 2025 reflected the successful onboarding of a number of new clients and expanding relationships with existing clients.

The Company’s acquisition of Preqin in March 2025 added private markets data capabilities to its existing Aladdin and eFront workflow offerings, creating a preeminent private markets technology and data provider. As clients’ private market allocations continue to grow, they will require more standardized and transparent data on their investments, creating an additional growth opportunity for Preqin.

BlackRock is focused on enhancing Aladdin, with continued investment into areas such as AI, whole portfolio, private markets, and wealth. BlackRock continues to evolve and enable clients to further simplify their operating infrastructure with Aladdin. Clients increasingly want to tailor how they use Aladdin to meet their specific needs, and BlackRock is providing them with choice and flexibility. BlackRock is empowering clients with data and APIs, as well as creating connectivity with ecosystem providers and third-party technology solutions, which include asset servicers, cloud providers, digital asset platforms, trading systems and others. This connectivity helps clients work in their Aladdin environments with a more customized and seamless end-to-end experience.
```

</details>

---

## q007 · single_fact

**Question:** On its adjusted (non-GAAP) basis, how much did MetLife earn for common shareholders in 2025?

**Gold answer:** $5.9 billion, up from $5.8 billion in 2024.

**Key points:**
1. $5.9 billion

**System answer:**

> MetLife's adjusted earnings available to common shareholders were $5.9 billion for 2025. That compares with $5.8 billion in 2024 and $5.5 billion in 2023 [1]. On a GAAP basis, net income available to common shareholders was $3.2 billion in 2025 [1].

<details><summary>Excerpts the system saw</summary>

```
[1] MetLife, fiscal year ended 2025-12-31 (MET_FY2025_10K), Item 7
Financial Highlights

•Net income available to MetLife, Inc.’s common shareholders was $3.2 billion, $4.2 billion and $1.4 billion for the years ended December 31, 2025, 2024 and 2023, respectively.

•Adjusted earnings available to common shareholders was $5.9 billion, $5.8 billion and $5.5 billion for the years ended December 31, 2025, 2024 and 2023, respectively.

62

Table of Contents

Consolidated Results

Years Ended December 31,
2025 | 2024 | 2023
(In millions)
Revenues
Premiums | $ | 49,779 | $ | 44,945 | $ | 44,283
Universal life and investment-type product policy fees | 5,003 | 4,974 | 5,152
Net investment income | 22,559 | 21,273 | 19,908
Other revenues | 2,827 | 2,601 | 2,526
Net investment gains (losses) | (1,145) | (1,184) | (2,824)
Net derivative gains (losses) | (1,939) | (1,623) | (2,140)
Total revenues | 77,084 | 70,986 | 66,905
Expenses
Policyholder benefits and claims and policyholder dividends | 50,271 | 45,323 | 45,212
Policyholder liability remeasurement (gains) losses | (150) | (206) | (45)
Market risk benefit remeasurement (gains) losses | (508) | (1,109) | (994)
Interest credited to policyholder account balances | 8,950 | 8,339 | 7,860
Amortization of deferred policy acquisition costs, value of business acquired and negative value of business acquired | 2,114 | 2,021 | 1,926
Interest expense on debt | 1,061 | 1,037 | 1,045
Other expenses, net of capitalization of deferred policy acquisition costs | 10,685 | 9,959 | 9,739

---

[2] MetLife, fiscal year ended 2025-12-31 (MET_FY2025_10K), Item 7
from organic business growth and an acquisition, primarily from real estate, public fixed income and private fixed income

Operating Margin Expansion - Increased adjusted earnings by $126 million:

•Transition to current market rate fees in 2025 for general account investments, coupled with expense management

Year Ended December 31, 2024 Compared with the Year Ended December 31, 2023

Unless otherwise stated, all amounts discussed below are net of income tax.

Adjusted Earnings - Decreased $15 million primarily due to the following business drivers:

Operating Margin Expansion - Decreased adjusted earnings by $15 million:

•Higher corporate-related expenses

84

Table of Contents

Corporate & Other

Years Ended December 31,
2025 | 2024 | 2023
(In millions)
Adjusted earnings available to common shareholders | $ | (487) | $ | (317) | $ | (295)
Adjusted premiums, fees and other revenues | $ | 2,470 | $ | 2,956 | $ | 3,444

Year Ended December 31, 2025 Compared with the Year Ended December 31, 2024

Unless otherwise stated, all amounts discussed below are net of income tax.

Adjusted Earnings Available to Common Shareholders - Decreased $170 million primarily due to the following business drivers:

Reinsurance Transaction - Decreased adjusted earnings available to common shareholders by approximately $7 million as a result of a reinsurance transaction that closed in December 2025

Market Factors - Decreased adjusted earnings available to common shareholders by $151 million:

---

[3] MetLife, fiscal year ended 2025-12-31 (MET_FY2025_10K), Item 7
to investment hedge adjustments, which are also included in adjusted earnings available to common shareholders. See “— Investments — Investment Portfolio Results” for additional information.

(4)See Note 6 of the Notes to the Consolidated Financial Statements for further information on the Company’s MRBs.

(5)See “— Non-GAAP and Other Financial Disclosures” for information regarding adjusted earnings available to common shareholders and related measures.

67

Table of Contents

Reconciliations of net income (loss) available to MetLife, Inc.’s common shareholders to adjusted earnings available to common shareholders and premiums, fees and other revenues to adjusted premiums, fees and other revenues

Year Ended December 31, 2025

Group Benefits | RIS | Asia | Latin America | EMEA | MIM | Corporate & Other | Total
(In millions)
Net income (loss) available to MetLife, Inc.'s common shareholders | $ | 1,473 | $ | 542 | $ | 885 | $ | 872 | $ | 338 | $ | 131 | $ | (1,068) | $ | 3,173
Add: Preferred stock dividends | — | — | — | — | — | — | 194 | 194
Add: Preferred stock redemption premium | — | — | — | — | — | — | 12 | 12
Add: Net income (loss) attributable to noncontrolling interests and redeemable noncontrolling interests | — | — | — | 7 | 5 | — | 12 | 24
Net income (loss) | 1,473 | 542 | 885 | 879 | 343 | 131 | (850) | 3,403
Less: adjustments from net income (loss) to adjusted earnings available to common shareholders:
Revenues:

---

[4] MetLife, fiscal year ended 2025-12-31 (MET_FY2025_10K), Item 7
and other insurance adjustments, litigation reserves and settlement costs, and tax adjustments - Decreased adjusted earnings available to common shareholders by $69 million on a reported basis:

Years Ended December 31, | Variance
2025 | 2024
(In millions, net of income tax)
Group Benefits | $ | (2) | $ | (58) | $ | 56
RIS | 13 | 104 | (91)
Asia | 70 | (41) | 111
Latin America | (104) | 4 | (108)
EMEA | (1) | (5) | 4
MIM | — | — | —
Corporate & Other | (19) | 22 | (41)
Total | $ | (43) | $ | 26 | $ | (69)

Year Ended December 31, 2024 Compared with the Year Ended December 31, 2023

Unless otherwise stated, all amounts discussed below are net of income tax and foreign currency fluctuations. Foreign currency fluctuations can result in significant variances in the financial statement line items.

Adjusted Earnings Available to Common Shareholders - Increased $271 million on a reported basis, primarily due to the following business drivers:

Reinsurance Transaction - Decreased adjusted earnings available to common shareholders by approximately $170 million as a result of the reinsurance transaction that closed in November 2023 in Corporate & Other

Foreign Currency - Decreased adjusted earnings available to common shareholders by $95 million, primarily in the Latin America and Asia segments

Market Factors - Increased adjusted earnings available to common shareholders by $232 million:

•Variable investment income increased - higher returns on private equity funds

---

[5] MetLife, fiscal year ended 2025-12-31 (MET_FY2025_10K), Item 7
shareholders by $134 million:

•Variable investment income increased - higher returns on private equity funds

•Decrease in interest credited expenses on long-duration products

Partially offset by:

•Recurring investment income decreased slightly - lower average invested assets due to business run-off, lower income on derivatives, and lower income on real estate investments, offset by the impact of tax equity investments accounted for under the proportional amortization method in 2024 and higher yields on fixed income securities

Volume Growth - Decreased adjusted earnings available to common shareholders by $40 million:

•Decline due to business run-off

Underwriting and Other Insurance Adjustments - Increased adjusted earnings available to common shareholders by $27 million:

•Favorable morbidity experience in our long-term care business

•Lower dividend expense due to business run-off

Interest Expense on Debt - Increased adjusted earnings available to common shareholders by $11 million:

•Surplus notes repayments at maturity in January and February 2024

•Senior note repayment at maturity in April 2024

•Early senior note redemptions in February 2023 and April 2024

•Interest rate decrease on surplus notes

Partially offset by:

•Senior note issuances in July 2023, March 2024, June 2024 and September 2024

Other Expenses - Increased adjusted earnings available to common shareholders by $30 million:
```

</details>

---

## q008 · single_fact

**Question:** In MetLife's consolidated results, what was GAAP net income available to common shareholders for 2025, in millions?

**Gold answer:** $3,173 million, down from $4,226 million in 2024.

**Key points:**
1. $3,173 million

**System answer:**

> MetLife's GAAP net income available to MetLife, Inc.'s common shareholders for 2025 was $3,173 million [4]. This is consistent with the roughly $3.2 billion reported in the Financial Highlights [1].

<details><summary>Excerpts the system saw</summary>

```
[1] MetLife, fiscal year ended 2025-12-31 (MET_FY2025_10K), Item 7
Financial Highlights

•Net income available to MetLife, Inc.’s common shareholders was $3.2 billion, $4.2 billion and $1.4 billion for the years ended December 31, 2025, 2024 and 2023, respectively.

•Adjusted earnings available to common shareholders was $5.9 billion, $5.8 billion and $5.5 billion for the years ended December 31, 2025, 2024 and 2023, respectively.

62

Table of Contents

Consolidated Results

Years Ended December 31,
2025 | 2024 | 2023
(In millions)
Revenues
Premiums | $ | 49,779 | $ | 44,945 | $ | 44,283
Universal life and investment-type product policy fees | 5,003 | 4,974 | 5,152
Net investment income | 22,559 | 21,273 | 19,908
Other revenues | 2,827 | 2,601 | 2,526
Net investment gains (losses) | (1,145) | (1,184) | (2,824)
Net derivative gains (losses) | (1,939) | (1,623) | (2,140)
Total revenues | 77,084 | 70,986 | 66,905
Expenses
Policyholder benefits and claims and policyholder dividends | 50,271 | 45,323 | 45,212
Policyholder liability remeasurement (gains) losses | (150) | (206) | (45)
Market risk benefit remeasurement (gains) losses | (508) | (1,109) | (994)
Interest credited to policyholder account balances | 8,950 | 8,339 | 7,860
Amortization of deferred policy acquisition costs, value of business acquired and negative value of business acquired | 2,114 | 2,021 | 1,926
Interest expense on debt | 1,061 | 1,037 | 1,045
Other expenses, net of capitalization of deferred policy acquisition costs | 10,685 | 9,959 | 9,739

---

[2] MetLife, fiscal year ended 2025-12-31 (MET_FY2025_10K), Item 7
from organic business growth and an acquisition, primarily from real estate, public fixed income and private fixed income

Operating Margin Expansion - Increased adjusted earnings by $126 million:

•Transition to current market rate fees in 2025 for general account investments, coupled with expense management

Year Ended December 31, 2024 Compared with the Year Ended December 31, 2023

Unless otherwise stated, all amounts discussed below are net of income tax.

Adjusted Earnings - Decreased $15 million primarily due to the following business drivers:

Operating Margin Expansion - Decreased adjusted earnings by $15 million:

•Higher corporate-related expenses

84

Table of Contents

Corporate & Other

Years Ended December 31,
2025 | 2024 | 2023
(In millions)
Adjusted earnings available to common shareholders | $ | (487) | $ | (317) | $ | (295)
Adjusted premiums, fees and other revenues | $ | 2,470 | $ | 2,956 | $ | 3,444

Year Ended December 31, 2025 Compared with the Year Ended December 31, 2024

Unless otherwise stated, all amounts discussed below are net of income tax.

Adjusted Earnings Available to Common Shareholders - Decreased $170 million primarily due to the following business drivers:

Reinsurance Transaction - Decreased adjusted earnings available to common shareholders by approximately $7 million as a result of a reinsurance transaction that closed in December 2025

Market Factors - Decreased adjusted earnings available to common shareholders by $151 million:

---

[3] MetLife, fiscal year ended 2025-12-31 (MET_FY2025_10K), Item 8
the Company’s auditor since at least 1968; however, an earlier year could not be reliably determined.

132

Table of Contents

MetLife, Inc.

Consolidated Balance Sheets

December 31, 2025 and 2024

(In millions, except share and per share data)
2025 | 2024
Assets
Investments:
Fixed maturity securities available-for-sale, at estimated fair value (net of allowance for credit loss of $ 249 and $ 160 , respectively); and amortized cost: $ 337,201 and $ 307,421 , respectively | $ | 315,931 | $ | 281,043
Equity securities, at estimated fair value | 858 | 712
Contractholder-directed equity securities and fair value option securities, at estimated fair value (includes $ 1,751 and $ 0 , respectively, relating to variable interest entities) | 13,959 | 10,672
Mortgage loans (net of allowance for credit loss of $ 1,193 and $ 800 , respectively; includes $ 35 and $ 0 , respectively, of mortgage loans held-for-sale) | 84,593 | 89,012
Policy loans | 8,547 | 8,545
Real estate and real estate joint ventures (includes $ 378 and $ 378 , respectively, under the fair value option; $ 132 and $ 65 , respectively, of real estate held-for-sale; $ 302 and $ 183 , respectively, relating to variable interest entities) | 13,440 | 13,342
Other limited partnership interests | 14,917 | 14,378
Short-term investments, principally at estimated fair value | 3,601 | 5,156

---

[4] MetLife, fiscal year ended 2025-12-31 (MET_FY2025_10K), Item 8
interests and redeemable noncontrolling interests | 24 | 18 | 24
Net income (loss) attributable to MetLife, Inc. | 3,379 | 4,426 | 1,578
Less: Preferred stock dividends | 194 | 200 | 198
Preferred stock redemption premium | 12 | — | —
Net income (loss) available to MetLife, Inc.’s common shareholders | $ | 3,173 | $ | 4,226 | $ | 1,380

Net income (loss) available to MetLife, Inc.’s common shareholders per common share:
Basic | $ | 4.74 | $ | 5.98 | $ | 1.82
Diluted | $ | 4.71 | $ | 5.94 | $ | 1.81

See accompanying notes to the consolidated financial statements.

134

Table of Contents

MetLife, Inc.

Consolidated Statements of Comprehensive Income (Loss)

Years Ended December 31, 2025, 2024 and 2023

(In millions)

2025 | 2024 | 2023
Net income (loss) | $ | 3,403 | $ | 4,444 | $ | 1,602
Other comprehensive income (loss):
Unrealized investment gains (losses), net of related offsets | 4,661 | ( 6,524 ) | 10,325
Deferred gains (losses) on derivatives | ( 2,461 ) | 211 | ( 1,811 )
Future policy benefits discount rate remeasurement gains (losses) | 2,021 | 4,997 | ( 4,361 )
Market risk benefit instrument-specific credit risk remeasurement gains (losses) | ( 31 ) | ( 124 ) | ( 102 )
Foreign currency translation adjustments | 952 | ( 858 ) | 296
Defined benefit plans adjustment | 63 | 5 | ( 88 )
Other comprehensive income (loss), before income tax | 5,205 | ( 2,293 ) | 4,259

---

[5] MetLife, fiscal year ended 2025-12-31 (MET_FY2025_10K), Item 8
the consolidated financial statements.

135

Table of Contents

MetLife, Inc.

Consolidated Statements of Equity

Years Ended December 31, 2025, 2024 and 2023

(In millions, except per share data)

Preferred Stock | Common Stock | Additional Paid-in Capital | Retained Earnings | Treasury Stock at Cost | Accumulated Other Comprehensive Income (Loss) | Total MetLife, Inc.’s Stockholders’ Equity | Noncontrolling Interests | Total Equity
Balance at December 31, 2022 | $ | — | $ | 12 | $ | 33,616 | $ | 40,332 | $ | ( 21,458 ) | $ | ( 22,621 ) | $ | 29,881 | $ | 244 | $ | 30,125
Treasury stock acquired in connection with share repurchases (includes $ 30 of excise tax) | ( 3,133 ) | ( 3,133 ) | ( 3,133 )
Stock-based compensation | 74 | 74 | 74
Dividends on preferred stock | ( 198 ) | ( 198 ) | ( 198 )
Dividends on common stock (declared per share of $ 2.060 ) | ( 1,566 ) | ( 1,566 ) | ( 1,566 )
Change in equity of noncontrolling interests | — | ( 12 ) | ( 12 )
Net income (loss) | 1,578 | 1,578 | 24 | 1,602
Other comprehensive income (loss), net of income tax | 3,379 | 3,379 | ( 18 ) | 3,361
Balance at December 31, 2023 | — | 12 | 33,690 | 40,146 | ( 24,591 ) | ( 19,242 ) | 30,015 | 238 | 30,253
Cumulative effects of changes in accounting principles, net of income tax | ( 219 ) | ( 219 ) | ( 219 )
Treasury stock acquired in connection with share repurchases (includes $ 30 of excise tax) | ( 3,207 ) | ( 3,207 ) | ( 3,207 )
Stock-based compensation | 101 | 101 | 101
```

</details>

---

## q009 · single_fact

**Question:** Which four areas does MetLife's New Frontier strategy prioritize for growth?

**Gold answer:** Extending leadership in Group Benefits; capitalizing on its retirement platform; accelerating growth in asset management; and expanding in high-growth international markets.

**Key points:**
1. Group Benefits
2. retirement platform
3. asset management
4. high-growth international markets

**System answer:**

> MetLife's New Frontier strategy prioritizes growth across four key areas of opportunity [2]:
> 
> 1. Extend its leadership in Group Benefits [2]
> 2. Capitalize on its unique retirement platform [2]
> 3. Accelerate its growth in asset management [2]
> 4. Expand in high-growth international markets [2]
> 
> The strategy was designed to accelerate growth across MetLife's global platform while delivering attractive returns and all-weather performance, and it builds on the earlier Next Horizon strategy implemented in 2019 [1].

<details><summary>Excerpts the system saw</summary>

```
[1] MetLife, fiscal year ended 2025-12-31 (MET_FY2025_10K), Item 1
Overview & Strategy

As used in this Form 10-K, “MetLife,” the “Company,” “we,” “our” and “us” refer to MetLife, Inc., a Delaware corporation incorporated in 1999, its subsidiaries and affiliates.

MetLife is one of the world’s leading financial services companies, providing insurance, annuities, employee benefits and asset management. We hold leading market positions in the United States (“U.S.”), Asia, Latin America, Europe and the Middle East. We are also one of the largest institutional investors in the U.S. with a general account portfolio invested primarily in fixed income securities (corporate, structured products, municipals, and government and agency) and mortgage loans, as well as real estate, real estate joint ventures (“REJVs”), other limited partnerships and equity securities.

We believe that our trusted global brand, diversified and resilient business, and position as a leader in attractive markets are the powers of our business. Over the next four years we will continue to execute on our New Frontier strategy, which was designed to accelerate growth across our global platform while delivering attractive returns and all-weather performance. New Frontier builds upon the success of our Next Horizon strategy, which we implemented in 2019, with an aim to focus, simplify and differentiate the Company.

Under our New Frontier strategy, we intend to leverage the Company’s strengths to prioritize growth across four key areas of opportunity:

---

[2] MetLife, fiscal year ended 2025-12-31 (MET_FY2025_10K), Item 1
an aim to focus, simplify and differentiate the Company.

Under our New Frontier strategy, we intend to leverage the Company’s strengths to prioritize growth across four key areas of opportunity:

• Extend our leadership in Group Benefits;
• Capitalize on our unique retirement platform;
• Accelerate our growth in asset management; and
• Expand in high growth international markets.

In the fourth quarter of 2025, MetLife executed a reorganization to align with its strategic initiative to accelerate growth in asset management. As part of this reorganization, the Company adjusted its segment structure. MetLife Investment Management, the Company’s institutional asset management business (“MIM”), which was previously reported in Corporate & Other, became a reportable segment. MetLife Holdings was removed as a reportable segment, and its business is now primarily reported in Corporate & Other. These changes were applied retrospectively for all years presented. Additionally, certain products formerly reported in MetLife Holdings have been moved to Group Benefits and Retirement and Income Solutions (“RIS”). This change was applied only for the year ended December 31, 2025.

---

[3] MetLife, fiscal year ended 2025-12-31 (MET_FY2025_10K), Item 7
estimated variable investment income for full year 2026; we expect to maintain the two-year average annual ratio of free cash flow to adjusted earnings, excluding total notable items, at 65% to 75%.

Further, based on the aforementioned assumptions, we are maintaining our near-term annual targets for (i) adjusted return on equity, excluding total notable items, of 15%-17%, and (ii) double-digit adjusted earnings per share growth, excluding total notable items.

Based on our continued focus on expense discipline and our overall efficiency mindset, we are committed to achieving a direct expense ratio target, excluding total notable items related to direct expenses and pension risk transfers, of (i) 12.1% for 2026 and (ii) 11.3% in 2029.

47

Table of Contents

Furthermore, we also remain fully committed to our New Frontier strategy, which was introduced at our December 2024 Investor Day.

Our outlook relies on the accuracy of our assumptions about future economic and business conditions, which can be affected by known and unknown risks, uncertainties and other factors. We continually review our assumptions, implement mitigation plans, and take precautions. We may revise our outlook as we obtain more information regarding economic conditions, regulatory changes, and other events, and the impact of these events on our business operations, investment portfolio, derivatives, financial results and financial condition.

Industry Trends

---

[4] MetLife, fiscal year ended 2025-12-31 (MET_FY2025_10K), Item 1
looking at embedded insurance opportunities to capitalize on trends driving the democratization of financial services and the growth of digital ecosystems, thereby expanding the addressable market.

In the U.S. and Japan, we compete with a large number of domestic and foreign-owned life insurance companies, many of which offer products in categories on which we focus. Elsewhere, we compete with the foreign insurance operations of large U.S. insurers and with global insurance groups and local companies. Because we and others underwrite many group insurance products annually, our group purchasers may be able to obtain more favorable terms from competitors rather than renewing coverage with us.

Insurers are focused on their core businesses, specifically in markets where they can achieve scale. Cost reduction efforts are a priority for industry players, with benefits resulting in price adjustments to favor customers and reinvestment capacity. They are increasingly seeking alternative sources of revenue focusing on monetization of assets, and fee-based services. They are also looking for opportunities to offer comprehensive solutions which include value-added services along with traditional products.

---

[5] MetLife, fiscal year ended 2025-12-31 (MET_FY2025_10K), Item 1
purpose driven and inclusive culture, talent and skill development, benefits and wellbeing, compensation, and attracting and retaining talent to support organizational readiness and business needs.

•Purpose-driven and inclusive culture: We cultivate a purpose driven and inclusive culture that serves as a driving force for meeting our business objectives. Global forums bring executives and senior leaders together to align on strategy, build capabilities, and provide feedback on operations, culture, and the future. Our monthly Chief Executive Officer-led “Let’s Talk Live!” town halls share key information and give employees the opportunity to engage directly with leadership. Our global community of employee-driven networks, MOMENTUM, is focused on actively engaging our employees in community outreach and learning and career development opportunities. We listen through MyVoice, our annual employee survey, that informs action-oriented solutions, and encourage openness through Speak Up, an online tool, and the Ethics & Fraud Hotline that allows employees to report concerns without fear of retaliation. Additionally, the MetLife Foundation supports volunteerism and community initiatives, reinforcing our commitment to purpose and impact beyond the workplace.
```

</details>

---

## q010 · single_fact

**Question:** How much capital did Lincoln raise from Bain Capital's minority investment in 2025, and how many shares did it issue?

**Gold answer:** About $825 million for approximately 18.8 million common shares.

**Key points:**
1. $825 million
2. about 18.8 million shares

**System answer:**

> Lincoln raised **$825 million** in aggregate consideration from the Bain Capital transaction, which closed on June 5, 2025 [2]. It issued **18,759,497 shares** of common stock at $44.00 per share, a 25% premium to the 30-day volume-weighted average price as of April 8, 2025 [2]. The shares represent 9.9% of Lincoln's outstanding common stock on a post-issuance basis [2]. The buyer was Bain Capital Prairie, LLC, a newly formed Bain Capital subsidiary [1][2].
> 
> Lincoln said it is deploying, and expects to keep deploying, the proceeds toward its strategic priorities. These include growing spread-based earnings, advancing portfolio management and asset sourcing capabilities, and optimizing its legacy life portfolio [1][3].

<details><summary>Excerpts the system saw</summary>

```
[1] Lincoln National (Lincoln Financial), fiscal year ended 2025-12-31 (LNC_FY2025_10K), Item 7
of strengthening and maintaining our balance sheet, improving our operational efficiency, increasing free cash flow and focusing on profitable growth. Notable actions in 2025 include the following:

•During the second quarter of 2025, we closed our stock purchase agreement (the “Purchase Agreement”) with Bain Capital Prairie, LLC (the “Buyer”), a newly formed subsidiary of Bain Capital, under which we agreed to sell shares representing 9.9% of our outstanding common stock on a post-issuance basis to the Buyer. Under the final terms, Lincoln sold approximately 18.8 million shares of its common stock for aggregate consideration of $825 million. The transaction provided us with capital that we are deploying and expect to continue to deploy toward our strategic priorities, including growing spread-based earnings, advancing our portfolio management efforts and asset sourcing capabilities and optimizing our legacy life portfolio. For additional information on the Bain Capital transaction, see Note 18.

---

[2] Lincoln National (Lincoln Financial), fiscal year ended 2025-12-31 (LNC_FY2025_10K), Item 8
or other similar provisions.

Our Series C and D Preferred Stock are without par value.

209

Table of Contents

Common Shares

The changes in our common stock (number of shares) were as follows:

For the Years Ended December 31,
2025 | 2024 | 2023
Common Stock
Balance as of beginning-of-year | 170,380,646 | 169,666,137 | 169,220,511
Issuance of common stock | 18,759,497 | – | –
Stock compensation/issued for benefit plans | 911,334 | 714,509 | 445,626
Balance as of end-of-year | 190,051,477 | 170,380,646 | 169,666,137

Our common stock is without par value.

Issuance of Common Stock

On June 5, 2025, we closed our purchase agreement (the “Purchase Agreement”) with Bain Capital Prairie, LLC (the “Buyer”), a newly formed subsidiary of Bain Capital, under which we agreed to sell shares representing 9.9% of our outstanding common stock on a post-issuance basis to the Buyer. Under the final terms, Lincoln issued 18,759,497 shares of common stock at $44.00 per share, based on a 25% premium to the 30-day volume-weighted average price as of April 8, 2025, for aggregate consideration of $825 million.

---

[3] Lincoln National (Lincoln Financial), fiscal year ended 2025-12-31 (LNC_FY2025_10K), Item 7
for more information.

LNC made interest payments to service debt to third parties of $309 million, $308 million and $311 million for the years ended December 31, 2025, 2024 and 2023, respectively.

For additional information about our short-term and long-term debt and our credit facility, see Note 13.

98

Table of Contents

Preferred Stock

Details underlying preferred stock dividends paid (in millions) were as follows:

For the Years Ended December 31,
2025 | 2024 | 2023
Series C preferred stock dividends | $ | 46 | $ | 46 | $ | 36
Series D preferred stock dividends | 45 | 45 | 46
Total preferred stock dividends | $ | 91 | $ | 91 | $ | 82

For additional information on preferred stock, see Note 18.

Issuance of Common Stock

On June 5, 2025, we closed our stock sale transaction pursuant to the Purchase Agreement with Bain Capital Prairie, LLC, a newly formed subsidiary of Bain Capital, under which we agreed to sell shares representing 9.9% of our outstanding common stock on a post-issuance basis to the Buyer. Under the final terms, Lincoln sold approximately 18.8 million shares of its common stock for aggregate consideration of $825 million. The transaction provided us with capital that we are deploying and expect to continue to deploy toward our strategic priorities, including growing spread-based earnings, advancing our portfolio management efforts and asset sourcing capabilities and optimizing our legacy life portfolio.

---

[4] Lincoln National (Lincoln Financial), fiscal year ended 2025-12-31 (LNC_FY2025_10K), Item 7
quarter of 2025 using proceeds from the Bain Capital transaction. For more information on the Bain Capital transaction, see “Issuance of Common Stock” below and Note 18.

97

Table of Contents

During 2024, LNC contributed $929 million of investments and $22 million in cash to LPINE, a wholly owned subsidiary of LNC and a licensed Bermuda-based life and annuity reinsurance company, in support of an inter-company reinsurance agreement with LNL. LNC made $5 million and $7 million in capital contributions in cash to other subsidiaries in 2024 and 2023, respectively.

On May 6, 2024, we closed the sale of all of the ownership interests in the subsidiaries of the Company that comprised the Company’s wealth management business operated through LFN to Osaic Holdings, Inc., a Delaware corporation. We received $723 million in cash that was primarily used to increase LNL’s RBC ratio. We also used a portion of the proceeds to reduce our leverage ratio. For more information on the sale of our wealth management business, see Note 1.

Debt

Although our subsidiaries currently generate adequate cash flow to meet the needs of our normal operations, periodically LNC may issue debt to maintain ratings and increase liquidity, as well as to fund internal growth, acquisitions and the retirement of its debt.

Details underlying our debt activities (in millions) for the year ended December 31, 2025, were as follows:

---

[5] Lincoln National (Lincoln Financial), fiscal year ended 2025-12-31 (LNC_FY2025_10K), Item 7
advancing our portfolio management efforts and asset sourcing capabilities and optimizing our legacy life portfolio. For additional information on the Bain Capital transaction, see Note 18.

•In the second quarter of 2025, we exercised in full our issuance right under the 10-year facility agreement dated as of August 18, 2020, and issued $500 million of fixed-rate senior notes and used the net proceeds to early extinguish long-term debt pursuant to a tender offer. Additionally in the second quarter of 2025, we entered into a $1.0 billion 30-year facility agreement that increased our access to liquidity by $500 million. In the fourth quarter of 2025, we completed the issuance of $500 million of fixed-rate senior notes and intend to use $400 million of the net proceeds to prefund the repayment of our senior notes due in 2026. For additional information, see “Liquidity and Capital Resources – Holding Company Sources and Uses of Liquidity and Capital – Debt” below and Note 13.

•During 2025, LNL entered into affiliate reinsurance transactions with Lincoln Pinehurst Reinsurance Company (Bermuda) Limited (“LPINE”), a wholly owned subsidiary of LNC that operates as a Bermuda-based life and annuity reinsurance company. For additional information, see “Liquidity and Capital Resources – Holding Company Sources and Uses of Liquidity and Capital – Subsidiaries’ Capital” below.
```

</details>

---

## q011 · single_fact

**Question:** What cash dividend per common share did Lincoln declare in 2025?

**Gold answer:** $1.80 per share, the same as in 2024 and 2023.

**Key points:**
1. $1.80

**System answer:**

> The excerpts don't say what cash dividend per common share Lincoln declared in 2025. They cover preferred stock dividends only. Per-share and aggregate dividends were declared on the Series C and Series D preferred stock: $2,312.50 and $2,250.00 per share, respectively, for a total of $91 million in 2025 [1]. Preferred dividends paid were also $91 million in 2025 [3].
> 
> On common stock, the excerpts only mention that Lincoln sold about 18.8 million shares to Bain Capital Prairie for $825 million in 2025 [3][4]. They give no common dividend per share.

<details><summary>Excerpts the system saw</summary>

```
[1] Lincoln National (Lincoln Financial), fiscal year ended 2025-12-31 (LNC_FY2025_10K), Item 8
shares | 10,000,000 | 40,000 | 40,000 | 10,000,000 | 40,000 | 40,000

The per share and aggregate dividends declared for preferred stock by series (in millions except per share data) was as follows:

For the Years Ended December 31,
2025 | 2024
Series | Dividend Per Share | Aggregate Dividend | Dividend Per Share | Aggregate Dividend
Series C | $ | 2,312.50 | $ | 46 | $ | 2,312.50 | 46
Series D | 2,250.00 | 45 | 2,250.00 | 45
Total | $ | 4,562.50 | $ | 91 | $ | 4,562.50 | 91

In November 2022, we issued 500,000 depositary shares (“Series C Depositary Shares”), each representing a 1/25th interest in a share of our 9.250% Fixed Rate Reset Non-Cumulative Preferred Stock, Series C liquidation preference $25,000 per share (the “Series C Preferred Stock”) and in the aggregate representing 20,000 shares of Series C Preferred Stock, for aggregate net cash proceeds of $493 million. Dividends, if declared, will be payable commencing on March 1, 2023, and will accrue and be payable on the first day of March and

208

Table of Contents

---

[2] Lincoln National (Lincoln Financial), fiscal year ended 2025-12-31 (LNC_FY2025_10K), Item 8
aggregate net cash proceeds of $493 million. Dividends, if declared, will be payable commencing on March 1, 2023, and will accrue and be payable on the first day of March and

208

Table of Contents

September each year, in arrears, at an annual rate of 9.250% on the liquidation preference of $25,000 per share. From, and including March 1, 2028 (the first “reset date”), the annual rate will reset every five years at a rate equal to the five-year treasury rate as of the most recent reset dividend determination date plus 5.318%. We may, at our option, redeem our Series C Preferred Stock in whole but not in part within 90 days after certain rating agency events, or a regulatory capital event, or in whole or in part, from time to time, during the three-month period prior to each reset date.

---

[3] Lincoln National (Lincoln Financial), fiscal year ended 2025-12-31 (LNC_FY2025_10K), Item 7
for more information.

LNC made interest payments to service debt to third parties of $309 million, $308 million and $311 million for the years ended December 31, 2025, 2024 and 2023, respectively.

For additional information about our short-term and long-term debt and our credit facility, see Note 13.

98

Table of Contents

Preferred Stock

Details underlying preferred stock dividends paid (in millions) were as follows:

For the Years Ended December 31,
2025 | 2024 | 2023
Series C preferred stock dividends | $ | 46 | $ | 46 | $ | 36
Series D preferred stock dividends | 45 | 45 | 46
Total preferred stock dividends | $ | 91 | $ | 91 | $ | 82

For additional information on preferred stock, see Note 18.

Issuance of Common Stock

On June 5, 2025, we closed our stock sale transaction pursuant to the Purchase Agreement with Bain Capital Prairie, LLC, a newly formed subsidiary of Bain Capital, under which we agreed to sell shares representing 9.9% of our outstanding common stock on a post-issuance basis to the Buyer. Under the final terms, Lincoln sold approximately 18.8 million shares of its common stock for aggregate consideration of $825 million. The transaction provided us with capital that we are deploying and expect to continue to deploy toward our strategic priorities, including growing spread-based earnings, advancing our portfolio management efforts and asset sourcing capabilities and optimizing our legacy life portfolio.

---

[4] Lincoln National (Lincoln Financial), fiscal year ended 2025-12-31 (LNC_FY2025_10K), Item 7
of strengthening and maintaining our balance sheet, improving our operational efficiency, increasing free cash flow and focusing on profitable growth. Notable actions in 2025 include the following:

•During the second quarter of 2025, we closed our stock purchase agreement (the “Purchase Agreement”) with Bain Capital Prairie, LLC (the “Buyer”), a newly formed subsidiary of Bain Capital, under which we agreed to sell shares representing 9.9% of our outstanding common stock on a post-issuance basis to the Buyer. Under the final terms, Lincoln sold approximately 18.8 million shares of its common stock for aggregate consideration of $825 million. The transaction provided us with capital that we are deploying and expect to continue to deploy toward our strategic priorities, including growing spread-based earnings, advancing our portfolio management efforts and asset sourcing capabilities and optimizing our legacy life portfolio. For additional information on the Bain Capital transaction, see Note 18.

---

[5] Lincoln National (Lincoln Financial), fiscal year ended 2025-12-31 (LNC_FY2025_10K), Item 8
per Depositary Share), plus an amount equal to any dividends per share that have accrued but not been declared and paid for the then-current dividend period to, but excluding, such redemption date.

In November 2022, we issued 20,000,000 depositary shares (“Series D Depositary Shares”), each representing a 1/1000th interest in a share of our 9.000% Series D, Non-Cumulative Preferred Stock, liquidation preference $25,000 per share (the “Series D Preferred Stock”) and in the aggregate representing 20,000 shares of Series D Preferred Stock, for aggregate net cash proceeds of $493 million. Dividends, if declared, will be payable commencing on March 1, 2023, and will accrue and be payable quarterly on the first day of March, June, September, and December each year, in arrears, at an annual rate of 9.000%. We may, at our option, redeem our Series D Preferred Stock in whole but not in part within 90 days after certain rating agency events, or a regulatory capital event, or in whole or in part, at any time or from time to time, on or after December 1, 2027.
```

</details>

---

## q012 · single_fact

**Question:** Where are Lincoln National's principal executive offices, and in which state was the company organized?

**Gold answer:** Radnor, Pennsylvania; organized under Indiana law in 1968.

**Key points:**
1. Radnor, Pennsylvania
2. Indiana

**System answer:**

> Lincoln National's principal executive offices are in Radnor, Pennsylvania, and the company was organized under the laws of the state of Indiana in 1968 [1].

<details><summary>Excerpts the system saw</summary>

```
[1] Lincoln National (Lincoln Financial), fiscal year ended 2025-12-31 (LNC_FY2025_10K), Item front matter
statements and the accompanying notes to the consolidated financial statements (“Notes”) are presented in “Part II – Item 8. Financial Statements and Supplementary Data.”

Item 1. Business

OVERVIEW

Lincoln National Corporation (“LNC,” which also may be referred to as “Lincoln,” “we,” “our” or “us”) is a holding company that operates multiple insurance and retirement businesses through subsidiary companies. Through our business segments, we sell a wide range of wealth accumulation, wealth protection, group protection and retirement income products and solutions. LNC was organized under the laws of the state of Indiana in 1968. We currently maintain our principal executive offices in Radnor, Pennsylvania. “Lincoln Financial” is the marketing name for LNC and its subsidiary companies.

We provide products and services and report results through four business segments as follows:

•Annuities

•Life Insurance

•Group Protection

•Retirement Plan Services

We also have Other Operations, which includes the financial results for operations that are not directly related to the business segments.

---

[2] Lincoln National (Lincoln Financial), fiscal year ended 2025-12-31 (LNC_FY2025_10K), Item 1C
Professional designation. The CISO has a staff of more than 100 employees dedicated to protecting the data and systems belonging to the Company, our customers, business partners and consumers.

37

Table of Contents

Item 2. Properties

As of December 31, 2025, LNC and our subsidiaries owned or leased 2.2 million square feet of office and other space. We leased 0.2 million square feet of office space in Radnor, Pennsylvania, for our corporate center and for LFD. We leased 0.6 million square feet of office space in Fort Wayne, Indiana, primarily for our Annuities and Retirement Plan Services segments. We owned 0.8 million square feet of office space in Greensboro, North Carolina, primarily for our Life Insurance segment. We owned 0.3 million square feet of office space in Omaha, Nebraska, primarily for our Group Protection segment. An additional 0.3 million square feet of office space is leased for other office space.

Item 3. Legal Proceedings

For information regarding legal proceedings, see “Regulatory and Litigation Matters” in Note 17, which is incorporated herein by reference.

Item 4. Mine Safety Disclosures

Not applicable.

38

Table of Contents

Information About our Executive Officers

---

[3] Lincoln National (Lincoln Financial), fiscal year ended 2025-12-31 (LNC_FY2025_10K), Item 3
and Litigation Matters” in Note 17, which is incorporated herein by reference.

Item 4. Mine Safety Disclosures

Not applicable.

38

Table of Contents

Information About our Executive Officers

Our Executive Officers as of February 12, 2026, were as follows:
Name | Age (1) | Position with LNC and Business Experience During the Past Five Years
Ellen G. Cooper | 61 | President, Chief Executive Officer and Director (since May 2022); Chairman of the Board of Directors (since May 2023). Until May 2022, Executive Vice President (since August 2012), Head of Enterprise Risk (since 2019) and Head of Annuity Solutions Group (since March 2021). Chief Investment Officer (August 2012 - November 2021).
Nilanjan (Neel) Adhya | 51 | Executive Vice President, Chief AI, Data and Analytics Officer (since January 2026). Chief Digital Officer and Global Head of Digital Platforms and Experiences (August 2021 - December 2025), BlackRock, an investment management corporation. Chief Digital Officer and Vice President of Digital Transformation (June 2019 - August 2021), IBM, a technology company.
Craig T. Beazer | 58 | Executive Vice President and General Counsel (since December 2020).
Jennifer Charters | 53 | Executive Vice President and Chief Information Officer (since November 2024). Executive Vice President and Chief Information Officer, Flagstar Bank (June 2018 - August 2024).

---

[4] Lincoln National (Lincoln Financial), fiscal year ended 2025-12-31 (LNC_FY2025_10K), Item 15
Pursuant to the requirements of Section 13 or 15(d) of the Securities Exchange Act of 1934, LNC has duly caused this report to be signed on its behalf by the undersigned, thereunto duly authorized.

LINCOLN NATIONAL CORPORATION
Dated: February 19, 2026 | By: | /s/ Christopher Neczypor
Christopher Neczypor
Executive Vice President and Chief Financial Officer

Pursuant to the requirements of the Securities Exchange Act of 1934, this report has been signed below by the following persons on behalf of the registrant and in the capacities indicated on February 19, 2026.

Signature | Title
/s/ Ellen G. Cooper | President, Chief Executive Officer and Director
Ellen G. Cooper | (Principal Executive Officer)
/s/ Christopher Neczypor | Executive Vice President and Chief Financial Officer
Christopher Neczypor | (Principal Financial Officer)
/s/ Adam Cohen | Senior Vice President, Chief Accounting Officer and Treasurer
Adam Cohen | (Principal Accounting Officer)
/s/ Deirdre P. Connelly | Director
Deirdre P. Connelly
/s/ William H. Cunningham | Director
William H. Cunningham
/s/ Reginald E. Davis | Director
Reginald E. Davis
/s/ Eric G. Johnson | Director
Eric G. Johnson
/s/ Gary C. Kelly | Director
Gary C. Kelly
/s/ M. Leanne Lachman | Director
M. Leanne Lachman
/s/ Dale LeFebvre | Director
Dale LeFebvre
/s/ James Morris | Director
James Morris
/s/ Owen Ryan | Director
Owen Ryan

237

Table of Contents

Index to Financial Statement Schedules

---

[5] Lincoln National (Lincoln Financial), fiscal year ended 2025-12-31 (LNC_FY2025_10K), Item 1
registration requirements. We regard our trademarks as valuable assets in marketing our products and services and intend to protect them against infringement and dilution.

HUMAN CAPITAL MANAGEMENT

As of December 31, 2025, we had a total of 9,423 employees. Our mission is to provide financial protection and security to our customers and their families by offering products and services across our four core businesses. We believe that every move we make, including how we manage talent, shapes the future we share with our customers, communities and investors. Accordingly, each of our employees has access to important resources designed to, among other things, help them improve their well-being, understand the value of their work, develop their careers and thrive. From the moment our employees become part of Lincoln, they’re empowered to live and act with integrity, accountability and passion in their communities, relationships and daily interactions with colleagues and clients. Our enterprise strategy is driven by continued focus on this unique employee culture, including the following key areas:

Employee Feedback and Employee Engagement
```

</details>

---

## q013 · single_fact

**Question:** How much in client assets did Principal administer at the end of 2025, and how much of that did it manage?

**Gold answer:** $1,814.6 billion in assets under administration, including $781.0 billion in assets under management.

**Key points:**
1. $1,814.6 billion AUA
2. $781.0 billion AUM

**System answer:**

> The excerpts don't give a company-wide figure for client assets administered or managed, so I can't answer for Principal as a whole. They do cover one business, Workplace Savings and Retirement Solutions (WSRS).
> 
> - **Administered (WSRS only):** As of December 31, 2025, WSRS served over 42,000 defined contribution plans with $625.3 billion in assets and over 1,600 defined benefit plans with $17.2 billion in assets [2]. Together that is about $642.5 billion, which is my own sum of the two figures.
> - **Managed by Principal (WSRS only):** About 30% of WSRS account values were managed by the Principal Asset Management segment. Third-party asset managers handled 66% without being under contract to sub-advise a Principal product, 2% were sub-advised, and 2% were employer securities [2].
> 
> The filing gives the 30% as a share of "account values" and doesn't tie it to the $642.5 billion total. Applying it would give a rough figure of about $193 billion, but that is only an estimate.
> 
> The other excerpts include Principal Asset Management segment revenue and earnings figures [3] but no total assets under management or administration. I can't say what Principal managed or administered across the whole company from these excerpts.

<details><summary>Excerpts the system saw</summary>

```
[1] Principal Financial Group (Principal), fiscal year ended 2025-12-31 (PFG_FY2025_10K), Item 8
over time as the service is performed based upon contractual rates applied to the market value of the clients’ portfolios.

The types of revenues from contracts with customers were as follows:

| | | | | | | | | |
| | For the year ended December 31,
| | 2025 | | 2024 | | 2023
| | (in millions)
Administrative service fee revenue | | $ | 587.5 | | $ | 651.1 | | $ | 539.5 |
Deposit account fee revenue | | | 13.3 | | | 12.4 | | | 11.3 |
Commission income | | | 5.9 | | | 3.6 | | | 1.9 |
Other fee revenue | | — | | — | | 3.6 |
Total revenues from contracts with customers | | 606.7 | | 667.1 | | 556.3 |
Fees and other revenues not within the scope of revenue recognition guidance | | 1,190.4 | | 1,123.3 | | 1,118.7 |
Total fees and other revenues | | 1,797.1 | | 1,790.4 | | 1,675.0 |
Premiums and other considerations | | 2,979.1 | | 3,136.9 | | 2,935.0 |
Net investment income | | 3,405.7 | | 3,048.8 | | 2,640.2 |
Total operating revenues | | $ | 8,181.9 | | $ | 7,976.1 | | $ | 7,250.2 |

Principal Asset Management

---

[2] Principal Financial Group (Principal), fiscal year ended 2025-12-31 (PFG_FY2025_10K), Item 1
investment options managed by our Principal Asset Management segment as well as third party asset managers. In addition, WSRS offers plan sponsors trust services through an affiliated trust company.

As of December 31, 2025, we provided WSRS products to (a) over 42,000 defined contribution plans including $625.3 billion in assets and covering approximately 11.3 million eligible plan participants, and (b) to over 1,600 defined benefit plans, including $17.2 billion in assets and covering over 371,000 eligible plan participants. As of December 31, 2025, approximately 30% of our WSRS account values were managed by our Principal Asset Management segment, 66% were managed entirely by the third party asset managers that were not under contract to sub-advise a PFG product, 2% were sub-advised and 2% represented employer securities.

Markets and Distribution

---

[3] Principal Financial Group (Principal), fiscal year ended 2025-12-31 (PFG_FY2025_10K), Item 7
Principal Asset Management Segment Summary Financial Data

The following table presents certain summary financial data relating to the Principal Asset Management segment for the periods indicated:

| | | | | | | | |
| | For the year ended December 31,
| | | | | | | | Increase
| | 2025 | | 2024 | | (decrease)
| | (in millions)
Operating revenues: | | | | | | | | |
Premiums and other considerations | | $ | 5.9 | | $ | 28.7 | | $ | (22.8)
Fees and other revenues | | 2,140.8 | | | 2,076.0 | | | 64.8
Net investment income | | 664.2 | | | 685.7 | | | (21.5)
Total operating revenues | | 2,810.9 | | | 2,790.4 | | | 20.5
Expenses: | | | | | | | |
Benefits, claims and settlement expenses | | 297.7 | | | 362.2 | | | (64.5)
Liability for future policy benefits remeasurement (gain) loss | | | (0.4) | | | 1.0 | | | (1.4)
Operating expenses | | 1,566.9 | | | 1,551.6 | | | 15.3
Total expenses | | 1,864.2 | | | 1,914.8 | | | (50.6)
| | | | | | | | |
Pre‐tax operating earnings attributable to noncontrolling interest | | 16.5 | | | 14.4 | | | 2.1
Pre‐tax operating earnings | | $ | 930.2 | | $ | 861.2 | | $ | 69.0

Year Ended December 31, 2025 Compared to Year Ended December 31, 2024

Pre-Tax Operating Earnings

---

[4] Principal Financial Group (Principal), fiscal year ended 2025-12-31 (PFG_FY2025_10K), Item 8
five years is as follows (in millions):

| | |
Year ending December 31: | | |
2026 | | $ | 50.3
2027 | | | 50.0
2028 | | | 33.9
2029 | | | 32.5
2030 | | | 32.5

Indefinite Lived Intangible Assets

The net carrying amount of unamortized indefinite lived intangible assets was $764.3 million and $755.1 million as of December 31, 2025 and 2024, respectively. As of both December 31, 2025 and 2024, $608.0 million relates to investment management contracts associated with our acquisition of WM Advisors, Inc. in 2006. The remaining balance primarily relates to the trade name intangible associated with our acquisition of Administradora de Fondos de Pensiones Cuprum S.A. (“Cuprum”) in 2013.

99

Table of Contents

Principal Financial Group, Inc.

Notes to Consolidated Financial Statements – (continued)

December 31, 2025

3. Variable Interest Entities

We have relationships with various types of entities that may be VIEs. Certain VIEs are consolidated in our financial results. See Note 1, Nature of Operations and Significant Accounting Policies, under the caption “Consolidation” for further details of our consolidation accounting policies. We did not provide financial or other support to investees designated as VIEs for the periods ended December 31, 2025 and December 31, 2024.

Consolidated Variable Interest Entities

Mandatory Retirement Savings Funds

---

[5] Principal Financial Group (Principal), fiscal year ended 2025-12-31 (PFG_FY2025_10K), Item 1
of large-scale annuity sales in a particular quarter. The Principal Asset Management segment primarily manages the assets supporting pension risk transfer account values.

Markets and Distribution

Our primary distribution channel for pension risk transfer products is comprised of several specialized home office sales consultants working through consultants and brokers that specialize in this type of business. Our sales consultants also make sales directly to institutions. Our nationally dispersed retirement services sales representatives act as a secondary distribution channel for these products.

Bank and Trust Services

Principal Bank is a U.S. federal savings bank that was formed in February 1998. As of December 31, 2025, Principal Bank had nearly 816,000 customers and approximately $9.3 billion in assets. Principal Bank operates under a limited purpose charter and may only accept deposits held in a fiduciary capacity and may not hold demand deposits. It also may not own commercial loans or originate loans.

Principal Custody Solutions (“PCS”) is a division of Principal Bank that provides trust and/or custodial support services to clients in a variety of market segments including corporations, endowments, foundations, health care organizations, insurance and financial institutions, public entities and government institutions.
```

</details>

---

## q018 · single_fact

**Question:** What effective fee rate, excluding performance fees, did Franklin earn in fiscal 2026?

**Gold answer:** 40.7 basis points, versus 40.5 basis points in fiscal 2025.

**Key points:**
1. 40.7 basis points

**System answer:**

> Franklin's effective investment management fee rate excluding performance fees was 40.7 basis points in fiscal year 2026, compared with 40.5 basis points in fiscal 2025 [1]. The rate is calculated as investment management fees excluding performance fees divided by average AUM [1].

<details><summary>Excerpts the system saw</summary>

```
[1] Franklin Templeton (formerly Franklin Resources), fiscal year ended 2026-09-30 (BEN_FY2026_10K), Item 7
2026 primarily due to an increase in average equity, multi-asset and alternative AUM and the acquisition of Apera, partially offset by a decrease in performance fees and the impact of WAM outflows.

Our effective investment management fee rate excluding performance fees (investment management fees excluding performance fees divided by average AUM) was 40.7 and 40.5 basis points for fiscal years 2026 and 2025.

Performance fees were $414.1 million and $474.0 million for fiscal years 2026 and 2025. The decrease was primarily driven by lower performance fees earned by our alternative investment managers, partially offset by higher performance fees earned by our equity investment managers.

Our product offerings and global operations are diverse. As such, the impact of future changes in AUM on investment management fees will be affected by the relative mix of asset class, geographic region, distribution channel and investment vehicle of the assets.

Sales and Distribution Fees

---

[2] Franklin Templeton (formerly Franklin Resources), fiscal year ended 2026-09-30 (BEN_FY2026_10K), Item 7
and multi-asset funds, partially offset by losses on global equity funds.

Expenses of consolidated investment products decreased $4.3 million in fiscal year 2026, due to activity of the funds.

Our investments in sponsored funds include initial cash investments made in the course of launching mutual fund and other investment product offerings, as well as investments for other business reasons. The market conditions that impact our AUM similarly affect the investment income earned or losses incurred on our investments in sponsored funds.

TAXES ON INCOME

Our effective income tax rate for fiscal year 2026 was 21.0% as compared to 30.2% in fiscal year 2025. The rate decrease in fiscal year 2026 was primarily due to a reduction in foreign earnings, an increase in net income attributable to noncontrolling interests, and the benefit from the release of a valuation allowance on capital loss carryforwards.

On July 4, 2025, the One Big Beautiful Bill Act (the “Act”) was signed into law. We have evaluated the impact of the Act on our consolidated financial statements, and we have concluded that there is no material impact.

Our effective income tax rate reflects the relative contributions of earnings in the jurisdictions in which we operate, which have varying tax rates. Changes in our pre-tax income mix, tax rates or tax legislation in such jurisdictions may affect our effective income tax rate and net income.

SUPPLEMENTAL NON-GAAP FINANCIAL MEASURES

---

[3] Franklin Templeton (formerly Franklin Resources), fiscal year ended 2026-09-30 (BEN_FY2026_10K), Item 7
and is not directed toward existing or potential clients of Franklin.

39

Table of Contents

OPERATING REVENUES

The table below presents the percentage change in each operating revenue category.

(in millions) | 2026 vs. 2025 | 2025 vs. 2024
for the fiscal years ended September 30, | 2026 | 2025 | 2024
Investment management fees | $ | 7,478.9 | $ | 6,981.8 | $ | 6,822.2 | 7 | % | 2 | %
Sales and distribution fees | 1,593.7 | 1,474.7 | 1,381.0 | 8 | % | 7 | %
Shareholder servicing fees | 289.4 | 264.5 | 229.3 | 9 | % | 15 | %
Other | 53.3 | 49.7 | 45.5 | 7 | % | 9 | %
Total Operating Revenues | $ | 9,415.3 | $ | 8,770.7 | $ | 8,478.0 | 7 | % | 3 | %

Investment Management Fees

Investment management fees are generally calculated under contractual arrangements with our investment products and the products for which we provide sub-advisory services as a percentage of AUM. Annual fee rates vary by asset class and type of services provided. Fee rates for products sold outside of the U.S. are generally higher than for U.S. products.

Investment management fees increased $497.1 million in fiscal year 2026 primarily due to an increase in average equity, multi-asset and alternative AUM and the acquisition of Apera, partially offset by a decrease in performance fees and the impact of WAM outflows.

---

[4] Franklin Templeton (formerly Franklin Resources), fiscal year ended 2026-09-30 (BEN_FY2026_10K), Item 7
at fair value.

Dividend and interest income increased $15.9 million in fiscal year 2026, primarily due to higher dividend income, partially offset by lower yields and lower average balances.

Investments held by the Company generated net gains of $13.0 million in fiscal year 2026, as compared to net losses of $37.6 million in the prior year. Net gains in the current year were primarily from assets invested for deferred compensation plans, partially offset by losses on investments measured at cost, adjusted for observable price changes and investments in nonconsolidated funds and separate accounts. Net losses in the prior year were primarily from investments measured at cost, adjusted for observable price changes and investments in nonconsolidated funds and separate accounts, partially offset by gains on assets invested for deferred compensation plans.

Equity method investees generated income of $90.8 million in fiscal year 2026 and $78.0 million in the prior year, largely related to various global alternative funds in the current year and global alternative and equity funds in the prior year.

Net foreign currency exchange gains were $5.1 million in fiscal year 2026, as compared to net losses of $11.6 million in the prior year, primarily due to fluctuations in the value of the U.S. dollar against the British Pound and Euro.

Other, net increased $57.6 million in fiscal year 2026, primarily due to gains recognized on the sale of owned office space.

---

[5] Franklin Templeton (formerly Franklin Resources), fiscal year ended 2026-09-30 (BEN_FY2026_10K), Item 7
in fiscal year 2026 primarily due to an increase of 5% in the related average AUM and a higher mix of equity funds, non-U.S. multi-asset funds and U.S. alternative funds, which generate higher fees.

Sales-based fees increased $19.7 million in fiscal year 2026 primarily due to a $10.3 million increase in contingent sales charges, driven by increased redemptions, and an increase of 13% in commissionable sales, partially offset by a higher mix of non-U.S. sales, which generate lower fees.

Shareholder Servicing Fees

Shareholder servicing fees are earned from our sponsored funds for providing transfer agency services, which include providing shareholder statements, transaction processing, client service and tax reporting. Shareholder servicing fees are determined based on a contractual margin, or a percentage of AUM and either the number of transactions in shareholder accounts or the number of shareholder accounts. Shareholder servicing fees also include fund reimbursements of expenses incurred while providing transfer agency services.

Shareholder servicing fees increased $24.9 million in fiscal year 2026, primarily due to higher levels of related AUM and increased revenue related to fees earned on a contractual basis.

OPERATING EXPENSES

The table below presents the percentage change in each operating expense category.
```

</details>

---

## q019 · multi_passage

**Question:** T. Rowe Price's AUM grew in 2025 even though clients withdrew money. What explains the growth, and which strategies and client types drove the withdrawals?

**Gold answer:** AUM rose $169.0 billion to $1,775.6 billion because $216.7 billion of market appreciation outweighed $56.9 billion of net cash outflows. Outflows came mainly from growth-oriented equity strategies, chiefly from financial intermediaries and institutional clients; fixed income, target date and alternatives saw inflows.

**Key points:**
1. market appreciation of $216.7 billion
2. net outflows of $56.9 billion
3. growth-oriented equity strategies
4. financial intermediaries and institutional clients

**System answer:**

> **What explains the growth:** T. Rowe Price's AUM rose $169.0 billion to $1,775.6 billion at December 31, 2025. Market appreciation, net of distributions not reinvested, added $216.7 billion, which more than offset net cash outflows of $56.9 billion [2]. Beginning July 1, 2025, AUM also includes managed account – model delivery portfolio assets, which had $9.2 billion at that date and are reflected in the increase [2]. Those figures reconcile: $216.7 billion less $56.9 billion is $159.8 billion, and adding the $9.2 billion gives the $169.0 billion increase [2]. The filing also describes higher average AUM, driven by stronger market returns and appreciation, as the reason investment advisory fees rose in 2025 and 2024, slightly offset by net outflows in both years [1].
> 
> **Which strategies and client types drove the withdrawals:** The excerpts don't say. They give the total net outflow of $56.9 billion and note that AUM is presented by asset class (equity, fixed income including money market, multi-asset, alternatives) and client type (institutional, retail) [2]. But the excerpts contain no breakdown of the outflows by those categories, so I can't say which ones drove them.

<details><summary>Excerpts the system saw</summary>

```
[1] T. Rowe Price, fiscal year ended 2025-12-31 (TROW_FY2025_10K), Item 7
and 2024, the increases in investment advisory fees were due to higher average AUM as stronger market returns and appreciation were slightly offset by net outflows in each of the last two years.

Performance-based advisory fees in each period were primarily from alternatives strategies, and the decline in 2025

Page 38

Table of Contents

from prior periods were primarily related to lower overall market returns.

Capital allocation-based income includes the change in accrued carried interest along with acquisition-related amortization and impairments. For 2025, the change in accrued carried interest increased net revenues by $149.5 million compared to $134.1 million for 2024. The year‐over‐year change reflects relative performance and market impacts between 2025 and 2024. Additionally, the decrease in acquisition-related amortization and impairments for 2025 compared to 2024 period was primarily due to higher impairments recognized in 2024.The firm realized carried interest of $117.8 million compared to $139.6 million in 2024.

---

[2] T. Rowe Price, fiscal year ended 2025-12-31 (TROW_FY2025_10K), Item 1
value and composition of our assets under management. Accordingly, fluctuations in financial markets and in the composition of assets under management impact our revenues and results of operations.

At December 31, 2025, we had $1,775.6 billion in assets under management, an increase of $169.0 billion from the end of 2024. This increase in assets under management was driven by market appreciation, net of distributions not reinvested, of $216.7 billion, offset by net cash outflows of $56.9 billion. Beginning on July 1, 2025, assets under management include managed account - model delivery portfolios assets, which had $9.2 billion in assets as of that date, and are reflected in the increase from December 31, 2024.

The following charts show our AUM (in billions) by asset class, client type, geography, and account type as of December 31 for the prior three years:

Equity | Institutional (3)
Fixed Income, including money market | Retail (4)
Multi-Asset (1)
Alternatives (2)

(1)The underlying AUM of the multi-asset products have been aggregated and presented in this category and not reported in the equity and fixed income rows.

---

[3] T. Rowe Price, fiscal year ended 2025-12-31 (TROW_FY2025_10K), Item 7
Price funds AUM that has outperformed for the time periods indicated. Total AUM included for this analysis includes $272B for 1 year, $262B for 3 years, $260B for 5 years, and $252B for 10 years.

(5) Composite net returns are calculated using the highest applicable separate account fee schedule. Excludes money market composites. All composites compared to official GIPS composite primary benchmark. The top chart reflects the percentage of T. Rowe Price composites with 1 year, 3 year, 5 year, and 10 year track record that are outperforming their benchmarks. The bottom chart reflects the percentage of T. Rowe Price composite AUM that has outperformed for the time periods indicated. Total AUM included for this analysis includes $1,565B for 1 year, $1,557B for 3 years, $1,551B for 5 years, and $1,512B for 10 years.

---

[4] BlackRock, fiscal year ended 2025-12-31 (BLK_FY2025_10K), Item 7
non-US dollar denominated AUM into US dollars for reporting purposes.

(4)
Average AUM is calculated as the average of the month-end spot AUM amounts for the trailing thirteen months.

47

AUM increased $2.5 trillion to $14.0 trillion at December 31, 2025 from $11.6 trillion at December 31, 2024, driven by market appreciation, net inflows, led by flows into ETFs, systematic active equities, private markets, outsourcing and cash, the positive impact of foreign exchange movements and AUM added from the HPS and ElmTree Transactions.

Net market appreciation of $1.5 trillion was primarily driven by US and global equity market appreciation.

AUM increased $221 billion due to the impact of foreign exchange movements, primarily driven by the weakening of the US dollar, largely against the euro, the British pound and the Canadian dollar.

For further discussion on AUM, see Part I, Item 1 – Business – Assets Under Management.

Component Changes in AUM for 2024

The following table presents the component changes in AUM by product type for 2024(1).

---

[5] BlackRock, fiscal year ended 2025-12-31 (BLK_FY2025_10K), Item 7
AUM amounts for the trailing thirteen months.

(5)
Amounts include commodity ETFs and ETPs.

The following table presents the component changes in AUM by client type and product type for 2024(1).

December 31, | Net inflows | Market | FX | December 31, | Full year average
(in millions) | 2023 | (outflows) | Acquisition (2) | change | impact (3) | 2024 | AUM (4)
Retail:
Equity | $ | 435,734 | $ | 15,285 | $ | 4,074 | $ | 54,257 | $ | (4,232 | ) | $ | 505,118 | $ | 485,161
Fixed income | 312,799 | 11,671 | — | 1,483 | (7,312 | ) | 318,641 | 316,520
Multi-asset | 139,537 | (2,328 | ) | — | 14,420 | (651 | ) | 150,978 | 147,169
Private markets | 16,449 | 18 | — | (473 | ) | (245 | ) | 15,749 | 16,055
Liquid alternatives | 24,418 | (121 | ) | — | 538 | (100 | ) | 24,735 | 24,372
Retail subtotal | 928,937 | 24,525 | 4,074 | 70,225 | (12,540 | ) | 1,015,221 | 989,277
ETFs:
Equity | 2,532,631 | 236,357 | — | 359,322 | (21,912 | ) | 3,106,398 | 2,845,456
Fixed income | 898,403 | 112,341 | — | (16,291 | ) | (8,801 | ) | 985,652 | 948,250
Multi-asset | 9,140 | 1,025 | — | 841 | (272 | ) | 10,734 | 9,451
Digital assets | — | 40,815 | — | 14,491 | — | 55,306 | 22,486
Commodities | 59,125 | (105 | ) | — | 13,428 | (163 | ) | 72,285 | 66,845
ETFs subtotal | 3,499,299 | 390,433 | — | 371,791 | (31,148 | ) | 4,230,375 | 3,892,488
Institutional:
Active:
Equity | 186,688 | 5,380 | — | 30,876 | (4,096 | ) | 218,848 | 207,929
```

</details>

---

## q021 · multi_passage

**Question:** What did BlackRock donate in December 2025, what did it cost, and how did it factor into the year's decline in GAAP operating income?

**Gold answer:** BlackRock contributed part of its stake in Circle Internet Group to the BlackRock Charitable Fund, creating a $109 million operating expense (offset by a $29 million tax benefit). This noncash contribution, along with noncash acquisition-related expenses, drove the $529 million decline in GAAP operating income to $7.0 billion.

**Key points:**
1. part of its Circle stake
2. $109 million expense
3. $29 million tax benefit
4. contributed to the $529 million operating income decline

**System answer:**

> The excerpts don't say what BlackRock donated or when, only that it made a "Charitable Contribution." They do give the cost and its effect on operating results.
> 
> - **Cost:** The Charitable Contribution was noncash and totaled $109 million in 2025 [5]. The excerpts do not identify the recipient, the asset donated, or confirm that it occurred in December 2025.
> - **Effect on operating income:** GAAP operating income was $7.0 billion in 2025, down $529 million from 2024, and operating margin fell 800 bps to 29.1% [1]. The excerpt attributes these decreases to noncash acquisition-related expenses and the noncash Charitable Contribution [1], even as revenue rose [1]. The $109 million is part of the expense base, and it is recorded in general and administration expense [5]. Operating income went from $7,574 million in 2024 to $7,045 million in 2025 [3].
> - **Other items:** The year also included a $39 million restructuring charge [1][5]. By comparison, 2024 expense included a $50 million noncash impairment charge [1].
> - **Tax effect:** The contribution produced a discrete tax benefit of $29 million [4]. The as-adjusted effective tax rate of 21.5% excluded the tax impact of the contribution because of its nonrecurring nature [4].
> 
> The excerpts do not break out how much of the $529 million decline is due specifically to the contribution. They name it as one of two drivers, alongside the noncash acquisition-related expenses [1].

<details><summary>Excerpts the system saw</summary>

```
[1] BlackRock, fiscal year ended 2025-12-31 (BLK_FY2025_10K), Item 7
7.7 million Subco Units outstanding.

(5)
Total BlackRock stockholders’ equity divided by total shares of common stock outstanding at December 31 of the respective year-end.

2025 Compared with 2024

GAAP. Operating income of $7.0 billion decreased $529 million and operating margin of 29.1% decreased 800 bps from 2024. Operating income and operating margin reflected higher revenue, driven by organic base fee growth, positive impact of markets and fees related to the HPS and GIP Transactions, as well as higher technology services and subscription revenue. Decreases in GAAP operating income and operating margin were driven by noncash acquisition-related expenses and the noncash Charitable Contribution. Operating income and operating margin for 2025 also included the impact of a $39 million restructuring charge, comprised of severance and compensation expense for accelerated vesting of previously granted deferred compensation awards, in connection with an initiative to modify the Company's organization to fit more closely with strategic priorities. In addition, expense for 2024 included a $50 million noncash impairment charge related to certain indefinite-lived open-end management contracts.

Nonoperating income (expense) net of NCI - CIPs decreased $266 million from 2024, primarily driven by lower net interest income (expense).

---

[2] BlackRock, fiscal year ended 2025-12-31 (BLK_FY2025_10K), Item FS
entity structure, $37 million related to vested stock-based compensation awards, and a net noncash discrete tax expense of $14 million related to the revaluation of deferred income tax liabilities

At December 31, 2025 and 2024, the Company had available state net operating loss carryforwards of $2.8 billion and $2.9 billion, respectively, which will begin to expire in 2027. At December 31, 2025 and 2024, the Company had foreign net operating loss carryforwards of $266 million and $193 million, respectively, of which $21 million will begin to expire in 2026. At December 31, 2025, the Company had foreign tax credit carryforwards for income tax purposes of $105 million which will begin to expire in 2034.

At December 31, 2025 and 2024, the Company had $181 million and $69 million of valuation allowances for deferred income tax assets, respectively, recorded on the consolidated statements of financial condition.

Current income taxes are recorded net on the consolidated statements of financial condition when related to the same tax jurisdiction. At December 31, 2025, the Company had current income taxes receivable and payable of $247 million and $188 million, respectively, recorded in other assets and accounts payable and accrued liabilities, respectively. At December 31, 2024, the Company had current income taxes receivable and payable of $215 million and $134 million, respectively, recorded in other assets and accounts payable and accrued liabilities, respectively.

---

[3] BlackRock, fiscal year ended 2025-12-31 (BLK_FY2025_10K), Item 7
investments. Amount for 2024 included a pre-tax gain of approximately $66 million in connection with a transaction related to a minority investment in the EquiLend Transaction.

Income Tax Expense

GAAP | As Adjusted (1)
(in millions) | 2025 | 2024 | 2025 | 2024
Operating income | $ | 7,045 | $ | 7,574 | $ | 9,600 | $ | 8,110
Total nonoperating income (expense) (2) | $ | 312 | $ | 578 | $ | 251 | $ | 533
Income before income taxes (2) | $ | 7,357 | $ | 8,152 | $ | 9,851 | $ | 8,643
Income tax expense | $ | 1,677 | $ | 1,783 | $ | 2,115 | $ | 2,031
Effective tax rate | 22.8 | % | 21.9 | % | 21.5 | % | 23.5 | %

(1)
As adjusted items are described in more detail in Non-GAAP Financial Measures.

(2)
Net of net income (loss) attributable to NCI - CIPs.

The Company’s tax rate is affected by tax rates in foreign jurisdictions and the relative amount of income earned in those jurisdictions, which the Company expects to be fairly consistent in the near term. The significant foreign jurisdictions that have different statutory tax rates than the US federal statutory rate of 21% include the UK, Channel Islands, British Virgin Islands and Germany.

2025 Income tax expense (GAAP) reflected:

•
a net discrete tax benefit of $251 million realized from changes in the Company's organizational entity structure;

•
a discrete tax benefit of $67 million related to stock-based compensation awards that vested in 2025; and

---

[4] BlackRock, fiscal year ended 2025-12-31 (BLK_FY2025_10K), Item 7
of $251 million realized from changes in the Company's organizational entity structure;

•
a discrete tax benefit of $67 million related to stock-based compensation awards that vested in 2025; and

•
a discrete tax benefit of $29 million recognized in connection with the Charitable Contribution.

The as adjusted effective tax rate of 21.5% for 2025 excluded the tax impact associated with the Charitable Contribution due to its nonrecurring nature.

On July 4, 2025, the One Big Beautiful Bill Act was enacted into law, which includes permanently extending key tax provisions from the Tax Cuts and Jobs Act and modifications to the international tax framework. The Company is evaluating the impact of these provisions on the Company's consolidated financial statements.

2024 Income tax expense (GAAP) reflected:

•
a discrete tax benefit of $137 million recognized in connection with the reorganization and establishment of a more efficient global intellectual property and technology platform and corporate structure;

•
a discrete tax benefit of $63 million related to the realization of changes in the Company's organizational entity structure;

•
a net discrete tax benefit of $37 million related to stock-based compensation awards that vested in 2024; and

•
a $14 million net noncash tax expense related to the revaluation of certain deferred income tax liabilities.

---

[5] BlackRock, fiscal year ended 2025-12-31 (BLK_FY2025_10K), Item 7
a noncash Charitable Contribution(1) of $109 million and a restructuring charge(1) of $39 million. Expense for 2024 included the previously mentioned noncash impairment charge of $50 million.

Employee compensation and benefits expense of $8.4 billion in 2025 increased $1.9 billion from $6.5 billion in 2024, primarily reflecting the impact of the GIP, HPS and Preqin Transactions, including nonrecurring retention-related deferred compensation expense(1) and higher incentive compensation as a result of higher operating income and performance fees.

Sales, asset and account expense of $4.5 billion in 2025 increased $685 million from $3.8 billion in 2024, driven by higher direct fund expense and distribution and servicing costs, primarily reflecting higher average AUM.

General and administration expense of $2.7 billion in 2025 increased $474 million from $2.3 billion in 2024, primarily associated with the impact of the GIP, HPS and Preqin Transactions, including higher acquisition-related transaction costs(1) recorded in professional services, as well as the Charitable Contribution(1) and higher technology expense, and marketing and promotional expense, including the impact from higher travel and entertainment expense.

Change in fair value of contingent consideration(1) of $720 million in 2025 increased $756 million from $(36) million in 2024, primarily due to the impact of the GIP and HPS Transactions.
```

</details>

---

## q022 · multi_passage

**Question:** How did BlackRock pay for HPS Investment Partners, and how many of those instruments were outstanding at year-end 2025 compared with its common shares?

**Gold answer:** Substantially all consideration was paid in Class B-2 common units of BlackRock Saturn Subco (Subco Units). At December 31, 2025 there were 7.7 million Subco Units outstanding versus 155.1 million common shares.

**Key points:**
1. Subco Units (Class B-2 common units)
2. 7.7 million Subco Units
3. 155.1 million common shares

**System answer:**

> **How BlackRock paid:** BlackRock paid for HPS almost entirely with equity in a subsidiary rather than cash. Substantially all of the consideration was Class B-2 common units ("Subco Units") of BlackRock Saturn Subco, LLC, a consolidated subsidiary [2][5]. At the July 1, 2025 close, about 8.5 million Subco Units went to former HPS equityholders. They were valued at $8.5 billion, based on BlackRock's June 30, 2025 stock price of about $1,049 and discounted for a one-year lack of marketability before exchange rights begin [2].
> 
> **Outstanding at year-end 2025:** About 7.7 million Subco Units were outstanding at December 31, 2025 [3].
> 
> **Comparison with common shares:** The excerpts don't give BlackRock's number of common shares outstanding, so I can't say how the 7.7 million units compare with the common share count. The only per-share information provided is the dividend and the June 30, 2025 stock price, and neither gives the share count directly [2][3].

<details><summary>Excerpts the system saw</summary>

```
[1] BlackRock, fiscal year ended 2025-12-31 (BLK_FY2025_10K), Item front matter
Certain Relationships and Related Transactions, and Director Independence | 68
Item 14 | Principal Accountant Fees and Services | 68
PART IV
Item 15 | Exhibits and Financial Statement Schedules | 69
Item 16 | Form 10-K Summary | 72
Signatures | 73

Part I

Item 1. Business

Overview

BlackRock, Inc. (together, with its subsidiaries, unless the context otherwise indicates, “BlackRock” or the “Company”) is a leading publicly traded investment management firm with $14.0 trillion of assets under management (“AUM”) at December 31, 2025. With approximately 24,900 employees in more than 30 countries who serve clients in over 100 countries across the globe, BlackRock provides a broad range of investment management and technology and subscription services to institutional and retail clients worldwide. On July 1, 2025, BlackRock completed the acquisition of 100% of the business and assets of HPS Investment Partners (the "HPS Transaction" or "HPS"), a leading global credit investment manager, with substantially all consideration paid in Class B-2 common units ("Subco Units") of BlackRock Saturn Subco, LLC ("Subco"), a consolidated subsidiary of the Company. Concurrent with the acquisition, BlackRock Finance, Inc., Global Infrastructure Management, LLC ("GIP"), HPS, and their respective subsidiaries became wholly owned subsidiaries of Subco.

---

[2] BlackRock, fiscal year ended 2025-12-31 (BLK_FY2025_10K), Item FS
in earnings and, where applicable, are offset by the corresponding gain or loss on the related foreign-denominated or hedged assets or liabilities, on the consolidated statements of income.

The Company may also use financial instruments designated as net investment hedges for accounting purposes to hedge net investments in international subsidiaries, the functional currency of which is not US dollars. The gain or loss from revaluing net investment hedges at the spot rate is deferred and reported within AOCI on the consolidated statements of financial condition. The Company reassesses the effectiveness of its net investment hedge at least quarterly.

3. Acquisitions

HPS Investment Partners

On July 1, 2025, BlackRock completed the acquisition of 100% of the business and assets of HPS, a leading global credit investment manager, with substantially all consideration paid in Subco Units. The HPS Transaction, which added $165 billion of client AUM and $118 billion of fee-paying AUM, positions the Company to provide an integrated private credit platform with both public and private income solutions for clients across their whole portfolios. At close, approximately 8.5 million Subco Units were delivered to former equityholders of HPS and valued at $8.5 billion, based on the price of BlackRock's common stock on June 30, 2025 of approximately $1,049 and discounted for a one-year lack of marketability before exchange rights begin.

---

[3] BlackRock, fiscal year ended 2025-12-31 (BLK_FY2025_10K), Item FS
| )
Foreign currency translation adjustments (1) | 606 | ( 338 | ) | 261
Change in BlackRock, Inc.'s ownership interest | 27 | — | —
Ending balance | $ | ( 545 | ) | $ | ( 1,178 | ) | $ | ( 840 | )

(1)
Amount for 2025 includes a loss from a net investment hedge of $96 million (net of tax benefit of $30 million). Amount for 2024 includes a gain from a net investment hedge of $37 million (net of tax expense of $12 million). Amount for 2023 includes a loss from a net investment hedge of $20 million (net of tax benefit of $6 million).

23. Capital Stock

Cash Dividends for Common Shares / RSUs. During 2025, 2024 and 2023, the Company paid cash dividends of $20.84 per share (or $3.3 billion), $20.40 per share (or $3.1 billion) and $20.00 per share (or $3.0 billion), respectively.

The HPS Transaction. On July 1, 2025, as part of the closing of the HPS Transaction, the Company issued approximately 8.5 million Subco Units to former equity holders of HPS. See Note 1, Business Overview, Note 2, Significant Accounting Policies, and Note 3, Acquisitions, for additional information. As of December 31, 2025, there were approximately 7.7 million Subco Units outstanding.

F-39

---

[4] BlackRock, fiscal year ended 2025-12-31 (BLK_FY2025_10K), Item FS
) | $ | ( 949 | )
Established contingent consideration liabilities in connection with acquisitions | $ | 3,413 | $ | 4,246 | $ | —

See accompanying notes to consolidated financial statements.

F-8

BlackRock, Inc.

Notes to the Consolidated Financial Statements

1. Business Overview

BlackRock, Inc. (together, with its subsidiaries, unless the context otherwise indicates, “BlackRock” or the “Company”) is a leading publicly traded investment management firm providing a broad range of investment management and technology services to institutional and retail clients worldwide. On July 1, 2025, BlackRock completed the acquisition of 100% of the business and assets of HPS Investment Partners (the "HPS Transaction" or "HPS"), a leading global credit investment manager, with substantially all consideration paid in Class B-2 common units ("Subco Units") of BlackRock Saturn Subco, LLC ("Subco"), a consolidated subsidiary of the Company. Concurrent with the acquisition, BlackRock Finance, Inc., Global Infrastructure Management, LLC ("GIP"), HPS, and their respective subsidiaries became wholly owned subsidiaries of Subco. See Note 3, Acquisitions, for information on the HPS Transaction.

---

[5] BlackRock, fiscal year ended 2025-12-31 (BLK_FY2025_10K), Item 7
December 31, 2024, which was filed with the SEC on February 25, 2025.

Certain prior period presentations were reclassified to ensure comparability with current period classifications.

Acquisitions

On March 3, 2025, BlackRock completed the acquisition of 100% of the shares of Preqin, a leading provider of private markets data, for £2.5 billion (or approximately $3.2 billion) in cash. The Company believes bringing together Preqin's data and research tools with the complementary workflows of Aladdin and eFront in a unified platform will create a preeminent private markets technology and data provider.

38

On July 1, 2025, BlackRock completed the acquisition of 100% of the business and assets of HPS, a leading global credit investment manager, with substantially all consideration paid in Class B-2 common units ("Subco Units") of BlackRock Saturn Subco, LLC ("Subco"), a consolidated subsidiary of the Company. The HPS Transaction, which added $165 billion of client AUM and $118 billion of fee-paying AUM, positions the Company to provide an integrated private credit platform with both public and private income solutions for clients across their whole portfolios. At close, approximately 8.5 million Subco Units were delivered to former equityholders of HPS and valued at $8.5 billion, based on the price of BlackRock's common stock on June 30, 2025 of approximately $1,049 and discounted for a one-year lack of marketability before exchange rights begin.
```

</details>

---

## q026 · multi_passage

**Question:** Who does Lincoln's top information security executive report to, how often do they brief the board's Audit Committee, and how large is their team?

**Gold answer:** The CISO reports directly to the Chief Information Officer (a Senior Management Committee member) and indirectly to the Audit Committee, briefing it twice a year (biannually). The CISO has a staff of more than 100 employees.

**Key points:**
1. reports to the CIO
2. briefs Audit Committee biannually
3. more than 100 staff

**System answer:**

> Lincoln's top information security executive is the Chief Information Security Officer (CISO).
> 
> - **Reporting line:** The CISO reports directly to the Company's Chief Information Officer (CIO), who is a member of the Senior Management Committee. The CISO also reports indirectly to the Audit Committee of the Board of Directors [1].
> - **Frequency of Audit Committee briefings:** The CISO reports to the Audit Committee biannually on the cybersecurity risks facing the Company and on cybersecurity developments generally [1]. Other reporting to the Audit Committee comes from different functions. Internal Audit reports the results of its annual security audit, and the Chief Compliance Officer reports key Privacy risk indicators quarterly [1].
> - **Team size:** The CISO has a staff of more than 100 employees dedicated to protecting data and systems belonging to the Company, its customers, business partners and consumers [1].

<details><summary>Excerpts the system saw</summary>

```
[1] Lincoln National (Lincoln Financial), fiscal year ended 2025-12-31 (LNC_FY2025_10K), Item 1C
which provides oversight of our enterprise-wide risk structure and of our processes to identify, measure, monitor and manage significant risks, including, but not limited to, cybersecurity risk.

The Information Security organization is led by our CISO. The head of each of the four divisions of our Information Security team reports directly to the CISO. The CISO reports directly to the Company’s Chief Information Officer (“CIO”), who is a member of the Company’s Senior Management Committee. As a result, all information security personnel report into the CISO, and ultimately the CIO. The CISO also reports indirectly to the Audit Committee of the Board of Directors. Biannually, the CISO reports to the Audit Committee on the cybersecurity risks facing the Company and cybersecurity developments generally. In addition, as discussed above, the Company’s Internal Audit team reports to the Audit Committee the results of its annual security audit focused on cybersecurity risks. The Company’s Chief Compliance Officer reports key Privacy risk indicators and statistics (including those related to cybersecurity risks) to the Audit Committee on a quarterly basis.

Our current CISO has over 20 years of experience in the field of cybersecurity and holds a Certified Information Security Systems Professional designation. The CISO has a staff of more than 100 employees dedicated to protecting the data and systems belonging to the Company, our customers, business partners and consumers.

37

---

[2] Lincoln National (Lincoln Financial), fiscal year ended 2025-12-31 (LNC_FY2025_10K), Item 1C
Audit Committee of the Company’s Board of Directors. This audit process provides an additional layer of support to help ensure that cybersecurity risks are managed and responded to appropriately.

While our Information Security team uses some third-party resources as part of its efforts to assess, identify and manage material risks from cybersecurity threats (e.g., certain third-party software tools, threat intelligence and periodic penetration testing), our cybersecurity efforts are predominantly conducted through our internal resources.

Monitoring and Incident Response

The CSRI division of our Information Security team is responsible for the operation of our internal Security Operations Center (“SOC”), which performs monitoring and alerting for security events 24 hours a day, 7 days a week, 365 days a year. The CSRI division also actively seeks out cybersecurity threats that might affect the organization and/or our customers. The CSRI team is a component of Lincoln’s formal security incident response team (“SIRT”) and process. In addition to the Information Security team, the SIRT also includes representatives from the Company’s legal and compliance teams (including Privacy), office of business resiliency, chief risk office, corporate communications, as well as the information technology team. While the CSRI division is responsible for cybersecurity responses generally, should a critical event arise, such an event would be raised to and addressed by the SIRT.

36

---

[3] Lincoln National (Lincoln Financial), fiscal year ended 2025-12-31 (LNC_FY2025_10K), Item 1C
risks. The Board has also delegated certain of its risk oversight efforts to its committees. Oversight of cybersecurity risk has been delegated to the Audit Committee of the Board of Directors.

The Company’s senior management is primarily responsible for establishing policies and procedures designed to identify, assess and manage the Company’s significant risks, with our Chief Information Security Officer (“CISO”) having primary responsibility with respect to material risks from cybersecurity threats. We also have a Corporate Enterprise Risk and Capital Committee, made up of members of senior management and the Company’s Chief Risk Officer, which provides oversight of our enterprise-wide risk structure and of our processes to identify, measure, monitor and manage significant risks, including, but not limited to, cybersecurity risk.

---

[4] Lincoln National (Lincoln Financial), fiscal year ended 2025-12-31 (LNC_FY2025_10K), Item 1C
subject to third-party information system and other operational risks due to our reliance on third-party vendors and suppliers and the outsourcing of certain of our business operations” and “Item 1A. Risk Factors – Legislative, Regulatory and Tax – Compliance with existing and emerging privacy laws and regulations could result in increased compliance costs and/or lead to changes in business practices and policies, and any failure to protect the confidentiality of personal information could adversely affect our reputation and have a material adverse effect on our business, financial condition and results of operations.”

Governance

The Company’s Board of Directors is responsible for regular oversight of the Company’s overall risk management process. The Board reviews the most significant risks the Company faces and the manner in which our executives manage these risks. The Board has also delegated certain of its risk oversight efforts to its committees. Oversight of cybersecurity risk has been delegated to the Audit Committee of the Board of Directors.

---

[5] Lincoln National (Lincoln Financial), fiscal year ended 2025-12-31 (LNC_FY2025_10K), Item 1C
technology team. While the CSRI division is responsible for cybersecurity responses generally, should a critical event arise, such an event would be raised to and addressed by the SIRT.

36

Table of Contents

Our Privacy team, which is part of the Company’s compliance function, has a dedicated incident response team responsible for assessing, identifying and managing risks from cybersecurity threats involving personal information. The team follows documented processes for investigation, research, assessment, notification, regulatory reporting and, if necessary, escalation to management, and such processes have been integrated into our Information Security incident response program. The Information Security team works closely with our Privacy team to respond to any cybersecurity incidents involving personal information. The Privacy team engages third parties to assist with incident assessment and notification.

Supplier Risk Management and Strategy
```

</details>

---

## q027 · multi_passage

**Question:** Why does Principal Financial Group's capacity to return capital hinge on Principal Life, and how much could Principal Life pay out in 2026 without asking the Iowa regulator?

**Gold answer:** As a holding company, PFG's ability to pay dividends, repurchase shares and meet obligations depends on dividends and distributions from Principal Life, which Iowa law limits. Based on 2025 statutory results, Principal Life could pay about $1,234.0 million in ordinary dividends in 2026 without prior approval.

**Key points:**
1. depends on distributions from Principal Life
2. Iowa limits
3. about $1,234.0 million in 2026

**System answer:**

> Why it hinges on Principal Life: Principal Financial Group (PFG) is an insurance holding company whose assets include all the outstanding common stock of Principal Life and other subsidiaries. Its ability to pay stockholder dividends, make share repurchases, and meet obligations (operating expenses and debt service) depends on receiving dividends or other distributions from Principal Life [2]. Iowa insurance laws limit what Principal Life can pay to its parent, so any inability of Principal Life to pay could leave PFG unable to pay dividends to stockholders or meet other obligations [2].
> 
> The Iowa limits: Principal Life may pay dividends only from earned surplus arising from its business. It needs prior approval from the Iowa Commissioner of Insurance for any distribution exceeding certain statutory limits, and the Commissioner has discretion to disapprove requests above those limits [1][3]. Extraordinary dividends are those that, together with other distributions in the preceding twelve months, exceed the greater of (i) 10% of statutory policyholder surplus at the previous year-end (excluding admitted disallowed interest maintenance reserve) or (ii) the prior calendar year's statutory net gain from operations, not to exceed earned surplus [1][3].
> 
> 2026 capacity without approval: Based on 2025 statutory results, Principal Life could pay approximately $1,234.0 million in ordinary stockholder dividends in 2026 without prior regulatory approval [3]. There is a caveat: because the test looks at dividends paid over rolling twelve-month periods, if dividends are paid before a specified date in 2026, some or all may be extraordinary and require approval [5].
> 
> Context: Principal Life paid $1,055.0 million in 2025 and $1,010.0 million in 2024, all of it extraordinary and approved by the Commissioner [5]. PFG also had $2,362.3 million of cash and liquid assets in its holding companies and other subsidiaries at December 31, 2025, available for corporate purposes [5].

<details><summary>Excerpts the system saw</summary>

```
[1] Principal Financial Group (Principal), fiscal year ended 2025-12-31 (PFG_FY2025_10K), Item 7
and other factors deemed relevant by the Board. No significant restrictions limit the payment of dividends by PFG, except those generally applicable to corporations incorporated in Delaware.

Dividends or other distributions from Principal Life, our primary subsidiary, are limited by Iowa law. Under Iowa law, Principal Life may pay dividends or make other distributions only from the earned surplus arising from its business and must receive the prior approval of the Commissioner of Insurance of the State of Iowa (the “Commissioner”) to pay stockholder dividends or make any other distribution if such distribution would exceed certain statutory limitations. Iowa law gives the Commissioner discretion to disapprove requests for distributions in excess of these limitations. Extraordinary dividends include those made, together with dividends and other distributions, within the preceding twelve months that exceed the greater of (i) 10% of statutory policyholder surplus as of the previous year-end excluding admitted disallowed interest maintenance reserve or (ii) the statutory net gain from operations from the previous calendar year, not to exceed earned surplus. Based on statutory results for the year ended December 31, 2025, the ordinary stockholder dividend limitation for Principal Life is approximately $1,234.0 million in 2026.

---

[2] Principal Financial Group (Principal), fiscal year ended 2025-12-31 (PFG_FY2025_10K), Item 1A
to pay stockholder dividends, make share repurchases and meet our obligations may be constrained by the limitations on dividends or other distributions Iowa insurance laws impose on Principal Life.

We are an insurance holding company whose assets include all the outstanding shares of the common stock of Principal Life and other subsidiaries. Our ability to pay dividends to our stockholders, make share repurchases and meet our obligations, including paying operating expenses and any debt service, depends upon the receipt of dividends or other distributions from Principal Life. Iowa insurance laws impose limitations on the ability of Principal Life to pay dividends or make other distributions to its parent. Any inability of Principal Life to pay dividends or make other distributions in the future may cause us to be unable to pay dividends to our stockholders and meet our other obligations. See Item 7. “Management’s Discussion and Analysis of Financial Condition and Results of Operations — Liquidity and Capital Resources” for a discussion of regulatory restrictions on Principal Life’s ability to pay dividends or make other distributions.

Changes in accounting standards may adversely affect our reported results of operations and financial condition.

---

[3] Principal Financial Group (Principal), fiscal year ended 2025-12-31 (PFG_FY2025_10K), Item 8
and other factors deemed relevant by the Board. No significant restrictions limit the payment of dividends by us, except those generally applicable to corporations incorporated in Delaware.

Under Iowa law, Principal Life may pay dividends or make other distributions only from the earned surplus arising from its business and must receive the prior approval of the Commissioner of Insurance of the State of Iowa (“the Commissioner”) to pay stockholder dividends or make any other distribution if such distribution would exceed certain statutory limitations. Iowa law gives the Commissioner discretion to disapprove requests for distributions in excess of these limitations. Extraordinary dividends include those made, together with dividends and other distributions, within the preceding twelve months that exceed the greater of (i) 10% of Principal Life’s statutory policyholder surplus as of the previous year-end excluding admitted disallowed interest maintenance reserve or (ii) the statutory net gain from operations from the previous calendar year, not to exceed earned surplus. Based on this limitation and 2025 statutory results, Principal Life could pay approximately $1,234.0 million in ordinary stockholder dividends in 2026 without prior regulatory approval.

---

[4] Principal Financial Group (Principal), fiscal year ended 2025-12-31 (PFG_FY2025_10K), Item 8
include penalties for early surrenders, minimum notice requirements or, in the case of funding agreements with survivor options, minimum pre-death holding periods and specific maximum amounts.

Funding agreements include those issued directly to nonqualified institutional investors and those issued to the FHLB Des Moines under their membership funding programs. As of December 31, 2025 and 2024, $3,972.5 million and $3,976.5 million, respectively, of liabilities were outstanding with respect to issuances under the program with FHLB Des Moines. In addition, we have five separate programs where the funding agreements have been issued directly or indirectly to unconsolidated special purpose entities. Claims for principal and interest under funding agreements are afforded equal priority to claims of life insurance and annuity policyholders under insolvency provisions of Iowa Insurance Laws.

Principal Life was authorized to issue up to $4.0 billion of funding agreements under a program established in 1998 to support the prospective issuance of medium term notes by an unaffiliated entity in non-U.S. markets. As of December 31, 2025 and 2024, $75.7 million and $75.8 million, respectively, of liabilities were outstanding with respect to the issuance outstanding under this program.

---

[5] Principal Financial Group (Principal), fiscal year ended 2025-12-31 (PFG_FY2025_10K), Item 7
to exceed earned surplus. Based on statutory results for the year ended December 31, 2025, the ordinary stockholder dividend limitation for Principal Life is approximately $1,234.0 million in 2026. However, because the dividend test is based on dividends previously paid over rolling twelve month periods, if paid before a specified date during 2026, some or all of such dividends may be extraordinary and require regulatory approval.

Total stockholder dividends paid by Principal Life to its parent in 2025 were $1,055.0 million, all of which was extraordinary and approved by the Commissioner. As of December 31, 2025, we had $2,362.3 million of cash and liquid assets held in our holding companies and other subsidiaries, which is available for corporate purposes. Corporate balances held in foreign holding companies meet the indefinite reinvestment exception.

In 2024, total stockholder dividends paid by Principal Life to its parent were $1,010.0 million, all of which was extraordinary and approved by the Commissioner.
```

</details>

---

## q029 · multi_passage

**Question:** What drove Franklin's rise in general and administrative expenses in fiscal 2026, and how is the largest driver treated in its adjusted operating income?

**Gold answer:** G&A rose $147.7 million, mainly from a $100.0 million regulatory settlement, plus a $33.2 million increase in contingent consideration fair value and $21.5 million in higher fund-related expenses. Charges for significant regulatory settlements are excluded from adjusted operating income.

**Key points:**
1. G&A up $147.7 million
2. $100.0 million regulatory settlement
3. excluded from adjusted operating income

**System answer:**

> **Drivers of the increase.** General, administrative and other operating expenses rose $147.7 million in fiscal 2026 [1]. The table shows the line going from $774.5 million to $922.2 million, a 19% increase [2]. The filing cites these drivers [1]:
> 
> - **A $100.0 million regulatory settlement.** This is the largest driver.
> - **A $33.2 million increase in the fair value of a contingent consideration liability.**
> - **A $21.5 million increase in fund-related expenses.** The filing attributes this to higher placement and platform fees.
> - **A $16.7 million decrease in advertising and promotion costs.** This partly offset the increases.
> 
> **Treatment in adjusted operating income.** The excerpts don't say how the $100.0 million regulatory settlement is treated in adjusted operating income. They mention a "Supplemental Non-GAAP Financial Measures" section only in footnotes on compensation items [3]. That section isn't included, so I can't say whether the settlement is excluded or included.

<details><summary>Excerpts the system saw</summary>

```
[1] Franklin Templeton (formerly Franklin Resources), fiscal year ended 2026-09-30 (BEN_FY2026_10K), Item 7
For certain vehicles, we may agree to compensate third parties for services provided by sharing a portion of the performance fees we earn. These payments are classified as sub-advisory expenses.

General, administrative and other operating expenses increased $147.7 million in fiscal year 2026, primarily due to a $100.0 million regulatory settlement, an increase of $33.2 million in the fair value of a contingent consideration liability, and an increase of $21.5 million in fund-related expenses due to higher placement and platform fees. These increases were partially offset by a decrease of $16.7 million in advertising and promotion costs.

43

Table of Contents

OTHER INCOME (EXPENSES)

Other income (expenses) consisted of the following:

(in millions) | 2026 vs. 2025 | 2025 vs. 2024
for the fiscal years ended September 30, | 2026 | 2025 | 2024
Investment and other income, net:
Dividend and interest income | $ | 157.3 | $ | 141.4 | $ | 176.9 | 11 | % | (20 | %)
Gains (losses) on investments, net | 13.0 | (37.6) | 57.6 | NM | NM
Income from investments in equity method investees | 90.8 | 78.0 | 137.5 | 16 | % | (43 | %)
Losses on crypto assets, net | (19.4) | — | — | NM | NM
Rental income | 45.6 | 44.1 | 43.7 | 3 | % | 1 | %
Foreign currency exchange gains (losses), net | 5.1 | (11.6) | (19.9) | NM | (42 | %)
Other, net | 56.1 | (1.5) | (0.3) | NM | 400 | %
Investment and other income, net | 348.5 | 212.8 | 395.5 | 64 | % | (46 | %)

---

[2] Franklin Templeton (formerly Franklin Resources), fiscal year ended 2026-09-30 (BEN_FY2026_10K), Item 7
levels of related AUM and increased revenue related to fees earned on a contractual basis.

OPERATING EXPENSES

The table below presents the percentage change in each operating expense category.

(in millions) | 2026 | 2025 | 2024 | 2026 vs. 2025 | 2025 vs. 2024
for the fiscal years ended September 30,
Compensation and benefits | $ | 3,963.4 | $ | 3,818.2 | $ | 3,831.1 | 4 | % | 0 | %
Sales, distribution and marketing | 2,200.5 | 2,010.9 | 1,863.1 | 9 | % | 8 | %
Information systems and technology | 644.7 | 643.6 | 620.1 | 0 | % | 4 | %
Occupancy | 277.2 | 286.3 | 325.4 | (3 | %) | (12 | %)
Amortization of intangible assets | 198.4 | 406.5 | 338.2 | (51 | %) | 20 | %
Impairment of intangible assets | 33.0 | 226.6 | 389.2 | (85 | %) | (42 | %)
General, administrative and other | 922.2 | 774.5 | 703.3 | 19 | % | 10 | %
Total Operating Expenses | $ | 8,239.4 | $ | 8,166.6 | $ | 8,070.4 | 1 | % | 1 | %

41

Table of Contents

Compensation and Benefits

The components of compensation and benefits expenses are presented below.

---

[3] Franklin Templeton (formerly Franklin Resources), fiscal year ended 2026-09-30 (BEN_FY2026_10K), Item 7
Expenses | $ | 8,239.4 | $ | 8,166.6 | $ | 8,070.4 | 1 | % | 1 | %

41

Table of Contents

Compensation and Benefits

The components of compensation and benefits expenses are presented below.

(in millions) | 2026 vs. 2025 | 2025 vs. 2024
for the fiscal years ended September 30, | 2026 | 2025 | 2024
Salaries, wages and benefits | $ | 1,747.5 | $ | 1,724.0 | $ | 1,686.6 | 1 | % | 2 | %
Incentive compensation | 1,762.0 | 1,676.6 | 1,613.7 | 5 | % | 4 | %
Acquisition-related retention 1 | 75.1 | 162.4 | 263.6 | (54 | %) | (38 | %)
Acquisition-related performance fee pass through 1 | 76.7 | 106.7 | 97.5 | (28 | %) | 9 | %
Other 1, 2 | 302.1 | 148.5 | 169.7 | 103 | % | (12 | %)
Compensation and Benefits Expenses | $ | 3,963.4 | $ | 3,818.2 | $ | 3,831.1 | 4 | % | 0 | %

_______________

1 See “Supplemental Non-GAAP Financial Measures” for additional information.

2 Includes impact of gains and losses on investments related to deferred compensation plans, which is offset in investment and other income (losses), net; minority interests in certain subsidiaries, which is offset in net income (loss) attributable to redeemable noncontrolling interests; and termination benefits.

Salaries, wages and benefits increased $23.5 million in fiscal year 2026 primarily due to annual salary increases, higher post-retirement benefit costs and additional compensation expenses associated with the acquisition of Apera, partially offset by savings from cost reduction initiatives.

---

[4] Franklin Templeton (formerly Franklin Resources), fiscal year ended 2026-09-30 (BEN_FY2026_10K), Item 7
distribution costs.

Sales-based expenses increased $8.6 million in fiscal year 2026 primarily due to an increase of 13% in commissionable sales, partially offset by a higher mix of non-U.S. sales.

Amortization of deferred sales commissions increased $17.2 million in fiscal year 2026 primarily due to higher sales.

Occupancy

Occupancy expenses decreased $9.1 million in fiscal year 2026, primarily due to initiatives to reduce office space, including the consolidation of our office space in New York City.

Amortization of intangible assets

Amortization of intangible assets decreased $208.1 million in fiscal year 2026, primarily due to the effect of intangible assets which became fully amortized during fiscal years 2026 and 2025, partially offset by an increase in amortization due to the reclassification of certain indefinite-lived intangible assets to definite-lived intangible assets and a reduction in the useful lives of certain definite-lived intangible assets related to trade names.

Impairment of intangible assets

---

[5] Franklin Templeton (formerly Franklin Resources), fiscal year ended 2026-09-30 (BEN_FY2026_10K), Item 7
30, | 2026 | 2025 | 2024
Operating cash flows | $ | 836.7 | $ | 1,066.1 | $ | 971.3
Investing cash flows | (4,323.0) | (2,342.7) | (2,423.7)
Financing cash flows | 4,335.9 | 452.4 | 1,415.6

Net cash provided by operating activities decreased in fiscal year 2026 primarily due to higher net purchases of investments by consolidated investment products partially offset by an increase in accounts payable, accrued expenses and other liabilities. Net cash used in investing activities increased as compared to the prior year primarily due to higher net purchases of investments by collateralized loan obligations partially offset by net consolidation of CIPs as compared to net deconsolidation in the prior year. Net cash provided by financing activities increased as compared to the prior year primarily due to higher net proceeds from debt of CIPs and higher net proceeds from issuance of debt.

49

Table of Contents
```

</details>

---

## q030 · multi_passage

**Question:** Which firm did Franklin acquire at the start of fiscal 2026, and what part did it play in the change in investment management fees that year?

**Gold answer:** Apera Asset Management, a pan-European private credit firm, acquired October 1, 2025. Investment management fees rose $497.1 million, driven by higher average equity, multi-asset and alternative AUM and the Apera acquisition, partly offset by lower performance fees and WAM outflows.

**Key points:**
1. Apera Asset Management
2. October 1, 2025
3. fees up $497.1 million
4. Apera contributed to the increase

**System answer:**

> Franklin acquired Apera Asset Management ("Apera"), a pan-European private credit firm, on October 1, 2025, the start of fiscal year 2026 [4].
> 
> Apera contributed to the increase in investment management fees. Fees rose $497.1 million in fiscal 2026, primarily because of higher average equity, multi-asset and alternative AUM and the Apera acquisition. A decrease in performance fees and the impact of WAM outflows partly offset these gains [1]. Total investment management fees were $7,478.9 million in 2026, up from $6,981.8 million in 2025, a 7% increase [1].
> 
> The excerpts do not say how much of the $497.1 million increase came from Apera alone.

<details><summary>Excerpts the system saw</summary>

```
[1] Franklin Templeton (formerly Franklin Resources), fiscal year ended 2026-09-30 (BEN_FY2026_10K), Item 7
and is not directed toward existing or potential clients of Franklin.

39

Table of Contents

OPERATING REVENUES

The table below presents the percentage change in each operating revenue category.

(in millions) | 2026 vs. 2025 | 2025 vs. 2024
for the fiscal years ended September 30, | 2026 | 2025 | 2024
Investment management fees | $ | 7,478.9 | $ | 6,981.8 | $ | 6,822.2 | 7 | % | 2 | %
Sales and distribution fees | 1,593.7 | 1,474.7 | 1,381.0 | 8 | % | 7 | %
Shareholder servicing fees | 289.4 | 264.5 | 229.3 | 9 | % | 15 | %
Other | 53.3 | 49.7 | 45.5 | 7 | % | 9 | %
Total Operating Revenues | $ | 9,415.3 | $ | 8,770.7 | $ | 8,478.0 | 7 | % | 3 | %

Investment Management Fees

Investment management fees are generally calculated under contractual arrangements with our investment products and the products for which we provide sub-advisory services as a percentage of AUM. Annual fee rates vary by asset class and type of services provided. Fee rates for products sold outside of the U.S. are generally higher than for U.S. products.

Investment management fees increased $497.1 million in fiscal year 2026 primarily due to an increase in average equity, multi-asset and alternative AUM and the acquisition of Apera, partially offset by a decrease in performance fees and the impact of WAM outflows.

---

[2] Franklin Templeton (formerly Franklin Resources), fiscal year ended 2026-09-30 (BEN_FY2026_10K), Item 1
firm in July 2020, (ix) the O’Shaughnessy Asset Management quantitative asset management firm in December 2021, (x) the Lexington Partners global alternatives investment firm in April 2022, (xi) the Alcentra alternative credit investment firm in November 2022, (xii) the Putnam global investment firm in January 2024, (xiii) the Apera asset management firm in October 2025, and (xiv) the 250 Digital active cryptocurrency investment management firm in June 2026.

OUR BUSINESS STRUCTURE

Through our subsidiaries, we are committed to helping investors navigate global markets, as well as continuing to evolve and build on our strengths to meet the needs of our clients. We generally derive our revenues and income from providing investment management and related services to our products and the products we sub-advise. Our investment management fees, which represent a majority of our revenues, depend to a large extent on the level and relative mix of our AUM and the types of services provided, which are subject to change.

---

[3] Franklin Templeton (formerly Franklin Resources), fiscal year ended 2026-09-30 (BEN_FY2026_10K), Item 7
2026 primarily due to an increase in average equity, multi-asset and alternative AUM and the acquisition of Apera, partially offset by a decrease in performance fees and the impact of WAM outflows.

Our effective investment management fee rate excluding performance fees (investment management fees excluding performance fees divided by average AUM) was 40.7 and 40.5 basis points for fiscal years 2026 and 2025.

Performance fees were $414.1 million and $474.0 million for fiscal years 2026 and 2025. The decrease was primarily driven by lower performance fees earned by our alternative investment managers, partially offset by higher performance fees earned by our equity investment managers.

Our product offerings and global operations are diverse. As such, the impact of future changes in AUM on investment management fees will be affected by the relative mix of asset class, geographic region, distribution channel and investment vehicle of the assets.

Sales and Distribution Fees

---

[4] Franklin Templeton (formerly Franklin Resources), fiscal year ended 2026-09-30 (BEN_FY2026_10K), Item 7
for our services, which are based on contracts with our funds and customers, fund sales, and the number of shareholder transactions and accounts. These arrangements could change in the future.

During the fiscal year ended September 30, 2026 (“fiscal year 2026”), U.S. and global equity markets generated positive returns, supported by resilient economic growth, strong corporate earnings, and continued AI-driven investment despite elevated inflation, higher interest rates, and geopolitical uncertainty. The S&P 500 Index and MSCI World Index each increased 15.7% for the fiscal year. The global bond markets declined as the Bloomberg Global Aggregate Index decreased 2.4% for the fiscal year.

Our total AUM was $1,795.1 billion at September 30, 2026, 8% higher than at September 30, 2025. Simple monthly average AUM (“average AUM”) increased 8% during fiscal year 2026.

On October 1, 2025, we acquired Apera Asset Management (“Apera”), a pan-European private credit firm.

The business and regulatory environments in which we operate globally remain complex, uncertain and subject to change. We are subject to various laws, rules and regulations globally that impose restrictions, limitations, registration, reporting and disclosure requirements on our business, and add complexity to our global compliance operations.

---

[5] Franklin Templeton (formerly Franklin Resources), fiscal year ended 2026-09-30 (BEN_FY2026_10K), Item 8
Shareholder servicing fees | 231.3 | 31.2 | 1.7 | 0.3 | — | 264.5
Other | 48.4 | 0.1 | 1.1 | — | 0.1 | 49.7
Total | $ | 6,614.2 | $ | 1,295.7 | $ | 327.8 | $ | 254.0 | $ | 279.0 | $ | 8,770.7

(in millions) | United States | Luxembourg | Asia-Pacific | Americas Excluding United States | Europe, Middle East and Africa, Excluding Luxembourg | Total
for the fiscal year ended September 30, 2024
Investment management fees | $ | 5,142.8 | $ | 862.3 | $ | 283.8 | $ | 228.1 | $ | 305.2 | $ | 6,822.2
Sales and distribution fees | 979.2 | 342.8 | 19.2 | 39.8 | — | 1,381.0
Shareholder servicing fees | 195.3 | 31.7 | 2.2 | 0.1 | — | 229.3
Other | 40.5 | 0.7 | 3.7 | — | 0.6 | 45.5
Total | $ | 6,357.8 | $ | 1,237.5 | $ | 308.9 | $ | 268.0 | $ | 305.8 | $ | 8,478.0

Operating revenues are attributed to geographic areas based on the jurisdiction of the subsidiaries that provide the services, which may differ from the regions in which the related investment products are sold and domicile of the fund vehicle or client.

Revenues earned from sponsored funds were 84%, 84% and 82% of the Company’s total operating revenues for the fiscal years 2026, 2025 and 2024.

Note 5 – Investments

The disclosures below include details of the Company’s investments, excluding those of CIPs. See Note 10 – Consolidated Investment Products for information related to the investments held by these entities.

Investments consisted of the following:
```

</details>

---

## q034 · comparison

**Question:** At the end of 2025, how did Principal's assets under management compare with T. Rowe Price's?

**Gold answer:** T. Rowe Price managed $1,775.6 billion versus Principal's $781.0 billion, more than twice as much (Principal's $1,814.6 billion is assets under administration, not management).

**Key points:**
1. T. Rowe Price $1,775.6 billion
2. Principal AUM $781.0 billion
3. T. Rowe Price more than double
4. don't confuse Principal's AUA with AUM

**System answer:**

> The excerpts cover only T. Rowe Price, so they give no figures for Principal's assets under management, and I can't make the comparison.
> 
> For T. Rowe Price, assets under management were $1,775.6 billion at December 31, 2025. That was $169.0 billion higher than at the end of 2024 [2].
> 
> If you meant a different company, or want a different T. Rowe Price figure, tell me and I can look again.

<details><summary>Excerpts the system saw</summary>

```
[1] T. Rowe Price, fiscal year ended 2025-12-31 (TROW_FY2025_10K), Item 1
(4)Retail includes assets sourced through our direct-marketed business and financial intermediaries.

United States | U.S. Defined Contribution
APAC, EMEA, Canada | Other Retirement
Other Accounts

In 2025, our target date retirement products experienced net cash inflows of $5.2 billion. The assets under management in our target date retirement products totaled $561.4 billion at December 31, 2025, or 31.6% of our managed assets at December 31, 2025, compared to 29.6% at the end of 2024.

Additional information concerning our assets under management, results of operations, and financial condition during the past three years is contained in Part II, Item 7. Management’s Discussion and Analysis of Financial Condition and Results of Operations as well as our consolidated financial statements, which are included in Item 8. of this Form 10-K.

INVESTMENT MANAGEMENT SERVICES.

Investment Capabilities

We manage a broad range of investment strategies in equity, fixed income, multi-asset, and alternatives across sectors, styles and regions. Our strategies are designed to meet the varied and changing needs of investors and are delivered across a range of vehicles. We also offer specialized advisory services, including management of stable value investment contracts, customized multi-asset solutions, and a distribution management service for the disposition of equity securities our clients receive from third-party venture capital investment pools.

Page 4

Table of Contents

---

[2] T. Rowe Price, fiscal year ended 2025-12-31 (TROW_FY2025_10K), Item 1
value and composition of our assets under management. Accordingly, fluctuations in financial markets and in the composition of assets under management impact our revenues and results of operations.

At December 31, 2025, we had $1,775.6 billion in assets under management, an increase of $169.0 billion from the end of 2024. This increase in assets under management was driven by market appreciation, net of distributions not reinvested, of $216.7 billion, offset by net cash outflows of $56.9 billion. Beginning on July 1, 2025, assets under management include managed account - model delivery portfolios assets, which had $9.2 billion in assets as of that date, and are reflected in the increase from December 31, 2024.

The following charts show our AUM (in billions) by asset class, client type, geography, and account type as of December 31 for the prior three years:

Equity | Institutional (3)
Fixed Income, including money market | Retail (4)
Multi-Asset (1)
Alternatives (2)

(1)The underlying AUM of the multi-asset products have been aggregated and presented in this category and not reported in the equity and fixed income rows.

---

[3] T. Rowe Price, fiscal year ended 2025-12-31 (TROW_FY2025_10K), Item 7
are reflected in the increase from December 31, 2024.

Page 32

Table of Contents

The following table details changes in our assets under management, by asset class, during the last three years:

(in billions) | Equity | Fixed income, including money market | Multi-asset (2) | Alternatives (3) | Total
Assets under management at December 31, 2022 | $ | 664.2 | $ | 167.0 | $ | 400.1 | $ | 43.4 | $ | 1,274.7
Net cash flows prior to manager-driven distributions | (85.4) | (6.8) | 9.1 | 3.9 | (79.2)
Manager-driven distributions | — | — | — | (2.6) | (2.6)
Net cash flows | (85.4) | (6.8) | 9.1 | 1.3 | (81.8)
Net market appreciation (depreciation) and income (4) | 164.8 | 9.8 | 73.8 | 3.2 | 251.6
Change during the period | 79.4 | 3.0 | 82.9 | 4.5 | 169.8
Assets under management at December 31, 2023 | 743.6 | 170.0 | 483.0 | 47.9 | 1,444.5
Net cash flows prior to manager-driven distributions | (52.0) | 12.6 | (6.5) | 6.4 | (39.5)
Manager-driven distributions | — | — | — | (3.7) | (3.7)
Net cash flows | (52.0) | 12.6 | (6.5) | 2.7 | (43.2)
Net market appreciation (depreciation) and income (4) | 138.1 | 5.5 | 59.5 | 2.2 | 205.3
Change during the period | 86.1 | 18.1 | 53.0 | 4.9 | 162.1
Assets under management at December 31, 2024 | 829.7 | 188.1 | 536.0 | 52.8 | 1,606.6
Managed account - model delivery assets (5) | 9.2 | — | — | — | 9.2
Net cash flows prior to manager-driven distributions | (74.9) | 12.5 | 1.8 | 6.9 | (53.7)
Manager-driven distributions | — | — | — | (3.2) | (3.2)

---

[4] T. Rowe Price, fiscal year ended 2025-12-31 (TROW_FY2025_10K), Item 7
and funds managed outside of the our complex. As of December 31, 2025, our assets under administration were $314 billion, of which $178 billion were assets we manage.

INVESTMENT PERFORMANCE.(1)

Strong investment performance and brand awareness is a key driver to attracting and retaining assets—and to our long-term success. Our performance disclosures include specific asset classes, assets under management weighted performance, U.S. fund performance against passive peers, and composite performance against benchmarks. The following tables present investment performance for the one-, three-, five-, and 10-years ended December 31, 2025. Past performance is not a guarantee nor a reliable indicator of future performance.

% of U.S. funds that outperformed Morningstar median (2),(3)
1 year | 3 years | 5 years | 10 years
Equity | 48% | 50% | 51% | 56%
Fixed income | 64% | 62% | 52% | 59%
Multi-asset | 38% | 57% | 34% | 68%
All funds | 49% | 56% | 46% | 61%
% of U.S. funds that outperformed passive peer median (2),(4)
1 year | 3 years | 5 years | 10 years
Equity | 39% | 44% | 42% | 46%
Fixed income | 65% | 58% | 58% | 59%
Multi-asset | 20% | 43% | 29% | 39%
All funds | 39% | 47% | 43% | 48%
% of composites that outperformed benchmarks (5)
1 year | 3 years | 5 years | 10 years
Equity | 17% | 28% | 26% | 45%
Fixed income | 56% | 60% | 57% | 69%
All composites | 34% | 41% | 39% | 54%

Page 34

Table of Contents

---

[5] T. Rowe Price, fiscal year ended 2025-12-31 (TROW_FY2025_10K), Item 1
assets under management at the end of 2025.

The following table outlines the five distribution channels and vehicles through which our assets under management are sourced as of December 31, 2025.

Vehicle | Retail | Institutional
Americas financial intermediaries | EMEA & APAC financial intermediaries | Individual U.S. investors on a direct basis | U.S. Defined Contribution | Institutional investors
U.S. Mutual Funds | x | x | x | x
Collective Investment Trusts | x | x | x
Exchange-Traded Funds | x | x | x
College Savings Plans | x | x
Model Portfolios | x | x | x (6)
Separately Managed Accounts (SMAs) (1) | x | x | x
Subadvised Accounts | x | x | x | x
Separate Accounts | x | x | x | x | x
SICAVs (2) / FCPs (3) | x | x | x
Canadian Pooled Funds | x | x
OEICs (4) | x | x
Japanese ITMs (5) | x | x
Australian Unit Trusts | x | x
Private Funds | x
Collateralized Loan Obligations | x
Business Development Company (BDC) | x | x
Interval Funds | x | x

Page 6

Table of Contents

(1) Includes both model delivery and manager traded SMAs,. (2)Société d'Investissement à Capital Variable (Luxembourg), (3)Fonds Commun de Placement (Luxembourg), (4)Open-Ended Investment Company (U.K.), (5)Japanese Investment Trust Management Funds, (6) Provided through our ActivePlus and Retirement Advisory Service Portfolios.

INVESTMENT ADVISORY FEES.
```

</details>

---

## q035 · comparison

**Question:** Which earned more GAAP net income for common shareholders in 2025, MetLife or Lincoln, and did each improve or decline from 2024?

**Gold answer:** MetLife: $3,173 million (down from $4,226 million). Lincoln: $1,086 million (down from $3,184 million). MetLife earned more; both declined.

**Key points:**
1. MetLife $3,173 million
2. Lincoln $1,086 million
3. both declined from 2024

**System answer:**

> I can only partly answer this from the excerpts.
> 
> **MetLife:** Net income available to common shareholders was $3.2 billion in 2025, down from $4.2 billion in 2024, so it declined [2]. (Adjusted earnings, a non-GAAP measure, rose slightly, from $5.8 billion to $5.9 billion [2].)
> 
> **Lincoln:** The excerpts do not give Lincoln's 2025 or 2024 net income. They only mention the $825 million sale of about 18.8 million shares to Bain Capital [3] and the auditor's report on the financial statements [5], with no income figures. Because of this, I can't say which company earned more in 2025, or whether Lincoln's net income improved or declined from 2024.

<details><summary>Excerpts the system saw</summary>

```
[1] MetLife, fiscal year ended 2025-12-31 (MET_FY2025_10K), Item 1
Overview & Strategy

As used in this Form 10-K, “MetLife,” the “Company,” “we,” “our” and “us” refer to MetLife, Inc., a Delaware corporation incorporated in 1999, its subsidiaries and affiliates.

MetLife is one of the world’s leading financial services companies, providing insurance, annuities, employee benefits and asset management. We hold leading market positions in the United States (“U.S.”), Asia, Latin America, Europe and the Middle East. We are also one of the largest institutional investors in the U.S. with a general account portfolio invested primarily in fixed income securities (corporate, structured products, municipals, and government and agency) and mortgage loans, as well as real estate, real estate joint ventures (“REJVs”), other limited partnerships and equity securities.

We believe that our trusted global brand, diversified and resilient business, and position as a leader in attractive markets are the powers of our business. Over the next four years we will continue to execute on our New Frontier strategy, which was designed to accelerate growth across our global platform while delivering attractive returns and all-weather performance. New Frontier builds upon the success of our Next Horizon strategy, which we implemented in 2019, with an aim to focus, simplify and differentiate the Company.

Under our New Frontier strategy, we intend to leverage the Company’s strengths to prioritize growth across four key areas of opportunity:

---

[2] MetLife, fiscal year ended 2025-12-31 (MET_FY2025_10K), Item 7
Financial Highlights

•Net income available to MetLife, Inc.’s common shareholders was $3.2 billion, $4.2 billion and $1.4 billion for the years ended December 31, 2025, 2024 and 2023, respectively.

•Adjusted earnings available to common shareholders was $5.9 billion, $5.8 billion and $5.5 billion for the years ended December 31, 2025, 2024 and 2023, respectively.

62

Table of Contents

Consolidated Results

Years Ended December 31,
2025 | 2024 | 2023
(In millions)
Revenues
Premiums | $ | 49,779 | $ | 44,945 | $ | 44,283
Universal life and investment-type product policy fees | 5,003 | 4,974 | 5,152
Net investment income | 22,559 | 21,273 | 19,908
Other revenues | 2,827 | 2,601 | 2,526
Net investment gains (losses) | (1,145) | (1,184) | (2,824)
Net derivative gains (losses) | (1,939) | (1,623) | (2,140)
Total revenues | 77,084 | 70,986 | 66,905
Expenses
Policyholder benefits and claims and policyholder dividends | 50,271 | 45,323 | 45,212
Policyholder liability remeasurement (gains) losses | (150) | (206) | (45)
Market risk benefit remeasurement (gains) losses | (508) | (1,109) | (994)
Interest credited to policyholder account balances | 8,950 | 8,339 | 7,860
Amortization of deferred policy acquisition costs, value of business acquired and negative value of business acquired | 2,114 | 2,021 | 1,926
Interest expense on debt | 1,061 | 1,037 | 1,045
Other expenses, net of capitalization of deferred policy acquisition costs | 10,685 | 9,959 | 9,739

---

[3] Lincoln National (Lincoln Financial), fiscal year ended 2025-12-31 (LNC_FY2025_10K), Item 7
of strengthening and maintaining our balance sheet, improving our operational efficiency, increasing free cash flow and focusing on profitable growth. Notable actions in 2025 include the following:

•During the second quarter of 2025, we closed our stock purchase agreement (the “Purchase Agreement”) with Bain Capital Prairie, LLC (the “Buyer”), a newly formed subsidiary of Bain Capital, under which we agreed to sell shares representing 9.9% of our outstanding common stock on a post-issuance basis to the Buyer. Under the final terms, Lincoln sold approximately 18.8 million shares of its common stock for aggregate consideration of $825 million. The transaction provided us with capital that we are deploying and expect to continue to deploy toward our strategic priorities, including growing spread-based earnings, advancing our portfolio management efforts and asset sourcing capabilities and optimizing our legacy life portfolio. For additional information on the Bain Capital transaction, see Note 18.

---

[4] Lincoln National (Lincoln Financial), fiscal year ended 2025-12-31 (LNC_FY2025_10K), Item 4
Senior Vice President and Head of Alternatives, Structured Credit and Investment Strategy (2020 - November 2021). Senior Vice President and Head of Investment Risk and Strategy (April 2018 - 2020).
Andrew D. Rallis | 63 | Executive Vice President and Chief Risk Officer (since May 2023). Executive Vice President and Global Chief Actuary (July 2012 - May 2023), MetLife, Inc.
James Reid | 59 | Executive Vice President and President, Workplace Solutions (since August 2022). President and Chief Executive Officer (April 2021 - August 2022), Versant Health, a managed vision care company. Executive Vice President and Head of Global Employee Benefits (January 2016 - March 2021), MetLife, Inc.
Sean N. Woodroffe | 62 | Executive Vice President and Chief People, Communications and Enterprise Services Officer (since November 2025). Executive Vice President and Chief People, Culture and Communications Officer (May 2023 - November 2025). Senior Executive Vice President and Chief People Officer (March 2018 - April 2023), TIAA, a financial services provider.

(1) Age shown is based on the officer’s age as of February 12, 2026.

(2) Denotes an affiliate of LNC.

39

Table of Contents

PART II

Item 5. Market for Registrant’s Common Equity, Related Stockholder Matters and Issuer Purchases of Equity Securities

(a) Stock Market and Dividend Information

---

[5] Lincoln National (Lincoln Financial), fiscal year ended 2025-12-31 (LNC_FY2025_10K), Item 8
changes in conditions, or that the degree of compliance with the policies or procedures may deteriorate.

/s/ Ernst & Young LLP

Philadelphia, Pennsylvania

February 19, 2026

112

Table of Contents

Report of Independent Registered Public Accounting Firm

To the Stockholders and the Board of Directors of Lincoln National Corporation

Opinion on the Financial Statements

We have audited the accompanying consolidated balance sheets of Lincoln National Corporation (the Company) as of December 31, 2025 and 2024, the related consolidated statements of comprehensive income (loss), stockholders’ equity and cash flows for each of the three years in the period ended December 31, 2025, and the related notes and financial statement schedules listed in the Index at Item 15(a) (collectively referred to as the “consolidated financial statements”). In our opinion, the consolidated financial statements present fairly, in all material respects, the financial position of the Company at December 31, 2025 and 2024, and the results of its operations and its cash flows for each of the three years in the period ended December 31, 2025, in conformity with U.S. generally accepted accounting principles.
```

</details>

---

## q036 · comparison

**Question:** How many reportable business segments do MetLife and Principal each have, and which has more?

**Gold answer:** MetLife has six (Group Benefits; RIS; Asia; Latin America; EMEA; MIM); Principal has three (Retirement and Income Solutions; Principal Asset Management; Benefits and Protection). MetLife has more.

**Key points:**
1. MetLife six
2. Principal three
3. MetLife has more

**System answer:**

> I can't give a full comparison, because the excerpts don't cover MetLife. Nothing in them describes MetLife's segments, so I can't say how many it has or which company has more.
> 
> For Principal (fiscal year 2025), the excerpts point to four segments:
> 
> - Retirement and Income Solutions [3]
> - Principal Asset Management [3]
> - Benefits and Protection [4]
> - Corporate [1][2][4]
> 
> The segment operating revenue table in the notes shows these four columns: Retirement and Income Solutions, Principal Asset Management, Benefits and Protection, and Corporate [4]. The notes also say the segments are managed and reported separately because they have different products and services, strategies, or markets and distribution channels [3].
> 
> If you can provide MetLife's 10-K excerpts, I can finish the comparison.

<details><summary>Excerpts the system saw</summary>

```
[1] Principal Financial Group (Principal), fiscal year ended 2025-12-31 (PFG_FY2025_10K), Item 1
as exiting the business, business transition, retaining key employees and retirement planning. Key employees also have needs to supplement retirement income, survivor income and business protection. We believe the Business Owner Solutions segment offers growth opportunities and we will continue to develop strategies to capitalize on this expanding market.

We distribute our individual life and individual disability insurance products through our affiliated financial representatives and independent brokers, as well as other marketing and distribution alliances. To meet the needs of the various marketing channels, particularly the independent brokers, we employ wholesale distributors — Regional Vice Presidents for nonqualified, business solutions and individual disability.

Corporate Segment

Our Corporate segment manages the assets representing capital that has not been allocated to any other segment. Financial results of the Corporate segment primarily reflect our financing activities (including financing costs), income on capital not allocated to other segments, inter-segment eliminations, income tax risks and certain income, expenses and other adjustments not allocated to the segments based on the nature of such items. Results of Principal Securities, Inc., our retail broker-dealer and registered investment advisor, and our exited group medical and long-term care insurance businesses are reported in this segment.

12

Table of Contents

Competition

---

[2] Principal Financial Group (Principal), fiscal year ended 2025-12-31 (PFG_FY2025_10K), Item 8
life insurance (including indexed universal life), traditional life insurance (including participating whole life, adjustable life products and term life insurance) and our exited ULSG business.

Our Corporate segment manages the assets representing capital that has not been allocated to any other segment. Financial results of the Corporate segment primarily reflect our financing activities (including financing costs), income on capital not allocated to other segments, inter-segment eliminations, income tax risks and certain income, expenses and other adjustments not allocated to the segments based on the nature of such items. Results of Principal Securities, Inc. (“PSI”), our retail broker-dealer and registered investment advisor (“RIA”); and our exited group medical and long-term care insurance businesses are reported in this segment.

---

[3] Principal Financial Group (Principal), fiscal year ended 2025-12-31 (PFG_FY2025_10K), Item 8
segment. The segments are managed and reported separately because they provide different products and services, have different strategies or have different markets and distribution channels.

The Retirement and Income Solutions segment provides retirement and related financial products and services primarily to businesses, their employees and other individuals. The segment includes workplace savings and retirement solutions, banking, trust and custodial services, individual variable annuities (including RILAs), pension risk transfer, investment only and our exited retail fixed annuities business.

The Principal Asset Management segment provides global investment solutions to institutional, retirement, retail and high net worth investors in the U.S. and select emerging markets. The segment is organized into Investment Management, which provides public, multi-asset and private market capabilities across all asset classes, including equity, fixed income, real estate and alternatives, to serve a breadth of client investment objectives; and International Pension, which provides long-term savings and retirement solutions through pension accumulation and income annuities in Asia and Latin America.

---

[4] Principal Financial Group (Principal), fiscal year ended 2025-12-31 (PFG_FY2025_10K), Item 8
Table of Contents

Principal Financial Group, Inc.

Notes to Consolidated Financial Statements – (continued)

December 31, 2025

20. Segment Information – (continued)

Segment Operating Revenues

| | | | | | | | | | | | | | | |
| | For the year ended December 31, 2025
| | Retirement | | Principal | | | | | | | | |
| | and Income | | Asset | | Benefits and | | | | | | |
| | Solutions | | Management | | Protection | | Corporate | | Total
| | (in millions)
Revenue from contracts with external customers (1) | | $ | 4,806.7 | | $ | 1,848.2 | | $ | 4,274.1 | | $ | 269.3 | | $ | 11,198.3 |
Adjustments for revenue from contracts with external customers not included in operating revenues (2) | | | ( 70.3 ) | | | — | | 28.8 | | — | | ( 41.5 ) |
Net investment income included in operating revenues | | | 3,409.3 | | | 437.2 | | 653.3 | | 193.3 | | 4,693.1 |
Operating revenues from equity method investments | | | — | | | 209.6 | | — | | ( 0.4 ) | | 209.2 |
Inter-segment operating revenues | | | 36.2 | | | 315.9 | | 8.9 | | 325.9 | | 686.9 |
Eliminations of inter-segment operating revenues | | | — | | | — | | — | | ( 686.9 ) | | ( 686.9 ) |
Segment operating revenues (3) | | $ | 8,181.9 | | $ | 2,810.9 | | $ | 4,965.1 | | $ | 101.2 | | | 16,059.1 |
Net realized capital gains, net of related revenue adjustments | | | | | | | | | | | | | | 41.0 |
Revenues from exited business (4) | | | | | | | | | | | | | | | ( 364.4 ) |

---

[5] Principal Financial Group (Principal), fiscal year ended 2025-12-31 (PFG_FY2025_10K), Item 1
of large-scale annuity sales in a particular quarter. The Principal Asset Management segment primarily manages the assets supporting pension risk transfer account values.

Markets and Distribution

Our primary distribution channel for pension risk transfer products is comprised of several specialized home office sales consultants working through consultants and brokers that specialize in this type of business. Our sales consultants also make sales directly to institutions. Our nationally dispersed retirement services sales representatives act as a secondary distribution channel for these products.

Bank and Trust Services

Principal Bank is a U.S. federal savings bank that was formed in February 1998. As of December 31, 2025, Principal Bank had nearly 816,000 customers and approximately $9.3 billion in assets. Principal Bank operates under a limited purpose charter and may only accept deposits held in a fiduciary capacity and may not hold demand deposits. It also may not own commercial loans or originate loans.

Principal Custody Solutions (“PCS”) is a division of Principal Bank that provides trust and/or custodial support services to clients in a variety of market segments including corporations, endowments, foundations, health care organizations, insurance and financial institutions, public entities and government institutions.
```

</details>

---

## q038 · comparison

**Question:** Whose chief information security officer has more experience, BlackRock's or Lincoln's?

**Gold answer:** BlackRock's: over 31 years in information technology, including 25 years focused on information security, versus Lincoln's CISO with over 20 years in cybersecurity.

**Key points:**
1. BlackRock 31+ years (25 in security)
2. Lincoln 20+ years
3. BlackRock more

**System answer:**

> The excerpts don't allow a comparison. For Lincoln, the CISO has over 20 years of cybersecurity experience and holds a Certified Information Security Systems Professional designation [1]. The BlackRock excerpts cover the company's business, acquisitions, and cyber-attack risk factors, but they say nothing about its CISO or that person's experience [3][4][5].

<details><summary>Excerpts the system saw</summary>

```
[1] Lincoln National (Lincoln Financial), fiscal year ended 2025-12-31 (LNC_FY2025_10K), Item 1C
which provides oversight of our enterprise-wide risk structure and of our processes to identify, measure, monitor and manage significant risks, including, but not limited to, cybersecurity risk.

The Information Security organization is led by our CISO. The head of each of the four divisions of our Information Security team reports directly to the CISO. The CISO reports directly to the Company’s Chief Information Officer (“CIO”), who is a member of the Company’s Senior Management Committee. As a result, all information security personnel report into the CISO, and ultimately the CIO. The CISO also reports indirectly to the Audit Committee of the Board of Directors. Biannually, the CISO reports to the Audit Committee on the cybersecurity risks facing the Company and cybersecurity developments generally. In addition, as discussed above, the Company’s Internal Audit team reports to the Audit Committee the results of its annual security audit focused on cybersecurity risks. The Company’s Chief Compliance Officer reports key Privacy risk indicators and statistics (including those related to cybersecurity risks) to the Audit Committee on a quarterly basis.

Our current CISO has over 20 years of experience in the field of cybersecurity and holds a Certified Information Security Systems Professional designation. The CISO has a staff of more than 100 employees dedicated to protecting the data and systems belonging to the Company, our customers, business partners and consumers.

37

---

[2] Lincoln National (Lincoln Financial), fiscal year ended 2025-12-31 (LNC_FY2025_10K), Item 3
and Litigation Matters” in Note 17, which is incorporated herein by reference.

Item 4. Mine Safety Disclosures

Not applicable.

38

Table of Contents

Information About our Executive Officers

Our Executive Officers as of February 12, 2026, were as follows:
Name | Age (1) | Position with LNC and Business Experience During the Past Five Years
Ellen G. Cooper | 61 | President, Chief Executive Officer and Director (since May 2022); Chairman of the Board of Directors (since May 2023). Until May 2022, Executive Vice President (since August 2012), Head of Enterprise Risk (since 2019) and Head of Annuity Solutions Group (since March 2021). Chief Investment Officer (August 2012 - November 2021).
Nilanjan (Neel) Adhya | 51 | Executive Vice President, Chief AI, Data and Analytics Officer (since January 2026). Chief Digital Officer and Global Head of Digital Platforms and Experiences (August 2021 - December 2025), BlackRock, an investment management corporation. Chief Digital Officer and Vice President of Digital Transformation (June 2019 - August 2021), IBM, a technology company.
Craig T. Beazer | 58 | Executive Vice President and General Counsel (since December 2020).
Jennifer Charters | 53 | Executive Vice President and Chief Information Officer (since November 2024). Executive Vice President and Chief Information Officer, Flagstar Bank (June 2018 - August 2024).

---

[3] BlackRock, fiscal year ended 2025-12-31 (BLK_FY2025_10K), Item front matter
Certain Relationships and Related Transactions, and Director Independence | 68
Item 14 | Principal Accountant Fees and Services | 68
PART IV
Item 15 | Exhibits and Financial Statement Schedules | 69
Item 16 | Form 10-K Summary | 72
Signatures | 73

Part I

Item 1. Business

Overview

BlackRock, Inc. (together, with its subsidiaries, unless the context otherwise indicates, “BlackRock” or the “Company”) is a leading publicly traded investment management firm with $14.0 trillion of assets under management (“AUM”) at December 31, 2025. With approximately 24,900 employees in more than 30 countries who serve clients in over 100 countries across the globe, BlackRock provides a broad range of investment management and technology and subscription services to institutional and retail clients worldwide. On July 1, 2025, BlackRock completed the acquisition of 100% of the business and assets of HPS Investment Partners (the "HPS Transaction" or "HPS"), a leading global credit investment manager, with substantially all consideration paid in Class B-2 common units ("Subco Units") of BlackRock Saturn Subco, LLC ("Subco"), a consolidated subsidiary of the Company. Concurrent with the acquisition, BlackRock Finance, Inc., Global Infrastructure Management, LLC ("GIP"), HPS, and their respective subsidiaries became wholly owned subsidiaries of Subco.

---

[4] BlackRock, fiscal year ended 2025-12-31 (BLK_FY2025_10K), Item 1
Aladdin Wealth provides wealth management firms and their financial professionals with institutional-quality business management, portfolio construction, modeling and risk analytics capabilities.

Through the Company's Cachematrix platform, BlackRock is also a leading provider of financial technology which simplifies the cash management process for banks and their corporate clients in a streamlined, open-architecture platform. In March 2025, BlackRock completed the acquisition of 100% of the shares of Preqin Holding Limited ("Preqin"), a leading provider of private markets data, for £2.5 billion (or approximately $3.2 billion) in cash (the "Preqin Transaction").

At year-end, BlackRock technology services and subscription clients included asset managers, insurance companies, wealth managers, pension funds, official institutions, banks, asset servicers, corporations, law firms, consultants and other investors across North America, South America, Europe, the Middle East, Asia, Africa and Australia.

---

[5] BlackRock, fiscal year ended 2025-12-31 (BLK_FY2025_10K), Item 1A
the Company’s protective measures could itself create a risk of security issues or system disruptions for the Company, as well as for clients who rely upon, or have exposure to, BlackRock’s systems.

In addition, due to BlackRock’s interconnectivity with third-party vendors, advisors, central agents, exchanges, clearing houses and other financial institutions, BlackRock or any such third-party may be adversely affected if any of them (or their service providers) is subject to a successful cyber-attack or other information security event, including those arising due to the use of mobile technology or a third-party cloud environment. BlackRock also routinely transmits and receives personal, confidential or proprietary information by email and other electronic means. The Company collaborates with clients, vendors and other third parties to develop secure transmission capabilities and protect against cyber-attacks. However, BlackRock or such third parties may not have all appropriate controls in place to protect the confidentiality of such information.
```

</details>

---

## q039 · comparison

**Question:** Whose revenue grew faster in 2025, BlackRock's or T. Rowe Price's?

**Gold answer:** BlackRock's: total revenue rose from $20,407 million to $24,216 million (about 18.7%), versus T. Rowe Price's net revenues up 3.1% to $7,314.8 million.

**Key points:**
1. BlackRock ~18.7% ($20,407M to $24,216M)
2. T. Rowe Price 3.1%
3. BlackRock faster

**System answer:**

> I can't make that comparison from the excerpts, because they contain nothing on T. Rowe Price. They cover only BlackRock's FY2025 10-K.
> 
> For BlackRock, one excerpt says revenue rose "or 19%, from 2024," though the opening of that sentence is cut off, so the total revenue figure isn't shown. The growth is attributed to market gains, organic base fee growth, fees from the GIP and HPS transactions, and higher technology services and subscription revenue [3]. Investment advisory, administration fees and securities lending revenue was $19.2 billion in 2025, up from $16.1 billion in 2024 [3].
> 
> To answer the question, I would need T. Rowe Price's 2025 revenue growth from its own filing.

<details><summary>Excerpts the system saw</summary>

```
[1] BlackRock, fiscal year ended 2025-12-31 (BLK_FY2025_10K), Item front matter
Certain Relationships and Related Transactions, and Director Independence | 68
Item 14 | Principal Accountant Fees and Services | 68
PART IV
Item 15 | Exhibits and Financial Statement Schedules | 69
Item 16 | Form 10-K Summary | 72
Signatures | 73

Part I

Item 1. Business

Overview

BlackRock, Inc. (together, with its subsidiaries, unless the context otherwise indicates, “BlackRock” or the “Company”) is a leading publicly traded investment management firm with $14.0 trillion of assets under management (“AUM”) at December 31, 2025. With approximately 24,900 employees in more than 30 countries who serve clients in over 100 countries across the globe, BlackRock provides a broad range of investment management and technology and subscription services to institutional and retail clients worldwide. On July 1, 2025, BlackRock completed the acquisition of 100% of the business and assets of HPS Investment Partners (the "HPS Transaction" or "HPS"), a leading global credit investment manager, with substantially all consideration paid in Class B-2 common units ("Subco Units") of BlackRock Saturn Subco, LLC ("Subco"), a consolidated subsidiary of the Company. Concurrent with the acquisition, BlackRock Finance, Inc., Global Infrastructure Management, LLC ("GIP"), HPS, and their respective subsidiaries became wholly owned subsidiaries of Subco.

---

[2] BlackRock, fiscal year ended 2025-12-31 (BLK_FY2025_10K), Item 1
Aladdin Wealth provides wealth management firms and their financial professionals with institutional-quality business management, portfolio construction, modeling and risk analytics capabilities.

Through the Company's Cachematrix platform, BlackRock is also a leading provider of financial technology which simplifies the cash management process for banks and their corporate clients in a streamlined, open-architecture platform. In March 2025, BlackRock completed the acquisition of 100% of the shares of Preqin Holding Limited ("Preqin"), a leading provider of private markets data, for £2.5 billion (or approximately $3.2 billion) in cash (the "Preqin Transaction").

At year-end, BlackRock technology services and subscription clients included asset managers, insurance companies, wealth managers, pension funds, official institutions, banks, asset servicers, corporations, law firms, consultants and other investors across North America, South America, Europe, the Middle East, Asia, Africa and Australia.

---

[3] BlackRock, fiscal year ended 2025-12-31 (BLK_FY2025_10K), Item 7
or 19%, from 2024, primarily reflecting the positive impact of markets, organic base fee growth, fees related to the GIP and HPS Transactions and higher technology services and subscription revenue.

Investment advisory, administration fees and securities lending revenue of $19.2 billion in 2025 increased $3.1 billion from $16.1 billion in 2024, primarily driven by organic base fee growth, the impact of market beta and foreign exchange movements on average AUM and the impact of the GIP and HPS Transactions. Securities lending revenue of $705 million increased $90 million from $615 million in 2024, primarily reflecting higher average balances of securities on loan and higher spreads.

Investment advisory performance fees of $1.4 billion in 2025 increased $217 million from $1.2 billion in 2024, primarily reflecting higher revenue from private markets, including the impact of the HPS Transaction, partially offset by lower revenue from liquid alternative products.

Technology services and subscription revenue of $2.0 billion in 2025 increased $378 million from $1.6 billion in 2024, reflecting the sustained demand for Aladdin technology offerings and approximately $210 million of revenue related to the Preqin Transaction.

Expense

The following table presents expense for 2025 and 2024.

---

[4] BlackRock, fiscal year ended 2025-12-31 (BLK_FY2025_10K), Item 7
in liquid credit strategies, included within fixed income AUM. BlackRock’s alternatives platform totals approximately $676 billion in client assets, making it a top five alternatives provider.

BlackRock's investments in infrastructure, private credit, and alternatives-to-wealth underpin its ambition to raise $400 billion in private markets by 2030. The Company has a significant opportunity to deliver better outcomes and experiences for clients in their private markets allocations. For example, BlackRock is the largest general account manager for insurers with $720 billion in long-term AUM. With HPS, it's now also one of the largest asset-based finance and high-grade managers. The Company is focused on helping insurers build more dynamic and diversified portfolios across public and private markets, which could contribute to organic AUM and base fee growth.

Similarly in wealth, BlackRock is working to expand access to private markets. The Company is bringing together investment performance track records with its scaled global distribution model. BlackRock plans to continue to expand and diversify distribution of HPS' nontraded business development companies to US wirehouses and registered investment advisors. It also plans to widen its product range through an H-Series family of funds in 2026. The Company aims to bring together the building blocks to serve wealth investors through a coordinated, multi-alternatives portfolio.

---

[5] BlackRock, fiscal year ended 2025-12-31 (BLK_FY2025_10K), Item 7
liabilities related to securities lending or other indemnification obligations; and (28) the impact of problems, instability or failure of other financial institutions or the failure or negative performance of products offered by other financial institutions.

Overview

BlackRock, Inc. (together, with its subsidiaries, unless the context otherwise indicates, “BlackRock” or the “Company”) is a leading publicly traded investment management firm with $14.0 trillion of AUM at December 31, 2025. With approximately 24,900 employees in more than 30 countries, BlackRock provides a broad range of investment management and technology services to institutional and retail clients in more than 100 countries across the globe. For further information see Note 1, Business Overview, and Note 27, Segment Information, in the notes to the consolidated financial statements contained in Part II, Item 8.

The following discussion includes a comparison of BlackRock’s results for 2025 and 2024. For a discussion of BlackRock’s results for 2023 and a comparison of results for 2024 and 2023, see Item 7, Management’s Discussion and Analysis of Financial Condition and Results of Operations, of the Company’s Annual Report on Form 10-K for the year ended December 31, 2024, which was filed with the SEC on February 25, 2025.

Certain prior period presentations were reclassified to ensure comparability with current period classifications.

Acquisitions
```

</details>

---

## q040 · comparison

**Question:** In their latest fiscal years, did the effective fee rates (excluding performance fees) at Franklin and T. Rowe Price move in the same direction?

**Gold answer:** No. Franklin's rose slightly, from 40.5 to 40.7 basis points (fiscal 2026 vs 2025). T. Rowe Price's average effective fee rate for 2025 declined from 2024, as flows shifted assets toward lower-fee strategies.

**Key points:**
1. Franklin up 40.5 to 40.7 bps
2. T. Rowe Price declined
3. opposite directions

**System answer:**

> The excerpts don't let me answer this for the latest fiscal years, because T. Rowe Price's 2025 fee rate isn't included.
> 
> - **Franklin Templeton:** The effective investment management fee rate excluding performance fees was 40.7 basis points in fiscal 2026 and 40.5 in fiscal 2025, so it rose [2].
> - **T. Rowe Price:** The Item 7 excerpt from the FY2025 filing only covers 2024 versus 2023. The rate excluding performance-based fees fell from 41.9 to 41.0 basis points. The company attributed the decline largely to a mix shift toward lower-fee products and asset classes [1]. The excerpts give no 2025 rate, so I can't tell the direction of its latest-year move.
> 
> The only comparison available is not like-for-like. T. Rowe's rate fell in 2024 [1], while Franklin's rose in fiscal 2026 [2]. Those are different periods, so they don't show whether the two moved together in their latest years.

<details><summary>Excerpts the system saw</summary>

```
[1] T. Rowe Price, fiscal year ended 2025-12-31 (TROW_FY2025_10K), Item 7
with tiered-fee structures.

Investment advisory fees earned in 2024 increased 12.1% compared to 2023 as average assets under management increased $199.6 billion, or 14.7%, to $1,561.9 billion.

The average annualized effective fee rate, excluding performance-based advisory fees, earned on our assets under management was 41.0 basis points in 2024, compared to 41.9 basis points earned in 2023. Our effective fee rate has declined largely due to a mix shift in assets toward lower fee products and asset classes from client flows and transfers, partially offset by higher market returns. The average annualized fee rate, excluding performance-based fees, was 40.5 basis points for the fourth quarter of 2024.

Operating expenses were $4,760.3 million in 2024, an increase of 6.4% compared to 2023. The increase was primarily driven by higher compensation costs, distribution and servicing costs, and advertising and promotion costs. Additionally, 2023 included a $82.4 million reduction in operating expenses related to the remeasurement of the contingent consideration liability compared to a $13.4 million reduction in 2024.

---

[2] Franklin Templeton (formerly Franklin Resources), fiscal year ended 2026-09-30 (BEN_FY2026_10K), Item 7
2026 primarily due to an increase in average equity, multi-asset and alternative AUM and the acquisition of Apera, partially offset by a decrease in performance fees and the impact of WAM outflows.

Our effective investment management fee rate excluding performance fees (investment management fees excluding performance fees divided by average AUM) was 40.7 and 40.5 basis points for fiscal years 2026 and 2025.

Performance fees were $414.1 million and $474.0 million for fiscal years 2026 and 2025. The decrease was primarily driven by lower performance fees earned by our alternative investment managers, partially offset by higher performance fees earned by our equity investment managers.

Our product offerings and global operations are diverse. As such, the impact of future changes in AUM on investment management fees will be affected by the relative mix of asset class, geographic region, distribution channel and investment vehicle of the assets.

Sales and Distribution Fees

---

[3] Franklin Templeton (formerly Franklin Resources), fiscal year ended 2026-09-30 (BEN_FY2026_10K), Item 7A
distribution fee revenues. Such a change for the fiscal year ended September 30, 2026 would have resulted in an increase or decrease in operating revenues of $838.4 million.

Interest Rate Risk

We are exposed to changes in interest rates primarily through our investments in funds that invest in debt securities, which were $3,004.7 million at September 30, 2026. Our exposure to interest rate risks from these investments is mitigated by the low average duration exposure and a broad range of products in various global jurisdictions. We had no exposure to changes in interest rates from debt obligations at September 30, 2026 as all of our outstanding debt was issued at fixed rates. Any borrowings under the Second Amended and Restated Credit Agreement would bear interest at variable rates.

As of September 30, 2026, we have considered the potential impact of a 100 basis point movement in market interest rates on our investments in funds that invest in debt securities. Based on our analysis, we do not expect that such a change would have a material impact on our earnings in the next 12 months.

Foreign Currency Exchange Risk

---

[4] Franklin Templeton (formerly Franklin Resources), fiscal year ended 2026-09-30 (BEN_FY2026_10K), Item 7
in fiscal year 2026 primarily due to an increase of 5% in the related average AUM and a higher mix of equity funds, non-U.S. multi-asset funds and U.S. alternative funds, which generate higher fees.

Sales-based fees increased $19.7 million in fiscal year 2026 primarily due to a $10.3 million increase in contingent sales charges, driven by increased redemptions, and an increase of 13% in commissionable sales, partially offset by a higher mix of non-U.S. sales, which generate lower fees.

Shareholder Servicing Fees

Shareholder servicing fees are earned from our sponsored funds for providing transfer agency services, which include providing shareholder statements, transaction processing, client service and tax reporting. Shareholder servicing fees are determined based on a contractual margin, or a percentage of AUM and either the number of transactions in shareholder accounts or the number of shareholder accounts. Shareholder servicing fees also include fund reimbursements of expenses incurred while providing transfer agency services.

Shareholder servicing fees increased $24.9 million in fiscal year 2026, primarily due to higher levels of related AUM and increased revenue related to fees earned on a contractual basis.

OPERATING EXPENSES

The table below presents the percentage change in each operating expense category.

---

[5] T. Rowe Price, fiscal year ended 2025-12-31 (TROW_FY2025_10K), Item 1
services; and other advisory services. We take an active, independent approach to investing, offering our dynamic perspective and meaningful partnership, so our clients can feel more confident.

The late Thomas Rowe Price, Jr., founded our firm in 1937, and the common stock of T. Rowe Price Associates, Inc. was first offered to the public in 1986. The T. Rowe Price Group corporate holding company structure was established in 2000. Our common stock trades on the NASDAQ Global Select Market under the symbol "TROW".

Our core capabilities have enabled us to deliver excellent operating results since our initial public offering. We maintain a strong corporate culture focused on delivering superior long-term investment performance and world-class service to our clients. We distribute our broad array of active investment solutions through a diverse set of distribution channels and vehicles to meet the needs of our clients globally. These vehicles include an array of U.S. mutual funds, collective investment trusts, exchange-traded funds, subadvised funds, separately managed accounts, and other sponsored products. The other sponsored products include: open-ended investment products offered to investors outside the U.S., products offered through variable annuity life insurance plans in the U.S., affiliated private investment funds, business development companies, interval funds, models, and collateralized loan obligations (CLOs).
```

</details>

---

## q041 · unanswerable

**Question:** How much total compensation did BlackRock pay its CEO for 2025?

**Gold answer:** This information is not in the documents. BlackRock's 10-K doesn't disclose CEO compensation; Item 11 incorporates it by reference from the proxy statement.

**Key points:**
1. States that the documents don't contain this information
2. Does not guess or invent a figure

**System answer:**

> The excerpts don't say how much BlackRock paid its CEO for 2025. CEO pay would normally appear in the proxy statement or an executive compensation section, and none of the excerpts covers it.
> 
> What the excerpts do give is company-wide compensation data:
> - Employee compensation and benefits expense was $8.4 billion in 2025, up $1.9 billion from $6.5 billion in 2024 [3].
> - Accrued compensation and benefits at December 31, 2025 totaled $3.8 billion, including $2.7 billion of annual incentive compensation [2].
> - Total stock-based compensation expense was $1,307 million in 2025, compared with $753 million in 2024 [4].
> 
> None of these figures breaks out the CEO's pay.

<details><summary>Excerpts the system saw</summary>

```
[1] BlackRock, fiscal year ended 2025-12-31 (BLK_FY2025_10K), Item 7
7.7 million Subco Units outstanding.

(5)
Total BlackRock stockholders’ equity divided by total shares of common stock outstanding at December 31 of the respective year-end.

2025 Compared with 2024

GAAP. Operating income of $7.0 billion decreased $529 million and operating margin of 29.1% decreased 800 bps from 2024. Operating income and operating margin reflected higher revenue, driven by organic base fee growth, positive impact of markets and fees related to the HPS and GIP Transactions, as well as higher technology services and subscription revenue. Decreases in GAAP operating income and operating margin were driven by noncash acquisition-related expenses and the noncash Charitable Contribution. Operating income and operating margin for 2025 also included the impact of a $39 million restructuring charge, comprised of severance and compensation expense for accelerated vesting of previously granted deferred compensation awards, in connection with an initiative to modify the Company's organization to fit more closely with strategic priorities. In addition, expense for 2024 included a $50 million noncash impairment charge related to certain indefinite-lived open-end management contracts.

Nonoperating income (expense) net of NCI - CIPs decreased $266 million from 2024, primarily driven by lower net interest income (expense).

---

[2] BlackRock, fiscal year ended 2025-12-31 (BLK_FY2025_10K), Item 7
by the Company that are not yet legally binding. The Company intends to make additional capital commitments from time to time to fund additional investment products for, and with, its clients.

Compensation and Benefit Obligations. The Company has various compensation and benefit obligations, including bonuses, commissions and incentive payments payable, defined contribution plan matching contribution obligations, and deferred compensation arrangements. Accrued compensation and benefits at December 31, 2025 totaled $3.8 billion and included annual incentive compensation of $2.7 billion, deferred compensation of $0.5 billion and other compensation and benefits related obligations of $0.5 billion. Substantially all of the incentive compensation liability was paid in the first quarter of 2026, while the deferred compensation obligations are payable over various periods, with the majority payable over periods of up to three years.

---

[3] BlackRock, fiscal year ended 2025-12-31 (BLK_FY2025_10K), Item 7
a noncash Charitable Contribution(1) of $109 million and a restructuring charge(1) of $39 million. Expense for 2024 included the previously mentioned noncash impairment charge of $50 million.

Employee compensation and benefits expense of $8.4 billion in 2025 increased $1.9 billion from $6.5 billion in 2024, primarily reflecting the impact of the GIP, HPS and Preqin Transactions, including nonrecurring retention-related deferred compensation expense(1) and higher incentive compensation as a result of higher operating income and performance fees.

Sales, asset and account expense of $4.5 billion in 2025 increased $685 million from $3.8 billion in 2024, driven by higher direct fund expense and distribution and servicing costs, primarily reflecting higher average AUM.

General and administration expense of $2.7 billion in 2025 increased $474 million from $2.3 billion in 2024, primarily associated with the impact of the GIP, HPS and Preqin Transactions, including higher acquisition-related transaction costs(1) recorded in professional services, as well as the Charitable Contribution(1) and higher technology expense, and marketing and promotional expense, including the impact from higher travel and entertainment expense.

Change in fair value of contingent consideration(1) of $720 million in 2025 increased $756 million from $(36) million in 2024, primarily due to the impact of the GIP and HPS Transactions.

---

[4] BlackRock, fiscal year ended 2025-12-31 (BLK_FY2025_10K), Item FS
balance | $ | 124 | $ | 133
Acquisition (1) | 3 | —
Additions (2) | 218 | 84
Revenue recognized that was included in the beginning balance | ( 85 | ) | ( 93 | )
Ending balance | $ | 260 | $ | 124

(1)
Amount for 2025 includes deferred revenue acquired in connection with the Preqin Transaction, net of revenue recognized. See Note 3, Acquisitions, for information on the Preqin Transaction.

(2)
Amounts are net of revenue recognized.

F-34

18. Stock-Based Compensation

Prior to May 15, 2024, the Company maintained the BlackRock, Inc. Second Amended and Restated 1999 Stock Award and Incentive Plan. On May 15, 2024, the Company adopted, pursuant to shareholder approval, the BlackRock, Inc. Third Amended and Restated 1999 Stock Award and Incentive Plan (the "Award Plan"). Any awards granted on or after May 15, 2024 are granted pursuant to such plan.

The components of stock-based compensation expense are as follows:

(in millions) | 2025 | 2024 | 2023
Stock-based compensation:
RSUs (1) | $ | 1,282 | $ | 718 | $ | 596
Stock options | 25 | 35 | 34
Total stock-based compensation (2) | $ | 1,307 | $ | 753 | $ | 630

(1)
Amount for 2025 includes incentive retention awards granted in connection with the HPS and GIP Transactions of $394 million and $142 million, respectively. Amount for 2024 includes $71 million of incentive retention awards granted in connection with the GIP Transaction.

---

[5] BlackRock, fiscal year ended 2025-12-31 (BLK_FY2025_10K), Item 1
and contributions of BlackRock employees. Accordingly, the ability to attract, develop and retain qualified professionals is critical to the Company’s long-term success.

1

Financial Highlights

(in millions, except per share data)
GAAP: | 2025 | 2024 | 2023 | 2022 | 2021
Total revenue | $ | 24,216 | $ | 20,407 | $ | 17,859 | $ | 17,873 | $ | 19,374
Operating income | $ | 7,045 | $ | 7,574 | $ | 6,275 | $ | 6,385 | $ | 7,450
Operating margin | 29.1 | % | 37.1 | % | 35.1 | % | 35.7 | % | 38.5 | %
Nonoperating income (expense) (1) | $ | 312 | $ | 578 | $ | 706 | $ | 89 | $ | 419
Net income attributable to BlackRock, Inc. | $ | 5,553 | $ | 6,369 | $ | 5,502 | $ | 5,178 | $ | 5,901
Diluted earnings per common share | $ | 35.31 | $ | 42.01 | $ | 36.51 | $ | 33.97 | $ | 38.22

(in millions, except per share data)
As adjusted (2) : | 2025 | 2024 | 2023 | 2022 | 2021
Operating income | $ | 9,600 | $ | 8,110 | $ | 6,593 | $ | 6,711 | $ | 7,747
Operating margin | 44.1 | % | 44.5 | % | 41.7 | % | 42.8 | % | 46.8 | %
Nonoperating income (expense) (1) | $ | 251 | $ | 533 | $ | 648 | $ | 89 | $ | 419
Net income attributable to BlackRock, Inc. | $ | 7,736 | $ | 6,612 | $ | 5,692 | $ | 5,391 | $ | 6,254
Diluted earnings per common share | $ | 48.09 | $ | 43.61 | $ | 37.77 | $ | 35.36 | $ | 40.51

(1)
Net of net income (loss) attributable to noncontrolling interests ("NCI") - consolidated sponsored investment products ("CIPs") (redeemable and nonredeemable).
```

</details>

---

## q043 · unanswerable

**Question:** How many of MetLife's employees work in Japan?

**Gold answer:** This information is not in the documents. MetLife gives a total headcount (about 46,000) but no breakdown by country.

**Key points:**
1. States that the documents don't contain this information
2. Does not guess or invent a figure

**System answer:**

> The excerpts don't say how many MetLife employees work in Japan.
> 
> - MetLife had approximately 46,000 employees in total at December 31, 2025 [5]. The excerpt gives no breakdown by country or region.
> - Japan is the largest of MetLife's operations in Asia, where it operates in nine jurisdictions [1]. That is a statement about the scale of the business, not a headcount.
> - The other excerpts cover Japan-related policyholder account balances and insurance liabilities, not workforce figures [2][3][4].
> 
> So a Japan-specific employee count is not available from the provided material.

<details><summary>Excerpts the system saw</summary>

```
[1] MetLife, fiscal year ended 2025-12-31 (MET_FY2025_10K), Item 1
agreements are issued by certain of our insurance subsidiaries to the Federal Home Loan Bank of New York (“FHLBNY”) and to a subsidiary of the Federal Agricultural Mortgage Corporation.

Asia

Our Asia operations are geographically diverse encompassing both developed and emerging markets. We operate in nine jurisdictions throughout Asia, with our largest operation in Japan. We market our products and services through a range of proprietary and third-party distribution channels.

In Japan, our face-to-face channels, including both career and general agency, continue to be critical to our overall distribution strategy, catering to various needs of individual retail customers. Outside of Japan, our distribution strategies vary by market and leverage a combination of career and general agencies and bancassurance. In select markets, we also use independent brokers for retail sales and our employee sales force to sell group products.

Major Products
Life Insurance | Whole and term life, endowments, universal and variable life, as well as group life products.
Accident & Health Insurance | Full range of accident & health products, including hospitalization, cancer, critical illness, disability, income protection and personal accident coverage.
Retirement and Savings | Fixed and variable annuities, as well as regular savings products.

Latin America

---

[2] MetLife, fiscal year ended 2025-12-31 (MET_FY2025_10K), Item 8
| $ | 10,640 | $ | 24 | $ | 231 | $ | 1,001 | $ | 11,896
Equal to or greater than 2 % but less than 4 % | 5,932 | 15,634 | 7,801 | 7,669 | 37,036
Equal to or greater than 4 % | 250 | — | — | — | 250
Products with either a fixed rate or no GMCR | N/A | N/A | N/A | N/A | 557
Total | $ | 16,822 | $ | 15,658 | $ | 8,032 | $ | 8,670 | $ | 49,739

195

Table of Contents

MetLife, Inc.

Notes to the Consolidated Financial Statements — (continued)

5. Policyholder Account Balances (continued)

Fixed Annuities

Information regarding the Asia segment’s fixed annuity PAB liability in Japan was as follows:

Years Ended December 31,
2025 | 2024 | 2023
(Dollars in millions)
Balance at January 1, | $ | 38,421 | $ | 36,863 | $ | 32,454
Deposits | 6,889 | 6,221 | 8,115
Policy charges | ( 4 ) | ( 2 ) | ( 2 )
Surrenders and withdrawals | ( 2,003 ) | ( 2,760 ) | ( 2,344 )
Benefit payments | ( 1,836 ) | ( 2,208 ) | ( 2,156 )
Interest credited | 1,290 | 1,070 | 866
Effect of foreign currency translation and other, net | 431 | ( 763 ) | ( 70 )
Balance at December 31, | $ | 43,188 | $ | 38,421 | $ | 36,863
Weighted-average annual crediting rate | 3.2 % | 2.9 % | 2.5 %
At period end:
Cash surrender value | $ | 38,891 | $ | 34,105 | $ | 31,936
Net amount at risk, excluding offsets from reinsurance:
In the event of death (1) | $ | 2 | $ | 1 | $ | 73

__________________

---

[3] MetLife, fiscal year ended 2025-12-31 (MET_FY2025_10K), Item 8
less than 2 % | $ | — | $ | — | $ | 20 | $ | 1,651 | $ | 1,671
Equal to or greater than 2 % but less than 4 % | 249 | 34 | 105 | 432 | 820
Equal to or greater than 4 % | 4,346 | — | 282 | 5 | 4,633
Products with either a fixed rate or no GMCR | N/A | N/A | N/A | N/A | 10,587
Total | $ | 4,595 | $ | 34 | $ | 407 | $ | 2,088 | $ | 17,711

193

Table of Contents

MetLife, Inc.

Notes to the Consolidated Financial Statements — (continued)

5. Policyholder Account Balances (continued)

Asia

Universal and Variable Universal Life

The Asia segment’s universal and variable universal life PABs in Japan primarily include interest sensitive whole life products. Information regarding this liability was as follows:

Years Ended December 31,
2025 | 2024 | 2023
(Dollars in millions)
Balance at January 1, | $ | 50,801 | $ | 49,739 | $ | 46,417
Deposits | 6,478 | 5,885 | 7,595
Policy charges | ( 994 ) | ( 1,046 ) | ( 1,210 )
Surrenders and withdrawals | ( 3,157 ) | ( 3,171 ) | ( 2,959 )
Benefit payments | ( 536 ) | ( 451 ) | ( 508 )
Interest credited | 1,662 | 1,517 | 1,408
Effect of foreign currency translation and other, net | 120 | ( 1,672 ) | ( 1,004 )
Balance at December 31, | $ | 54,374 | $ | 50,801 | $ | 49,739
Weighted-average annual crediting rate | 3.2 % | 3.1 % | 3.0 %
At period end:
Cash surrender value | $ | 47,525 | $ | 44,685 | $ | 42,577
Net amount at risk, excluding offsets from reinsurance:
In the event of death (1) | $ | 82,387 | $ | 86,683 | $ | 93,172

---

[4] MetLife, fiscal year ended 2025-12-31 (MET_FY2025_10K), Item 8
products in Japan offer a contract feature whereby the Company guarantees to the contractholder a secondary guarantee. Information regarding these additional insurance liabilities was as follows:

Years Ended December 31,
2025 | 2024 | 2023 | 2025 | 2024 | 2023
Variable Life | Universal and Variable Universal Life
(Dollars in millions)
Balance, at January 1, | $ | 1,108 | $ | 1,258 | $ | 1,381 | $ | 355 | $ | 424 | $ | 455
Less: AOCI adjustment | — | — | — | 10 | ( 14 ) | ( 33 )
Balance, at January 1, before AOCI adjustment | 1,108 | 1,258 | 1,381 | 345 | 438 | 488
Effect of changes in cash flow assumptions | ( 3 ) | 17 | ( 4 ) | ( 46 ) | ( 23 ) | ( 2 )
Effect of actual variances from expected experience | ( 16 ) | ( 12 ) | ( 10 ) | ( 6 ) | ( 34 ) | ( 24 )
Adjusted balance | 1,089 | 1,263 | 1,367 | 293 | 381 | 462
Assessments accrual | ( 4 ) | ( 4 ) | ( 3 ) | ( 4 ) | — | —
Interest accrual | 17 | 17 | 19 | 5 | 6 | 7
Excess benefits paid | ( 33 ) | ( 38 ) | ( 36 ) | — | — | —
Effect of foreign currency translation and other, net | 5 | ( 130 ) | ( 89 ) | 4 | ( 42 ) | ( 31 )
Balance, at December 31, before AOCI adjustment | 1,074 | 1,108 | 1,258 | 298 | 345 | 438
Add: AOCI adjustment | — | — | — | 32 | 10 | ( 14 )
Balance, at December 31, | $ | 1,074 | $ | 1,108 | $ | 1,258 | $ | 330 | $ | 355 | $ | 424
Weighted-average duration of the liability | 16 years | 16 years | 16 years | 42 years | 42 years | 42 years

---

[5] MetLife, fiscal year ended 2025-12-31 (MET_FY2025_10K), Item 1
and other changes affecting the regulatory environment can affect our competitive position within the life insurance industry and the broader financial services industry. See “— Regulation.”

Human Capital Resources

At December 31, 2025, we had approximately 46,000 employees.

As a financial services company, meeting our business objectives requires that we rely significantly on our global workforce, leveraging a wide variety of professional, technical, management, business, and other skills and expertise, to create value for our stakeholders. Our priorities include a purpose driven and inclusive culture, talent and skill development, benefits and wellbeing, compensation, and attracting and retaining talent to support organizational readiness and business needs.
```

</details>

---

## q045 · unanswerable

**Question:** How much stock does Lincoln plan to repurchase in 2026?

**Gold answer:** This information is not in the documents. Lincoln discloses $714 million of remaining repurchase authorization at year-end 2025 with no expiration, but no planned 2026 repurchase amount; timing and amount depend on capital ratios and other factors.

**Key points:**
1. States that the documents don't contain this information
2. Does not guess or invent a figure

**System answer:**

> The excerpts don't state a planned 2026 repurchase amount for Lincoln. They only describe the existing authorization and recent activity:
> 
> - As of December 31, 2025, Lincoln's remaining security repurchase authorization was $714 million, out of a total aggregate authorization of $1.5 billion. The authorization has no expiration date [3].
> - The amount and timing of any repurchases depend on key capital ratios, rating agency expectations, free cash flow generation, and an evaluation of the costs and benefits of alternative uses of capital [3].
> - No shares were purchased under publicly announced plans or programs in the quarter ended December 31, 2025 [3].
> - In 2025, Lincoln sold about 18.8 million shares of its common stock to Bain Capital Prairie for $825 million, and it plans to deploy that capital toward strategic priorities such as growing spread-based earnings, portfolio management and asset sourcing, and optimizing its legacy life portfolio [1]. The excerpt does not mention repurchases as a use of that capital.
> 
> So the most that can be said is that up to $714 million remains available for repurchase, with no specific 2026 plan or target given. (The 2026 repurchase figures in the excerpts belong to Franklin Templeton, not Lincoln [2][5].)

<details><summary>Excerpts the system saw</summary>

```
[1] Lincoln National (Lincoln Financial), fiscal year ended 2025-12-31 (LNC_FY2025_10K), Item 7
of strengthening and maintaining our balance sheet, improving our operational efficiency, increasing free cash flow and focusing on profitable growth. Notable actions in 2025 include the following:

•During the second quarter of 2025, we closed our stock purchase agreement (the “Purchase Agreement”) with Bain Capital Prairie, LLC (the “Buyer”), a newly formed subsidiary of Bain Capital, under which we agreed to sell shares representing 9.9% of our outstanding common stock on a post-issuance basis to the Buyer. Under the final terms, Lincoln sold approximately 18.8 million shares of its common stock for aggregate consideration of $825 million. The transaction provided us with capital that we are deploying and expect to continue to deploy toward our strategic priorities, including growing spread-based earnings, advancing our portfolio management efforts and asset sourcing capabilities and optimizing our legacy life portfolio. For additional information on the Bain Capital transaction, see Note 18.

---

[2] Franklin Templeton (formerly Franklin Resources), fiscal year ended 2026-09-30 (BEN_FY2026_10K), Item 7
in fiscal year 2025. We currently expect to continue paying comparable regular dividends on a quarterly basis to holders of our common stock depending upon earnings and other relevant factors.

We maintain a stock repurchase program to manage our equity capital with the objective of maximizing shareholder value. Our stock repurchase program is effected through open-market purchases and private transactions in accordance with applicable laws and regulations, and is not subject to an expiration date. The size and timing of these purchases will depend on business conditions, price, market and other factors, including the terms of any 10b5-1 stock purchase plan that may be in effect at any given time. During fiscal years 2026 and 2025, we repurchased 17.0 million and 10.7 million shares of our common stock at a cost of $533.2 million and $240.3 million. The fiscal 2026 repurchases included 6.2 million

51

Table of Contents

shares repurchased from Great-West Lifeco Inc. (“Great-West”) for an aggregate purchase price of $208.0 million. In December 2025, our Board of Directors authorized the repurchase of up to an additional 20.8 million shares of our common stock in either open market or private transactions, for a total of up to 40.0 million shares available for repurchase under the stock repurchase program as of such authorization date. At September 30, 2026, 23.0 million shares remained available for repurchase under this authorization.

---

[3] Lincoln National (Lincoln Financial), fiscal year ended 2025-12-31 (LNC_FY2025_10K), Item 5
received in connection with the exercise of stock options and related taxes. For the quarter ended December 31, 2025, there were no shares purchased as part of publicly announced plans or programs.

(2) On November 10, 2021, our Board of Directors authorized an increase in our securities repurchase authorization, bringing the total aggregate repurchase authorization to $1.5 billion. As of December 31, 2025, our remaining security repurchase authorization was $714 million. The security repurchase authorization does not have an expiration date. The amount and timing of share repurchases depends on key capital ratios, rating agency expectations, the generation of free cash flow and an evaluation of the costs and benefits associated with alternative uses of capital. Our stock repurchases may be effected from time to time through open market purchases or in privately negotiated transactions and may be made pursuant to an accelerated share repurchase agreement or Rule 10b5-1 plan.

Item 6. [Reserved]

40

Table of Contents

Item 7. Management’s Discussion and Analysis of Financial Condition and Results of Operations

Index to Management’s Discussion and Analysis of Financial Condition and Results of Operations

---

[4] Lincoln National (Lincoln Financial), fiscal year ended 2025-12-31 (LNC_FY2025_10K), Item 8
of the fair value for mortgage loans on real estate. The cash received in these transactions is primarily invested in cash and invested cash or fixed maturity AFS securities.

145

Table of Contents

We have repurchase agreements through which we can obtain liquidity by pledging securities. The collateral requirements are generally 80% to 95% of the fair value of the securities, and our agreements with third parties contain contractual provisions to allow for additional collateral to be obtained when necessary. The cash received in our repurchase program is typically invested in fixed maturity AFS securities. Lincoln National Corporation guarantees the obligations of certain reinsurance subsidiaries under certain repurchase agreements. As of December 31, 2025 and 2024, we were not participating in any open repurchase agreements.

Increase (decrease) in payables for collateral on investments (in millions) consisted of the following:

For the Years Ended December 31,
2025 | 2024 | 2023
Collateral payable for derivative investments | $ | 596 | $ | 1,963 | $ | 1,966
Securities pledged under securities lending agreements | ( 12 ) | ( 48 ) | ( 93 )
Investments pledged for FHLB lending program | ( 2,650 ) | – | ( 480 )
Total increase (decrease) in payables for collateral on investments | $ | ( 2,066 ) | $ | 1,915 | $ | 1,393

---

[5] Franklin Templeton (formerly Franklin Resources), fiscal year ended 2026-09-30 (BEN_FY2026_10K), Item 5
July 2026 | 83,144 | $ | 33.61 | 83,144 | 25,485,906
August 2026 | 2,408,375 | 34.15 | 2,408,375 | 23,077,531
September 2026 | 30,447 | 32.41 | 30,447 | 23,047,084
Total | 2,521,966 | 2,521,966

Under our stock repurchase program, which is not subject to an expiration date, we can repurchase shares of our common stock from time to time in the open market and in private transactions in accordance with applicable laws and regulations, including without limitation applicable federal securities laws. In order to pay taxes due in connection with the vesting of employee and executive officer stock and stock unit awards, we may repurchase shares under our program using a net stock issuance method. In December 2025, our Board of Directors authorized the repurchase of up to an additional 20.8 million shares of our common stock in either open market or private transactions, for a total of up to 40.0 million shares available for repurchase under the stock repurchase program as of such authorization date.

Item 6. [Reserved]

Item 7. Management’s Discussion and Analysis of Financial Condition and Results of Operations.

FORWARD-LOOKING STATEMENTS
```

</details>

---

## q047 · unanswerable

**Question:** What were T. Rowe Price's ETF assets under management at the end of 2025?

**Gold answer:** This information is not in the documents. T. Rowe Price mentions its ETFs but doesn't report ETF AUM separately.

**Key points:**
1. States that the documents don't contain this information
2. Does not guess or invent a figure

**System answer:**

> The excerpts do not give T. Rowe Price's ETF assets under management at the end of 2025.
> 
> They do show related figures:
> - Total assets under management were $1,775.6 billion at December 31, 2025 [3].
> - ETFs are listed as one of the vehicles through which assets are sourced [2].
> 
> No excerpt breaks out AUM by vehicle for ETFs, so I can't provide that number.

<details><summary>Excerpts the system saw</summary>

```
[1] T. Rowe Price, fiscal year ended 2025-12-31 (TROW_FY2025_10K), Item 1
(4)Retail includes assets sourced through our direct-marketed business and financial intermediaries.

United States | U.S. Defined Contribution
APAC, EMEA, Canada | Other Retirement
Other Accounts

In 2025, our target date retirement products experienced net cash inflows of $5.2 billion. The assets under management in our target date retirement products totaled $561.4 billion at December 31, 2025, or 31.6% of our managed assets at December 31, 2025, compared to 29.6% at the end of 2024.

Additional information concerning our assets under management, results of operations, and financial condition during the past three years is contained in Part II, Item 7. Management’s Discussion and Analysis of Financial Condition and Results of Operations as well as our consolidated financial statements, which are included in Item 8. of this Form 10-K.

INVESTMENT MANAGEMENT SERVICES.

Investment Capabilities

We manage a broad range of investment strategies in equity, fixed income, multi-asset, and alternatives across sectors, styles and regions. Our strategies are designed to meet the varied and changing needs of investors and are delivered across a range of vehicles. We also offer specialized advisory services, including management of stable value investment contracts, customized multi-asset solutions, and a distribution management service for the disposition of equity securities our clients receive from third-party venture capital investment pools.

Page 4

Table of Contents

---

[2] T. Rowe Price, fiscal year ended 2025-12-31 (TROW_FY2025_10K), Item 1
assets under management at the end of 2025.

The following table outlines the five distribution channels and vehicles through which our assets under management are sourced as of December 31, 2025.

Vehicle | Retail | Institutional
Americas financial intermediaries | EMEA & APAC financial intermediaries | Individual U.S. investors on a direct basis | U.S. Defined Contribution | Institutional investors
U.S. Mutual Funds | x | x | x | x
Collective Investment Trusts | x | x | x
Exchange-Traded Funds | x | x | x
College Savings Plans | x | x
Model Portfolios | x | x | x (6)
Separately Managed Accounts (SMAs) (1) | x | x | x
Subadvised Accounts | x | x | x | x
Separate Accounts | x | x | x | x | x
SICAVs (2) / FCPs (3) | x | x | x
Canadian Pooled Funds | x | x
OEICs (4) | x | x
Japanese ITMs (5) | x | x
Australian Unit Trusts | x | x
Private Funds | x
Collateralized Loan Obligations | x
Business Development Company (BDC) | x | x
Interval Funds | x | x

Page 6

Table of Contents

(1) Includes both model delivery and manager traded SMAs,. (2)Société d'Investissement à Capital Variable (Luxembourg), (3)Fonds Commun de Placement (Luxembourg), (4)Open-Ended Investment Company (U.K.), (5)Japanese Investment Trust Management Funds, (6) Provided through our ActivePlus and Retirement Advisory Service Portfolios.

INVESTMENT ADVISORY FEES.

---

[3] T. Rowe Price, fiscal year ended 2025-12-31 (TROW_FY2025_10K), Item 1
value and composition of our assets under management. Accordingly, fluctuations in financial markets and in the composition of assets under management impact our revenues and results of operations.

At December 31, 2025, we had $1,775.6 billion in assets under management, an increase of $169.0 billion from the end of 2024. This increase in assets under management was driven by market appreciation, net of distributions not reinvested, of $216.7 billion, offset by net cash outflows of $56.9 billion. Beginning on July 1, 2025, assets under management include managed account - model delivery portfolios assets, which had $9.2 billion in assets as of that date, and are reflected in the increase from December 31, 2024.

The following charts show our AUM (in billions) by asset class, client type, geography, and account type as of December 31 for the prior three years:

Equity | Institutional (3)
Fixed Income, including money market | Retail (4)
Multi-Asset (1)
Alternatives (2)

(1)The underlying AUM of the multi-asset products have been aggregated and presented in this category and not reported in the equity and fixed income rows.

---

[4] T. Rowe Price, fiscal year ended 2025-12-31 (TROW_FY2025_10K), Item 7
delivery assets.

(2) The underlying assets under management of the multi-asset products have been aggregated and presented in this category and not reported in the equity and fixed income columns.

(3) The alternatives asset class includes strategies authorized to invest more than 50% of its holdings in private credit, leveraged loans, mezzanine, real assets/CRE, structured products, stressed/distressed, non-investment grade CLOs, special situations, business development companies, or that have absolute return as its investment objective. Generally, only those strategies with longer than daily liquidity are included. Unfunded capital commitments were $21.6 billion at December 31, 2025, $16.2 billion at December 31, 2024, and $11.6 billion at December 31, 2023, and are not reflected in fee basis AUM above.

(4) Includes net distributions not reinvested of $6.8 billion in 2025, $5.9 billion in 2024, and $2.9 billion in 2023.

(5) Amount represents the net assets as of July 1, 2025 and all activity for the second half of 2025 is presented in the lines that follow.

Investment advisory clients outside the United States account for 8.8% of our assets under management at December 31, 2025 and December 31, 2024 and 8.6% at December 31, 2023.

The following table details our assets under management and net flows in our target date retirement products, which are included in the multi-asset column shown above:

---

[5] T. Rowe Price, fiscal year ended 2025-12-31 (TROW_FY2025_10K), Item 7
| Total returned to stockholders
2023 | $ | 1,121.9 | $ | 254.3 | $ | 1,376.2
2024 | 1,135.2 | 334.5 | 1,469.7
2025 | 1,143.4 | 624.6 | 1,768.0
Total | $ | 3,400.5 | $ | 1,213.4 | $ | 4,613.9

We anticipate property, equipment, software and other capital expenditures, including internal labor capitalization, for the full-year 2026 to be about $270 million, of which more than three-quarters is planned for technology initiatives. We expect to fund our anticipated capital expenditures with operating cash flows and other available resources.

Cash Flows

The following tables summarize the cash flows for 2025, 2024 and 2023, that are attributable to T. Rowe Price Group, our consolidated investment products, and the related eliminations required in preparing the consolidated statement of cash flows.
```

</details>

---

## q048 · unanswerable

**Question:** How many clients use BlackRock's Aladdin platform?

**Gold answer:** This information is not in the documents. BlackRock reports Aladdin revenue and ACV growth but no client count.

**Key points:**
1. States that the documents don't contain this information
2. Does not guess or invent a figure

**System answer:**

> The excerpts do not give a number of clients using Aladdin. They describe the types and geographic reach of clients, but not a count.
> 
> - Technology services and subscription clients at year-end included asset managers, insurance companies, wealth managers, pension funds, official institutions, banks, asset servicers, corporations, law firms, consultants and other investors across North America, South America, Europe, the Middle East, Asia, Africa and Australia [4]. This is for technology services and subscription clients overall, not Aladdin alone.
> - Aladdin Enterprise serves BlackRock and "a growing number of institutional investors around the world" [2].
> - Revenue growth in 2025 reflected the onboarding of a number of new clients and expanding relationships with existing clients [5].
> 
> Other Aladdin metrics are given, but they are not client counts:
> - Technology services and subscription revenue was $2.0 billion, up 24% year-over-year [5].
> - Annual contract value rose 31% including Preqin and 16% excluding Preqin, driven by strong net sales of Aladdin [5].
> - Aladdin represented the majority of technology services and subscription revenue [5].

<details><summary>Excerpts the system saw</summary>

```
[1] BlackRock, fiscal year ended 2025-12-31 (BLK_FY2025_10K), Item 7
them with choice and flexibility. Through the integration of Aladdin and eFront, clients are able to better manage and analyze risk across their whole portfolio spanning public and private markets. BlackRock is empowering clients with data and opening Aladdin by creating connectivity with ecosystem providers and third-party technology solutions, which include asset servicers, cloud providers, digital asset platforms, trading systems, and others. This connectivity helps clients work in their Aladdin environments with a more customized and seamless end-to-end experience. Investments in Aladdin AI copilots, enhancements in openness supporting ecosystem partnerships, and advancing whole portfolio solutions including private markets and digital assets are expected to further augment the value of using Aladdin. BlackRock’s acquisition of Preqin further expanded capabilities beyond private markets investment management and technology to data.

---

[2] BlackRock, fiscal year ended 2025-12-31 (BLK_FY2025_10K), Item 1
median information, as selected by BlackRock. Peer medians are based in part on data either from Lipper, Inc. or Morningstar, Inc. for each included product.

TECHNOLOGY SERVICES AND SUBSCRIPTION

BlackRock offers investment management technology systems, risk analytics, private markets data subscriptions, investment accounting services and wealth management tools on a fee basis. Aladdin Enterprise is the Company's proprietary technology platform, providing an end-to-end, investment and risk management solution for both BlackRock and a growing number of institutional investors around the world. BlackRock offers risk analytics via Aladdin Risk, as well as investment accounting capabilities. eFront is a leading end-to-end alternative investment management software and solutions provider to enable clients to manage portfolios across public and private asset classes on a single platform. eFront is offered to clients both as a standalone offering and as part of an integrated “Whole Portfolio” solution that provides transparency across clients’ public and private assets. Aladdin Wealth provides wealth management firms and their financial professionals with institutional-quality business management, portfolio construction, modeling and risk analytics capabilities.

---

[3] BlackRock, fiscal year ended 2025-12-31 (BLK_FY2025_10K), Item 1
of positions managed on the platform are fixed income. Revenue growth in 2025 reflected the successful onboarding of a number of new clients and expanding relationships with existing clients.

The Company’s acquisition of Preqin in March 2025 added private markets data capabilities to its existing Aladdin and eFront workflow offerings, creating a preeminent private markets technology and data provider. As clients’ private market allocations continue to grow, they will require more standardized and transparent data on their investments, creating an additional growth opportunity for Preqin.

BlackRock is focused on enhancing Aladdin, with continued investment into areas such as AI, whole portfolio, private markets, and wealth. BlackRock continues to evolve and enable clients to further simplify their operating infrastructure with Aladdin. Clients increasingly want to tailor how they use Aladdin to meet their specific needs, and BlackRock is providing them with choice and flexibility. BlackRock is empowering clients with data and APIs, as well as creating connectivity with ecosystem providers and third-party technology solutions, which include asset servicers, cloud providers, digital asset platforms, trading systems and others. This connectivity helps clients work in their Aladdin environments with a more customized and seamless end-to-end experience.

---

[4] BlackRock, fiscal year ended 2025-12-31 (BLK_FY2025_10K), Item 1
Aladdin Wealth provides wealth management firms and their financial professionals with institutional-quality business management, portfolio construction, modeling and risk analytics capabilities.

Through the Company's Cachematrix platform, BlackRock is also a leading provider of financial technology which simplifies the cash management process for banks and their corporate clients in a streamlined, open-architecture platform. In March 2025, BlackRock completed the acquisition of 100% of the shares of Preqin Holding Limited ("Preqin"), a leading provider of private markets data, for £2.5 billion (or approximately $3.2 billion) in cash (the "Preqin Transaction").

At year-end, BlackRock technology services and subscription clients included asset managers, insurance companies, wealth managers, pension funds, official institutions, banks, asset servicers, corporations, law firms, consultants and other investors across North America, South America, Europe, the Middle East, Asia, Africa and Australia.

---

[5] BlackRock, fiscal year ended 2025-12-31 (BLK_FY2025_10K), Item 1
official institutions, banks, asset servicers, corporations, law firms, consultants and other investors across North America, South America, Europe, the Middle East, Asia, Africa and Australia.

Technology services and subscription revenue of $2.0 billion was up 24% year-over-year. Annual contract value (“ACV”) increased 31% year-over-year including ACV related to Preqin, and increased 16% excluding ACV related to Preqin, driven by strong net sales of Aladdin in 2025. Aladdin assignments are typically long-term contracts that provide recurring revenue. At the end of any period, BlackRock generally has recurring revenue contracts in place for a large portion of total annual revenue. BlackRock measures the fees related to these agreements and refers to this as ACV. For further information on ACV, see Item 7. Management’s Discussion and Analysis of Financial Condition and Results of Operations — Non-GAAP Financial Measures.

Aladdin, which represented the majority of technology services and subscription revenue for the year, continues to benefit from trends favoring global platform and multi-asset risk solutions across public and private markets. In addition, while Aladdin is a multi-asset system, the majority of positions managed on the platform are fixed income. Revenue growth in 2025 reflected the successful onboarding of a number of new clients and expanding relationships with existing clients.
```

</details>

---

## q050 · unanswerable

**Question:** What is the name of Lincoln's Chief Information Security Officer?

**Gold answer:** This information is not in the documents. Lincoln describes the CISO's experience and reporting line but doesn't name the person.

**Key points:**
1. States that the documents don't contain this information
2. Does not guess or invent a figure

**System answer:**

> The excerpts do not give the name of Lincoln's Chief Information Security Officer. They describe the role without naming the person. The CISO has over 20 years of cybersecurity experience, holds a Certified Information Security Systems Professional designation, and leads a staff of more than 100 employees [1]. The CISO reports directly to the Chief Information Officer [1], and the excerpts name Jennifer Charters as the CIO [4]. The CISO also has primary responsibility for material risks from cybersecurity threats [2].

<details><summary>Excerpts the system saw</summary>

```
[1] Lincoln National (Lincoln Financial), fiscal year ended 2025-12-31 (LNC_FY2025_10K), Item 1C
which provides oversight of our enterprise-wide risk structure and of our processes to identify, measure, monitor and manage significant risks, including, but not limited to, cybersecurity risk.

The Information Security organization is led by our CISO. The head of each of the four divisions of our Information Security team reports directly to the CISO. The CISO reports directly to the Company’s Chief Information Officer (“CIO”), who is a member of the Company’s Senior Management Committee. As a result, all information security personnel report into the CISO, and ultimately the CIO. The CISO also reports indirectly to the Audit Committee of the Board of Directors. Biannually, the CISO reports to the Audit Committee on the cybersecurity risks facing the Company and cybersecurity developments generally. In addition, as discussed above, the Company’s Internal Audit team reports to the Audit Committee the results of its annual security audit focused on cybersecurity risks. The Company’s Chief Compliance Officer reports key Privacy risk indicators and statistics (including those related to cybersecurity risks) to the Audit Committee on a quarterly basis.

Our current CISO has over 20 years of experience in the field of cybersecurity and holds a Certified Information Security Systems Professional designation. The CISO has a staff of more than 100 employees dedicated to protecting the data and systems belonging to the Company, our customers, business partners and consumers.

37

---

[2] Lincoln National (Lincoln Financial), fiscal year ended 2025-12-31 (LNC_FY2025_10K), Item 1C
risks. The Board has also delegated certain of its risk oversight efforts to its committees. Oversight of cybersecurity risk has been delegated to the Audit Committee of the Board of Directors.

The Company’s senior management is primarily responsible for establishing policies and procedures designed to identify, assess and manage the Company’s significant risks, with our Chief Information Security Officer (“CISO”) having primary responsibility with respect to material risks from cybersecurity threats. We also have a Corporate Enterprise Risk and Capital Committee, made up of members of senior management and the Company’s Chief Risk Officer, which provides oversight of our enterprise-wide risk structure and of our processes to identify, measure, monitor and manage significant risks, including, but not limited to, cybersecurity risk.

---

[3] Lincoln National (Lincoln Financial), fiscal year ended 2025-12-31 (LNC_FY2025_10K), Item 1C
subject to third-party information system and other operational risks due to our reliance on third-party vendors and suppliers and the outsourcing of certain of our business operations” and “Item 1A. Risk Factors – Legislative, Regulatory and Tax – Compliance with existing and emerging privacy laws and regulations could result in increased compliance costs and/or lead to changes in business practices and policies, and any failure to protect the confidentiality of personal information could adversely affect our reputation and have a material adverse effect on our business, financial condition and results of operations.”

Governance

The Company’s Board of Directors is responsible for regular oversight of the Company’s overall risk management process. The Board reviews the most significant risks the Company faces and the manner in which our executives manage these risks. The Board has also delegated certain of its risk oversight efforts to its committees. Oversight of cybersecurity risk has been delegated to the Audit Committee of the Board of Directors.

---

[4] Lincoln National (Lincoln Financial), fiscal year ended 2025-12-31 (LNC_FY2025_10K), Item 3
and Litigation Matters” in Note 17, which is incorporated herein by reference.

Item 4. Mine Safety Disclosures

Not applicable.

38

Table of Contents

Information About our Executive Officers

Our Executive Officers as of February 12, 2026, were as follows:
Name | Age (1) | Position with LNC and Business Experience During the Past Five Years
Ellen G. Cooper | 61 | President, Chief Executive Officer and Director (since May 2022); Chairman of the Board of Directors (since May 2023). Until May 2022, Executive Vice President (since August 2012), Head of Enterprise Risk (since 2019) and Head of Annuity Solutions Group (since March 2021). Chief Investment Officer (August 2012 - November 2021).
Nilanjan (Neel) Adhya | 51 | Executive Vice President, Chief AI, Data and Analytics Officer (since January 2026). Chief Digital Officer and Global Head of Digital Platforms and Experiences (August 2021 - December 2025), BlackRock, an investment management corporation. Chief Digital Officer and Vice President of Digital Transformation (June 2019 - August 2021), IBM, a technology company.
Craig T. Beazer | 58 | Executive Vice President and General Counsel (since December 2020).
Jennifer Charters | 53 | Executive Vice President and Chief Information Officer (since November 2024). Executive Vice President and Chief Information Officer, Flagstar Bank (June 2018 - August 2024).

---

[5] Lincoln National (Lincoln Financial), fiscal year ended 2025-12-31 (LNC_FY2025_10K), Item 1C
engineering division, which leads our “security by design” efforts to help ensure cybersecurity considerations are taken into account in our applications, cloud architecture and infrastructure;

•The governance, risk and compliance division, which includes responsibility for developing cybersecurity-related policies and procedures, training and supplier security review;

•The cybersecurity response and investigations (“CSRI”) division; and

•The identity access management division, which is responsible for managing access to our data and technology infrastructure.

The work done by each of these divisions is applied both tactically and strategically to operations, as well as to broader risk management activities.

The governance, risk and compliance division of our Information Security team includes a dedicated information technology (“IT”) and cyber operation risk assessment team. This team conducts assessments that are focused on the Company’s most significant IT and cyber risks, the results of which are leveraged by the Company’s IT leadership, among other inputs, to mitigate, reduce and/or manage against such risks. While it is not possible to be certain that all risks, threats and vulnerabilities to our information and systems have been identified, our cybersecurity risk management processes are designed to, using a risk-based approach, identify reasonably known risks from cybersecurity threats and ensure material risks are managed appropriately.
```

</details>
