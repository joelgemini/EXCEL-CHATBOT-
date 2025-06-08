# EXCEL CHATBOT AI Insights Assistant (https://excel-chatbot-foog.onrender.com/)

This project is a web-based conversational assistant built as part of the AI Engineer Use Case for NeoStats. The application allows business users to upload an Excel file, ask questions about the data in natural language, and receive answers in the form of text, tables, or visualizations.

## ✨ Features

* **Natural Language Queries**: Ask questions in plain English (e.g., "What's the total revenue?" or "Compare sales by region").
* **Excel File Upload**: Simply upload a standard `.xlsx` file to get started.
* **Schema-Agnostic**: The assistant works with any Excel file that has a clear header row. It does not rely on hardcoded column names or data structures.
* **Dynamic Visualizations**: Generates appropriate charts (bar, line, histograms) based on the user's query.
* **Data Preprocessing**: Automatically normalizes column names for more reliable analysis.
* **Usability**: Clean, intuitive, and responsive user interface.

## 🛠️ Technology Stack

* **Backend & Frontend**: [Streamlit](https://streamlit.io/)
* **LLM Framework**: [LangChain](https://www.langchain.com/) (specifically, the Pandas DataFrame Agent)
* **Language Model**: [OpenAI GPT-3.5/GPT-4](https://openai.com/)
* **Data Handling**: [Pandas](https://pandas.pydata.org/)
* **Plotting**: [Plotly](https://plotly.com/)

## 🚀 How It Works

The core of the application is the **LangChain Pandas DataFrame Agent**. When a user asks a question:
1.  The agent, powered by an OpenAI LLM, analyzes the question and the structure of the uploaded DataFrame.
2.  It formulates a plan and generates Python (Pandas) code to answer the question.
3.  This code is executed in a secure environment against the DataFrame.
4.  The result of the execution (whether it's a number, a piece of text, or a plot) is returned to the user.

This agent-based approach ensures maximum flexibility and fulfills the key requirement of being schema-agnostic.

## ⚙️ Setup and Local Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/joelgemini/EXCEL-CHATBOT.git]
2.  **Create a virtual environment and install dependencies:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3.  **Set up your OpenAI API Key:**
    Create a file `.streamlit/secrets.toml` and add your API key:
    ```toml
    OPENAI_API_KEY="sk-..."
    ```

4.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```
    The application will open in your web browser.

## 🌐 Deployment on Streamlit Community Cloud

Follow these steps to host the application live:

1.  **Push to GitHub**: Make sure all your files (`app.py`, `requirements.txt`, `README.md`) are pushed to a public GitHub repository.
2.  **Sign up/in to Streamlit**: Go to [share.streamlit.io](https://share.streamlit.io/) and sign in with your GitHub account.
3.  **Deploy App**: Click "New app", select your repository and branch, and ensure `app.py` is the main file path.
4.  **Add Secrets**: In the advanced settings during deployment (or in the app settings later), add your `OPENAI_API_KEY` as a secret. The key should be `OPENAI_API_KEY` and the value should be your `sk-...` token.
5.  **Deploy!**: Click the "Deploy!" button. Your application will be live in a few minutes.
