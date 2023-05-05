import requests
import random
import time
from datetime import datetime, timedelta

NUM_DATA_POINTS = 5000
TIME_INTERVAL = 60  # 1 minuto
API_URL = "http://localhost:5000/sensor_data/"
VARIABLES = ["temperatura", "umidade", "pressao"]


def generate_sensor_data():
    sensor_data = {
        "sensor_id": random.randint(1, 100),
        "timestamp": (
            datetime.utcnow() - timedelta(seconds=random.randint(1, 3600))
        ).isoformat(),
        "variable": random.choice(VARIABLES),
        "value": random.uniform(0, 100),
        "unit": "unidade",
    }
    return sensor_data


def send_sensor_data(data):
    try:
        response = requests.post(API_URL, json=data, timeout=5)
        if response.status_code == 200:
            print("Dados enviados com sucesso")
        else:
            print(f"Erro ao enviar dados: {response.status_code}")
    except requests.exceptions.RequestException:
        print("Erro ao enviar dados: conexão falhou")


def main():
    start_time = time.time()
    data_points_sent = 0

    while data_points_sent < NUM_DATA_POINTS:
        sensor_data = generate_sensor_data()
        send_sensor_data(sensor_data)
        data_points_sent += 1

        elapsed_time = time.time() - start_time
        if elapsed_time < TIME_INTERVAL:
            time_to_finish = TIME_INTERVAL - elapsed_time
            sleep_time = time_to_finish / (NUM_DATA_POINTS - data_points_sent)
            time.sleep(sleep_time)


if __name__ == "__main__":
    main()
