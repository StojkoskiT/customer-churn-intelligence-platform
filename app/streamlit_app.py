import streamlit as st
import pandas as pd
import joblib

model = joblib.load("models/churn_model.pkl")
scaler = joblib.load("models/scaler.pkl")
model_features = joblib.load("models/model_features.pkl")

st.set_page_config(page_title="Customer Churn Predictor", layout="wide")

st.title("Customer Churn Intelligence Platform")
st.write("Predict whether a customer is likely to churn based on service and billing information.")

st.sidebar.header("Customer Information")

tenure = st.sidebar.slider("Tenure (months)", 0, 72, 12)
monthly_charges = st.sidebar.slider("Monthly Charges", 0.0, 150.0, 70.0)
total_charges = tenure * monthly_charges

contract = st.sidebar.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
internet_service = st.sidebar.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
payment_method = st.sidebar.selectbox(
    "Payment Method",
    ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
)

senior_citizen = st.sidebar.selectbox("Senior Citizen", [0, 1])
partner = st.sidebar.selectbox("Partner", ["Yes", "No"])
dependents = st.sidebar.selectbox("Dependents", ["Yes", "No"])
paperless_billing = st.sidebar.selectbox("Paperless Billing", ["Yes", "No"])

input_data = pd.DataFrame(columns=model_features)
input_data.loc[0] = 0

input_data["tenure"] = tenure
input_data["MonthlyCharges"] = monthly_charges
input_data["TotalCharges"] = total_charges
input_data["SeniorCitizen"] = senior_citizen

def set_feature(column_name):
    if column_name in input_data.columns:
        input_data[column_name] = 1

set_feature(f"Contract_{contract}")
set_feature(f"InternetService_{internet_service}")
set_feature(f"PaymentMethod_{payment_method}")
set_feature(f"Partner_{partner}")
set_feature(f"Dependents_{dependents}")
set_feature(f"PaperlessBilling_{paperless_billing}")

scaled_input = scaler.transform(input_data)

prediction = model.predict(scaled_input)[0]
probability = model.predict_proba(scaled_input)[0][1]

st.subheader("Prediction Result")

if prediction == 1:
    st.error(f"High Risk of Churn: {probability:.2%}")
else:
    st.success(f"Low Risk of Churn: {probability:.2%}")

st.subheader("Customer Input Summary")
st.dataframe(input_data)
