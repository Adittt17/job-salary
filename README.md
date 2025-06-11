
# 📊 Job Salary Prediction Report

## 📌 Project Domain

### Context
Job salary prediction based on candidate attributes (age, experience, education, etc.) is a classic data science case relevant to the HR Tech and recruitment industry. According to the World Economic Forum (2023), the ability to accurately estimate salaries helps companies set fair compensation and helps candidates establish realistic expectations.

### Why This Problem Matters
- Reduces wage gaps caused by gender and other non-technical biases.
- Automates HR processes in determining salary ranges.
- Provides greater transparency in recruitment processes.

### References
- **Brynjolfsson, E. & McAfee, A. (2017).** *Machine, Platform, Crowd*. W.W. Norton & Company.
- **LinkedIn Talent Insights (2022)**: https://business.linkedin.com/talent-solutions/blog

---

## 🧠 Business Understanding

### Problem Statement
How can we predict a candidate’s salary based on demographic and professional features such as age, work experience, industry, and education level?

### Goals
- Build a salary prediction model using machine learning.
- Compare two approaches: linear and non-linear models.
- Improve prediction accuracy through preprocessing and tuning.

### Solution Statements
1. **Baseline Linear Model:** Use **Lasso Regression**, as it performs regularization and handles multicollinearity.
2. **Improved Non-linear Model:** Use **XGBoost Regressor**, an ensemble model based on gradient boosting known for high regression accuracy.

---

## 📊 Data Understanding

### Data Source and Structure
The dataset contains candidate information: `Age`, `Gender`, `Education Level`, `Job Title`, `Years of Experience`, `Industry`, `Location`, and `Salary`.

### Data Preparation Steps
- **Remove duplicates & missing values** to eliminate noise.
- **Encode categorical features** using LabelEncoder for compatibility with both linear and tree-based models.
- **Standardization** ensures features have a consistent scale.
- **Outlier Removal** using IQR filtering to prevent distortion from extreme values.

---

## ⚙️ Modelling

### Model 1: Lasso Regression
- **Pros:** Simple, efficient for high-dimensional data, prevents overfitting through L1 regularization.
- **Cons:** Cannot capture non-linear relationships between features.
- **Results:**
  - MAE: 11774.46
  - MSE: 246034125.37
  - R²: 0.8698

### Model 2: XGBoost Regressor
- **Pros:** Captures non-linear relationships, robust to missing values, provides feature importance.
- **Cons:** More complex, requires more tuning, and has a longer training time.
- **Results:**
  - MAE: 9635.31
  - MSE: 174149213.84
  - R²: 0.9078

### Best Model
XGBoost is selected as the best model because it has a higher R² score (0.9078 vs 0.8698) and a lower MAE (9635 vs 11774), indicating better predictive accuracy and variance explanation.

---

## 📏 Evaluation

### Evaluation Metrics

1. **MAE (Mean Absolute Error)**  
   \[ MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i| \]  
   → Measures the average magnitude of errors in predictions.

2. **MSE (Mean Squared Error)**  
   \[ MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 \]  
   → Penalizes larger errors more heavily, sensitive to outliers.

3. **R² Score (Coefficient of Determination)**  
   \[ R^2 = 1 - \frac{\sum (y - \hat{y})^2}{\sum (y - \bar{y})^2} \]  
   → Indicates how well the model explains the variance of the target variable.
