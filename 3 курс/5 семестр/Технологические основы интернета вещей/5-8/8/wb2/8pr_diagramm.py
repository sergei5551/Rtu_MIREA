import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Используем бэкенд который не требует GUI
plt.switch_backend("Agg")


def save_visualizations():
    try:
        print("Загрузка данных...")

        # Читаем данные
        df = pd.read_csv(
            "data.csv",
            sep=",",
            skip_blank_lines=True,
            engine="python",
            on_bad_lines="skip",
            header=None,
            skiprows=1,
        )

        df.columns = ["timestamp", "sound", "co2", "voltage", "case_no"]

        # Обрабатываем числовые данные
        df["sound"] = pd.to_numeric(df["sound"], errors="coerce")
        df["co2"] = pd.to_numeric(df["co2"], errors="coerce")
        df["voltage"] = pd.to_numeric(df["voltage"], errors="coerce")

        print(f"Данные загружены: {len(df)} строк")
        print(f"Звук: {df['sound'].count()} записей")
        print(f"CO2: {df['co2'].count()} записей")
        print(f"Напряжение: {df['voltage'].count()} записей")

        # Создаем папку для графиков
        os.makedirs("graphs", exist_ok=True)
        print("Создана папка 'graphs'")

        # 1. ГИСТОГРАММА ЗВУКА
        plt.figure(figsize=(10, 6))
        sound_data = df["sound"].dropna()
        if len(sound_data) > 0:
            plt.hist(
                sound_data, bins=15, color="lightblue", edgecolor="black", alpha=0.7
            )
            plt.title(
                "Гистограмма показаний датчика звука", fontsize=14, fontweight="bold"
            )
            plt.xlabel("Уровень звука", fontsize=12)
            plt.ylabel("Частота", fontsize=12)
            plt.grid(True, alpha=0.3)
        else:
            plt.text(
                0.5, 0.5, "Нет данных по звуку", ha="center", va="center", fontsize=16
            )
            plt.title("Гистограмма звука")

        plt.tight_layout()
        plt.savefig("graphs/sound_histogram.png", dpi=150, bbox_inches="tight")
        print("✓ Сохранен graphs/sound_histogram.png")
        plt.close()

        # 2. ЛИНЕЙНЫЙ ГРАФИК CO2
        plt.figure(figsize=(12, 6))
        co2_data = df["co2"].dropna()
        if len(co2_data) > 0:
            plt.plot(
                co2_data.values, color="green", marker="o", markersize=2, linewidth=1
            )
            plt.title("Показания датчика CO2", fontsize=14, fontweight="bold")
            plt.xlabel("Номер измерения", fontsize=12)
            plt.ylabel("Уровень CO2 (ppm)", fontsize=12)
            plt.grid(True, alpha=0.3)
        else:
            plt.text(
                0.5, 0.5, "Нет данных по CO2", ha="center", va="center", fontsize=16
            )
            plt.title("Показания CO2")

        plt.tight_layout()
        plt.savefig("graphs/co2_timeline.png", dpi=150, bbox_inches="tight")
        print("✓ Сохранен graphs/co2_timeline.png")
        plt.close()

        # 3. КРУГОВАЯ ДИАГРАММА НАПРЯЖЕНИЯ
        plt.figure(figsize=(10, 8))
        voltage_data = df["voltage"].dropna()
        if len(voltage_data) > 0:
            # Создаем диапазоны
            ranges = pd.cut(
                voltage_data,
                bins=[0, 10, 15, 20, 25, 30],
                labels=["0-10V", "10-15V", "15-20V", "20-25V", "25-30V"],
            )
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
            else:
                plt.text(
                    0.5,
                    0.5,
                    "Нет валидных данных",
                    ha="center",
                    va="center",
                    fontsize=16,
                )
                plt.title("Напряжение")
        else:
            plt.text(
                0.5,
                0.5,
                "Нет данных по напряжению",
                ha="center",
                va="center",
                fontsize=16,
            )
            plt.title("Напряжение")

        plt.tight_layout()
        plt.savefig("graphs/voltage_pie.png", dpi=150, bbox_inches="tight")
        print("✓ Сохранен graphs/voltage_pie.png")
        plt.close()

        # 4. ОБЩИЙ СТАТИСТИЧЕСКИЙ ГРАФИК
        plt.figure(figsize=(12, 8))

        # Звук
        plt.subplot(2, 2, 1)
        if len(sound_data) > 0:
            plt.hist(sound_data, bins=10, color="lightblue", alpha=0.7)
            plt.title("Распределение звука")
            plt.xlabel("Уровень звука")
            plt.ylabel("Частота")

        # CO2
        plt.subplot(2, 2, 2)
        if len(co2_data) > 0:
            plt.plot(co2_data.values, color="green", alpha=0.7)
            plt.title("Показания CO2")
            plt.xlabel("Измерения")
            plt.ylabel("Уровень CO2")

        # Напряжение
        plt.subplot(2, 2, 3)
        if len(voltage_data) > 0:
            voltage_data.hist(bins=15, color="orange", alpha=0.7)
            plt.title("Распределение напряжения")
            plt.xlabel("Напряжение")
            plt.ylabel("Частота")

        # Статистика
        plt.subplot(2, 2, 4)
        stats_text = "СТАТИСТИКА:\n\n"
        if len(sound_data) > 0:
            stats_text += f"Звук: {len(sound_data)} зап.\n"
        if len(co2_data) > 0:
            stats_text += f"CO2: {len(co2_data)} зап.\n"
        if len(voltage_data) > 0:
            stats_text += f"Напряжение: {len(voltage_data)} зап."

        plt.text(0.1, 0.5, stats_text, fontsize=12, verticalalignment="center")
        plt.axis("off")
        plt.title("Общая статистика")

        plt.tight_layout()
        plt.savefig("graphs/summary.png", dpi=150, bbox_inches="tight")
        print("✓ Сохранен graphs/summary.png")
        plt.close()

        print("\nВСЕ ГРАФИКИ СОХРАНЕНЫ!")
        print("Папка 'graphs' содержит:")
        print("   - sound_histogram.png (гистограмма звука)")
        print("   - co2_timeline.png (линейный график CO2)")
        print("   - voltage_pie.png (круговая диаграмма напряжения)")
        print("   - summary.png (сводный график)")

        # Проверяем что файлы создались
        print(f"\nПроверка файлов:")
        for file in [
            "sound_histogram.png",
            "co2_timeline.png",
            "voltage_pie.png",
            "summary.png",
        ]:
            path = f"graphs/{file}"
            if os.path.exists(path):
                size = os.path.getsize(path)
                print(f"   ✓ {file} ({size} bytes)")
            else:
                print(f"   ✗ {file} - НЕ СОЗДАН!")

    except Exception as e:
        print(f"❌ Ошибка: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    save_visualizations()
