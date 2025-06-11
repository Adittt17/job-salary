# --- STREAMLIT APP CODE ---
import streamlit as st
import joblib
import json

# Load model dan scaler
model = joblib.load('xgb_model.pkl')
scaler = joblib.load('scaler.pkl')

# Load mapping
with open('education_map.json', 'r') as f:
    education_map = json.load(f)

with open('job_title_map.json', 'r') as f:
    job_title_map = json.load(f)

reverse_edu_map = {v: k for k, v in education_map.items()}
reverse_job_map = {v: k for k, v in job_title_map.items()}

st.title("💼 Salary Predictor")

age = st.number_input("Age", min_value=18, max_value=100, value=25)

education_level = st.selectbox(
    "Education Level",
    options=list(education_map.keys()),
    index=0
)

job_title = st.selectbox(
    "Job Title",
    options=list(job_title_map.keys()),
    index=0
)

years_exp = st.number_input("Years of Experience", min_value=0, max_value=50, value=2)

if st.button("Predict Salary"):
    try:
        edu_encoded = education_map[education_level]
        job_encoded = job_title_map[job_title]

        input_data = [[age, edu_encoded, job_encoded, years_exp]]
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)[0]

        st.success(f"💰 Predicted Salary: ${prediction:,.2f}")
    except Exception as e:
        st.error(f"Something went wrong: {e}")
