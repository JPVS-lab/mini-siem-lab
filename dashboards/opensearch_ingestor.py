import json
from kafka import KafkaConsumer
from opensearchpy import OpenSearch

consumer = KafkaConsumer(
    "siem-events",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

client = OpenSearch(
    hosts=[{"host": "localhost", "port": 9200}],
    http_auth=("admin", "admin"),
    use_ssl=False
)

INDEX = "siem-events"

# Crear índice si no existe
if not client.indices.exists(index=INDEX):
    client.indices.create(index=INDEX)

print("[*] OpenSearch ingestor running...")

for message in consumer:
    event = message.value
    client.index(index=INDEX, body=event)

