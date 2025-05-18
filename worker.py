import pika
import json
import smtplib
import time

def send_email(recipient, message):
    """Send an email notification using SMTP."""
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('your-email@gmail.com', 'your-password')
        server.sendmail('your-email@gmail.com', recipient, message)
        server.quit()
        print(f"✅ Email sent successfully to {recipient}!")
        return True
    except Exception as e:
        print(f"❌ Failed to send email: {str(e)}")
        return False

def callback(ch, method, properties, body):
    """Handles incoming RabbitMQ messages and processes notifications."""
    try:
        data = json.loads(body)
        print(f"Received notification: {data}")

        success = False
        if data['type'] == 'email':
            success = send_email(data['recipient'], data['message'])

        if success:
            ch.basic_ack(delivery_tag=method.delivery_tag)
        else:
            print("❌ Notification failed. Retrying...")
            time.sleep(2)
            ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)

    except Exception as e:
        print(f"❌ Error processing notification: {str(e)}")
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)

def connect_rabbitmq():
    """Establish connection to RabbitMQ and start listening."""
    while True:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
            channel = connection.channel()
            channel.queue_declare(queue='notification_queue', durable=True)
            print("🚀 Worker is listening for notifications...")
            channel.basic_consume(queue='notification_queue', on_message_callback=callback)
            channel.start_consuming()
        except pika.exceptions.AMQPConnectionError as e:
            print(f"❌ RabbitMQ connection failed: {str(e)}. Retrying in 5 seconds...")
            time.sleep(5)

if __name__ == "__main__":
    connect_rabbitmq()