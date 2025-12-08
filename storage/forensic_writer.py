import json
from kafka import KafkaConsumer
from minio import Minio
from datetime import datetime

minio_client = Minio(
    "localhost:9000",
    access_key="minio",
    secret_key="minio123",
    secure=False
)

BUCKET = "forensics"

if not minio_client.bucket_exists(BUCKET):
    minio_client.make_bucket(BUCKET)

consumer = KafkaConsumer(
    "siem-events",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

print("[*] Forensic writer running...")

for message in consumer:
    event = message.value
    filename = f"{datetime.utcnow().isoformat()}.json"

    with open("/tmp/event.json", "w") as f:
        f.write(json.dumps(event))

    minio_client.fput_object(
        BUCKET,
        filename,
        "/tmp/event.json"
    )
