import json
from kafka import KafkaConsumer
from opensearchpy import OpenSearch
from datetime import datetime

# -----------------------------
# CONFIGURACIÓN
# -----------------------------
KAFKA_TOPIC = "raw-events"
KAFKA_BOOTSTRAP = "localhost:9092"   # usa kafka:9092 si lo corres dentro de docker
INDEX_NAME = "siem-events"

OPENSEARCH_HOST = "localhost"
OPENSEARCH_PORT = 9200
OPENSEARCH_USER = "admin"
OPENSEARCH_PASS = ".1973asdF"   # cambia si usaste otro password

# -----------------------------
# CLIENTE OPENSEARCH
# -----------------------------
client = OpenSearch(
    hosts=[{"host": OPENSEARCH_HOST, "port": OPENSEARCH_PORT}],
    http_auth=(OPENSEARCH_USER, OPENSEARCH_PASS),
    use_ssl=True,
    verify_certs=False,
    ssl_show_warn=False
)

# -----------------------------
# CREAR ÍNDICE SI NO EXISTE
# -----------------------------
if not client.indices.exists(index=INDEX_NAME):
    client.indices.create(
        index=INDEX_NAME,
        body={
            "mappings": {
                "properties": {
                    "@timestamp": {"type": "date"},
                    "event": {"type": "object"},
                    "host": {"type": "object"},
                    "user": {"type": "object"},
                    "source": {"type": "object"},
                    "destination": {"type": "object"},
                    "log": {"type": "object"}
                }
            }
        }
    )
    print(f"[+] Index '{INDEX_NAME}' created")

# -----------------------------
# CONSUMIDOR KAFKA
# -----------------------------
consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_BOOTSTRAP,
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    auto_offset_reset="latest",
    enable_auto_commit=True
)

print("[*] OpenSearch Ingestor running...")

# -----------------------------
# LOOP PRINCIPAL
# -----------------------------
for message in consumer:
    event = message.value

    # asegurar timestamp válido
    if "@timestamp" not in event:
        event["@timestamp"] = datetime.utcnow().isoformat() + "Z"

    try:
        client.index(index=INDEX_NAME, body=event)
        print(f"[+] Indexed event: {event.get('event', {}).get('id', 'no-id')}")
    except Exception as e:
        print(f"[!] Error indexing event: {str(e)}")
