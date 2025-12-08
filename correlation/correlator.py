import json
from collections import defaultdict
from kafka import KafkaConsumer

TOPIC = "siem-events"

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

failed_attempts = defaultdict(int)

print("[*] Correlation engine running...")

for event in consumer:
    data = event.value

    if data.get("event_type") == "auth" and data.get("status") == "failed":
        user = data.get("user", "unknown")
        failed_attempts[user] += 1
        
        if failed_attempts[user] >= 3:
            print(f"[CORRELATED ALERT] Brute force suspected for user: {user}")
            failed_attempts[user] = 0
