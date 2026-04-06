import streamlit as st
import os
from langchain_groq import ChatGroq

# 🔐 API Key
groq_api_key = os.getenv("GROQ_API_KEY")

# 🤖 LLM
llm = ChatGroq(
    temperature=0,
    model_name="llama-3.1-8b-instant",
    groq_api_key=groq_api_key
)

# 🛠️ Functions
def calculate_attendance(attended, total):
    return (attended / total) * 100

def predict_risk(attendance):
    if attendance >= 75:
        return "Low Risk (Safe)"
    elif attendance >= 60:
        return "Medium Risk"
    else:
        return "High Risk (Danger)"

def classes_needed(attended, total):
    extra = 0
    while (attended / total) * 100 < 75:
        attended += 1
        total += 1
        extra += 1
    return extra

# 🎨 UI
st.set_page_config(page_title="Attendance Risk Predictor", layout="centered")

st.title("🎯 Attendance Risk Predictor AI")

st.write("Enter your attendance details below:")

# Input fields
attended = st.number_input("Classes Attended", min_value=0)
total = st.number_input("Total Classes", min_value=1)

# Buttons
if st.button("Calculate Attendance"):
    percentage = calculate_attendance(attended, total)
    st.success(f"📊 Attendance: {percentage:.2f}%")

if st.button("Check Risk"):
    percentage = calculate_attendance(attended, total)
    risk = predict_risk(percentage)
    st.warning(f"⚠️ Risk Level: {risk}")

if st.button("Classes Needed for 75%"):
    extra = classes_needed(attended, total)
    st.info(f"📚 You need to attend {extra} more classes")

# AI Chat Section
st.subheader("💬 Ask AI")

user_query = st.text_input("Ask anything:")

if st.button("Ask AI"):
    if user_query:
        response = llm.invoke(user_query)
        st.write("🤖 AI:", response.content)