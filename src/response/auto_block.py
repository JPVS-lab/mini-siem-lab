import time
from datetime import datetime

ALERT_LOG = "alerts.log"

def block_ip(ip):
    with open(ALERT_LOG, "a") as f:
        f.write(f"[{datetime.utcnow()}] IP blocked: {ip}\n")
    print(f"[ACTION] Blocked IP: {ip}")

if __name__ == "__main__":
    print("[*] Auto-response engine running...")

    # Simulación
    while True:
        fake_attacker_ip = "192.168.1.10"
        block_ip(fake_attacker_ip)
        time.sleep(30)
