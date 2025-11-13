import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_result_email(candidate_email, candidate_name, avg_score, status):
    sender_email = "hrchatbot0@gmail.com"
    sender_password = "iuqnnpjdjpygzggf"

    subject = "Screening Result – HR Chatbot"

    if status.lower() == "selected":
        result_message = f"""
Dear {candidate_name},

We are pleased to inform you that you have been shortlisted based on your performance in the screening process.  
Your average score: {avg_score}/10

Our recruitment team will review your profile in detail and contact you shortly with information regarding the next steps in the selection process.

We appreciate the time and effort you dedicated to completing the assessment and look forward to further interactions.

Sincerely,  
HR Chatbot Team
"""
    else:
        result_message = f"""
Dear {candidate_name},

Thank you for participating in the screening process.  
Your average score: {avg_score}/10

After careful consideration, we regret to inform you that you have not been shortlisted for the next stage of the recruitment process.  

We appreciate the effort you put into your application and encourage you to apply again for future opportunities that match your profile.

Sincerely,  
HR Chatbot Team
"""

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = candidate_email
    msg['Subject'] = subject
    msg.attach(MIMEText(result_message, 'plain'))

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
