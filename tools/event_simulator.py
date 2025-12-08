import json
import time
import uuid
from datetime import datetime
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def generate_event():
    return {
        "@timestamp": datetime.utcnow().isoformat() + "Z",
        "event": {
            "id": str(uuid.uuid4()),
            "category": "authentication"
        },
        "host": {"hostname": "lab-server"},
        "user": {"name": "analyst"},
        "source": {"ip": "192.168.1.10"},
        "destination": {"ip": "192.168.1.20"},
        "log": {"message": "failed login attempt"}
    }

while True:
    event = generate_event()
    producer.send("raw-events", event)
    print("sent:", event["event"]["id"])
    time.sleep(1)
