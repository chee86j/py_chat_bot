# Import necessary classes from langchain_ollama library and TextBlob for sentiment analysis.
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from textblob import TextBlob

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

# Function to analyze sentiment of user input for richer conversational experience.
# This is used to help the model understand the user's mood and respond accordingly in
# a more human-like manner to recognize to tailor its responses to more empathetic or helpful.
def analyze_sentiment(text):
    analysis = TextBlob(text)
    # Returns 'positive', 'negative', or 'neutral' based on the polarity score.
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity < 0:
        return 'negative'
    else:
        return 'neutral'

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

        # Perform sentiment analysis on the user input.
        sentiment = analyze_sentiment(user_input)
        print(f"Detected sentiment: {sentiment}.")  # Display detected sentiment.

        print("Thinking...")  # Indicate that the Bot is Processing.
        try:
            # Append sentiment information to the context for the model to use.
            sentiment_context = f"{context} Sentiment: {sentiment}."
            # Invoke the Model w/ Current Context & the New User Question.
            result = chain.invoke({"context": sentiment_context, "question": user_input})
            # Strip the Response from the Model to Ensure No Leading/Trailing Whitespaces.
            response = result.strip()
            print("Bot:", response)  # Print the Bot's Response.
            # Update the Context w/ the Latest Exchange.
            context += f"\nYou: {user_input}\nAI: {response}"
        except Exception as e:
            # Handle Any Exceptions.
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    handle_conversation()  # Start the conversation handling function.
