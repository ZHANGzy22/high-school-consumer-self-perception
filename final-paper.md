# Seeing the Gap: An Interactive Shopping-Platform Simulation for High School Students

Zhiyan Zhang
Research Advisor: Lawted Wu

## Abstract

High school students routinely encounter discounts, recommendations, countdowns, reviews, and default options, yet confidence in consumer judgment may not correspond to behavior within these interfaces. Existing research has examined advertising literacy, self-report bias, consumer decision styles, and manipulative interface design, but these strands have rarely been combined in a short interactive experience that compares self-perception with simulated choice. This study developed a browser-based shopping-platform simulation in which users completed pre-use measures, made five controlled shopping decisions, received a rule-based comparison of their responses and actions, and completed the same awareness measure afterward. Using a within-participant pre-test/post-test design, the study examined change in awareness of the gap between intended and simulated behavior among [TODO: actual or target N and recruitment population]. We expected post-use awareness to be higher than pre-use awareness, with data collection and results pending.

## Introduction

High school students made consumer decisions within a dense digital environment shaped by shopping platforms, short videos, product recommendations, peer culture, online reviews, discounts, membership systems, and interface design. These decisions involved more than personal preference or available money. Urgency messages, default options, price framing, and conflicting information could shape behavior at the point of choice.

Many students also held an image of themselves as careful, budget-conscious, or information-aware consumers. However, this self-perception did not necessarily indicate how they would act in a realistic choice environment. Advertising knowledge may not be activated at the moment of exposure (Rozendaal et al., 2011), and self-report measures may reflect socially desirable or idealized descriptions rather than observed behavior (Donaldson & Grant-Vallone, 2002). This distinction made it necessary to compare stated judgment habits with actions rather than rely on self-report alone.

Research on adolescents' self-reported advertising literacy showed that young people could describe their ability to recognize, understand, and resist advertising (De Jans et al., 2018). Consumer decision-making research likewise treated judgment as multidimensional, including price awareness, impulsiveness, quality concern, and confusion from excessive choice (Sproles & Kendall, 1986). At the interface level, online shopping environments have used urgency, social proof, default choices, and hidden costs to guide behavior (Mathur et al., 2019). Controlled vignette methods offered a way to retain recognizable situations while isolating specific mechanisms for analysis (Steiner et al., 2017).

The present study connected these areas in one interactive artifact. Rather than classifying participants as rational or irrational, it examined whether a shopping-platform simulation could make differences between consumer self-perception and simulated choice more visible. The research question was: How did an interactive shopping-platform simulation affect high school students' recognition of gaps between their consumer self-perception and their simulated shopping choices? It was hypothesized that awareness of this gap would be higher after the simulation than before it.

## Methods

### Artifact and Procedure

The deployed artifact was a single-page, browser-based shopping-platform simulation designed for high school students. On entering the tool, participants answered two background questions concerning their monthly disposable-money range and product categories encountered during the previous 30 days. They then completed three pre-use awareness items and four consumer self-perception items. All seven items used five-point response scales. The self-perception items addressed budget impact, information checking, attention to additional services, and responses to sudden price reductions.

Participants subsequently completed five controlled shopping stages: a product feed, a price-drop pop-up, a product-detail page, a checkout page containing a preselected paid service, and a final page combining conflicting review information with a budget warning. Each stage imposed a 60-second limit and recorded one selected action. A short addition task separated consecutive shopping stages and was not included in the consumer measures. No real purchase or payment occurred.

The product feed displayed four cards. Product categories were selected from the participant's recent-category responses and from categories that the participant had not selected. Displayed prices were calculated deterministically from the budget anchor assigned to the selected disposable-money range, using target ratios of 8%, 12%, 18%, and 32%. The system recorded a randomly generated session identifier, background and scale responses, action order, stage, selected action, product category and name, whether the product belonged to a recently encountered category, displayed price, price as a percentage of the budget anchor, and time remaining at selection.

After the fifth stage, the result screen displayed rule-based comparisons between self-perception and recorded choices. It then administered the same three awareness items as a post-test, a five-point rating of perceived profile fit, and two optional open-text prompts asking what the participant had learned and which page elements had influenced the choices.

All product names, shopping messages, reviews, page mechanisms, and result-classification rules were prewritten and curated for the study. The artifact did not call an AI model, a generative-AI service, a live shopping service, or a prediction API. Its personalized product feed and “consumer profile” were deterministic mock outputs derived from the participant's budget range, selected categories, scale responses, and recorded actions. Supabase REST endpoints were used only to store anonymous research records.

### Research Design and Measures

The study used a single-group, within-participant pre-test/post-test design. The independent variable was measurement time relative to the simulation (pre-use versus post-use). The primary dependent variable was awareness of the gap between intended and simulated shopping behavior, operationalized as the mean of three repeated items: perceived ability to predict one's shopping choices, perceived correspondence between intentions and actions, and perceived ability to identify influential page information. The primary comparison was the within-participant change in mean awareness score. An increase of at least 0.5 points in the sample mean was prespecified as an exploratory success criterion rather than a confirmatory threshold.

Secondary behavioral outcomes included product-path selection, responses to the price-drop prompt, review or rule checking, retention or cancellation of the default paid service, continuation under budget pressure, selection of a cheaper specification, stopping the simulated purchase, action order, and remaining decision time. The interface also generated descriptive mismatch indicators by comparing each self-perception dimension with its corresponding recorded action.

### Consent and Data Handling

Informed consent was presented as a required first screen. It stated that participation was voluntary, nonparticipation had no consequences, participants could leave at any time by closing the page, responses would be used only for classroom research, and names, telephone numbers, and student identifiers would not be collected. Participants continued by selecting “I agree, start the test”; those who did not agree were instructed to close the page. The tool also stated that no real purchase records or payment information were collected. Records were linked through a randomly generated session identifier rather than a direct personal identifier. [TODO: Add an explicit statement that the activity was non-clinical to the deployed first screen before recruiting participants, then describe that implemented wording here.] [TODO: State any parent/guardian permission or school approval procedure actually used for participants under 18.]

### Participants, Recruitment, and Analysis

The target population consisted of high school students. [TODO: State the actual recruitment channel, setting, dates, eligibility criteria, compensation, number recruited, and number of valid completed sessions.] No participant count was reported before real data collection.

The analysis protocol treated each anonymous session as one case. Pre-test and post-test awareness scores and within-participant change scores were summarized using counts, means, standard deviations, medians, and ranges. Frequencies and percentages were calculated for recorded actions and rule-based mismatch indicators. Recently encountered and other product-category pathways were compared descriptively. [TODO: Specify the validity and exclusion rules, handling of incomplete or timed-out sessions, and the paired inferential test actually used, if any.]

The two open-text responses were supplementary qualitative material. [TODO: Before coding, specify whether the codebook was inductive or theory-led, whether multiple codes could be assigned to one response, who coded the responses, how disagreements were resolved, and whether inter-coder agreement was calculated.] No coded qualitative findings were reported before this procedure had been completed.

## Results

[Pending data: this section will report the valid sample, pre-test and post-test awareness summaries, within-participant change, behavioral-action frequencies, and mismatch indicators after test records have been excluded and real participant data have been collected.]

## Discussion

[Pending real results. No interpretation was written before data collection and analysis.]

## References

De Jans, S., Hudders, L., & Cauberghe, V. (2018). Adolescents' self-reported level of dispositional advertising literacy: How do adolescents resist advertising in the current commercial media environment? *Young Consumers, 19*(4), 402–420. https://doi.org/10.1108/YC-02-2018-00782

Donaldson, S. I., & Grant-Vallone, E. J. (2002). Understanding self-report bias in organizational behavior research. *Journal of Business and Psychology, 17*, 245–260. https://doi.org/10.1023/A:1019637632584

Mathur, A., Acar, G., Friedman, M. J., Lucherini, E., Mayer, J., Chetty, M., & Narayanan, A. (2019). Dark patterns at scale: Findings from a crawl of 11K shopping websites. *Proceedings of the ACM on Human-Computer Interaction, 3*(CSCW), Article 81. https://doi.org/10.1145/3359183

Rozendaal, E., Lapierre, M. A., van Reijmersdal, E. A., & Buijzen, M. (2011). Reconsidering advertising literacy as a defense against advertising effects. *Media Psychology, 14*(4), 333–354. https://doi.org/10.1080/15213269.2011.620540

Sproles, G. B., & Kendall, E. L. (1986). A methodology for profiling consumers' decision-making styles. *Journal of Consumer Affairs, 20*(2), 267–279. https://doi.org/10.1111/j.1745-6606.1986.tb00382.x

Steiner, P. M., Atzmuller, C., & Su, D. (2017). Designing valid and reliable vignette experiments for survey research. *Journal of Methods and Measurement in the Social Sciences, 7*(2). https://doi.org/10.2458/v7i2.20321
