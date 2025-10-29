import paho.mqtt.client as mqtt
import json
import xml.etree.ElementTree as ET
from datetime import datetime
import socket
import threading
import time
import os

# Параметры подключения
HOST = "192.168.1.27"  # IP стенда
PORT = 1883
KEEPALIVE = 17

# Топики для WB-demo-kit v.3
SUB_TOPICS = {
    '/devices/wb-msw-v3_64/controls/Current Motion': 'motion',
    'devices/wb-msw-v3_64/controls/Temperature': 'temperature',
    '/devices/wb-map12e_35/controls/Ch 3 P L1': 'voltage'
}

JSON_LIST = []
JSON_DICT = {}
for value in SUB_TOPICS.values():
    JSON_DICT[value] = 0

# Флаги для управления
collector_running = False
client = None


# =============================================================================
# СБОРЩИК ДАННЫХ
# =============================================================================

def get_suitcase_number():
    """Получение номера чемодана (последние две цифры IP)"""
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip.split('.')[-1]
    except:
        return "27"  # Запасное значение


def on_connect(client, userdata, flags, rc):
    print("✅ Connected with result code " + str(rc))
    for topic in SUB_TOPICS.keys():
        client.subscribe(topic)
        print(f"📡 Subscribed to: {topic}")


def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    topic = msg.topic

    param_name = SUB_TOPICS[topic]
    JSON_DICT[param_name] = payload
    JSON_DICT['time'] = str(datetime.now())
    JSON_DICT['suitcase_number'] = get_suitcase_number()

    JSON_LIST.append(JSON_DICT.copy())

    print(f"📨 {topic}: {payload}")

    # Сохранение в JSON
    with open('data.json', 'w') as file:
        json.dump(JSON_LIST, file)

    # Сохранение в XML каждые 5 сообщений
    if len(JSON_LIST) % 5 == 0:
        save_to_xml()


def save_to_xml():
    """Сохранение последней записи в XML"""
    if JSON_LIST:
        data = JSON_LIST[-1]
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'sensor_data_{timestamp}.xml'

        root = ET.Element('sensor_data')
        for key, value in data.items():
            element = ET.SubElement(root, key)
            element.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        print(f"💾 Data saved to XML: {filename}")


def start_collector():
    """Запуск сборщика данных"""
    global collector_running, client

    if collector_running:
        print("⚠️  Сборщик уже запущен!")
        return

    print("🚀 Запуск сборщика MQTT данных...")
    collector_running = True

    def collector_thread():
        global client
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message

        try:
            client.connect(HOST, PORT, KEEPALIVE)
            client.loop_forever()
        except Exception as e:
            print(f"❌ Ошибка подключения: {e}")
            collector_running = False

    thread = threading.Thread(target=collector_thread, daemon=True)
    thread.start()
    print("✅ Сборщик запущен. Данные сохраняются в data.json")


def stop_collector():
    """Остановка сборщика данных"""
    global collector_running, client

    if client and collector_running:
        client.disconnect()
        collector_running = False
        print("🛑 Сборщик остановлен")
    else:
        print("⚠️  Сборщик не запущен")


# =============================================================================
# ПАРСЕР
# =============================================================================

def show_sensor_data():
    """Показать данные датчиков"""
    print("\n🔍 ДАННЫЕ ДАТЧИКОВ")
    print("=" * 50)

    try:
        if not os.path.exists('data.json'):
            print("❌ Файл data.json не найден")
            return

        with open('data.json', 'r', encoding='utf-8') as file:
            data_list = json.load(file)

        if not data_list:
            print("❌ Нет данных в файле")
            return

        print(f"📊 Всего записей: {len(data_list)}\n")

        # Показать последние 5 записей
        print("📋 ПОСЛЕДНИЕ ЗАПИСИ:")
        print("=" * 50)

        start_index = max(0, len(data_list) - 5)
        for i, data in enumerate(data_list[start_index:], start_index + 1):
            print(f"\n📄 Запись #{i}:")
            print(f"  🎯 Движение: {data.get('motion', 'N/A')}")
            print(f"  🌡️  Температура: {data.get('temperature', 'N/A')}")
            print(f"  ⚡ Напряжение: {data.get('voltage', 'N/A')}")
            print(f"  🕒 Время: {data.get('time', 'N/A')}")
            print(f"  🧳 Чемодан: {data.get('suitcase_number', 'N/A')}")
            print("-" * 30)

    except Exception as e:
        print(f"❌ Ошибка чтения данных: {e}")


def show_last_record():
    """Показать только последнюю запись"""
    print("\n🎯 ПОСЛЕДНЯЯ ЗАПИСЬ")
    print("=" * 40)

    try:
        if not os.path.exists('data.json'):
            print("❌ Файл data.json не найден")
            return

        with open('data.json', 'r', encoding='utf-8') as file:
            data_list = json.load(file)

        if data_list:
            data = data_list[-1]
            print(f"🎯 Движение: {data.get('motion', 'N/A')}")
            print(f"🌡️  Температура: {data.get('temperature', 'N/A')}")
            print(f"⚡ Напряжение: {data.get('voltage', 'N/A')}")
            print(f"🕒 Время: {data.get('time', 'N/A')}")
            print(f"🧳 Чемодан: {data.get('suitcase_number', 'N/A')}")
        else:
            print("❌ Нет данных")

    except Exception as e:
        print(f"❌ Ошибка: {e}")


def show_statistics():
    """Показать простую статистику"""
    print("\n📈 СТАТИСТИКА")
    print("=" * 40)

    try:
        if not os.path.exists('data.json'):
            print("❌ Файл data.json не найден")
            return

        with open('data.json', 'r', encoding='utf-8') as file:
            data_list = json.load(file)

        if not data_list:
            print("❌ Нет данных")
            return

        print(f"📊 Всего записей: {len(data_list)}")

        # Статистика по движению
        motion_count = sum(1 for data in data_list if data.get('motion') == '1')
        print(f"🎯 Движение обнаружено: {motion_count} раз")

        # Последние значения
        if data_list:
            last = data_list[-1]
            print(f"🌡️  Текущая температура: {last.get('temperature', 'N/A')}")
            print(f"⚡ Текущее напряжение: {last.get('voltage', 'N/A')}")

    except Exception as e:
        print(f"❌ Ошибка: {e}")


def show_xml_files():
    """Показать созданные XML файлы"""
    print("\n📁 XML ФАЙЛЫ")
    print("=" * 40)

    xml_files = [f for f in os.listdir('.') if f.startswith('sensor_data_') and f.endswith('.xml')]

    if not xml_files:
        print("❌ XML файлы не найдены")
        return

    print(f"📄 Найдено XML файлов: {len(xml_files)}")
    for xml_file in sorted(xml_files):
        print(f"  📋 {xml_file}")


# =============================================================================
# ГЛАВНОЕ МЕНЮ
# =============================================================================

def show_menu():
    """Показать главное меню"""
    print("\n" + "=" * 60)
    print("           🚀 WB-DEMO-KIT v.3 - СБОРЩИК И ПАРСЕР")
    print("=" * 60)
    print("📡 УПРАВЛЕНИЕ СБОРЩИКОМ:")
    print("  1 - Запустить сборщик данных")
    print("  2 - Остановить сборщик данных")
    print("  3 - Статус сборщика")
    print("\n🔍 ПРОСМОТР ДАННЫХ:")
    print("  4 - Показать все данные")
    print("  5 - Показать последнюю запись")
    print("  6 - Статистика")
    print("  7 - Список XML файлов")
    print("\n  0 - Выход")
    print("-" * 60)


def main():
    """Основная функция программы"""
    print("🚀 WB-Demo-Kit v.3 - Система мониторинга")
    print("💡 Сборщик данных + Парсер в одной программе")

    while True:
        show_menu()
        choice = input("Выберите действие (0-7): ").strip()

        if choice == "1":
            start_collector()
        elif choice == "2":
            stop_collector()
        elif choice == "3":
            status = "✅ Запущен" if collector_running else "❌ Остановлен"
            print(f"📊 Статус сборщика: {status}")
            if os.path.exists('data.json'):
                try:
                    with open('data.json', 'r') as f:
                        data = json.load(f)
                    print(f"📁 Записей в файле: {len(data)}")
                except:
                    print("📁 Файл данных: есть (ошибка чтения)")
            else:
                print("📁 Файл данных: отсутствует")
        elif choice == "4":
            show_sensor_data()
        elif choice == "5":
            show_last_record()
        elif choice == "6":
            show_statistics()
        elif choice == "7":
            show_xml_files()
        elif choice == "0":
            print("👋 Выход из программы...")
            stop_collector()
            break
        else:
            print("❌ Неверный выбор, попробуйте снова")

        input("\n↵ Нажмите Enter для продолжения...")


if __name__ == "__main__":
    main()