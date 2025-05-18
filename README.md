1.Notification System (Flask, RabbitMQ, Email, SMS, and In-App):

This repository contains a backend notification service designed using Flask, RabbitMQ, PostgreSQL, and third-party APIs for email and SMS notifications. The system facilitates the sending of notifications via different channels, ensuring efficient communication and seamless user experience. It supports email notifications through SMTP, SMS notifications via Twilio, and in-app notifications stored in PostgreSQL. RabbitMQ is utilized for handling asynchronous message processing, improving performance and reliability. The REST API allows users to trigger notifications dynamically.

2.Setup Instructions:

To set up the notification system, begin by installing the required dependencies. Ensure Python is installed on your machine, then install the necessary packages by running the command "pip install flask sqlalchemy pika twilio psycopg2." Next, set up the PostgreSQL database by creating a new database using the command "CREATE DATABASE notifications_db;" and verifying that the "SQLALCHEMY_DATABASE_URI" is correctly configured within "notification_server.py."
For message queue management, RabbitMQ must be installed and running. Start the RabbitMQ server using the command "rabbitmq-server" , and confirm that queues are active by running "rabbitmqctl list_queues"
To enable email notifications, configure the email credentials within "notification_server.py" . Set "EMAIL_USERNAME" as your email address and "EMAIL_PASSWORD" as your Google App Password, which can be generated through Google's App Password service. This ensures secure authentication for sending emails. For SMS notifications, create a Twilio account and configure the Twilio credentials, including the account SID, authentication token, and Twilio phone number.
Once the configuration is complete, create a JSON file for testing notification requests. Open Notepad and copy the following JSON data:
{
  "type": "email",
  "recipient": "recipient@example.com",
  "message": "Hello, this is your notification!"
}
Save the file as data.json in an accessible directory.
To run the server, execute "python notification_server.py" , ensuring that Flask is listening for requests. To process notifications, start the RabbitMQ worker using the command "python worker.py". This worker ensures that queued notifications are processed efficiently.
To test the notification system, send a request using curl by executing the command "curl -X POST http://127.0.0.1:5000/notifications -H "Content-Type: application/json" --data @data.json". Alternatively, you can use Python to send a request programmatically:
import requests

data = {"type": "email", "recipient": "recipient@example.com", "message": "Hello, this is your notification!"}
requests.post("http://127.0.0.1:5000/notifications", json=data)

3.Project Structure:

The repository consists of several essential files. The "models.py" file defines database models for storing notifications. The "notification_server.py" script implements the Flask API responsible for handling notification requests. The "worker.py" file contains the RabbitMQ consumer that processes notifications asynchronously. The "README.md" file provides documentation, and "data.json" serves as a test payload for sending notifications.

4.Assumptions:

The system is designed with several assumptions. PostgreSQL is used to store in-app notifications, requiring a properly configured database connection. RabbitMQ must be running to handle asynchronous message processing, ensuring notifications are efficiently managed. Email authentication relies on Google App Passwords rather than a regular email password to improve security. SMS notifications are handled via Twilio, necessitating a registered Twilio account for sending messages.
Following these steps ensures the notification system operates correctly. If additional modifications or troubleshooting are required, reviewing logs from Flask and RabbitMQ can help identify issues. The system is built for scalability and can be enhanced further based on specific application needs. 
