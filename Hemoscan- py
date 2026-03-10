import streamlit as st
from groq_use import get_ai_advice

st.set_page_config(page_title="HemoScan AI", layout="centered")

st.title("🩸 HemoScan AI")
st.subheader("Anemia Detection & Risk Analysis System")

st.write("Enter your health details to check anemia risk.")

# User Inputs
age = st.number_input("Age", 1, 100)
gender = st.selectbox("Gender", ["Male", "Female"])

hemoglobin = st.number_input("Hemoglobin Level (g/dL)", 0.0, 20.0)

fatigue = st.selectbox("Do you feel frequent fatigue?", ["No", "Yes"])
dizziness = st.selectbox("Do you experience dizziness?", ["No", "Yes"])
pale_skin = st.selectbox("Do you have pale skin?", ["No", "Yes"])
short_breath = st.selectbox("Shortness of breath?", ["No", "Yes"])

# Risk calculation
def calculate_risk():
    score = 0

    if hemoglobin < 12:
        score += 2

    if fatigue == "Yes":
        score += 1
    if dizziness == "Yes":
        score += 1
    if pale_skin == "Yes":
        score += 1
    if short_breath == "Yes":
        score += 1

    if score <= 1:
        return "Low Risk"
    elif score <= 3:
        return "Moderate Risk"
    else:
        return "High Risk"


if st.button("Analyze Risk"):

    risk = calculate_risk()

    st.subheader("📊 Risk Analysis Result")
    st.success(f"Your Anemia Risk Level: **{risk}**")

    user_data = f"""
    Age: {age}
    Gender: {gender}
    Hemoglobin: {hemoglobin}
    Fatigue: {fatigue}
    Dizziness: {dizziness}
    Pale Skin: {pale_skin}
    Shortness of Breath: {short_breath}
    Risk Level: {risk}
    """

    advice = get_ai_advice(user_data)

    st.subheader("🤖 AI Health Suggestions")
    st.write(advice)

st.markdown("---")
st.caption("HemoScan AI | AI Powered Health Screening System")
