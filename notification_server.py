from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# ✅ Email Configuration
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USERNAME = "farharizwan1910@gmail.com"
EMAIL_PASSWORD = "gamc pvix nnre ijix"  # Use an App Password instead of your real password

# ✅ Function to Send Email Notifications
def send_email_notification(recipient, subject, message):
    try:
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()
        server.login(EMAIL_USERNAME, EMAIL_PASSWORD)

        msg = MIMEMultipart()
        msg["From"] = EMAIL_USERNAME
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(message, "plain"))

        server.sendmail(EMAIL_USERNAME, recipient, msg.as_string())
        server.quit()
        print(f"✅ Email sent successfully to {recipient}!")
        return True
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
        return False

# ✅ Flask Route for Sending Notifications
@app.route('/notifications', methods=['POST'])
def send_notification():
    data = request.get_json()
    notification_type = data.get("type")
    recipient = data.get("recipient")
    message = data.get("message")

    if notification_type == "email":
        success = send_email_notification(recipient, "New Notification", message)
        if success:
            return jsonify({"status": "✅ Email sent!"}), 200
        else:
            return jsonify({"error": "❌ Email failed to send"}), 500
    
    return jsonify({"error": "Unsupported notification type"}), 400

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)