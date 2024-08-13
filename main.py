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
        
        # Invoke the model with the context and user input
        result = chain.invoke({"context": context, "question": user_input})
        
        # Ensure Clean & Concise Response
        response = result.strip() if isinstance(result, str) else result
        print("Bot:", response)
        
        # Update the context with the latest conversation turn
        context += f"\nYou: {user_input}\nAI: {response}"
        
if __name__ == "__main__":
    handle_conversation()
