# Week 7 / Week 7-2 Progress Check

## Current Project Status

The project now has a working interactive shopping-platform simulation, a Supabase backend, a valid dataset, and a first full analysis written into `final-paper.md`.

Core research question:

How does an interactive shopping platform simulation affect high school students' recognition of gaps between their consumer self-perception and their observed choices?

Current interpretation:

The post-test score decreased. This is interpreted as self-perception recalibration: after seeing the gap between self-image and simulated behavior, many participants became less confident that they could predict or explain their own consumer choices.

## Week 7: What Is Done

1. The artifact exists and can be opened as a website.
2. The artifact has an informed-consent first screen.
3. The study has a clear research question and hypothesis.
4. The method is written as a within-participant pre-test/post-test design.
5. The data collection path is connected to Supabase.
6. The final paper now has updated Methods, Results, and Discussion sections.
7. The analysis uses 41 completed anonymous sessions.

## Week 7: What Still Needs Attention

1. The recruitment paragraph has been added: the link was shared with classmates, a class group chat, and the researcher's social media feed from July 12 to July 22, 2026; participation was voluntary and unpaid.
2. The paper now describes the data as structured interaction records from the designed shopping simulation. The analysis focuses on the stages, choices, products, prices, timing fields, and feedback fields recorded by this project.
3. The hypothesis wording has been clarified. The original expectation was an increase in awareness, while the observed decrease is interpreted as self-perception recalibration.
4. Ethics details are included: anonymous, voluntary, no payment, no names, no phone numbers, no real purchases, classroom research only.

## Week 7-2: What Is Done

1. Supabase tables have been checked:
   - `sessions`: 41 rows
   - `simulation_events`: 205 rows
   - `result_feedback`: 41 rows
2. Every completed participant has five shopping-stage events.
3. Pre-test and post-test awareness scores are complete for 41 participants.
4. Rule-based gap indicators are complete in `profile_label_details`.
5. Descriptive statistics have been calculated.
6. Main action distributions have been calculated.
7. Open-text feedback has been coded with a first-pass theme count.

## Data Health Check

Supabase audit result:

| Check | Result |
|---|---:|
| Missing result feedback | 0 |
| Sessions without five events | 0 |
| Missing stage or action fields | 0 |
| Missing product category fields | 0 |
| Missing product name fields | 0 |
| Missing price fields | 0 |
| Missing budget pressure fields | 0 |
| Missing decision time fields | 0 |
| Gap sum inconsistent with mismatch count | 0 |
| Completion time before start time | 0 |

Data collection time range in China time:

July 12, 2026, 10:05 to July 22, 2026, 09:42.

## Week 7-2: Main Results

Valid sample: 41 participants.

Pre-test mean: 3.821.

Post-test mean: 3.228.

Mean change: -0.593.

Direction:

30 participants decreased, 5 stayed the same, and 6 increased.

Interpretation:

Participants generally rated their ability to predict or understand their own choices lower after the simulation. This supports the idea that the simulation made the gap more visible.

Important interpretation note:

The original hypothesis expected the awareness score to increase. The actual score decreased. This should not be written as a simple failure. The repeated score asks participants how well they think they can predict or explain their own consumer choices. After the simulation, many participants may have realized that they were less able to predict their own behavior than they had assumed. In that sense, the lower score can be interpreted as a recalibration of self-understanding: users became more aware of their own overconfidence.

Mismatch result:

31 out of 41 participants had at least one gap between self-perception and simulated choice.

Most common gap dimensions:

1. Budget-control gap: 22 participants.
2. Default-option gap: 22 participants.
3. Time-pressure gap: 20 participants.
4. Information-checking gap: 19 participants.

Stronger pattern:

Participants with more mismatch indicators showed larger decreases in post-test self-rating. This is the strongest quantitative support for the project.

## What Still Needs To Be Finished

1. The Week 7-2 exit ticket has been written in `analysis/week7-2-exit-ticket.md`. It includes the cleaning rule, final valid N = 41, and the rule that records are filtered by completion quality rather than by result direction.

2. Add 2-3 representative open-text responses to the Results or Discussion if the teacher allows short qualitative evidence.

3. Decide whether the exploratory paired t statistic should stay in the main Results or move to a smaller note. It can stay, but the wording must remain cautious due to the small classroom sample.

4. Insert the three generated figures into the final presentation or paper:
   - `analysis/charts/pre-post-awareness.svg`
   - `analysis/charts/gap-indicators.svg`
   - `analysis/charts/mismatch-recalibration.svg`

5. Keep the limitation clear: this is a small, voluntary, non-random classroom prototype study, so the result can suggest a pattern but cannot prove a causal effect for all high school students.
