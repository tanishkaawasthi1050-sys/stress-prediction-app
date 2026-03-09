import streamlit as st
import numpy as np
import joblib
import matplotlib.pyplot as plt

# ---------- Load Model ----------
model = joblib.load("stress_model.pkl")

# ---------- Page Settings ----------
st.set_page_config(page_title="Student Stress Predictor", layout="centered")

# ---------- Custom Styling ----------
st.markdown("""
<style>
.stApp {
background: linear-gradient(to right, #667eea, #764ba2);
color: white;
}

h1 {
text-align:center;
color:#FFD700;
}

.stButton>button {
background-color:#FF4B4B;
color:white;
border-radius:10px;
height:3em;
width:220px;
font-size:16px;
}
</style>
""", unsafe_allow_html=True)

# ---------- Title ----------
st.title("🧠 Student Stress Level Predictor")

st.write("Understand your stress level based on lifestyle habits.")

# ---------- Sidebar ----------
st.sidebar.title("ℹ About")

st.sidebar.write("""
This AI model predicts **student stress levels** using:

😴 Sleep Hours  
🤕 Headache Frequency  
📚 Academic Performance  
📝 Study Load  
⚽ Extracurricular Activities  
""")

# ---------- Inputs ----------
st.subheader("📋 Enter Your Details")

col1, col2 = st.columns(2)

with col1:
    sleep_hours = st.slider("😴 Sleep Hours", 0, 12, 6)
    headaches = st.slider("🤕 Headache Frequency", 0, 10, 2)
    extracurricular = st.slider("⚽ Extracurricular Activities", 0, 10, 4)

with col2:
    academic_performance = st.slider("📚 Academic Performance", 0, 10, 7)
    study_load = st.slider("📝 Study Load", 0, 10, 5)

# ---------- Prediction ----------
if st.button("🔍 Predict Stress Level"):

    input_data = np.array([[sleep_hours, headaches, academic_performance, study_load, extracurricular]])

    prediction = model.predict(input_data)[0]

    st.subheader("📊 Prediction Result")

    if prediction == 0:
        st.success("😊 Low Stress Level")

    elif prediction == 1:
        st.warning("⚠ Moderate Stress Level")

    else:
        st.error("🚨 High Stress Level")

    # ---------- Lifestyle Graph ----------
    st.subheader("📈 Lifestyle Analysis")

    features = ["Sleep", "Headaches", "Academic", "Study Load", "Activities"]
    values = [sleep_hours, headaches, academic_performance, study_load, extracurricular]

    fig, ax = plt.subplots()
    ax.bar(features, values)
    ax.set_ylabel("Score")
    ax.set_title("Lifestyle Factors")

    st.pyplot(fig)

    # ---------- Probability Graph ----------
    if hasattr(model, "predict_proba"):

        st.subheader("📊 Stress Probability")

        prob = model.predict_proba(input_data)[0]
        labels = ["Low", "Moderate", "High"]

        fig2, ax2 = plt.subplots()
        ax2.bar(labels, prob)
        ax2.set_ylabel("Probability")
        ax2.set_title("Prediction Confidence")

        st.pyplot(fig2)

    # ---------- Suggestions ----------
    st.subheader("💡 Suggestions")

    if prediction == 0:

        st.markdown("""
### 😊 Low Stress

Great! Your stress level is low.

✔ Maintain good sleep schedule  
✔ Continue healthy study habits  
✔ Stay active in extracurricular activities  
✔ Keep social connections strong
""")

    elif prediction == 1:

        st.markdown("""
### ⚠ Moderate Stress

Try improving these habits:

✔ Improve sleep routine  
✔ Take breaks while studying  
✔ Practice meditation or breathing exercises  
✔ Reduce unnecessary academic pressure
""")

    else:

        st.markdown("""
### 🚨 High Stress

Consider these steps:

✔ Get proper rest and sleep  
✔ Practice yoga or relaxation techniques  
✔ Talk with friends, mentors, or family  
✔ Reduce workload temporarily  
✔ Seek professional help if stress persists
""")

# ---------- Footer ----------
st.markdown("---")
st.write("💙 Stay Positive • Stay Balanced • Take Care of Your Mental Health")
