import paho.mqtt.client as mqtt
import json
import xml.etree.ElementTree as ET
from datetime import datetime
import threading
import os

# Параметры подключения к MQTT-брокеру
HOST = "192.168.1.17"
PORT = 1883
KEEPALIVE = 17

# Словарь с топиками и собираемыми из них параметрами
SUB_TOPICS = {
    '/devices/wb-map12e_23/controls/Ch 1 P L2': 'power',
    '/devices/wb-msw-v3_21/controls/Current Motion': 'motion',
    '/devices/wb-ms_11/controls/Temperature': 'temperature',
    '/devices/wb-msw-v3_21/controls/Sound Level': 'sound'
}

# Глобальные переменные
JSON_LIST = []
JSON_DICT = {}
for value in SUB_TOPICS.values():
    JSON_DICT[value] = 0

# Флаги для управления потоками
collector_running = False
client = None


# =============================================================================
# ЧАСТЬ 1: СБОРЩИК ДАННЫХ (ваш оригинальный код + улучшения)
# =============================================================================

def on_connect(client, userdata, flags, rc):
    """Функция, вызываемая при подключении к брокеру"""
    print("✅ Connected with result code " + str(rc))
    for topic in SUB_TOPICS.keys():
        client.subscribe(topic)
        print(f"📡 Subscribed to: {topic}")


def on_message(client, userdata, msg):
    """Функция, вызываемая при получении сообщения от брокера"""
    payload = msg.payload.decode()
    topic = msg.topic

    param_name = SUB_TOPICS[topic]
    JSON_DICT[param_name] = payload
    JSON_DICT['time'] = str(datetime.now())

    JSON_LIST.append(JSON_DICT.copy())

    print(f"📨 {topic}: {payload}")

    # Автосохранение при каждом сообщении (как в вашем коде)
    with open('data.json', 'w') as file:
        json_string = json.dumps(JSON_LIST)
        file.write(json_string)


def start_collector():
    """Запуск сборщика данных в отдельном потоке"""
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

    if client:
        client.disconnect()
        collector_running = False
        print("🛑 Сборщик остановлен")
    else:
        print("⚠️  Сборщик не запущен")


# =============================================================================
# ЧАСТЬ 2: ПАРСЕР ДАННЫХ
# =============================================================================

def parse_all_data():
    """Парсинг всех данных из JSON файла"""
    print("\n🔍 ПАРСИНГ ВСЕХ ДАННЫХ")
    print("=" * 60)

    try:
        with open('data.json', 'r', encoding='utf-8') as file:
            data_list = json.load(file)

        if not data_list:
            print("❌ Файл пуст или не содержит данных")
            return

        print(f"📊 Найдено записей: {len(data_list)}")
        print("=" * 60)

        for i, data in enumerate(data_list, 1):
            print(f"\n📄 Запись #{i}")
            print("-" * 40)
            display_sensor_data(data)

    except FileNotFoundError:
        print("❌ Файл data.json не найден")
    except Exception as e:
        print(f"❌ Ошибка: {e}")


def parse_last_record():
    """Парсинг последней записи"""
    print("\n🎯 ПОСЛЕДНЯЯ ЗАПИСЬ")
    print("=" * 50)

    try:
        with open('data.json', 'r', encoding='utf-8') as file:
            data_list = json.load(file)

        if data_list:
            display_sensor_data(data_list[-1])
        else:
            print("❌ Нет данных")
    except FileNotFoundError:
        print("❌ Файл data.json не найден")
    except Exception as e:
        print(f"❌ Ошибка: {e}")


def display_sensor_data(data):
    """Отображение данных датчиков"""
    print(f"⚡ Потребляемая мощность: {data.get('power', 'N/A')}")
    print(f"🎯 Датчик движения: {data.get('motion', 'N/A')}")
    print(f"🌡️  Датчик температуры: {data.get('temperature', 'N/A')}")
    print(f"🔊 Уровень звука: {data.get('sound', 'N/A')}")
    print(f"🕒 Время записи: {data.get('time', 'N/A')}")
    print("-" * 40)


def export_to_xml():
    """Экспорт данных в XML"""
    try:
        with open('data.json', 'r', encoding='utf-8') as file:
            data_list = json.load(file)

        if not data_list:
            print("❌ Нет данных для экспорта")
            return

        root = ET.Element('sensor_data_collection')

        for i, data in enumerate(data_list, 1):
            record_element = ET.SubElement(root, 'record', id=str(i))
            for key, value in data.items():
                field_element = ET.SubElement(record_element, key)
                field_element.text = str(value)

        xml_filename = f"sensor_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xml"
        tree = ET.ElementTree(root)
        tree.write(xml_filename, encoding='utf-8', xml_declaration=True)

        print(f"✅ Данные экспортированы в {xml_filename}")
        print(f"📊 Записей: {len(data_list)}")

    except Exception as e:
        print(f"❌ Ошибка экспорта: {e}")


def show_statistics():
    """Показать статистику по данным"""
    try:
        with open('data.json', 'r', encoding='utf-8') as file:
            data_list = json.load(file)

        if not data_list:
            print("❌ Нет данных для статистики")
            return

        print("\n📈 СТАТИСТИКА ДАННЫХ")
        print("=" * 40)
        print(f"📊 Всего записей: {len(data_list)}")

        if len(data_list) >= 2:
            first_time = data_list[0].get('time', '')
            last_time = data_list[-1].get('time', '')
            print(f"🕒 Первая запись: {first_time}")
            print(f"🕒 Последняя запись: {last_time}")

    except Exception as e:
        print(f"❌ Ошибка: {e}")


# =============================================================================
# ОСНОВНОЕ МЕНЮ И УПРАВЛЕНИЕ
# =============================================================================

def show_menu():
    """Отображение главного меню"""
    print("\n" + "=" * 60)
    print("           🚀 MQTT ДАТЧИКИ - СБОРЩИК И ПАРСЕР")
    print("=" * 60)
    print("📡 УПРАВЛЕНИЕ СБОРЩИКОМ:")
    print("  1 - Запустить сборщик данных")
    print("  2 - Остановить сборщик данных")
    print("  3 - Статус сборщика")
    print("\n🔍 РАБОТА С ДАННЫМИ:")
    print("  4 - Показать все данные")
    print("  5 - Показать последнюю запись")
    print("  6 - Экспорт в XML")
    print("  7 - Статистика")
    print("\n  0 - Выход")
    print("-" * 60)


def main():
    """Основная функция программы"""
    print("🚀 MQTT Система мониторинга датчиков")
    print("💡 Сборщик + Парсер в одной программе")

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
            parse_all_data()
        elif choice == "5":
            parse_last_record()
        elif choice == "6":
            export_to_xml()
        elif choice == "7":
            show_statistics()
        elif choice == "0":
            print("👋 Выход из программы...")
            stop_collector()
            break
        else:
            print("❌ Неверный выбор, попробуйте снова")

        input("\n↵ Нажмите Enter для продолжения...")


if __name__ == "__main__":
    main()