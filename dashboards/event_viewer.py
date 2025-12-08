import json
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "siem-events",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="latest",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

print("[*] Event viewer running...")

for message in consumer:
    event = message.value
    print(f"[EVENT] {event}")
