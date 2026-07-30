# Credit Score Prediction using Machine Learning (Paisabazaar Banking Dataset)

## Overview

This project develops a machine learning model to predict a customer's **Credit Score** using financial and credit-related information. The project compares the performance of **Decision Tree Classifier** and **Random Forest Classifier**, followed by **feature selection using Permutation Importance** to identify the most influential financial attributes affecting credit score prediction.

The final Random Forest model achieves approximately **82% classification accuracy** while using only the most important features, making the model simpler and more interpretable without a significant loss in performance.

---

## Problem Statement

Financial institutions evaluate a customer's creditworthiness before approving loans, credit cards, or other financial products. Manual assessment is time-consuming and often involves analyzing a large number of customer attributes.

The objective of this project is to build a machine learning model capable of accurately predicting customer credit score categories while identifying the most influential financial features that contribute to the prediction.

---

## Dataset

**Dataset:** Paisabazar Banking Dataset

* Records: **100,000**
* Original Features: **28**
* Target Variable:

  * Credit_Score

The dataset contains customer demographic information, income details, loan history, repayment behavior, outstanding debt, investment information, and other financial indicators.

### Major Features

* Annual Income
* Monthly Inhand Salary
* Number of Bank Accounts
* Number of Credit Cards
* Interest Rate
* Number of Loans
* Outstanding Debt
* Credit Utilization Ratio
* Credit History Age
* Total EMI per Month
* Monthly Investment
* Payment Behaviour
* Credit Mix
* Payment of Minimum Amount
* Delay from Due Date
* Number of Delayed Payments
* and several other customer financial attributes.

---

## Data Preprocessing

The following preprocessing steps were performed:

* Converted month values from numerical (1–8) to month names (Jan–Aug).
* Applied One-Hot Encoding to categorical variables such as Occupation.
* Applied MultiLabelBinarizer to the Type_of_Loan column.
* Replaced ambiguous "NM" values in Payment_of_Min_Amount using a Decision Tree prediction approach.
* One-Hot Encoded Payment_of_Min_Amount.
* Label Encoded the target variable Credit_Score.
* Prepared the final numerical dataset for machine learning.

---

## Machine Learning Models

### Decision Tree Classifier

Experiments performed:

* Baseline model
* Manual hyperparameter tuning
* GridSearchCV

### Best Performance

Accuracy:

**74.09%**

---

### Random Forest Classifier

Experiments performed:

* Baseline model
* Feature Selection using Permutation Importance
* Iterative feature elimination (12 iterations)

### Best Performance

Accuracy:

**82.11%**

The Random Forest model significantly outperformed the Decision Tree classifier.

---

## Feature Selection

Permutation Importance from sklearn.inspection was used to estimate the contribution of each feature.

The process consisted of:

1. Train Random Forest.
2. Calculate permutation importance.
3. Remove low-importance features.
4. Retrain the model.
5. Evaluate performance.
6. Repeat until performance started stabilizing.

After **12 iterations**, the model retained **18 important features** while maintaining nearly the same predictive performance.

### Selected Important Features

* Annual_Income
* Monthly_Inhand_Salary
* Num_Bank_Accounts
* Num_Credit_Card
* Interest_Rate
* Delay_from_due_date
* Num_of_Delayed_Payment
* Changed_Credit_Limit
* Num_Credit_Inquiries
* Outstanding_Debt
* Credit_History_Age
* Total_EMI_per_month
* Amount_invested_monthly
* Credit_Mix_Good
* Credit_Mix_Standard
* Credit_Mix_Bad
* Payment_of_Min_Amount_Yes
* Payment_of_Min_Amount_No

---

## Model Performance

### Decision Tree

| Model        | Accuracy |
| ------------ | -------- |
| Baseline     | 73.86%   |
| Tuned        | 74.09%   |
| GridSearchCV | ~74%     |

### Random Forest

| Model                   | Accuracy   |
| ----------------------- | ---------- |
| Baseline                | **82.11%** |
| After Feature Selection | **81.87%** |

The reduced-feature model maintained almost the same accuracy while using fewer predictors.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Jupyter Notebook

## Future Improvements

* SHAP Explainability
* LIME Explainability
* Hyperparameter optimization using Optuna
* Model deployment using Streamlit
* Model monitoring and performance tracking
* Cross-validation using Stratified K-Fold
* Compare with XGBoost, LightGBM, and CatBoost

---

## Results

* Successfully built a multiclass credit score prediction model.
* Random Forest outperformed Decision Tree.
* Achieved approximately **82% classification accuracy**.
* Reduced the model to **18 important features** using permutation importance.
* Demonstrated that feature reduction can simplify the model while maintaining predictive performance.

---


## Author

**Chaitanya**

M.Sc. Big Data Analytics

Interested in Machine Learning, Data Science, Explainable AI, and Financial Analytics.

---
