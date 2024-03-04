import pika
from app.models import Announcement

def send_announcement(announcement: Announcement):
    connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
    channel = connection.channel()
    channel.queue_declare(queue="announcements", durable=True)
    channel.basic_publish(exchange="", routing_key="announcements", body=announcement.json(), properties=pika.BasicProperties(delivery_mode=2))
    connection.close()