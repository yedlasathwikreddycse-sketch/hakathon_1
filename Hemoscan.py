import streamlit as st
import pandas as pd
from groq import Groq

# Page configuration
st.set_page_config(page_title="HemoScan AI", page_icon="🩸", layout="centered")

st.title("🩸 HemoScan AI – Anemia Detection & Risk Analysis System")
st.write("AI-based system to analyze anemia risk using health parameters.")

# Sidebar input
st.sidebar.header("Patient Details")

age = st.sidebar.slider("Age", 1, 100, 25)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
hemoglobin = st.sidebar.number_input("Hemoglobin (g/dL)", min_value=5.0, max_value=20.0, value=12.0)
rbc = st.sidebar.number_input("RBC Count (million cells/mcL)", min_value=3.0, max_value=7.0, value=4.5)
mcv = st.sidebar.number_input("MCV (fL)", min_value=70, max_value=110, value=90)
mch = st.sidebar.number_input("MCH (pg)", min_value=20, max_value=40, value=30)

# Function to detect anemia risk
def detect_anemia(gender, hemoglobin):
    if gender == "Male":
        if hemoglobin < 13:
            return "High Risk"
        else:
            return "Low Risk"
    elif gender == "Female":
        if hemoglobin < 12:
            return "High Risk"
        else:
            return "Low Risk"

risk = detect_anemia(gender, hemoglobin)

# Display patient data
st.subheader("📊 Patient Information")

patient_data = pd.DataFrame({
    "Age": [age],
    "Gender": [gender],
    "Hemoglobin": [hemoglobin],
    "RBC Count": [rbc],
    "MCV": [mcv],
    "MCH": [mch]
})

st.dataframe(patient_data)

# Risk result
st.subheader("🧪 Anemia Risk Result")

if risk == "High Risk":
    st.error("⚠️ High Risk of Anemia Detected")
else:
    st.success("✅ Hemoglobin levels appear normal")

# Groq AI report
st.subheader("🤖 AI Health Report")

api_key = st.text_input("Enter Groq API Key", type="password")

if st.button("Generate AI Report"):

    if api_key.strip() == "":
        st.warning("Please enter a valid Groq API Key")

    else:
        try:
            client = Groq(api_key=api_key)

            prompt = f"""
            Patient Details:
            Age: {age}
            Gender: {gender}
            Hemoglobin: {hemoglobin}
            RBC Count: {rbc}
            MCV: {mcv}
            MCH: {mch}

            Risk Level: {risk}

            Explain whether the patient might have anemia and give health suggestions.
            """

            response = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[{"role": "user", "content": prompt}]
            )

            report = response.choices[0].message.content
            st.write(report)

        except Exception as e:
            st.error("Failed to generate AI report.")
            st.write(str(e))

st.markdown("---")
st.caption("HemoScan AI | Anemia Detection & Risk Analysis System")