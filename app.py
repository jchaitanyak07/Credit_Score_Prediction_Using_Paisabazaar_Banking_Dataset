import streamlit as st
import pandas as pd
import joblib

data_train = pd.read_csv("D:\CreditScoreApp\data\credit_score_data_train.csv")

numerical_cols = ["Annual_Income", "Monthly_Inhand_Salary", "Num_Bank_Accounts", "Num_Credit_Card", "Interest_Rate", "Delay_from_due_date",
 "Num_of_Delayed_Payment", "Changed_Credit_Limit", "Num_Credit_Inquiries", "Outstanding_Debt", "Credit_History_Age",
 "Total_EMI_per_month", "Amount_invested_monthly"]

num_cols_min_max_values = {}

for col in numerical_cols:
    num_cols_min_max_values[col] = [data_train[col].min(), data_train[col].max()]


credit_score_model = joblib.load("credit_score_model.pkl")

#st.title("Credit Score Predictor")

model_features_list = list(credit_score_model.feature_names_in_)

Annual_Income = st.number_input("Annual Income", min_value = num_cols_min_max_values["Annual_Income"][0], max_value = num_cols_min_max_values["Annual_Income"][1])

Monthly_Inhand_Salary = st.number_input("Monthly Inhand Salary", min_value = num_cols_min_max_values["Monthly_Inhand_Salary"][0], max_value = num_cols_min_max_values["Monthly_Inhand_Salary"][1])

Num_Bank_Accounts = st.number_input("No of Bank Accounts", min_value = num_cols_min_max_values["Num_Bank_Accounts"][0], max_value = num_cols_min_max_values["Num_Bank_Accounts"][1])

Num_Credit_Card = st.number_input("No of Credit Cards", min_value = num_cols_min_max_values["Num_Credit_Card"][0], max_value = num_cols_min_max_values["Num_Credit_Card"][1])

Interest_Rate = st.number_input("Interest Rate", min_value = num_cols_min_max_values["Interest_Rate"][0], max_value = num_cols_min_max_values["Interest_Rate"][1])

Delay_from_due_date = st.number_input("Days Delayed from Due Date", min_value = num_cols_min_max_values["Delay_from_due_date"][0], max_value = num_cols_min_max_values["Delay_from_due_date"][1])

Num_of_Delayed_Payment = st.number_input("No of Delayed Payments", min_value = num_cols_min_max_values["Num_of_Delayed_Payment"][0], max_value = num_cols_min_max_values["Num_of_Delayed_Payment"][1])

Changed_Credit_Limit = st.number_input("Changed Credit Limit", min_value = num_cols_min_max_values["Changed_Credit_Limit"][0], max_value = num_cols_min_max_values["Changed_Credit_Limit"][1])

Num_Credit_Inquiries = st.number_input("No of Credit Inquiries", min_value = num_cols_min_max_values["Num_Credit_Inquiries"][0], max_value = num_cols_min_max_values["Num_Credit_Inquiries"][1])

Outstanding_Debt = st.number_input("Outstanding Debt", min_value = num_cols_min_max_values["Outstanding_Debt"][0], max_value = num_cols_min_max_values["Outstanding_Debt"][1])

Credit_History_Age = st.number_input("Credit History Age", min_value = num_cols_min_max_values["Credit_History_Age"][0], max_value = num_cols_min_max_values["Credit_History_Age"][1])

Total_EMI_per_month = st.number_input("Total EMI per Month", min_value = num_cols_min_max_values["Total_EMI_per_month"][0], max_value = num_cols_min_max_values["Total_EMI_per_month"][1])

Amount_invested_monthly = st.number_input("Monthly Amount Investment", min_value = num_cols_min_max_values["Amount_invested_monthly"][0], max_value = num_cols_min_max_values["Amount_invested_monthly"][1])

Credit_Mix = st.selectbox("Credit Mix", ["Good", "Standard", "Bad"])
Credit_Mix_Good = 0
Credit_Mix_Standard = 0
Credit_Mix_Bad = 0

if Credit_Mix == "Standard":
    Credit_Mix_Standard = 1
    Credit_Mix_Bad = 0
elif Credit_Mix == "Bad":
    Credit_Mix_Bad = 1
    Credit_Mix_Standard = 0
else:
    Credit_Mix_Good = 1
    Credit_Mix_Standard = 0
    Credit_Mix_Bad = 0

Payment_of_Min_Amount = st.selectbox("Payment of Min Amount", ["Yes", "No"])
Payment_of_Min_Amount_Yes = 0
Payment_of_Min_Amount_No = 0

if Payment_of_Min_Amount == "Yes":
    Payment_of_Min_Amount_Yes = 1
    Payment_of_Min_Amount_No = 0
else:
    Payment_of_Min_Amount_Yes = 0
    Payment_of_Min_Amount_No = 1

features = [[Payment_of_Min_Amount_Yes, Credit_Mix_Good, Credit_Mix_Standard, Annual_Income, Monthly_Inhand_Salary, Num_Bank_Accounts, Num_Credit_Card, Interest_Rate, Delay_from_due_date, Num_of_Delayed_Payment, Changed_Credit_Limit, Num_Credit_Inquiries, Outstanding_Debt, Credit_History_Age, Total_EMI_per_month, Amount_invested_monthly, Credit_Mix_Bad, Payment_of_Min_Amount_No]]


if st.button("Predict"):

    Credit_Score = credit_score_model.predict(features)[0]

    if Credit_Score == 0:
        Credit_Score = "Good"
    elif Credit_Score == 1:
        Credit_Score = "Poor"
    else:
        Credit_Score = "Standard"

    st.success(f"Predicted Credit Score: {Credit_Score}")