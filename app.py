import streamlit as st
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

# ---------------- ML MODEL ----------------

X = [
    [8,5,8],
    [7,6,7],
    [6,8,5],
    [5,9,4],
    [4,10,3],
    [9,4,9],
    [3,11,2],
    [7,7,6]
]

y = ["Low","Low","Medium","Medium","High","Low","High","Medium"]

model = DecisionTreeClassifier()
model.fit(X,y)

# ---------------- PAGE ----------------

st.set_page_config(page_title="Smart Stress Meter",page_icon="🧠")

st.markdown(
"<h1 style='text-align:center;color:#ff5733;'>🧠 Smart Stress Meter</h1>",
unsafe_allow_html=True
)

st.markdown(
"<p style='text-align:center;font-size:18px;'>Understand your stress level and take care of your mental wellbeing 💙</p>",
unsafe_allow_html=True
)

st.write("---")

st.info("✨ Small changes in daily habits can reduce stress and improve your happiness.")

# ---------------- INPUT ----------------

st.subheader("Enter your daily routine")

sleep = st.slider("😴 Sleep Hours",0,12,7)
work = st.slider("💻 Work / Study Hours",0,14,6)
mood = st.slider("😊 Mood Level (1-10)",1,10,6)

st.write("---")

# ---------------- PREDICTION ----------------

if st.button("Check Stress Level"):

    result = model.predict([[sleep,work,mood]])[0]

    st.subheader("Your Stress Result")

    if result == "Low":
        meter = 30
        color = "#2ecc71"
        st.success("Stress Level: LOW 😌")
        suggestion = "You're doing great! Keep maintaining balance and positivity 🌿"

    elif result == "Medium":
        meter = 60
        color = "#f39c12"
        st.warning("Stress Level: MEDIUM 😐")
        suggestion = "Take small breaks, listen to music or go for a short walk 🎧"

    else:
        meter = 90
        color = "#e74c3c"
        st.error("Stress Level: HIGH 😟")
        suggestion = "Relax your mind. Try meditation, deep breathing or exercise 🧘"

# ---------------- STRESS METER ----------------

    st.markdown(
    f"""
    <div style="
    width:95%;
    background-color:#dddddd;
    border-radius:25px;
    height:40px;
    margin:auto;">
        <div style="
        width:{meter}%;
        background-color:{color};
        height:40px;
        border-radius:25px;
        text-align:center;
        color:white;
        font-size:18px;
        font-weight:bold;">
        {meter}%
        </div>
    </div>
    """,
    unsafe_allow_html=True
    )

# ---------------- SUGGESTION ----------------

    st.markdown(
    f"""
    <div style="
    background-color:#f8c471;
    padding:15px;
    border-radius:12px;
    font-size:18px;
    margin-top:10px;">
    💡 Suggestion: {suggestion}
    </div>
    """,
    unsafe_allow_html=True
    )

# ---------------- GRAPH ----------------

    stress_score = 100 - (sleep*5 + mood*4) + work*4

    fig, ax = plt.subplots()
    ax.bar(["Stress Score"], [stress_score])
    ax.set_ylim(0,100)
    ax.set_ylabel("Stress Level")

    st.pyplot(fig)

# ---------------- MOTIVATION ----------------

st.write("---")

st.markdown(
"""
🌼 **Remember:**  
Your mental health is just as important as your physical health.  
Take breaks, breathe deeply, and give yourself time to relax.

💬 *"Peace begins with a calm mind."*
"""
)

# ---------------- FOOTER ----------------

st.write("---")

st.markdown(
"""
<div style='text-align:center;font-size:16px;color:gray;'>

Made with ❤️ for mental wellbeing  

✨ Take care of your mind. Your happiness matters.  

</div>
""",
unsafe_allow_html=True
)
