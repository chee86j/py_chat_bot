# Local AI Chatbot with LLaMA

Welcome to the Local AI Chatbot project! This project demonstrates how to create a chatbot that leverages open-source AI models running locally on your machine. Unlike other chatbot implementations that rely on external APIs or paid services, this chatbot uses the LLaMA model, which you can run entirely on your own hardware.

## Project Overview

This project sets up a Python-based chatbot using the LLaMA language model, an open-source model designed to handle natural language processing tasks. The chatbot can understand and respond to user input, maintaining context over a conversation. It’s a great starting point for anyone interested in AI and chatbot development without relying on third-party subscriptions.

By default, the chatbot uses the LLaMA 3 model, which has 8 billion parameters, but you can easily switch to any other model supported by the Ollama platform based on your system's capabilities and needs.

## Features

- **Local Execution**: The chatbot runs entirely on your local machine, meaning no external API calls or subscriptions are needed.
- **Contextual Responses**: The chatbot maintains conversation history, allowing it to generate context-aware responses.
- **Customizable Model**: While the default model is LLaMA 3 (8 billion parameters), you can choose any other model supported by Ollama.
- **Virtual Environment**: The project is set up using a Python virtual environment to ensure isolated dependencies and a clean workspace.

## Prerequisites

Before you begin, ensure you have the following installed:

1. **Python 3.x**: The project is developed using Python 3. Ensure you have Python 3.x installed on your machine.
2. **Ollama**: A tool to run open-source language models locally. [Download Ollama](https://ollama.com).
3. **Git**: Optional, but recommended for version control.

## Installation

### Step 1: Clone the Repository

If you're using Git, clone this repository:

```bash
git clone https://github.com/your-username/local-ai-chatbot.git
cd local-ai-chatbot
```

### Step 2: Downlad Ollama & Your Preferred Model

Open your browser and download the Ollama tool from the [official website](https://ollama.com). You can also download the model of your choice from the same website.

1. Verify that Ollama has been installed correctly by running the following command:

```bash
ollama
```

2. Use Ollama to download the model of your choice. For example, to download the LLaMA 3 model, run:

```bash
ollama pull llama3
```

3. Make sure the model you choose is compatible with your system's hardware and memory capacity. Consult with the Ollama
   documentation at https://github.com/ollama/ollama for more information on Models, Parameters, and Hardware requirements.
   `You should have at least 8 GB of RAM available to run the 7B models, 16 GB to run the 13B models, and 32 GB to run the 33B models.`

4. Verify that the model (in my case llama3) has been downloaded successfully and is available for use by running:

```bash
ollama run llama3
```

and give it your first prompt to see how it responds.

### Step 3: Create a Virtual Environment

Create a Python virtual environment to manage dependencies:

--on MacOS and Linux:

```bash
python -m venv customChatbotName
```

--on Windows:

```bash
python3 -m venv customChatbotName
```

Activate the virtual environment:

--on MacOS and Linux:

```bash
source customChatbotName/bin/activate
```

--on Windows:

```bash
.\customChatbotName\Scripts\activate
```

or in PowerShell:

```bash
.\customChatbotName\Scripts\Activate.ps1
```

or in cmd:

```bash
.\customChatbotName\Scripts\activate.bat
```

Upon activation, you should see the virtual environment name prefix your terminal prompt.

### Step 4: Install Dependency Packages

In the activated virtual environment, install the required Python packages within the virtual environment:

```bash
pip install langchain langchain-ollama ollama
```

### Step 5: Run the Chatbot

Run the chatbot script to start the conversation:

```bash
python3 main.py
```
