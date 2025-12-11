# Ingest Module

Este módulo se encarga de:
- Consumir logs desde Kafka.
- Parsearlos (JSON, texto plano, syslog simulado).
- Normalizarlos al formato común del SIEM.
- Enviarlos a la capa de detección.

Archivos típicos:
- consumer.py
- parser.py
- normalizer.py

Objetivo:
Garantizar que todos los eventos entren al SIEM con un formato consistente.

