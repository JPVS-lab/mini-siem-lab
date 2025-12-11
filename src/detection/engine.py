import json
from kafka import KafkaConsumer

TOPIC = "siem-events"

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

print("[*] Detection engine running...")

for event in consumer:
    data = event.value
    if data.get("event_type") == "auth" and data.get("status") == "failed":
        print(f"[ALERT] Failed login detected: {data}")
