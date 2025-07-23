import re
import streamlit as st
import openai 

openai.api_key = st.secrets["TOGETHER_API_KEY"]
openai.base_url = "https://api.together.xyz/v1"

def evaluate_answer(question, answer):
    try:
        prompt = f"""
You are a strict technical interviewer evaluating candidate responses.

Evaluate the candidate's answer to the following interview question.
Give a score out of 10 and provide a brief explanation.

Respond ONLY in the following format:
Score: <number>/10
Explanation: <your explanation here>

⚠️ Do not write anything else or use formats like 9/1 or "Score is 8".
Stick to the format strictly.

Question: {question}
Answer: {answer}
"""

        response = openai.chat.completions.create(
            model="mistralai/Mixtral-8x7B-Instruct-v0.1",
            messages=[
                {"role": "system", "content": "You are an HR assistant evaluating interview responses."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=300
        )

        content = response.choices[0].message.content.strip()

        st.text_area("🔍 LLM Raw Response", content, height=200)

        score_match = re.search(r"Score:\s*(\d{1,2})\s*/\s*(\d{1,2})", content, re.IGNORECASE)
        explanation_match = re.search(r"Explanation:\s*(.*)", content, re.IGNORECASE | re.DOTALL)

        if score_match:
            score = int(score_match.group(1))
            denominator = int(score_match.group(2))

            if denominator != 10:
                score = 0
                explanation = "⚠️ Invalid score format returned by the model (not out of 10)."
            else:
                explanation = explanation_match.group(1).strip() if explanation_match else "No explanation found."
        else:
            score = 0
            explanation = "⚠️ Score not found in expected format."

        return score, explanation

    except Exception as e:
        st.error(f"❌ Error evaluating answer: {e}")
        return 0, "Evaluation failed due to an internal error."
