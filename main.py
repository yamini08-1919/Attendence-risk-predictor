# 🔕 Hide warnings
import warnings
warnings.filterwarnings("ignore")

# 📦 Imports
import os
from langchain_groq import ChatGroq

# 🔐 API Key
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("❌ Please set GROQ_API_KEY environment variable")

# 🤖 LLM (latest working model)
llm = ChatGroq(
    temperature=0,
    model_name="llama-3.1-8b-instant",
    groq_api_key=groq_api_key
)

# 🛠️ FUNCTIONS (TOOLS LOGIC)

def calculate_attendance(attended, total):
    return (attended / total) * 100

def predict_risk(attendance):
    if attendance >= 75:
        return "✅ Low Risk (Safe)"
    elif attendance >= 60:
        return "⚠️ Medium Risk"
    else:
        return "❌ High Risk (Danger)"

def classes_needed(attended, total):
    extra = 0
    while (attended / total) * 100 < 75:
        attended += 1
        total += 1
        extra += 1
    return extra

# 🚀 MAIN PROGRAM
print("🎯 Attendance Risk Predictor AI (Stable Version)")
print("Type 'exit' to quit\n")

while True:
    query = input("👤 You: ").lower()

    if query == "exit":
        print("👋 Exiting... Goodbye!")
        break

    try:
        # Extract numbers from input
        numbers = [int(s) for s in query.split() if s.isdigit()]

        if "attendance" in query and len(numbers) >= 2:
            attended, total = numbers[0], numbers[1]
            percentage = calculate_attendance(attended, total)
            print(f"🤖 AI: 📊 Attendance is {percentage:.2f}%")

        elif "risk" in query and len(numbers) >= 1:
            attendance = numbers[0]
            risk = predict_risk(attendance)
            print(f"🤖 AI: {risk}")

        elif "classes" in query and len(numbers) >= 2:
            attended, total = numbers[0], numbers[1]
            extra = classes_needed(attended, total)
            print(f"🤖 AI: 📚 You need to attend {extra} more classes to reach 75%")

        else:
            # fallback to AI response
            response = llm.invoke(query)
            print("🤖 AI:", response.content)

    except Exception as e:
        print("❌ Error:", str(e))
