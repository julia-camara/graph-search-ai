import os
import pandas as pd
import re
import ast
import google.generativeai as genai
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def extract_final_answer(response_text):
    match = re.search(r"Final Answer:\s*(\[.*?\])", response_text)
    if match:
        try:
            return ast.literal_eval(match.group(1))
        except Exception:
            return []
    return []

def process_llm():
    df = pd.read_csv("prompts.csv")
    results = []

    model = genai.GenerativeModel("models/gemini-1.5-flash")

    for _, row in df.iterrows():
        prompt_id = row["prompt_id"]
        problem_type = row["problem_type"]
        prompt = row["prompt"]
        expected = row["answer_nodes"].strip("[]").replace("'", "").split()

        response = model.generate_content(prompt)
        response_text = response.text
        predicted = extract_final_answer(response_text)

        is_correct = set(expected) == set(predicted)
        results.append({
            "prompt_id": prompt_id,
            "problem_type": problem_type,
            "expected": expected,
            "predicted": predicted,
            "is_correct": is_correct
        })

    pd.DataFrame(results).to_csv("llm/llm_answers.csv", index=False)

if __name__ == "__main__":
    process_llm()
