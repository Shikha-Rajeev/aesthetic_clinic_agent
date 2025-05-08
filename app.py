import os
from dotenv import load_dotenv
import google.generativeai as genai
MEMORY_FILE="memory.txt"

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def save_to_memory(user_input: str,ai_response: str):
    with open(MEMORY_FILE,"a") as f:
        f.write(f"User: {user_input}\nAI: {ai_response}\n\n")

def load_memory()->str:
    try:
        with open(MEMORY_FILE,"r") as f:
            return f.read()
    except FileNotFoundError:
        return "No memory yet."

model=genai.GenerativeModel("gemini-1.5-flash")

def ask(prompt: str) -> str:
    context=f""" 
    Past Conversations:
    {load_memory()}
    
    New question: {prompt}
    """
    response=model.generate_content(context)
    save_to_memory(prompt,response.text)
    print("💡 "+response.text)
    return response.text
    
def main():
    print("🌟 Aesthetic Clinic Assistant 🌟 (type 'quit' to exit)")
    while True:
        user_input=input("\nYou: ")
        if user_input.lower()=="quit":
            break
        ask(f"You're a clinic business expert. Answer briefly: {user_input}")
        
if __name__=="__main__":
    main()

#ask("What's one KPI for aesthetic clinics?")