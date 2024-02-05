# TikTok DS

## 1st round

### 1. Machine Learning

#### a) XGBoost: Loss Function Derivation and Feature Importance Calculation
- **Loss Function Derivation**: XGBoost uses a gradient boosting framework. The loss function typically starts with a standard form, like squared error for regression or logarithmic loss for classification. The loss is then expanded using a Taylor series to second order, and a boosting step involves finding the best-fit additive model by minimizing this loss.
  
- **Feature Importance Calculation**: XGBoost calculates feature importances using several methods:
  - **Weight**: The number of times a feature is used to split the data across all trees.
  - **Gain**: The average training loss reduction gained when using a feature for splitting.
  - **Cover**: The average coverage of a feature when it is used in trees.

#### b) SHAP for Feature Importance vs. XGBoost's Built-in Methods
- **SHAP (SHapley Additive exPlanations)**: SHAP values provide a way to interpret machine learning models by assigning each feature an importance value for a particular prediction. SHAP values are based on game theory and offer consistency and local accuracy. They are considered more reliable and have a solid theoretical foundation, as they are the only additive feature attribution method based on expectations that satisfies consistency and local accuracy.

### 2. Statistical Testing for Different Types of Indicators

#### a) Statistical Tests for Different Indicators
- Different types of indicators often require different statistical tests, for instance, mean comparisons might use t-tests or ANOVA, while proportions might use chi-squared tests.

#### b) Alternatives to Non-parametric Methods for Skewed Distributions
- For skewed distributions, transformation methods like log or Box-Cox transformation can be used before applying parametric tests. Bootstrap methods can also be effective.

#### c) Testing Ratio Indicators like CTR and CVR
- Ratio indicators can be tested using bootstrapping for confidence intervals or Bayesian methods to estimate distributions. The Z-test for two proportions is a common method when comparing two different CTRs or CVRs.

### 3. DoubleML Project

- **DoubleML** is a framework for causal inference and machine learning. The project involves using machine learning models to estimate treatment effects.
- **Background & Modeling Process**: Typically, it involves using two machine learning models: one predicts the outcome variable, and another predicts the treatment effect. The method is used to obtain more reliable inference on causal effects.
- **Advantages**: It combines machine learning's predictive power with statistical inference to understand the causal effect.
- **Disadvantages**: It can be computationally intensive and may require careful cross-validation and regularization to prevent overfitting.

### 4. Uplift Modeling Project

- **Model Selection & Process**: Uplift modeling involves choosing models that predict the incremental impact of a treatment (like a marketing campaign) on an individual's behavior. Techniques like transformed outcome methods or tree-based methods are common.
- **Uplift Assessment Metrics**: Metrics like Qini coefficient or AUUC (Area Under the Uplift Curve) are used. AUUC measures the quality of the uplift model by calculating the area under the uplift curve created by plotting the cumulative gain of the treatment group against the percentage of the population targeted.
- **AUUC vs. AUC**: While AUC is used in classification to measure the quality of the model's predictions, AUUC specifically measures the incremental impact of treatment, which is unique to uplift modeling.

### 5. Scenario Question: Measuring Impact of App Download on Usage Duration

- To measure the impact, one could set up an A/B test where one group is exposed to the app download (treatment group), and another is not (control group). The usage duration of Douyin would be measured over time, and statistical methods like t-tests or regression analysis could be used to infer the impact.

### 6. Anomaly Analysis for Douyin Submission Rate Drop

- Conducting anomaly analysis would involve several steps:
  - **Data Examination**: Look for trends, patterns, and anomalies in the submission rate over time.
  - **Change Point Detection**: Use statistical methods like CUSUM or Bayesian change point detection to identify when the change occurred.
  - **Correlation Analysis**: Investigate whether external factors or platform changes correlate with the drop.
  - **Root Cause Analysis**: Dive deeper into the data to understand the drivers behind the change, potentially using qualitative data from user feedback.



## 2nd round

### 1. Explaining CUPED (Controlled Experiments with Pre-Experiment Data)

CUPED is a variance reduction technique used in controlled experiments, particularly A/B testing. To explain it to a non-technical colleague, you could use the following analogy:

Imagine you want to assess the effect of a new fertilizer on plant growth. However, the plants might have different growth rates due to their genetic makeup, which could confound your results. CUPED is like first measuring how much each plant grows without the fertilizer and using this information to adjust your final measurements. This way, you account for the natural differences between plants and can more accurately assess the true effect of the fertilizer.

### 2. Scenario Using Causal Inference (DID with Major Sales Promotion)

Difference-in-Differences (DID) is a causal inference technique that compares the changes in outcomes over time between a group that is exposed to a treatment (like a sales promotion) and a control group. To "fit a synthetic parallel universe," which is creating a counterfactual scenario, we use methods like Synthetic Control, where we construct a weighted combination of control units that best represent the treated unit had it not received the treatment. This helps us estimate what would have happened without the treatment.

### 3. Complaint Rates Increase for Both Genders, But Not Overall

This could happen due to Simpson's Paradox, where a trend appears in different groups of data but disappears or reverses when these groups are combined. For instance, if before the promotion, there were many more female customers than male, and the promotion brought many new male customers who had a lower complaint rate than the existing female customers, the overall complaint rate could appear stable or even decrease.

### 4. Evaluating User Experience After a Promotion

If extreme complaint rates decrease after an event, it does not necessarily mean that overall user experience has improved. It could be that only the most severe issues were addressed, or that dissatisfied users stopped using the service. To validate whether the general dissatisfaction rate has truly decreased, we could conduct surveys, analyze customer feedback, or compare the rates of complaints before and after adjusting for any changes in user base or other factors.

### 5. SQL Query: Users Who Ordered Beauty Products for Three Consecutive Days

A SQL query to find such users would involve identifying sequences of dates where each user has orders and ensuring these sequences have no gaps larger than one day. This would typically involve window functions to look at preceding and following rows.

### 6. Prediction Accuracy Between Two Apps (Xiaohongshu and Douyin)

Predicting whether a user will 'like' a piece of content may depend on the platform's user engagement algorithms and the richness of user interaction data. Xiaohongshu (Little Red Book) might have more detailed user profiles and preferences due to its nature as a social e-commerce platform, which could potentially make predictions more accurate. Douyin (TikTok), being a short video platform, might excel in predicting user engagement based on content virality factors. The accuracy would depend on the nature of the content, user behavior on each platform, and the data available for the models.



## 3rd round

#### 1. Challenges Encountered with the CUPED Model and Solutions
With CUPED, difficulties may arise if the covariates used to adjust the variance are not well-correlated with the outcome, leading to inadequate variance reduction. Another issue could be the presence of trends or seasonality in the covariate data that might not align with the treatment effects. To solve these, you might:
- Select more relevant covariates that have a high correlation with the outcome.
- Use detrending or deseasonalizing techniques on your covariates to ensure they represent stable characteristics not affected by the treatment.

#### 2. Additional Data Processing Methods Used with the CUPED Model
When using CUPED, additional data processing steps might be necessary, such as:
- Outlier removal to prevent extreme covariate values from skewing results.
- Normalization or standardization of covariates to ensure they're on the same scale.
- Handling missing data through imputation to avoid bias in the variance reduction.

#### 3. Math Problem: Expected Number of Coin Toss Rounds (Geometric Series Summation)
This problem is a classic example of a geometric distribution, where the expected number of trials to get the first success in a sequence of independent Bernoulli trials is sought. The expectation E[N] for a fair coin toss where the probability of success (heads) is 0.5 at each round is 2. This is because the geometric series sum for a fair coin gives a probability of 1/2 for the first round, 1/4 for the second, and so on, resulting in an expected value calculation that converges to 2.

#### 4. Description of a Causal Inference Project
A causal inference project could involve assessing the impact of a new user interface on user engagement. The business problem here is to determine whether the interface change leads to more time spent on the platform, more content interaction, or higher conversion rates. In-depth aspects would cover the identification strategy, such as using a difference-in-differences approach, ensuring the parallel trends assumption holds, and dealing with potential confounders.

#### 5. Creating a Synthetic Control Group
Creating a synthetic control group is a method used when a natural control group is not present. This involves using data from several units that were not affected by the intervention to construct a synthetic version of the treated unit. Techniques include matching methods, where you find units with similar characteristics to the treated unit, or regression-based approaches, where you create a weighted combination of potential control units to best replicate the counterfactual state of the treated unit.

#### 6. Ensuring the Validity of the Control Group Post-Experiment Launch
In causal inference experiments, ensuring that the control group remains valid and credible throughout the experiment is crucial. This can be achieved by:
- Avoiding any interventions or changes in the control group that are not part of the experimental design.
- Monitoring for and excluding external events that could impact the control group, like holidays or other marketing campaigns.
- Keeping the conditions for the control group as stable and 'normal' as possible to ensure that any observed differences can be attributed to the treatment effect.

