import streamlit as st
import numpy as np
import joblib
import matplotlib.pyplot as plt

# ---------- Load ML Model ----------
try:
    model = joblib.load("stress_model.pkl")
except:
    model = None

# ---------- Page Settings ----------
st.set_page_config(page_title="Student Stress Predictor", layout="centered")

# ---------- Custom Theme ----------
st.markdown("""
<style>

.stApp {
background: linear-gradient(to right,#667eea,#764ba2);
color:white;
}

h1{
text-align:center;
color:#FFD700;
}

.stButton>button{
background-color:#FF4B4B;
color:white;
border-radius:10px;
height:3em;
width:220px;
font-size:16px;
}

</style>
""",unsafe_allow_html=True)

# ---------- Title ----------
st.title("🧠 Student Stress Level Predictor")
st.write("💡 Analyze your stress level based on lifestyle habits.")

# ---------- Sidebar ----------
st.sidebar.title("ℹ About This App")

st.sidebar.write("""
This AI model predicts student stress using:

😴 Sleep Hours  
🤕 Headaches  
📚 Academic Performance  
📝 Study Load  
⚽ Extracurricular Activities
""")

# ---------- Inputs ----------
st.subheader("📋 Enter Your Lifestyle Details")

col1,col2 = st.columns(2)

with col1:
    sleep_hours = st.slider("😴 Sleep Hours",0,12,6)
    headaches = st.slider("🤕 Headaches",0,10,2)
    extracurricular = st.slider("⚽ Extracurricular Activities",0,10,4)

with col2:
    academic_performance = st.slider("📚 Academic Performance",0,10,7)
    study_load = st.slider("📝 Study Load",0,10,5)

# ---------- Prediction ----------
if st.button("🔍 Predict Stress Level"):

    input_data = np.array([[sleep_hours,headaches,academic_performance,study_load,extracurricular]])

    prediction = None

    # ---------- Try ML Prediction ----------
    if model is not None:
        try:
            prediction = model.predict(input_data)[0]
        except:
            prediction = None

    # ---------- Flexible Rule Logic (Backup) ----------
    if prediction not in [0,1,2]:

        sleep_factor = (10 - sleep_hours) * 1.8
        headache_factor = headaches * 2
        study_factor = study_load * 2
        academic_factor = (10 - academic_performance) * 1.5
        activity_factor = extracurricular * 1.2

        stress_score = sleep_factor + headache_factor + study_factor + academic_factor - activity_factor

        if stress_score < 18:
            prediction = 0
        elif stress_score < 35:
            prediction = 1
        else:
            prediction = 2

    st.subheader("📊 Prediction Result")

    if prediction == 0:
        st.success("😊 Low Stress Level")
        meter = 30
        color = "#00FF7F"

    elif prediction == 1:
        st.warning("⚠ Moderate Stress Level")
        meter = 60
        color = "#FFA500"

    else:
        st.error("🚨 High Stress Level")
        meter = 90
        color = "#FF4B4B"

    # ---------- Custom Stress Meter ----------
    st.subheader("🧭 Stress Meter")

    st.markdown(
    f"""
    <div style="width:100%;background:#ddd;border-radius:20px;height:30px;">
    <div style="width:{meter}%;background:{color};height:30px;border-radius:20px;
    text-align:center;color:black;font-weight:bold;">
    {meter}%
    </div>
    </div>
    """,
    unsafe_allow_html=True
    )

    # ---------- Graph ----------
    st.subheader("📈 Lifestyle Analysis")

    features = ["Sleep","Headaches","Academic","Study Load","Activities"]
    values = [sleep_hours,headaches,academic_performance,study_load,extracurricular]

    fig,ax = plt.subplots()
    ax.bar(features,values)
    ax.set_ylabel("Score")
    ax.set_title("Lifestyle Factors")

    st.pyplot(fig)

    # ---------- Suggestions ----------
    st.subheader("💡 Suggestions")

    if prediction == 0:

        st.markdown("""
### 😊 Low Stress

✔ Maintain good sleep schedule  
✔ Continue balanced study habits  
✔ Stay active in extracurricular activities  
✔ Maintain healthy social life
""")

    elif prediction == 1:

        st.markdown("""
### ⚠ Moderate Stress

✔ Take short breaks during study  
✔ Improve sleep routine  
✔ Practice meditation or breathing exercises  
✔ Manage study time better
""")

    else:

        st.markdown("""
### 🚨 High Stress

✔ Get proper rest and sleep  
✔ Reduce academic pressure temporarily  
✔ Practice yoga or relaxation exercises  
✔ Talk with friends, mentors or family
""")

# ---------- Footer ----------
st.markdown("---")
st.write("💙 Stay Positive • Stay Balanced • Stay Healthy")
