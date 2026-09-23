# 📱 Smartphone Addiction Level Prediction

## 📌 Project Overview

This project uses Machine Learning to predict smartphone
addiction levels based on smartphone usage, lifestyle,
behavioral, and social factors.

The project follows an end-to-end Machine Learning workflow,
from data preprocessing and exploratory data analysis to
model training, evaluation, hyperparameter tuning, and
deployment using Streamlit.

---

## 🎯 Business Problem

Excessive smartphone usage can be associated with changes
in sleep, exercise, social interaction, and other lifestyle
patterns.

The objective of this project is to build a Machine Learning
model that predicts smartphone addiction levels using
relevant user-related features.

---

## 🎯 Objectives

- Clean and preprocess the dataset
- Perform Exploratory Data Analysis (EDA)
- Identify important patterns and relationships
- Perform feature engineering
- Select relevant features
- Train Machine Learning models
- Evaluate model performance
- Perform hyperparameter tuning
- Deploy the final model using Streamlit

---

## 📊 Dataset

The dataset contains:

- 6000 rows
- 22 columns

The features include smartphone usage, lifestyle,
behavioral, social, and other user-related attributes.

### Target Variable

`addiction_level`

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook

---

## 🔄 Machine Learning Workflow

```text
Data Collection
      ↓
Data Preprocessing
      ↓
Exploratory Data Analysis
      ↓
Feature Engineering
      ↓
Feature Selection
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Hyperparameter Tuning
      ↓
Final Model
      ↓
Streamlit Deployment


🔍 Exploratory Data Analysis

EDA was performed to understand:

Data distributions
Relationships between variables
Correlations
Outliers
Smartphone usage patterns
Lifestyle-related patterns

Visualizations were created using Matplotlib and Seaborn.

⚙️ Feature Engineering

New features were created using domain knowledge and
relationships between existing variables.

Examples include:

Social media usage ratios
Gaming usage ratios
Education usage ratios
Weekend usage ratios
Total entertainment hours
Emotional-related scores
Phone usage indicators
🤖 Machine Learning

Multiple Machine Learning models were trained and evaluated
to identify a suitable model for predicting addiction level.

The models were evaluated using appropriate regression
metrics such as:

MAE
MSE
RMSE
R² Score
🎛️ Hyperparameter Tuning

Hyperparameter tuning was performed to improve model
performance and identify suitable model parameters.

Techniques used:

GridSearchCV
RandomizedSearchCV
🌐 Deployment

The final Machine Learning model was deployed using
Streamlit.

Users can enter relevant smartphone usage and lifestyle
information through the web interface and receive a
predicted smartphone addiction level.

🚀 Live Application

Add your Streamlit link here:

STREAMLIT_LINK : https://predicting-smartphone-addiction-levels-using-machine-learning.streamlit.app/

📂 Project Structure
smartphone-addiction/
│
├── data/
│   └── dataset.csv
│
├── notebooks/
│   └── analysis.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── train.py
│   └── predict.py
│
├── models/
│   └── model.pkl
│
├── app/
│   └── app.py
│
├── .gitignore
├── requirements.txt
└── README.md
