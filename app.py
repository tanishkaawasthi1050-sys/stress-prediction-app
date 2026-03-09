import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ---------- Page Settings ----------
st.set_page_config(page_title="Student Stress Predictor", layout="centered")

# ---------- Custom Theme ----------
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

st.write("Analyze your stress level based on daily lifestyle habits.")

# ---------- Sidebar ----------
st.sidebar.title("ℹ About")

st.sidebar.write("""
This app predicts **student stress levels** using lifestyle factors:

😴 Sleep Hours  
🤕 Headaches  
📚 Academic Performance  
📝 Study Load  
⚽ Extracurricular Activities
""")

# ---------- Input Section ----------
st.subheader("📋 Enter Your Lifestyle Details")

col1, col2 = st.columns(2)

with col1:
    sleep_hours = st.slider("😴 Sleep Hours", 0, 12, 6)
    headaches = st.slider("🤕 Headache Frequency", 0, 10, 2)
    extracurricular = st.slider("⚽ Extracurricular Activities", 0, 10, 4)

with col2:
    academic_performance = st.slider("📚 Academic Performance", 0, 10, 7)
    study_load = st.slider("📝 Study Load", 0, 10, 5)

# ---------- Predict ----------
if st.button("🔍 Predict Stress Level"):

    # ---------- Stress Score Logic ----------
    stress_score = study_load + headaches + (10 - sleep_hours) + (10 - academic_performance) - extracurricular

    if stress_score <= 10:
        prediction = 0
    elif stress_score <= 20:
        prediction = 1
    else:
        prediction = 2

    st.subheader("📊 Prediction Result")

    if prediction == 0:
        st.success("😊 Low Stress Level")
        meter_color = "green"

    elif prediction == 1:
        st.warning("⚠ Moderate Stress Level")
        meter_color = "orange"

    else:
        st.error("🚨 High Stress Level")
        meter_color = "red"

    # ---------- Stress Meter ----------
    st.subheader("🧭 Stress Meter")

    if prediction == 0:
        st.progress(30)
    elif prediction == 1:
        st.progress(60)
    else:
        st.progress(90)

    # ---------- Lifestyle Graph ----------
    st.subheader("📈 Lifestyle Analysis")

    features = ["Sleep", "Headaches", "Academic", "Study Load", "Activities"]
    values = [sleep_hours, headaches, academic_performance, study_load, extracurricular]

    fig, ax = plt.subplots()
    ax.bar(features, values)
    ax.set_ylabel("Score")
    ax.set_title("Lifestyle Factors Affecting Stress")

    st.pyplot(fig)

    # ---------- Suggestions ----------
    st.subheader("💡 Suggestions")

    if prediction == 0:

        st.markdown("""
### 😊 Low Stress

Great! Keep maintaining your healthy routine.

✔ Maintain regular sleep schedule  
✔ Continue balanced study habits  
✔ Stay active in extracurricular activities  
✔ Spend time with friends and family
""")

    elif prediction == 1:

        st.markdown("""
### ⚠ Moderate Stress

Try improving your habits.

✔ Take short study breaks  
✔ Improve sleep routine  
✔ Practice meditation or breathing exercises  
✔ Manage your study schedule better
""")

    else:

        st.markdown("""
### 🚨 High Stress

Consider taking steps to reduce stress.

✔ Get enough sleep and rest  
✔ Reduce study pressure temporarily  
✔ Practice yoga or relaxation techniques  
✔ Talk to friends, mentors or family  
✔ Consider professional help if stress persists
""")

# ---------- Footer ----------
st.markdown("---")
st.write("💙 Stay Healthy • Stay Balanced • Take Care of Your Mental Health")
