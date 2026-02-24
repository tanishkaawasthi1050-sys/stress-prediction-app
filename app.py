import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("stress_model.pkl")

# App title
st.title("Student Stress Level Prediction App")
st.write("Enter your daily details below to predict your stress level:")

# Input sliders with realistic feature names
sleep_hours = st.slider("Hours of Sleep per Day", 0, 12, 7)
study_hours = st.slider("Hours of Study per Day", 0, 12, 3)
exercise_hours = st.slider("Hours of Exercise per Day", 0, 4, 1)

# Predict button
if st.button("Predict"):
    input_data = np.array([[sleep_hours, study_hours, exercise_hours]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Stress Level: {prediction[0]}")
