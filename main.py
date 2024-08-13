# Import necessary classes from langchain_ollama library.
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Define the template for the chatbot's responses, setting AI's role and how it should handle conversation context.
template = """
You are a helpful AI assistant. Below is the conversation history and a new question.

Conversation History:
{context}

New Question: {question}

Your Answer:
"""

# Initialize LLaMA model specifying which version to use, here 'llama3'.
model = OllamaLLM(model="llama3")

# Create a prompt template from predefined template string.
prompt = ChatPromptTemplate.from_template(template)

# Combine the prompt template w/ model to create a processing chain.
chain = prompt | model

# Define the function to handle ongoing conversation.
def handle_conversation():
    context = ""  # Initialize an empty context for conversation.
    print("Welcome to AI ChatBot! Type 'exit' to end, 'reset' to clear the conversation, or 'help' for more options.")
    while True:
        # Prompt User for Input.
        user_input = input("You: ").strip().lower()
        if user_input == "exit":
            break  # Break the Loop to Exit Chat.
        elif user_input == "reset":
            context = ""  # Clear the Context if User Types 'reset'.
            print("Conversation reset.")
            continue  # Continue to the Next Iteration of Loop.
        elif user_input == "help":
            # Provide Instructions to the User.
            print("Type any question or 'exit' to leave, 'reset' to start over.")
            continue

        print("Thinking...")  # Indicate that the Bot is Processing.
        try:
            # Invoke the Model w/ Current Context & the New User Question.
            result = chain.invoke({"context": context, "question": user_input})
            # Strip the Response from the Model to Ensure No Leading/Trailing Whitespaces.
            response = result.strip()
            print("Bot:", response)  # Print the Bot's Response.
            # Update the Context w.the Latest Exchange.
            context += f"\nYou: {user_input}\nAI: {response}"
        except Exception as e:
            # Handle Any Exceptions.
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    handle_conversation()  # Start the conversation handling function.
