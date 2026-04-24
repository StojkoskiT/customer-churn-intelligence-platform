# Customer Churn Intelligence Platform

## 📌 Overview
This project is an end-to-end data science solution designed to predict customer churn and provide actionable business insights. It combines data analysis, machine learning, and deployment into an interactive web application.

## 🚀 Key Features
- Exploratory Data Analysis (EDA) with business insights
- Feature engineering and preprocessing pipeline
- Machine learning models (Logistic Regression & Random Forest)
- Model evaluation with focus on business impact (churn recall)
- Interactive Streamlit web application

## 📊 Dataset
Telco Customer Churn dataset (~7,000 customers)

## 🧠 Key Insights
- Customers on month-to-month contracts have significantly higher churn rates
- Higher monthly charges correlate with increased churn
- Contract type, tenure, and pricing are the strongest churn drivers

## 🤖 Model Performance

| Model                | Accuracy | Churn Recall |
|---------------------|---------|-------------|
| Logistic Regression | 0.80    | 0.57        |
| Random Forest       | 0.79    | 0.50        |

Logistic Regression was selected as the final model due to better performance in detecting churned customers.

## 🖥️ Application

![App Screenshot](reports/figures/)

The application allows users to:
- Input customer data
- Predict churn probability
- Understand risk level instantly

## ⚙️ Tech Stack
- Python (Pandas, NumPy, Scikit-learn)
- Streamlit
- Matplotlib / Seaborn
- Git & GitHub

## 📁 Project Structure
customer-churn-intelligence-platform/
│
├── data/
├── notebooks/
├── models/
├── app/
├── reports/
└── README.md


## 🎯 Business Impact
This project demonstrates how machine learning can support customer retention strategies by identifying high-risk customers and enabling proactive intervention.

---

## 👤 Author
Trpo Stojkoski
- GitHub: https://github.com/StojkoskiT
- LinkedIn: https://www.linkedin.com/in/trpo-stojkoski/