from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
You are a helpful AI assistant. Below is the conversation history and a new question.

Conversation History:
{context}

New Question: {question}

Your Answer:
"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("Welcome to AI ChatBot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        print("Thinking...")  # Feedback to the User

        try:
            # Invoke Model w/ the Context & User Input
            result = chain.invoke({"context": context, "question": user_input})
            
            # Ensure Clean & Concise Response
            response = result.strip() if isinstance(result, str) else result
            print("Bot:", response)

            # Update the Context w/ the Latest Conversation turn
            context += f"\nYou: {user_input}\nAI: {response}"
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    handle_conversation()

