def extract_and_interpret_fat_data(hex_string):
    """
    Извлекает и интерпретирует определенные значения из шестнадцатеричной строки,
    переставляет байты для двухбайтовых значений и возвращает их в виде словаря
    с шестнадцатеричным, десятичным представлением и описательными названиями.

    Args:
        hex_string (str): Входная строка, содержащая шестнадцатеричные данные.

    Returns:
        dict: Словарь с извлеченными и интерпретированными значениями.
    """
    # Удаляем заголовок, смещения и ASCII-представление, оставляем только шестнадцатеричные данные
    lines = hex_string.strip().split('\n')
    hex_data = ""
    for line in lines:
        # Пропускаем строку заголовка
        if "offset" in line:
            continue
        # Отделяем шестнадцатеричные данные от смещения и ASCII-представления
        parts = line.split('|')
        if len(parts) > 0:
            # Удаляем пробелы и смещение (первые 8 символов)
            hex_data += parts[0][9:].replace(" ", "")

    # Преобразуем шестнадцатеричную строку в список целых чисел (байтов)
    bytes_list = []
    for i in range(0, len(hex_data), 2):
        bytes_list.append(int(hex_data[i:i+2], 16))

    extracted_values = {}

    # Определяем, какие названия использовать для каждого "единого целого"
    # Ключи словаря соответствуют номерам "единых целых"
    value_names = {
        2: "Размер сектора",
        3: "Количество секторов в кластере",
        4: "Количество зарезервированных секторов",
        5: "Количество FAT-таблиц",
        6: "Размер корневой директории",
        7: "Размер одной FAT-таблицы"
    }

    # Определяем единицы измерения для каждого "единого целого"
    units = {
        2: "байт",
        3: "сектор",
        4: "секторов",
        5: "штуки",
        6: "байт",
        7: "секторов"
    }

    counter = 2 # Начинаем счетчик "единых целых" с 2

    # Извлечение данных начиная с 00000000
    # Размер сектора (Единое целое 2), индексы 11 и 12
    byte_1 = bytes_list[11]
    byte_2 = bytes_list[12]
    swapped_value_2 = (byte_2 << 8) | byte_1
    extracted_values[f'{value_names[counter]}'] = \
        f"0x{swapped_value_2:04X} = {swapped_value_2} {units[counter]}"
    counter += 1
    
    # Количество секторов в кластере (Единое целое 3), индекс 13
    single_byte_value_3 = bytes_list[13]
    extracted_values[f'{value_names[counter]}'] = \
        f"0x{single_byte_value_3:02X} = {single_byte_value_3} {units[counter]}"
    counter += 1

    # Количество зарезервированных секторов (Единое целое 4), индексы 14 и 15
    byte_3 = bytes_list[14]
    byte_4 = bytes_list[15]
    swapped_value_4 = (byte_4 << 8) | byte_3
    extracted_values[f'{value_names[counter]}'] = \
        f"0x{swapped_value_4:04X} = {swapped_value_4} {units[counter]}"
    counter += 1

    # Извлечение данных начиная с 00000010 (т.е. со смещения 16 байтов от начала)
    offset_10_start_index = 16

    # Количество FAT-таблиц (Единое целое 5), индекс 0 относительно смещения
    single_byte_value_5 = bytes_list[offset_10_start_index + 0]
    extracted_values[f'{value_names[counter]}'] = \
        f"0x{single_byte_value_5:02X} = {single_byte_value_5} {units[counter]}"
    counter += 1

    # Размер корневой директории (Единое целое 6), индексы 1 и 2 относительно смещения
    byte_5 = bytes_list[offset_10_start_index + 1]
    byte_6 = bytes_list[offset_10_start_index + 2]
    swapped_value_6 = (byte_6 << 8) | byte_5
    extracted_values[f'{value_names[counter]}'] = \
        f"0x{swapped_value_6:04X} = {swapped_value_6} {units[counter]}"
    counter += 1

    # Размер одной FAT-таблицы (Единое целое 7), индексы 6 и 7 относительно смещения
    byte_7 = bytes_list[offset_10_start_index + 6]
    byte_8 = bytes_list[offset_10_start_index + 7]
    swapped_value_7 = (byte_8 << 8) | byte_7
    extracted_values[f'{value_names[counter]}'] = \
        f"0x{swapped_value_7:04X} = {swapped_value_7} {units[counter]}"
    counter += 1

    return extracted_values

hex_string = """
offset 00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
00000000 EB 3C 90 6D 6B 66 73 2E  66 61 74 00 02 01 07 00| ë<mkfs.fat.....
00000010 01 00 02 00 08 F8 06 00  10 00 02 00 00 00 00 00| .....ø..........
"""

result = extract_and_interpret_fat_data(hex_string)

for key, value in result.items():
    print(f"{key}: {value}")
