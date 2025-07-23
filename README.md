# 🧑‍💼 HR Chatbot for Candidate Screening

A smart AI-powered HR chatbot built with **Streamlit**, **OpenAI**, and **Google Vertex AI**, designed to automate candidate screening through real-time evaluations and email notifications.

---

## 🚀 Features

- 🧠 **AI-Powered Screening** using GPT-4 or Vertex AI
- ❓ **Auto-Generated Questions** based on job role
- 📊 **Answer Evaluation** with scoring logic
- ✅ **Final Status Summary** (Selected/Not Selected)
- 📁 **Responses Saved** to CSV
- 📧 **Email Notification** to candidates
- 🎨 **Clean UI** with custom CSS styling

 ## 🖥️ Live Demo

```
hr-chatbot/
├── app.py                  # Streamlit frontend
├── chatbot_logic.py        # Evaluation & AI logic
├── question_gen.py         # Question generation logic
├── email_utils.py          # Email sending functions
├── storage.py              # CSV saving utility
├── styles.css              # Custom styles
├── requirements.txt        # Python dependencies
└── .streamlit/
    └── secrets.toml        # API keys (hidden)
```


## 📤 Outputs
candidate_results.csv – contains candidate name, answers, scores, final status, and timestamp.

## 📧 Email Format
Candidates receive a mail like:

```Subject: Interview Result - HR Chatbot
Body: Hello [Candidate Name], Thank you for your submission. Your average score was [x]. You have been [Selected/Not Selected].
```

## 📌 To Do
1. Add resume upload and parsing
2.Deploy on Streamlit Cloud / Hugging Face Spaces
3.Add authentication for HR users
4.Real time face monitoring.
5.Tab-Switch Detection
6.UI/UX enhancements

🤝 Contributing
Pull requests are welcome! For major changes, open an issue first to discuss what you'd like to change.

🙌 Acknowledgements
Streamlit
OpenAI
Google Vertex AI
