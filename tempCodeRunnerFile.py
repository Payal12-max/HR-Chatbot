import re
import streamlit as st
import openai
from openai import OpenAI
import random

# Use OpenAI client but for Together API
client = OpenAI(
    api_key=st.secrets["TOGETHER_API_KEY"],
    base_url="https://api.together.xyz/v1"  # Correct Together base URL