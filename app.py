import streamlit as st
import joblib
import numpy as np

# Load your trained model
model = joblib.load("stress_model.pkl")

# App title
st.title("Student Stress Level Prediction")
st.write("Enter your details below to predict your stress level:")

# --- Number inputs for features ---
# Replace/add inputs here to match the number of features your model expects
feature1 = st.number_input("Feature 1", min_value=0.0, max_value=100.0, value=0.0)
feature2 = st.number_input("Feature 2", min_value=0.0, max_value=100.0, value=0.0)
feature3 = st.number_input("Feature 3", min_value=0.0, max_value=100.0, value=0.0)

# If your model has more features, add more inputs here
# Example:
# feature4 = st.number_input("Feature 4", min_value=0.0, max_value=100.0, value=0.0)
# feature5 = st.number_input("Feature 5", min_value=0.0, max_value=100.0, value=0.0)

# Predict button
if st.button("Predict"):
    # Collect all feature inputs into a numpy array
    input_data = np.array([[feature1, feature2, feature3]])  # Add more features if needed
    prediction = model.predict(input_data)
    st.success(f"Predicted Stress Level: {prediction[0]}")
