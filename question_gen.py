import re
import streamlit as st
from openai import OpenAI
import random

# Use OpenAI client but for Together API
client = OpenAI(
    api_key=st.secrets["TOGETHER_API_KEY"],
    base_url="https://api.together.xyz/v1"  # Correct Together base URL
)

def generate_questions(job_role):
    variation_tag = random.choice(["Set A", "Set B", "Creative Version", "Variant X", "Unique Angle"])
    prompt = f"""
You are an HR assistant.

Generate exactly 5 **creative and varied** candidate screening questions for a **{job_role}** role. 
Avoid generic or repetitive questions. Include technical, situational, and behavioral aspects.

({variation_tag})  
Number them like:
1. ...
2. ...
3. ...
4. ...
5. ...
"""

    # ✅ Corrected: use the `client` object (not `openai.chat.completions.create`)
    response = client.chat.completions.create(
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",  # make sure this model is supported
        messages=[
            {"role": "system", "content": "You are an HR assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.9
    )

    content = response.choices[0].message.content.strip()

    questions = re.findall(r"^\s*\d+[.)-]?\s+(.*)", content, re.MULTILINE)

    return questions[:5] if len(questions) >= 5 else ["Question generation failed."]
