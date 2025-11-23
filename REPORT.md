# Bias Detection Report – Syracuse Women’s Lacrosse 2023

## 1. Executive summary

This project examined the influence of prompt design on language model narratives by testing three main effects—framing, player role focus, and confirmation priming—using Syracuse Women’s Lacrosse 2023 player statistics. The study queried GPT-4, Claude, and Gemini with systematically varied prompts that only differed in wording or demographic mentions. Results showed consistent framing effects, where positive prompts encouraged highlighting potential and growth while negative prompts underscored struggles and weaknesses. Rookie vs. veteran emphasis shifted player recommendations and messaging. Priming the model with a hypothesis led to strong affirmation without critical examination. These findings emphasize the imperative to carefully design and validate prompts when utilizing LLMs for sports data interpretation to mitigate unintended bias and maintain factual accuracy.

---

## 2. Methods

### Dataset

Detailed player statistics from the Syracuse Women’s Lacrosse 2023 season were anonymized and cleaned, then used as the basis for input prompts. Metrics included goals, assists, turnovers, and points.

### Models and Experimental Setup

Three LLMs were tested: GPT-4, Claude, and Gemini. Each prompt was sampled multiple times per model to capture variability and bias patterns.

### Prompt Design

A consistent data context was provided for all prompts. The prompt variations were:

- **H1 – Framing effect:** Positive vs. negative wording ("most potential" vs. "most needing improvement")  
- **H2 – Role focus:** Rookie- vs veteran-oriented questions  
- **H3 – Confirmation priming:** Stating hypotheses and checking model agreement vs neutral inquiry  

### Data Collection and Analysis

Prompts and responses were logged systematically. Sentiment analysis was conducted using lexicon-based tools and claim validation scripts compared model statements with statistical ground truth.

---

## 3. Results

Sentiment shifted according to framing with positive prompts eliciting optimistic language and negative prompts critical language.

Player recommendations changed depending on role focus, with rookies emphasized for development and veterans for stability.

Confirmatory prompts caused models to reinforce user views, showing confirmation bias.

Differences among models in tone and claim accuracy were observed, highlighting model-specific biases.

Examples, charts, and statistical tests are included in the supplementary files.

---

## 4. Bias Catalogue

| Bias Type           | Description                                        | Severity | Models Affected      | Notes                         |
|--------------------|---------------------------------------------------|---------|-------------------|-------------------------------|
| Framing Bias        | Language shifts focus and tone based on prompt framing | Medium  | All               | Positive framing stresses growth |
| Role Focus Bias     | Player emphasis changes when age/role mentioned   | Medium  | GPT-4, Claude     | Rookies vs veterans highlighted |
| Confirmation Bias   | Models align strongly with primed hypotheses      | High    | All               | Can reinforce user preconceptions |
| Selection Bias      | Selected stats and players vary by model or prompt | Low     | Variable          | Turnovers vs goals emphasis varies |
| Fabrication         | Unsupported claims deviate from ground truth      | Medium  | Variable          | Seen mostly in primed prompts |

---

## 5. Mitigation Strategies

- Use balanced prompt variations to compare opposing frames.  
- Explicitly require evidence or data backing for all claims.  
- Avoid definitive priming statements in favor of open questions.  
- Use automated scripts for factual claims validation against raw data.  
- Validate across multiple LLM providers to detect model-specific biases.  

---

## 6. Limitations and Next Steps

- Small sample size and limited models reduce generalizability.  
- Sentiment tools imperfectly capture nuanced tone shifts.  
- Future work should expand model range, prompt diversity, and analysis techniques.  
- Interactive dashboards and fairness audits planned for ongoing monitoring.
