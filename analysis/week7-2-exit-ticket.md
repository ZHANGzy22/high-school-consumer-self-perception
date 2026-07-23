# Week 7-2 Exit Ticket

## Exit 1: Pre-Specified Cleaning Rule

Before looking at outcome patterns, I define a valid record as one anonymous session that has:

1. one row in `sessions`;
2. five shopping-stage records in `simulation_events`;
3. one row in `result_feedback`;
4. non-missing pre-test and post-test awareness scores.

This cleaning rule is about completion quality. It does not remove records based on whether they support the hypothesis.

Current audit result:

| Item | Count |
|---|---:|
| Completed anonymous sessions | 41 |
| Shopping-stage records | 205 |
| Sessions missing result feedback | 0 |
| Sessions without five shopping-stage records | 0 |
| Final valid sample | 41 |

## Exit 2: Results Draft

The final dataset included 41 completed anonymous sessions and 205 shopping-stage records. Each valid participant had five recorded shopping-stage actions and one post-test feedback record.

The mean pre-test awareness score was 3.821 (SD = 0.628). The mean post-test awareness score was 3.228 (SD = 0.529). The mean change score, calculated as post-test minus pre-test, was -0.593 (SD = 0.673). Thirty participants had lower post-test scores, five participants had no change, and six participants had higher post-test scores.

An exploratory paired-samples calculation produced t(40) = -5.646. The approximate 95% confidence interval for the mean change was from -0.805 to -0.381. The standardized within-participant change was dz = -0.882.

Action distribution by shopping stage:

| Stage | Main recorded pattern |
|---|---|
| Product feed | 41 opened a product |
| Price-drop pop-up | 21 viewed the price drop, 12 postponed, 8 closed the reminder |
| Product detail | 15 bought immediately, 9 added to cart, 11 checked reviews, 6 checked rules |
| Checkout | 27 kept the default paid service, 8 cancelled it, 6 checked more information |
| Final review | 29 submitted the simulated order, 6 stopped, 4 checked more reviews, 2 chose a cheaper option |

Rule-based mismatch indicators compared self-perception answers with recorded choices. Thirty-one participants, or 75.6% of the sample, had at least one mismatch. The average mismatch count was 2.024 out of four possible gap dimensions.

| Gap Type | Count | Percentage |
|---|---:|---:|
| Any gap | 31 | 75.6% |
| Budget-control gap | 22 | 53.7% |
| Default-option gap | 22 | 53.7% |
| Time-pressure gap | 20 | 48.8% |
| Information-checking gap | 19 | 46.3% |

Participants with zero mismatch indicators had an average recalibration score of 0.033 points. Participants with four mismatch indicators had an average recalibration score of 1.277 points. The correlation between mismatch count and recalibration score was 0.758.

Open-text feedback was coded with a first-pass theme-led method. One response could receive more than one code.

| Theme | Count |
|---|---:|
| Information checking / reviews / rules | 21 |
| Default service / checkout design | 20 |
| Time pressure / discount reminder / pop-up | 18 |
| Self-perception recalibration | 14 |
| Product interest | 11 |
| Budget / price concern | 10 |
| Blank reflection | 1 |
| Blank influence notes | 4 |

Representative anonymous responses, translated from Chinese:

1. "I thought I knew this kind of promotion trick, but I still clicked it."
2. "I thought I would compare more, but after seeing the price drop I quickly moved into checkout."
3. "I was very confident in my own judgment, but after adding something to the cart, I was more likely to continue along the process."

## Exit 3: Discussion Finding + One Limitation

The main finding is that the shopping-platform simulation made the self-perception gap visible through two patterns: many participants had recorded mismatches between their self-perception and choices, and many participants lowered their post-test rating of how well they could predict or explain their own choices.

The original hypothesis expected the awareness score to increase. The actual score decreased. I can explain this as self-perception recalibration. After using the artifact, many participants may have realized that they were less able to predict or explain their consumer choices than they had believed before the simulation.

One limitation is that this is a small, voluntary, non-random classroom sample. The result can show an early pattern in this group, but it cannot prove a causal effect for all high school students.

## Current Completion Status

Completed:

1. The website artifact has been built and deployed.
2. The first-screen informed consent has been added.
3. Supabase is connected and stores anonymous session, event, and feedback data.
4. The current dataset has 41 completed anonymous sessions.
5. Cleaning checks, descriptive statistics, action distributions, gap indicators, and first-pass qualitative coding have been prepared.
6. Three charts have been generated in `analysis/charts/`.

Still worth polishing:

1. Keep the paired-samples t statistic in the main Results, but label it as exploratory rather than final proof.
2. Choose 2-3 short open-text responses for the final paper if the teacher wants qualitative examples.
3. Insert the generated charts into the final presentation or final report.
4. Keep the original hypothesis, then explain the opposite score direction as recalibration rather than rewriting the hypothesis after seeing the data.
