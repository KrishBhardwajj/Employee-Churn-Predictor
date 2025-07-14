
# Employee Churn Risk Predictor & Actionable Agent

This project predicts **employee churn risk** using a **Random Forest Classifier** trained on the real **HR Analytics Employee Attrition Dataset**.  
It wraps the prediction with an **Actionable Agent** that recommends HR actions for at-risk employees, and can send automated **email notifications**.


# Project Structure


📁 Project-Delay-Agent/
├── Churn_Model_EDA.ipynb # Jupyter Notebook: EDA + training + save model
├── churn_model.pkl # Saved trained Random Forest model
├── app.py # Streamlit app for predictions + recommendations + email
├── HR_Attrition.csv # Real IBM HR dataset
├── Flowchart.png # Visual workflow diagram (Mermaid export)
├── README.md # This file!


# What does this project do

**Notebook (`Churn_Model_EDA.ipynb`):**
  - Loads real IBM HR data
  - Runs EDA (`.info()`, `.shape`, `.describe()`, `.head()`, `.tail()`)
  - Encodes categorical features
  - Trains a **Random Forest Classifier**
  - Evaluates accuracy (~97%)
  - Saves the model as `churn_model.pkl` using `joblib`

-  **Streamlit App (`app.py`):**
  - Upload fresh CSV
  - Loads the saved `.pkl` model
  - Encodes new data in same way
  - Predicts churn risk for each employee
  - Agent logic suggests actions (reduce overtime, review salary, assign mentor)
  - Sends **email notifications** via Gmail SMTP

  



## Deployment

How to run this project

1. Open **Jupyter Notebook** in this project folder:
```bash
  cd "C:\Users\KRISH BHARDWAJ\Desktop\Project-Delay-Agent"
  jupyter notebook
```

2. Open Churn_Model_EDA.ipynb

3. Run all cells — this trains the Random Forest & saves churn_model.pkl.

Now , run the Streamlit app

4. Make sure you are still in the same folder:
```bash
  cd "C:\Users\KRISH BHARDWAJ\Desktop\Project-Delay-Agent"
  
```

5. Run the app using:
```bash
  streamlit run app.py
  
```
6. In the app

-Upload your new HR_Attrition.csv or any similar HR data.

-View predicted churn risk and agent recommendations.

-Click Send Notification to send an email.


# Email Notification Setup

1. Uses Gmail SMTP.
Note- You must:

(i) Enable 2-Step Verification for your Gmail.

(ii) Create a Google App Password.

(iii) Generate App Password

2. Replace in app.py

```bash
from_email = "YOUR_EMAIL@gmail.com"
password = "YOUR_16_CHAR_APP_PASSWORD"
 
  
```









## Datasets

 - Source - Kaggle 
 - Size: ~1,470 employee records
 - Target: Attrition column — Yes/No


## Authors

  Krish Bhardwaj
- [@KrishBhardwajgithub](https://github.com/KrishBhardwajj/Employee_Churn_Risk_Predictor.git)

