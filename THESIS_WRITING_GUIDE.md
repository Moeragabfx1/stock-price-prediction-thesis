# Master's Dissertation Writing Guide
## Data Science / Empirical Research Focus

---

# 1. What Distinguishes Grade Levels

## Average (Pass - 50-59%)
- Demonstrates basic understanding but lacks depth
- Descriptive rather than analytical
- Limited engagement with literature
- Methods described but not justified
- Results presented without interpretation

## Merit (60-69%)
- Solid understanding with some critical analysis
- Engages with literature but synthesis is descriptive
- Methods appropriate and partially justified
- Results interpreted with some discussion of implications
- Clear structure but transitions may be weak

## Distinction (70%+)
- **Original critical insight** - goes beyond summarizing sources
- Strong theoretical framework with clear rationale
- Methods rigorously justified with awareness of limitations
- Results deeply contextualized against existing literature
- Arguments flow logically with clear signposting
- Writing demonstrates intellectual independence
- Shows awareness of debates and disagreements in the field

---

# 2. Avoiding Robotic/AI-Style Writing

## The Core Problem
AI text tends to be:
- Overly smooth with uniform sentence length
- Generic and lacking specific examples
- Missing personal voice or specific context
- Using filler phrases like "in conclusion," "it is important to note"
- Hedging without actually being cautious

## How to Make It Sound Human

### Add Specificity
❌ "Machine learning models are widely used in finance."
✓ "Since the seminal work of Fama and French (1992), ML models have increasingly been applied to predict stock returns, with recent studies like Chen et al. (2023) demonstrating that gradient boosting outperforms traditional factor models on S&P 500 data."

### Vary Sentence Structure
- Mix short punchy sentences with longer complex ones
- Use bullet points strategically for lists
- Occasionally start sentences with conjunctions ("However, the data suggest...")

### Include Your Voice
- Write "I chose X because..." not "X was chosen"
- Include brief reflective statements ("I initially considered Y, but discarded this because...")
- Show the reasoning behind decisions

### Avoid AI Filler Phrases
| Avoid | Replace With |
|-------|--------------|
| "It is important to note that" | Delete or make specific |
| "In conclusion" | "This suggests that..." or "Overall, the findings indicate..." |
| "It is worth mentioning" | Just say the thing |
| "As previously stated" | Reference naturally or delete |
| "Additionally" | "Furthermore" or "Moreover" — or just start the new point |

### Use Active Voice
❌ "The model was trained using historical data."
✓ "I trained the model on 10 years of daily returns from 2014-2024."

---

# 3. Chapter-by-Chapter Structure

## 3.1 Introduction (~10% of word count)

**Purpose:** Establish the "story" of your research

**Must Include:**
1. **Broad context** - Why does this topic matter in the real world?
2. **Narrow to gap** - What specifically is missing/underexplored?
3. **Research question(s)** - One clear question, 2-3 sub-questions max
4. **Significance** - What contribution will this make?
5. **Scope/delimitations** - What will you NOT cover (and why)?
6. **Structure overview** - Brief roadmap of the dissertation

**For Data Science:**
- Frame the practical problem (e.g., "Stock prediction is valuable but existing models fail to capture X")
- State the specific ML task (classification/regression, forecasting)
- Identify the specific gap (e.g., "existing studies focus on developed markets, leaving emerging markets understudied")

**Writing Pattern:**
> "Despite extensive research on [topic], little attention has been paid to [specific gap]. This dissertation addresses this gap by investigating [research question]. The study is motivated by [practical/theoretical motivation], and aims to [specific aim]."

---

## 3.2 Literature Review (~25% of word count)

**Purpose:** Position your work within existing scholarship and establish theoretical grounding

### Structure Options for Empirical Research:

**Option A: Thematic**
- Group by themes/concepts, not by author
- Each section synthesizes multiple perspectives

**Option B: Methodological**
- Group by research approach (e.g., traditional econometric vs. ML approaches)
- Compare and contrast what each reveals

**Option C: Chronological** (least preferred)
- Only use if the field evolved significantly over time

### Critical Analysis Checklist:
- [ ] Don't just describe what authors found — **evaluate** their methods and assumptions
- [ ] Identify **debates** in the field — not everything is settled
- [ ] Show **gaps** explicitly ("However, these studies all share a limitation: ...")
- [ ] Connect literature to YOUR specific research question
- [ ] Build toward a **conceptual framework** or testable hypotheses

### For Data Science/Finance LR:

```
Key areas to cover:
├── Financial ML literature (what ML methods have been tried, with what success)
├── Stock prediction specifically (what features, what timeframes)
├── Relevant finance theories (EMH, behavioral finance, etc.)
├── Methodological papers (how to evaluate ML models properly)
└── Identify the gap your work fills
```

### Synthesis vs. Summary:

❌ Summary: "Smith (2020) found that random forests outperform logit models. Jones (2021) also found that random forests are effective."

✓ Synthesis: "While both Smith (2020) and Jones (2021) demonstrate the effectiveness of tree-based methods, they differ in their conclusions about feature importance — Smith emphasizes technical indicators while Jones finds macro-economic variables more predictive. This suggests [your gap]."

---

## 3.3 Methodology (~20% of word count)

**Purpose:** Demonstrate rigor and enable replication

### For Empirical Data Science:

**Must Include:**
1. **Research Philosophy** - Briefly state (e.g., "This study adopts a post-positivist approach...")
2. **Data Description:**
   - Source (e.g., Bloomberg, Yahoo Finance, Kenneth French database)
   - Time period
   - Variables (dependent, independent, controls)
   - Sample size and selection criteria
   - Data cleaning steps
3. **Variable Operationalization:**
   - How you defined/measured each construct
   - Feature engineering details
4. **Model Selection & Justification:**
   - Why this model and not alternatives?
   - Brief intuition for how it works (markers may not be ML experts)
   - Hyperparameter choices or selection method
5. **Evaluation Metrics:**
   - Why these metrics?
   - How do they relate to your research question?
6. **Robustness Checks** - What will you do to prove it's not a fluke?
7. **Limitations** - Acknowledge methodological constraints

### Key Phrasing:
> "I selected [Model X] for three reasons: First, [theoretical basis]; second, [practical advantage for this data]; third, [prior literature using similar approaches]."

> "To ensure [finding] is robust, I also test alternative specifications: [list alternatives]."

---

## 3.4 Results (~15% of word count)

**Purpose:** Present findings clearly and completely

**Structure:**
1. Descriptive statistics and data overview
2. Main results (organized by research question or hypothesis)
3. Additional/robustness results

**For Data Science:**
- Lead with your main findings, not your methodology
- Use tables for comparisons
- Visualizations should be clear, well-labeled, and referenced in text
- Report both in-sample and out-of-sample performance
- Include effect sizes, not just significance

**Do:**
- Present results even if they didn't find what you expected
- Be precise: "The model achieved 73% accuracy" not "The model performed well"

**Don't:**
- Interpret results here (that's Discussion)
- Bury the main finding

---

## 3.5 Discussion (~20% of word count)

**Purpose:** Make meaning of your findings

### Must Do:
1. **Summarize key findings** — in plain language
2. **Interpret** — What do the results mean for your research question?
3. **Connect to literature** — Confirm, contradict, or extend prior work?
4. **Theoretical implications** — What does this mean for theory?
5. **Practical implications** — So what? (especially for finance)
6. **Limitations** — Be honest but not self-undermining
7. **Future research** — What should others do next?

### Critical Analysis Moves:
- "This finding contradicts [Author], who argued that... One possible explanation is..."
- "The strong performance of [Model] aligns with [Recent Study], suggesting that..."
- "However, [limitation] means these results should be interpreted with caution..."

### Common Mistakes:
- Repeating results word-for-word from previous chapter
- Not connecting back to research questions
- Overclaiming (don't say "this proves" — say "this suggests")
- Being too modest or too defensive about limitations

---

## 3.6 Conclusion (~10% of word count)

**Purpose:** Wrap up cleanly

**Structure:**
1. Restate the core research question
2. Summarize key findings (2-3 sentences max)
3. State the contribution
4. Acknowledge limitations
5. Final statement on significance/implications

**For Data Science:**
- Bring it back to the practical problem from Introduction
- What's the actionable insight?

**Do:**
- Be concise
- End with something memorable

**Don't:**
- Introduce new information
- Be vague ("more research is needed")
- Over-hedge

---

# 4. What Markers Reward

## Critical Indicators (in order of importance):

1. **Clear, focused research question** — Everything else flows from this
2. **Critical engagement** — Not just "what" but "so what" and "why"
3. **Methodological rigor** — Can they trust your results?
4. **Logical argument structure** — Every paragraph should build
5. **Appropriate depth** — Understanding the nuances
6. **Original contribution** — New insight, new application, or new data
7. **Quality of writing** — Clarity, precision, style

## Specific Marking Criteria (typical UK):

| Criterion | Weight | What They're Looking For |
|-----------|--------|---------------------------|
| Research Question | 15% | Clear, focused, achievable |
| Literature Review | 20% | Critical, synthesis, gap identification |
| Methodology | 20% | Rigorous, justified, replicable |
| Analysis/Findings | 20% | Appropriate, thorough, clearly presented |
| Discussion | 15% | Critical, contextualized, limitations acknowledged |
| Presentation | 10% | Structure, writing quality, references |

---

# 5. Common Mistakes That Lose Marks

## Writing Mistakes:
- [ ] **No clear research question** — "I'm going to study stock prediction" is not a question
- [ ] **Descriptive, not critical** — "Smith found X" without analysis
- [ ] **Literature review is a list** — Each source treated separately, no synthesis
- [ ] **Methods not justified** — "I used random forest because it's popular"
- [ ] **Results without interpretation** — Presenting numbers without explaining meaning
- [ ] **Disconnected chapters** — No explicit links between chapters
- [ ] **Signposting failure** — Reader doesn't know where you're going
- [ ] **Weak conclusion** — Just repeats abstract
- [ ] **Overuse of passive voice** — Makes writing robotic
- [ ] **Inconsistent citation style** — Pick one and stick to it

## Data Science-Specific Mistakes:
- [ ] **No baseline comparison** — How do you know your model is good?
- [ ] **Ignoring overfitting** — Not discussing in-sample vs. out-of-sample
- [ ] **No robustness checks** — What if you use different parameters?
- [ ] **Feature engineering not explained** — How did you create the features?
- [ ] **Evaluation metric not justified** — Why accuracy over AUC? Why MAPE over MAE?
- [ ] **Data leakage not addressed** — How did you handle train/test split?
- [ ] **No discussion of limitations** — Every model has limitations

---

# 6. Practical Writing Rules

## The 80/20 Checklist:

### Every Paragraph Should:
- [ ] Have a clear topic sentence
- [ ] Support claims with evidence
- [ ] Connect to the argument, not just the topic
- [ ] End with a transition or link

### Every Section Should:
- [ ] Have a clear purpose (obvious to the reader)
- [ ] Connect to the research question
- [ ] Be proportionate to its importance
- [ ] End with a summary or bridge

### Every Chapter Should:
- [ ] Start with a brief intro (what, why, how)
- [ ] End with a conclusion/summary
- [ ] Explicitly link to next chapter

## Concrete Rules While Drafting:

1. **Write your research question on a sticky note** — Reference it constantly
2. **One argument per paragraph** — If you need "and," you're trying to do two things
3. **Topic sentences are your friend** — "To test hypothesis 1, I first needed to..." signals structure
4. **After writing each section, ask:** "So what? Why does this matter?"
5. **Read paragraphs out loud** — If it sounds robotic, it reads robotic
6. **Cut the first draft by 20%** — You can always add, but paring makes it crisp
7. **Use citations as evidence, not decorations** — Every citation should support a claim
8. **Define terms explicitly** — Don't assume familiarity with your specific context
9. **Be specific about findings** — "73% accuracy on test set" not "good performance"
10. **Finish writing 2 weeks before deadline** — Time for review, not drafting

## Signposting Phrases That Work:

- "This section addresses [X], which is critical to [Y] because..."
- "Building on the findings in Chapter 3, I now examine..."
- "As will be shown in the discussion, these results have implications for..."
- "To answer RQ1, I first present descriptive statistics, then..."

## Critical Analysis Phrases:

- "This approach is limited by [assumption] because..."
- "While [Author] argues X, this ignores [factor] which is relevant because..."
- "The methodology used here differs from [Author] in [way], which matters because..."
- "This finding is consistent with [Theory], suggesting that..."

---

# 7. Quick Reference: Chapter Word Counts

For a 15,000-word dissertation:

| Chapter | Approx. Words | Purpose |
|---------|---------------|---------|
| Introduction | 1,500 | Set up research question, significance, structure |
| Literature Review | 3,750 | Position in field, identify gap, develop framework |
| Methodology | 3,000 | Show rigor, enable replication |
| Results | 2,250 | Present findings clearly |
| Discussion | 3,000 | Interpret, contextualize, limitations |
| Conclusion | 1,500 | Wrap up, contribution, final statement |

---

# 8. Data Science Specific Tips

## Presenting ML Results:

### Always Include:
- Baseline model performance (simple rule, or prior literature benchmark)
- Your main model performance
- Comparison table across models
- Confusion matrix or equivalent for classification
- Learning curves (overfitting visualization)
- Feature importance rankings
- Out-of-sample (or cross-validation) results

### For Finance Applications:
- Economic significance, not just statistical
- Transaction costs realistic? (Often missing, weakens paper)
- How does this perform during crisis periods?
- Is the result exploitable, or just statistical artifact?

### Evaluation Metrics by Task:
| Task | Recommended Metrics |
|------|---------------------|
| Classification | Accuracy, Precision, Recall, F1, AUC-ROC |
| Regression | MAE, RMSE, MAPE, R² |
| Forecasting | Diebold-Mariano test for significance |
| Risk | Sharpe ratio, Maximum Drawdown |

---

# Summary: The Distinction Formula

1. **Start with a focused research question** — The best dissertations answer a specific, achievable question
2. **Be critical, not descriptive** — Always ask "why does this matter?"
3. **Justify everything** — Your methods, your metrics, your choices
4. **Write like you have a voice** — Specific examples, varied sentence structure, clear opinions
5. **Connect everything to the research question** — Every paragraph should serve the argument
6. **Show you understand limitations** — Markers respect intellectual honesty
7. **End with impact** — Your conclusion should feel like a contribution

---

*Created for empirical data science dissertation. Adapt based on your specific university requirements.*