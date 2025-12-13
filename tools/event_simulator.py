import json
import time
import uuid
import random
from datetime import datetime
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

ATTACKER_IP = "192.168.1.10"
NOISE_IPS = [f"192.168.1.{i}" for i in range(20, 50)]

def generate_event():
    is_attack = random.random() < 0.6  # 60% ataque

    source_ip = (
        ATTACKER_IP if is_attack
        else random.choice(NOISE_IPS)
    )

    return {
        "@timestamp": datetime.utcnow().isoformat() + "Z",
        "event": {
            "id": str(uuid.uuid4()),
            "category": "authentication"
        },
        "host": {"hostname": "lab-server"},
        "user": {"name": random.choice(["admin", "root", "user"])},
        "source": {"ip": source_ip},
        "destination": {"ip": "192.168.1.20"},
        "log": {"message": "failed login attempt"}
    }

print("[*] Event simulator running...")

while True:
    event = generate_event()
    producer.send("raw-events", event)
    print("sent:", event["source"]["ip"])
    time.sleep(1)

