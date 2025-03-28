import smtplib
from email.mime.text import MIMEText

class AlertSystem:
    def __init__(self, email="your_email@gmail.com", password="your_password"):
        """Initialize email alert system."""
        self.email = email
        self.password = password

    def send_alert(self, message="🚨 Fall Detected! Immediate Action Required!"):
        """Send an email alert when a fall is detected."""
        try:
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login(self.email, self.password)
            msg = MIMEText(message)
            msg["Subject"] = "Fall Alert 🚨"
            msg["From"] = self.email
            msg["To"] = self.email
            server.sendmail(self.email, self.email, msg.as_string())
            server.quit()
            print("📧 Alert Sent Successfully!")
        except Exception as e:
            print(f"⚠️ Error sending alert: {e}")
