🛡️ Mini SIEM Lab

Un laboratorio de SIEM (Security Information and Event Management) construido desde cero con Python, Kafka, OpenSearch y Docker.
Este proyecto simula el flujo real de un SOC: ingestión de eventos, detección de amenazas, correlación y respuesta automática.

🚀 Funcionalidades

✅ Generación de eventos de seguridad en tiempo real
✅ Apache Kafka como sistema de mensajería
✅ OpenSearch para indexación y búsquedas
✅ OpenSearch Dashboards para visualización
✅ Detección de ataques de fuerza bruta
✅ Motor de correlación de eventos
✅ Almacenamiento forense con MinIO
✅ Motor de respuesta automática (bloqueo simulado de IPs)

🧱 Arquitectura

Generador de Eventos → Kafka → Motor de Detección → Motor de Correlación
                                  ↓
                             OpenSearch
                                  ↓
                      OpenSearch Dashboards

      Almacenamiento Forense → MinIO
      Respuesta Automática → Motor de Bloqueo

🛠️ Tecnologías Utilizadas

Python 3.x

Apache Kafka

OpenSearch

OpenSearch Dashboards

MinIO

Docker & Docker Compose

⚙️ Instalación y Ejecución

# Clonar repositorio
git clone https://github.com/JPVS-lab/mini-siem-lab.git
cd mini-siem-lab

# Levantar contenedores
docker compose up -d

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Ejecutar componentes
python generators/event_generator.py
python detection/detection_engine.py
python correlation/correlation_engine.py
python response/auto_block.py


🎯 Objetivos del Proyecto

Este laboratorio fue creado para:

Comprender la arquitectura de un SIEM real

Practicar procesamiento de logs de seguridad

Aprender Kafka y OpenSearch

Simular el trabajo de un SOC

Mostrar habilidades en ciberseguridad y DevSecOps

📌 Autor

Desarrollado por JPVS-lab
GitHub: https://github.com/JPVS-lab

## Disclamer
Proyecto educativo y de laboratorio
# mini-siem-lab
# mini-siem-lab
