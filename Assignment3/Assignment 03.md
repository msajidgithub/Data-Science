# Assignment 03

**Data Science Assignment: Employee Attrition Classification**

**Dataset:** Employee.csv  
**Target Variable:** LeaveOrNot (0 = stayed, 1 = left)

## Objective

Predict whether an employee will leave the company using classification techniques.

---

## Part 1: Data Exploration

1. Load the dataset and review its structure.
2. Identify the categorical and numerical features.
3. Check for missing values.
4. Compute summary statistics for numerical features (Age, PaymentTier, ExperienceInCurrentDomain).
5. Analyze the distribution of categorical features (Education, City, Gender, EverBenched).
6. Plot or visualize the distribution of the target variable LeaveOrNot.

---

## Part 2: Data Preprocessing

1. Encode categorical features (Education, City, Gender, EverBenched) appropriately.
2. Handle scaling of numerical features if needed (Age, ExperienceInCurrentDomain, JoiningYear, PaymentTier).
3. Split the dataset into training and testing sets (suggested: 80%-20%).

---

## Part 3: Model Building

Train at least two classification models:

### 1. Decision Tree Classifier
- Use this model to predict LeaveOrNot.
- Interpret the tree and understand the splits.

### 2. Random Forest Classifier
- Train a Random Forest and compare with Decision Tree.

**Optional:** Try Logistic Regression or other classification models for comparison.

---

## Part 4: Model Evaluation

1. Predict the target variable on the test set.
2. Compute evaluation metrics: accuracy.

---

## Part 5: Analysis Questions

1. Which features are most important in predicting employee attrition?
2. How do Age and ExperienceInCurrentDomain affect the likelihood of leaving?
3. Compare Decision Tree and Random Forest results. Which model performs better and why?
4. Suggest HR strategies based on your analysis.

---

## Submission Requirements

1. Complete this assignment using a Jupyter Notebook (.ipynb file).
2. Write Python code for each question.
3. Show the output of each question clearly.
4. Upload your Jupyter Notebook file to GitHub.
5. Submit your GitHub repository link on Google Classroom.
