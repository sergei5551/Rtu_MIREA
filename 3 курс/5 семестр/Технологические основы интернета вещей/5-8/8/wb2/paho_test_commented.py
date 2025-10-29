import paho.mqtt.client as mqtt
import json
from datetime import datetime
from time import sleep
import csv
import os

# Параметры подключения к MQTT-брокеру
HOST = "192.168.1.17"
PORT = 1883
KEEPALIVE = 17

# Словарь с топиками и собираемыми из них параметрами
SUB_TOPICS = {
    '/devices/wb-msw-v3_21/controls/Current Motion': 'motion',
    '/devices/wb-ms_11/controls/Temperature': 'temperature',
    '/devices/power_status/controls/Vin': 'volte'
}

CSV_FILE = 'data.csv'
CSV_HEADER = ['timestamp', 'motion', 'temperature', 'volte', 'case_no']

def on_connect(client, userdata, flags, rc, properties):
    print("Подключение установлено с кодом результата: " + str(rc))

    for topic in SUB_TOPICS.keys():
        client.subscribe(topic)
        print("Подписан на топик: " + topic)

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    topic = msg.topic

    param_name = SUB_TOPICS[topic]

    current_time = datetime.now()
    timestamp = current_time.strftime('%Y-%m-%d %H:%M:%S')

    # Инициализация строки с пустыми значениями
    row_data = {
        'timestamp': timestamp,
        'motion': '',
        'temperature': '',
        'volte': '',
        'case_no': HOST[-2:]  # Берем последние 2 символа IP-адреса как номер кейса
    }

    # Заполняем только тот параметр, который пришел
    row_data[param_name] = payload

    # Проверяем существование файла
    file_exists = os.path.isfile(CSV_FILE)

    # Записываем данные в CSV
    with open(CSV_FILE, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=CSV_HEADER)

        if not file_exists:
            writer.writeheader()

        writer.writerow(row_data)

    print("%s - %s: %s" % (timestamp, topic, payload))

def main():
    print("Запуск сбора данных на 10 минут...")
    print("Данные будут сохранены в файл: " + CSV_FILE)
    print("Собираемые параметры:")
    for topic, param in SUB_TOPICS.items():
        print(f"  - {param}: {topic}")

    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(HOST, PORT, KEEPALIVE)

    client.loop_start()

    try:
        # Сбор данных в течение 10 минут (600 секунд)
        sleep(600)
    except KeyboardInterrupt:
        print("Сбор данных прерван пользователем")

    client.loop_stop()
    print("Сбор данных завершен. Файл сохранен: " + CSV_FILE)

if __name__ == "__main__":
    main()