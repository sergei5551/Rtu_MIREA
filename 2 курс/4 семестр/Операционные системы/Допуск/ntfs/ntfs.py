def extract_ntfs_data(hex_string):
    """
    Извлекает и интерпретирует определенные значения из шестнадцатеричной строки
    для анализа структуры NTFS.

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

    # --- Извлечение данных относительно 00000000 ---

    # Размер одного сектора в байтах (12-я и 13-я пары, индексы 11 и 12)
    # Это двухбайтовое значение, переставляем байты
    byte_sector_size_low = bytes_list[11] # Младший байт (0x02)
    byte_sector_size_high = bytes_list[12] # Старший байт (0x04)
    sector_size = (byte_sector_size_high << 8) | byte_sector_size_low # Результат 0x0402
    extracted_values['Размер одного сектора в байтах'] = f"0x{sector_size:04X} = {sector_size} байт"

    # Количество секторов в одном кластере (14-я пара, индекс 13)
    # Это однобайтовое значение
    sectors_per_cluster = bytes_list[13] # 0x00
    extracted_values['Количество секторов в одном кластере'] = f"0x{sectors_per_cluster:02X} = {sectors_per_cluster} секторов"
    
    # --- Извлечение данных относительно 00000030 ---

    # Смещение до MFT-таблицы в кластерах (первая пара, индекс 0 относительно 00000030)
    # Смещение 0x30 соответствует индексу 0x30 = 48 в bytes_list
    mft_offset_index = 0x30 # 48
    mft_offset = bytes_list[mft_offset_index] # 0x08
    extracted_values['Смещение до MFT-таблицы в кластерах'] = f"0x{mft_offset:02X} = {mft_offset} кластеров"

    return extracted_values

hex_string = """
offset 00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
00000000 EB 52 90 4E 54 46 53 20  20 20 20 00 02 04 00 00| ëRNTFS    .....
00000010 00 00 00 00 00 F8 00 00  00 00 00 00 00 00 00 00| .....ø..........
00000020 00 00 00 00 80 00 80 00  DB 39 01 00 00 00 00 00| ......Û9......
00000030 08 00 00 00 00 00 00 00  3B 27 00 00 00 00 00 00| ........;'......
"""

result = extract_ntfs_data(hex_string)

for key, value in result.items():
    print(f"{key}: {value}")
