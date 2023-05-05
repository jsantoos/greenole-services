from threading import Thread
import requests
import time
from .config import settings

WATCHDOG_INTERVAL = 60  # Verificar o status dos serviços a cada 60 segundos

SERVICES = [
    {"name": "Microservice", "url": "http://localhost:8000/health_check"},
    # Adicione outros serviços aqui, se necessário
]


def check_services_status():
    for service in SERVICES:
        try:
            response = requests.get(service["url"], timeout=5)
            if response.status_code != 200:
                send_discord_notification(
                    f"O serviço {service['name']} está fora do ar."
                )
        except requests.exceptions.RequestException:
            send_discord_notification(f"O serviço {service['name']} está fora do ar.")


def send_discord_notification(message: str):
    webhook_url = settings.DISCORD_WEBHOOK_URL
    payload = {"content": message}
    requests.post(webhook_url, json=payload)


def watchdog_loop():
    while True:
        check_services_status()
        time.sleep(WATCHDOG_INTERVAL)


def start():
    watchdog_thread = Thread(target=watchdog_loop)
    watchdog_thread.start()
