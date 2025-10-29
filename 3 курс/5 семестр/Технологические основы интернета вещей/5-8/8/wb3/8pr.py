import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json
import os

# Используем бэкенд который не требует GUI
plt.switch_backend("Agg")


def parse_json_data(filename):
    """Парсим JSON данные и преобразуем в DataFrame"""
    try:
        with open(filename, "r") as f:
            content = f.read().strip()

        # Если это не валидный JSON, попробуем почистить
        if not content.startswith("["):
            content = "[" + content + "]"

        # Заменяем проблемы с кавычками и форматом
        content = content.replace('"{', "{").replace('}"', "}")
        content = content.replace("'", '"')

        # Парсим JSON
        data = json.loads(content)
        print(f"✓ Успешно загружено {len(data)} записей")

        # Преобразуем в DataFrame
        records = []
        for item in data:
            if isinstance(item, dict):
                record = {}
                for key, value in item.items():
                    # Обрабатываем вложенные структуры если есть
                    if isinstance(value, dict):
                        record.update(value)
                    else:
                        record[key] = value
                records.append(record)

        df = pd.DataFrame(records)
        print(f"✓ Создан DataFrame с {len(df)} строками и {len(df.columns)} столбцами")
        print(f"✓ Столбцы: {list(df.columns)}")

        return df

    except json.JSONDecodeError as e:
        print(f"❌ Ошибка парсинга JSON: {e}")
        # Попробуем ручной парсинг
        return parse_manual(filename)
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return None


def parse_manual(filename):
    """Ручной парсинг если автоматический не сработал"""
    print("Пробуем ручной парсинг...")
    try:
        with open(filename, "r") as f:
            content = f.read()

        # Разбиваем по записям
        records = []
        lines = content.split("}, {")

        for line in lines:
            line = line.replace("{", "").replace("}", "").strip()
            if line:
                record = {}
                parts = line.split("\t\t")
                for i in range(0, len(parts) - 1, 2):
                    if i + 1 < len(parts):
                        key = parts[i].strip('"')
                        value = parts[i + 1].strip('"')
                        record[key] = value
                records.append(record)

        df = pd.DataFrame(records)
        print(f"✓ Ручной парсинг: {len(df)} записей")
        return df

    except Exception as e:
        print(f"❌ Ошибка ручного парсинга: {e}")
        return None


def clean_and_convert_data(df):
    """Очистка и преобразование данных"""
    # Переименовываем столбцы для удобства
    column_mapping = {
        "Temperature": "temperature",
        "CO2": "co2",
        "Voltage": "voltage",
        "time": "timestamp",
    }

    df = df.rename(columns=column_mapping)

    # Преобразуем числовые колонки
    numeric_columns = ["temperature", "co2", "voltage"]
    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
            print(f"✓ Обработан {col}: {df[col].count()} валидных значений")

    # Обрабатываем время
    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
        df = df.dropna(subset=["timestamp"])
        df = df.sort_values("timestamp")
        print(f"✓ Обработано время: {len(df)} записей с валидными timestamp")

    return df


def create_wb3_visualizations(df):
    """Создание визуализаций для WB3"""

    # Создаем папку для графиков
    os.makedirs("wb3_graphs", exist_ok=True)
    print("✓ Создана папка 'wb3_graphs'")

    # 1. ЛИНЕЙНЫЙ ГРАФИК ТЕМПЕРАТУРЫ (временной ряд)
    plt.figure(figsize=(12, 6))
    if "temperature" in df.columns and "timestamp" in df.columns:
        temp_data = df[["timestamp", "temperature"]].dropna()
        if len(temp_data) > 0:
            plt.plot(
                temp_data["timestamp"],
                temp_data["temperature"],
                color="red",
                linewidth=2,
                marker="o",
                markersize=3,
            )
            plt.title("Температура по времени", fontsize=14, fontweight="bold")
            plt.xlabel("Время", fontsize=12)
            plt.ylabel("Температура (°C)", fontsize=12)
            plt.xticks(rotation=45)
            plt.grid(True, alpha=0.3)

            # Добавляем статистику
            avg_temp = temp_data["temperature"].mean()
            plt.axhline(
                y=avg_temp,
                color="r",
                linestyle="--",
                alpha=0.7,
                label=f"Средняя: {avg_temp:.1f}°C",
            )
            plt.legend()
        else:
            plt.text(
                0.5,
                0.5,
                "Нет данных по температуре",
                ha="center",
                va="center",
                fontsize=16,
            )
            plt.title("Температура по времени")
    else:
        plt.text(
            0.5,
            0.5,
            "Нет данных времени или температуры",
            ha="center",
            va="center",
            fontsize=16,
        )
        plt.title("Температура по времени")

    plt.tight_layout()
    plt.savefig("wb3_graphs/temperature_timeline.png", dpi=150, bbox_inches="tight")
    print("✓ Сохранен wb3_graphs/temperature_timeline.png")
    plt.close()

    # 2. СТОЛБИКОВАЯ ДИАГРАММА CO2 (распределение)
    plt.figure(figsize=(10, 6))
    if "co2" in df.columns:
        co2_data = df["co2"].dropna()
        if len(co2_data) > 0:
            # Создаем диапазоны для CO2
            bins = np.arange(co2_data.min(), co2_data.max() + 50, 50)
            plt.hist(co2_data, bins=bins, color="green", alpha=0.7, edgecolor="black")
            plt.title("Распределение уровня CO2", fontsize=14, fontweight="bold")
            plt.xlabel("Уровень CO2 (ppm)", fontsize=12)
            plt.ylabel("Частота", fontsize=12)
            plt.grid(True, alpha=0.3)

            # Статистика
            stats_text = f"Мин: {co2_data.min():.0f}\nМакс: {co2_data.max():.0f}\nСреднее: {co2_data.mean():.0f}"
            plt.annotate(
                stats_text,
                xy=(0.7, 0.7),
                xycoords="axes fraction",
                bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8),
            )
        else:
            plt.text(
                0.5, 0.5, "Нет данных по CO2", ha="center", va="center", fontsize=16
            )
            plt.title("Распределение уровня CO2")
    else:
        plt.text(0.5, 0.5, "Нет данных CO2", ha="center", va="center", fontsize=16)
        plt.title("Распределение уровня CO2")

    plt.tight_layout()
    plt.savefig("wb3_graphs/co2_histogram.png", dpi=150, bbox_inches="tight")
    print("✓ Сохранен wb3_graphs/co2_histogram.png")
    plt.close()

    # 3. КРУГОВАЯ ДИАГРАММА НАПРЯЖЕНИЯ (диапазоны)
    plt.figure(figsize=(10, 8))
    if "voltage" in df.columns:
        voltage_data = df["voltage"].dropna()
        if len(voltage_data) > 0:
            # Создаем диапазоны для напряжения
            bins = [0, 2, 3, 4, 5, 10]
            labels = ["0-2V", "2-3V", "3-4V", "4-5V", "5-10V"]

            ranges = pd.cut(voltage_data, bins=bins, labels=labels)
            range_counts = ranges.value_counts()
            range_counts = range_counts[range_counts > 0]

            if len(range_counts) > 0:
                colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0"]
                plt.pie(
                    range_counts.values,
                    labels=range_counts.index,
                    autopct="%1.1f%%",
                    colors=colors[: len(range_counts)],
                    startangle=90,
                )
                plt.title(
                    "Распределение напряжения по диапазонам",
                    fontsize=14,
                    fontweight="bold",
                )

                # Статистика
                stats_text = f"Всего: {len(voltage_data)} изм.\nСреднее: {voltage_data.mean():.2f}V"
                plt.figtext(
                    0.02,
                    0.02,
                    stats_text,
                    fontsize=10,
                    bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray"),
                )
            else:
                plt.text(
                    0.5,
                    0.5,
                    "Нет валидных данных\nпо напряжению",
                    ha="center",
                    va="center",
                    fontsize=16,
                )
                plt.title("Распределение напряжения")
        else:
            plt.text(
                0.5,
                0.5,
                "Нет данных по напряжению",
                ha="center",
                va="center",
                fontsize=16,
            )
            plt.title("Распределение напряжения")
    else:
        plt.text(
            0.5, 0.5, "Нет данных напряжения", ha="center", va="center", fontsize=16
        )
        plt.title("Распределение напряжения")

    plt.tight_layout()
    plt.savefig("wb3_graphs/voltage_pie.png", dpi=150, bbox_inches="tight")
    print("✓ Сохранен wb3_graphs/voltage_pie.png")
    plt.close()

    # 4. СВОДНЫЙ ГРАФИК
    create_summary_plot(df)


def create_summary_plot(df):
    """Создание сводного графика всех данных WB3"""
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))

    # Данные
    temp_data = (
        df[["timestamp", "temperature"]].dropna()
        if "temperature" in df.columns and "timestamp" in df.columns
        else None
    )
    co2_data = df["co2"].dropna() if "co2" in df.columns else pd.Series()
    voltage_data = df["voltage"].dropna() if "voltage" in df.columns else pd.Series()

    # 1. Температура по времени (верхний левый)
    if temp_data is not None and len(temp_data) > 0:
        axes[0, 0].plot(
            temp_data["timestamp"], temp_data["temperature"], color="red", alpha=0.7
        )
        axes[0, 0].set_title("Температура по времени", fontweight="bold")
        axes[0, 0].set_xlabel("Время")
        axes[0, 0].set_ylabel("Температура (°C)")
        axes[0, 0].tick_params(axis="x", rotation=45)
        axes[0, 0].grid(True, alpha=0.3)

    # 2. Гистограмма CO2 (верхний правый)
    if len(co2_data) > 0:
        axes[0, 1].hist(co2_data, bins=15, color="green", alpha=0.7)
        axes[0, 1].set_title("Распределение CO2", fontweight="bold")
        axes[0, 1].set_xlabel("Уровень CO2 (ppm)")
        axes[0, 1].set_ylabel("Частота")
        axes[0, 1].grid(True, alpha=0.3)

    # 3. Круговая диаграмма напряжения (нижний левый)
    if len(voltage_data) > 0:
        ranges = pd.cut(voltage_data, bins=[0, 2, 3, 4, 5, 10])
        range_counts = ranges.value_counts()
        range_counts = range_counts[range_counts > 0]

        if len(range_counts) > 0:
            axes[1, 0].pie(
                range_counts.values, labels=range_counts.index, autopct="%1.1f%%"
            )
            axes[1, 0].set_title("Напряжение по диапазонам", fontweight="bold")

    # 4. Статистика (нижний правый)
    stats_text = "СТАТИСТИКА WB3:\n\n"
    if temp_data is not None and len(temp_data) > 0:
        stats_text += f"ТЕМПЕРАТУРА:\n- Измерений: {len(temp_data)}\n- Диапазон: {temp_data['temperature'].min():.1f}-{temp_data['temperature'].max():.1f}°C\n- Среднее: {temp_data['temperature'].mean():.1f}°C\n\n"
    if len(co2_data) > 0:
        stats_text += f"CO2:\n- Измерений: {len(co2_data)}\n- Диапазон: {co2_data.min():.0f}-{co2_data.max():.0f} ppm\n- Среднее: {co2_data.mean():.0f} ppm\n\n"
    if len(voltage_data) > 0:
        stats_text += f"НАПРЯЖЕНИЕ:\n- Измерений: {len(voltage_data)}\n- Диапазон: {voltage_data.min():.2f}-{voltage_data.max():.2f}V\n- Среднее: {voltage_data.mean():.2f}V"

    axes[1, 1].text(
        0.1,
        0.9,
        stats_text,
        transform=axes[1, 1].transAxes,
        fontsize=10,
        verticalalignment="top",
        bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.5),
    )
    axes[1, 1].set_title("Общая статистика", fontweight="bold")
    axes[1, 1].axis("off")

    plt.tight_layout()
    plt.savefig("wb3_graphs/wb3_summary.png", dpi=150, bbox_inches="tight")
    print("✓ Сохранен wb3_graphs/wb3_summary.png")
    plt.close()


def main():
    print("=== ВИЗУАЛИЗАЦИЯ ДАННЫХ WB3 ===")
    print("Датчики: Температура, CO2, Напряжение")
    print()

    # Загружаем и обрабатываем данные
    df = parse_json_data("data.json")

    if df is not None and len(df) > 0:
        print("\n✓ Данные загружены успешно!")
        print(f"Первые 3 записи:")
        print(df.head(3))

        # Очищаем данные
        df_clean = clean_and_convert_data(df)

        # Создаем визуализации
        print("\n=== СОЗДАНИЕ ВИЗУАЛИЗАЦИЙ ===")
        create_wb3_visualizations(df_clean)

        print("\n🎉 ВИЗУАЛИЗАЦИИ WB3 СОЗДАНЫ!")
        print("📁 Папка 'wb3_graphs' содержит:")
        print("   - temperature_timeline.png (линейный график температуры)")
        print("   - co2_histogram.png (гистограмма CO2)")
        print("   - voltage_pie.png (круговая диаграмма напряжения)")
        print("   - wb3_summary.png (сводный график)")

        # Проверяем файлы
        print(f"\nПроверка файлов:")
        for file in [
            "temperature_timeline.png",
            "co2_histogram.png",
            "voltage_pie.png",
            "wb3_summary.png",
        ]:
            path = f"wb3_graphs/{file}"
            if os.path.exists(path):
                size = os.path.getsize(path)
                print(f"   ✓ {file} ({size} bytes)")
            else:
                print(f"   ✗ {file} - НЕ СОЗДАН!")
    else:
        print("❌ Не удалось загрузить данные")


if __name__ == "__main__":
    main()
