🛡️ Mini SIEM Lab

A lightweight Security Information and Event Management (SIEM) lab built with Python, Kafka, OpenSearch and Docker.
This project simulates real-time security event ingestion, threat detection, correlation, and automated response in a lab environment.

🚀 Features

✅ Real-time event generation and ingestion
✅ Apache Kafka for streaming security logs
✅ OpenSearch for indexing and search
✅ OpenSearch Dashboards for visualization
✅ Brute-force detection using alert monitors
✅ Event correlation engine
✅ Forensic evidence storage using MinIO
✅ Automated response engine (IP blocking simulation)

🧱 Architecture

Event Generator → Kafka → Detection Engine → Correlation Engine
                               ↓
                        OpenSearch
                               ↓
                     OpenSearch Dashboards

        Forensic Storage → MinIO
        Automated Response → Auto Block Engine


🛠️ Tech Stack

Python 3.x

Apache Kafka

OpenSearch

OpenSearch Dashboards

MinIO

Docker & Docker Compose

# Clone repo
git clone https://github.com/JPVS-lab/mini-siem-lab.git
cd mini-siem-lab

# Start containers
docker compose up -d

# Create virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run components
python generators/event_generator.py
python detection/detection_engine.py
python correlation/correlation_engine.py
python response/auto_block.py

🎯 Project Goals

This project was built to:

Understand SIEM architectures

Practice security log processing

Learn Kafka and OpenSearch

Simulate SOC workflows

Showcase cybersecurity and DevSecOps skills

📌 Author

Built by JPVS-lab
GitHub: https://github.com/JPVS-lab

## Disclamer
Proyecto educativo y de laboratorio
# mini-siem-lab
# mini-siem-lab
