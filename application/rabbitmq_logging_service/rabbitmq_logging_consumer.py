import pika
import pathlib
import json

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
HOST, PORT = "172.18.0.3", 5672


connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST, port=PORT))
channel = connection.channel()

channel.exchange_declare(exchange="logs", exchange_type="fanout", durable=True)

result = channel.queue_declare(queue="", exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange="logs", queue=queue_name)

print(" [*] Waiting for logs. To exit press CTRL+C")


def callback(ch, method, properties, body):
    print(" [x] %r" % body)
    body_decode = body.decode("utf-8")
    with open(BASE_DIR / "address_book_rabbitmq_logging.json", "a", encoding="utf-8") as file:
        file.write(body_decode)
        file.write("\n")


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
