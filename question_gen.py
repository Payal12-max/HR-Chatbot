'''import openai

def generate_questions(job_role):
    prompt = f"Generate 5 candidate screening questions for a {job_role} role."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an HR assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    questions = response['choices'][0]['message']['content'].split('\n')
    return [q.strip("- ").strip() for q in questions if q.strip()]


import cohere

co = cohere.Client("lefSWs11zMKsbaQZcwjRo5vOo9KMvICjXd0f0ecL")

def generate_questions(job_role):
    chat_response = co.chat(
        model='command-r-plus',  # or 'command-r'
        message=f"Generate 5 HR interview screening questions for the role of {job_role}."
    )
    
    lines = chat_response.text.strip().split('\n')
    return [q.strip("12345).•- ") for q in lines if q.strip()]'''

import re
import streamlit as st
from openai import OpenAI
import random

# Initialize Together AI client
client = OpenAI(
    api_key=st.secrets["TOGETHER_API_KEY"],  # ✅ Set this in .streamlit/secrets.toml
    base_url="https://api.together.xyz/v1"   # ✅ Required for Together AI
)

def generate_questions(job_role):
    # Add variation to prompt for more diverse output
    variation_tag = random.choice(["Set A", "Set B", "Creative Version", "Variant X", "Unique Angle"])

    # More expressive prompt for diverse, non-generic questions
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

    # Call Together AI Mixtral model
    response = client.chat.completions.create(
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        messages=[
            {"role": "system", "content": "You are an HR assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.9  # Higher for more randomness
    )

    # Get the model's response text
    content = response.choices[0].message.content.strip()

    # Use regex to extract exactly 5 numbered questions
    questions = re.findall(r"^\s*\d+[.)-]?\s+(.*)", content, re.MULTILINE)


    # Ensure fallback in case extraction fails
    return questions[:5] if len(questions) >= 5 else ["Question generation failed."]

