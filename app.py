import streamlit as st
import numpy as np
import joblib
import matplotlib.pyplot as plt

# Load model
model = joblib.load("stress_model.pkl")

# ---------- Custom Color Theme ----------
st.markdown("""
<style>

.stApp {
background: linear-gradient(to right, #667eea, #764ba2);
color: white;
}

h1 {
text-align: center;
color: #FFD700;
}

h2, h3 {
color: #FFDD95;
}

.stButton>button {
background-color: #FF4B4B;
color: white;
border-radius: 10px;
height: 3em;
width: 200px;
font-size: 16px;
}

.css-1d391kg {
background-color: #1f1f2e;
}

</style>
""", unsafe_allow_html=True)

# ---------- Title ----------
st.title("🧠 Student Stress Level Predictor")
st.write("💡 Understand your stress level and get helpful suggestions for a healthier lifestyle.")

# ---------- Sidebar ----------
st.sidebar.title("ℹ About This App")

st.sidebar.write("""
This AI model predicts student stress levels based on lifestyle habits such as:

😴 Sleep hours  
📚 Academic performance  
🤕 Headaches  
📝 Study load  
⚽ Extracurricular activities  

Use the sliders and click **Predict Stress** to see your result.
""")

st.sidebar.write("🌿 Built for Student Mental Wellness")

# ---------- Input Section ----------
st.subheader("📋 Enter Your Lifestyle Details")

col1, col2 = st.columns(2)

with col1:
    sleep_hours = st.slider("😴 Sleep Hours", 0, 12, 6)
    headaches = st.slider("🤕 Headaches Frequency", 0, 10, 2)
    extracurricular = st.slider("⚽ Extracurricular Activities", 0, 10, 4)

with col2:
    academic_performance = st.slider("📚 Academic Performance", 0, 10, 7)
    study_load = st.slider("📝 Study Load", 0, 10, 5)

# ---------- Prediction Button ----------
if st.button("🔍 Predict Stress Level"):

    input_data = np.array([[sleep_hours, headaches, academic_performance, study_load, extracurricular]])
    prediction = model.predict(input_data)

    st.subheader("📊 Prediction Result")

    if prediction[0] == 0:
        st.success("😊 Low Stress Level")
    elif prediction[0] == 1:
        st.warning("⚠ Moderate Stress Level")
    else:
        st.error("🚨 High Stress Level")

    # ---------- Graph ----------
    st.subheader("📈 Your Lifestyle Analysis")

    features = ["Sleep", "Headaches", "Academic", "Study Load", "Activities"]
    values = [sleep_hours, headaches, academic_performance, study_load, extracurricular]

    fig, ax = plt.subplots()
    ax.bar(features, values)
    ax.set_title("Lifestyle Factors Affecting Stress")

    st.pyplot(fig)

    # ---------- Suggestions ----------
    st.subheader("💡 Suggestions to Reduce Stress")

    st.markdown("""
🌿 **Improve Sleep**
- Try to sleep 7–8 hours regularly.

🧘 **Practice Relaxation**
- Meditation  
- Deep breathing  
- Yoga

📅 **Manage Study Time**
- Use time-blocking technique
- Avoid last minute study pressure

🤝 **Stay Social**
- Spend time with friends or family
- Participate in activities

📵 **Limit Screen Time**
- Avoid mobile before sleeping

🎧 **Listen to relaxing music**
- Music helps reduce mental pressure
""")

# ---------- Footer ----------
st.markdown("---")

st.write("💙 *Take care of your mental health*")
st.write("✨ Stay positive | Stay balanced | Stay healthy")

