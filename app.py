import streamlit as st
import pandas as pd
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_google_genai import ChatGoogleGenerativeAI

# --- Page Configuration ---
st.set_page_config(
    page_title="NeoStats AI Insights Assistant",
    page_icon="🤖",
    layout="wide"
)

# --- Helper Functions ---
def load_data(uploaded_file):
    """Loads and preprocesses an Excel file into a DataFrame."""
    try:
        df = pd.read_excel(uploaded_file, engine='openpyxl')
        df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')
        return df
    except Exception as e:
        st.error(f"Error reading the Excel file: {e}")
        return None

def create_agent(df, api_key):
    """
    Creates a LangChain Pandas DataFrame Agent using Google Gemini API.
    """
    try:
        llm = ChatGoogleGenerativeAI(
            model="models/gemini-1.5-flash-latest",
            google_api_key=api_key,
            temperature=0.3
        )
        agent = create_pandas_dataframe_agent(
            llm=llm,
            df=df,
            verbose=True,
            allow_dangerous_code=True  # Needed for DataFrame operations
        )
        return agent
    except Exception as e:
        st.error(f"Failed to create agent: {e}")
        return None

# --- Main Application UI ---
def main():
    st.title("🤖 AI-Powered Insights Assistant")
    st.write("Upload your Excel file and ask questions about your data using natural language.")

    try:
        api_key = st.secrets["GOOGLE_API_KEY"]
    except:
        st.warning("API Key not found in secrets. Please enter it below.")
        api_key = st.text_input("Enter your Google API Key:", type="password")

    if not api_key:
        st.info("Please provide an API key to proceed.")
        st.stop()

    uploaded_file = st.file_uploader(
        "📁 Upload an Excel file (.xlsx)",
        type="xlsx",
        help="Make sure the file has a single sheet with headers."
    )

    if uploaded_file:
        df = load_data(uploaded_file)

        if df is not None:
            st.success("✅ File loaded successfully!")
            with st.expander("📊 View Data"):
                st.dataframe(df.head())

            agent = create_agent(df, api_key)
            if agent is None:
                st.stop()

            st.header("💬 Ask a Question")
            user_query = st.text_input("e.g., 'Show average sales by region'")

            if st.button("Get Answer"):
                if user_query:
                    with st.spinner("Thinking..."):
                        try:
                            response = agent.run(user_query)
                            st.subheader("💡 Answer:")
                            st.write(response)
                        except Exception as e:
                            st.error(f"Error generating response: {e}")
                else:
                    st.warning("Please enter a question.")
    else:
        st.info("Awaiting file upload...")

if __name__ == "__main__":
    main()
