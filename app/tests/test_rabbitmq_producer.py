# app/tests/test_rabbitmq_producer.py
from app.producers import RabbitMQProducer
from app.models import Announcement
from app.database import Base
import pika
import datetime
from datetime import timedelta

def test_send_announcement():
    announcement_data = {
        "title": "Test Announcement",
        "content": "This is a test announcement.",
        "send_at": (datetime.now() + timedelta(minutes=1)).isoformat()
    }
    announcement = Announcement(**announcement_data)
    rabbitmq_producer = RabbitMQProducer()
    rabbitmq_producer.send_announcement(announcement)

    # Verify the message was sent to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
    channel = connection.channel()
    messages = channel.queue_messages("announcements")
    assert len(messages) == 1
    message = messages[0]
    assert message.body == announcement.json().encode()
    connection.close()