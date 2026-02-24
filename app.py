import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("stress_model.pkl")

st.title("Student Stress Level Prediction")

st.write("Enter the required details below:")

# Example input fields (we will adjust based on your columns)
feature1 = st.number_input("Feature 1")
feature2 = st.number_input("Feature 2")
feature3 = st.number_input("Feature 3")

if st.button("Predict"):
    input_data = np.array([[feature1, feature2, feature3]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Stress Level: {prediction[0]}")
