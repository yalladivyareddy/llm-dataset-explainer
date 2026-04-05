import os
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

# 👇 Get root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# 👇 Load .env from root
env_path = BASE_DIR / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("OPENAI_API_KEY")

print("ENV PATH:", env_path)
print("DEBUG KEY:", api_key)

if not api_key:
    raise ValueError("API key not found. Check your .env file.")

client = OpenAI(api_key=api_key)
def generate_insights(df):
    sample = df.head(20).to_string()
    shape = df.shape
    columns = list(df.columns)

    prompt = f"""
    You are a senior data analyst.

    Dataset Info:
    - Rows: {shape[0]}
    - Columns: {shape[1]}
    - Column Names: {columns}

    Sample Data:
    {sample}

    Your task:
    1. Explain what this dataset is about
    2. Give 3–5 key insights
    3. Highlight any unusual patterns
    4. Suggest possible business use cases

    Keep answers clear and structured.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
def ask_question(df, question):
    sample = df.head(20).to_string()

    prompt = f"""
    Dataset:
    {sample}

    Question: {question}

    Answer clearly with reasoning.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content