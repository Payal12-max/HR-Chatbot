import streamlit as st
from chatbot_logic import evaluate_answer
from question_gen import generate_questions
from storage import save_to_csv
from email_utils import send_result_email


# --- Set page config ---
st.set_page_config(
    page_title="HR Chatbot",
    page_icon="🧑‍💼",
    layout="wide"
)
# --- Load Custom CSS ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# --- Header ---
st.markdown("""
<div class="main-container">
<div class="header">
    <h1>🧑‍💼 HR Chatbot for Candidate Screening</h1>
    <p>Answer job-related questions, get scored, and receive your result instantly!</p>

</div>
""", unsafe_allow_html=True)  

# --- Candidate Info ---
st.markdown('<div class="section">', unsafe_allow_html=True)
candidate_name = st.text_input("👤 Enter your name:",key="name")
candidate_email = st.text_input("📧 Enter your email:")
job_role = st.selectbox("💼 Select the job role:", ["Software Engineer", "Data Analyst", "Marketing Executive", "Custom Role"])
st.markdown('</div>', unsafe_allow_html=True)

if job_role == "Custom Role":
    custom_role = st.text_input("📝 Enter the custom job role:")
    if custom_role.strip():
        job_role = custom_role 
         
# --- Session State ---
st.session_state.setdefault("questions", [])
st.session_state.setdefault("answers", [])
st.session_state.setdefault("scores", [])

# --- Start Screening ---
if st.button("🚀 Start Screening",key="pulse"):
    if not candidate_name.strip():
        st.warning("⚠️ Please enter your name.")
    elif not job_role.strip():
        st.warning("⚠️ Please enter/select a job role.")
    else:
        st.session_state.questions = generate_questions(job_role)
        st.session_state.answers = [""] * len(st.session_state.questions)
        st.session_state.scores = [None] * len(st.session_state.questions)

# --- Display Questions Dynamically ---
if st.session_state.questions:
    for i, question in enumerate(st.session_state.questions):
        st.markdown(f"<div class='question'><h3>Q{i+1}: {question}</h3></div>", unsafe_allow_html=True)

        st.session_state.answers[i] = st.text_area(
            label="✍️ Your Answer:",
            value=st.session_state.answers[i],
            key=f"answer_{i}",
            height=100
        )

        if st.button(f"🧠 Evaluate Q{i+1}", key=f"btn_eval_{i}"):
            if not st.session_state.answers[i].strip():
                st.warning("⚠️ Please write your answer before evaluation.")
            else:
                score, explanation = evaluate_answer(question, st.session_state.answers[i])
                st.session_state.scores[i] = score
                st.markdown(
                    f"""<div class='score-box'>✅ Score: {score}/10</div>""",
                    unsafe_allow_html=True
                    )
                st.markdown(
                    f"""<div class='explanation-box'>💡 Explanation: {explanation}</div>""",
                    unsafe_allow_html=True
                    )

# --- Submit Section ---
if st.button("📨 Submit All",key="all"):
    if not candidate_name.strip():
        st.error("⚠️ Please enter your name.")
    elif not candidate_email.strip():
        st.error("⚠️ Please enter your email.")
    elif any(score is None for score in st.session_state.scores):
        st.error("⚠️ Please evaluate all questions before submitting.")
    else:
        avg_score = sum(st.session_state.scores) / len(st.session_state.scores)
        status = "Selected" if avg_score >= 7 else "Not Selected"
        
        save_to_csv(
            candidate_name,
            candidate_email,
            job_role,
            st.session_state.questions,
            st.session_state.answers,
            st.session_state.scores,
            avg_score,
            status,
            filename="candidate_results.csv"
        )

        st.success("✅ Responses saved to CSV!")
        st.info(f"🎯 Final Status: **{status}** | Avg Score: {avg_score:.2f}/10")

        if send_result_email(candidate_email, candidate_name, avg_score, status):
            st.success("📧 Email sent to candidate!")
        else:
            st.error("❌ Failed to send email. Check credentials.")

# --- Close Main Container ---
st.markdown('</div>', unsafe_allow_html=True)
