import streamlit as st
import pandas as pd
import joblib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ✅ Page title
st.title("🚦 Employee Churn Risk Predictor & Actionable Agent")

# ✅ Upload CSV
uploaded_file = st.file_uploader("Upload IBM HR Analytics CSV", type=["csv"])

if uploaded_file is not None:
    # ✅ Read the uploaded CSV
    df = pd.read_csv(uploaded_file)
    st.write("📂 Uploaded Data Sample", df.head())

    # ✅ Encode same way as Notebook
    df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})
    df['Department'] = df['Department'].astype('category').cat.codes
    df['JobRole'] = df['JobRole'].astype('category').cat.codes
    df['OverTime'] = df['OverTime'].astype('category').cat.codes
    df['BusinessTravel'] = df['BusinessTravel'].astype('category').cat.codes
    df['EducationField'] = df['EducationField'].astype('category').cat.codes
    df['MaritalStatus'] = df['MaritalStatus'].astype('category').cat.codes
    df['Gender'] = df['Gender'].astype('category').cat.codes

    # ✅ Same features
    X = df.drop(['Attrition', 'EmployeeNumber', 'EmployeeCount', 'Over18', 'StandardHours'], axis=1)
    y = df['Attrition']

    # ✅ Load trained model
    model = joblib.load("churn_model.pkl")

    # ✅ Make predictions
    y_pred = model.predict(X)

    acc = (y_pred == y).mean()  # Optional accuracy check
    st.success(f"✅ Model Accuracy: {acc * 100:.2f}%")

    X = X.copy()
    X['Prediction'] = y_pred
    X['Actual'] = y.values

    at_risk = X[X['Prediction'] == 1]

    def recommend_action(row):
        if row['OverTime'] == 1:
            return "Recommend: Reduce overtime workload"
        elif 'JobSatisfaction' in row and row['JobSatisfaction'] < 2:
            return "Recommend: Assign mentor"
        elif 'MonthlyIncome' in row and row['MonthlyIncome'] < 4000:
            return "Recommend: Review salary"
        else:
            return "Recommend: Regular check-ins"

    if 'JobSatisfaction' in X.columns:
        at_risk['Action'] = at_risk.apply(recommend_action, axis=1)
    else:
        at_risk['Action'] = "Recommend: HR to follow up"

    st.subheader("🚩 Employees At Risk of Leaving")
    st.dataframe(at_risk[['Prediction', 'Action']].reset_index())

    # ✅ Email notification function
    def send_email(subject, body, to_email):
        from_email = "krishbhardwaj2019@gmail.com"  
        password = "mwif deee iznz ehrx"       

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()

    if not at_risk.empty:
        if st.button("📧 Send Notification Email"):
            body = ""
            for index, row in at_risk.iterrows():
                body += f"Employee Index: {index} → At Risk → Action: {row['Action']}\n"

            send_email(
                "🚨 Employee Churn Risk Report",
                body,
                "krish21csu500@ncuinida.edu"  # Replace with PM/HR email
            )
            st.success("✅ Notification email sent to HR!")
    else:
        st.info("No high-risk employees detected.")
