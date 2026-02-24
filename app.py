import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("stress_model.pkl")

# App title
st.title("Student Stress Level Prediction")
st.write("Enter your details below to predict your stress level:")

# --- Number inputs for 5 features ---
sleep_hours = st.number_input("Hours of Sleep per Day", min_value=0.0, max_value=12.0, value=7.0)
headaches = st.number_input("Number of Headache Episodes per Week", min_value=0, max_value=20, value=0)
academic_performance = st.number_input("Academic Performance (1=Poor, 5=Excellent)", min_value=1, max_value=5, value=3)
study_load = st.number_input("Daily Study Load (hours)", min_value=0.0, max_value=12.0, value=3.0)
extracurricular_activities = st.number_input("Hours of Extracurricular Activities per Day", min_value=0.0, max_value=6.0, value=1.0)

# Predict button
if st.button("Predict"):
    input_data = np.array([[sleep_hours, headaches, academic_performance, study_load, extracurricular_activities]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Stress Level: {prediction[0]}")
