import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_result_email(candidate_email, candidate_name, avg_score, status):
    sender_email = "hrchatbot0@gmail.com"  # ✅ Fixed
    sender_password = "iuqnnpjdjpygzggf"   # ✅ App Password

    subject = "🎯 Screening Result - HR Chatbot"
    body = f"""
Hi {candidate_name},

Thank you for taking the screening test.
Your average score is: {avg_score}/10
Result: {status}

{"Congratulations! You've been shortlisted!" if status == "Selected" else "Unfortunately, you were not shortlisted this time."}

Best regards,  
HR Chatbot Team
    """

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = candidate_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, candidate_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False
