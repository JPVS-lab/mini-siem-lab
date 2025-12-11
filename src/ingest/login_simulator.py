import json
import time
import random
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

users = ["admin", "root", "jvc", "guest"]

print("[*] Login simulator running...")

while True:
    event = {
        "event_type": "auth",
        "user": random.choice(users),
        "status": random.choice(["success", "failed"]),
        "ip": f"192.168.1.{random.randint(10,250)}"
    }

    producer.send("siem-events", event)
    print(f"[LOGIN EVENT] {event}")
    time.sleep(1)
