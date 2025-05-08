import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model=genai.GenerativeModel("gemini-1.5-flash")

def ask_gemini(question: str)->str:
    response=model.generate_content(question)
    return response.text

def main():
    print("🌟 Aesthetic Clinic Assistant 🌟")
    while True:
        user_input=input("\nAsk me anything (or type 'exit'):")
        if user_input.lower()=="exit":
            break
        print("\nThinking...")
        answer=ask_gemini(f"You're a business advisor for aesthetic clinics. Answer concisely: {user_input}")
        print(f"\n💡 {answer}")
        
if __name__=="__main__":
    main()

#print(ask_gemini("Explain aesthetic clinics in 3 sentences."))