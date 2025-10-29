from collections import Counter


# Функция для подсчета биграмм
def get_bigrams(text):
    bigrams = [text[i : i + 2] for i in range(len(text) - 1)]
    return bigrams


# Функция для подсчета триграмм
def get_trigrams(text):
    trigrams = [text[i : i + 3] for i in range(len(text) - 2)]
    return trigrams


# Анализ биграмм
def analyze_bigrams(text):
    bigrams = get_bigrams(text)
    bigram_counts = Counter(bigrams)
    return bigram_counts


# Анализ триграмм
def analyze_trigrams(text):
    trigrams = get_trigrams(text)
    trigram_counts = Counter(trigrams)
    return trigram_counts


strng = """
КНМЫН ЧШАЕЦ ЯЯВЦА НКЩНФ ПЯВНД НОЦЫЛ ЦЯЛЦЯ ЛЦЫШЯ ФЦКЦФ РЧЦНЩ ШЯЦЫН ЩЬЛБЭ РЫНДН АЩЛВН ЛНЕЬШ
ЩНЧРЯ ЛШФША НФШЕН КЦЫЫЬ РЧНАД ШКНЯН ИЬРТС ШЭВШШ ЩНМЯН РМШЫШ ФШУВБ ЯЛЕНШ ЯЛКЦЧ АЩЛЯН АМЦГС
ШЧЩНФ ЫБГШФ ФГАШГ ЕРЦФП ЫНЯЛШ ЛЭВЩН ВЦАЬК ЦТЯКН ГБЯЛЦ ЫНКВБ ДНЯЛГ АЩЛБЭ РЫЬШД НКНЕШ ЛХЛНШ
УЯБМП ИЦАЩЛ ШУЧШЕ АЩЛШУ ИЬЛШР КЯРАЩ ЛЭЛНН ЫШЧНД БЛМНЯ ЛШДЫБ ЛПШЩН АЫЦЛП ЛЭВЛЦ ЧЫЦУН МТЛЯТ
ЯЩРЖШ ЦФПЫЬ РФРЫЛ ЬЯАЦЩ ШЯЦЫЫ ЬЧШЫЦ ЫШУХФ РВЛЕШ ЭРЯВШ ЧШШЧЩ БФПЯЦ ЧШНЫШ ЯННЛК РЛЯЛК БГЛЛР
ЧЯЛЦШ ФШМКБ ЧЯЛЦЧ ЧШФФШ ЦЕМЦЧ ТКФРЫ ШШАЩЛ ЯВЦВШ ЧШЧНЮ РЛЯЛН ФВЫБЛ ПЯТЭР ФНКРВ КЫЦШИ НФРРИ
НДЦЛН ШКЩРЭ ЦЛФРЫ ШТЧШЮ ШАЫШЛ ЭВРЯФ ШИКЬЩ НМЫТФ ШВЕЬЗ ВБИЦЕ ЦИЦЫЦ АЩЛЛН БКШМР ФШИЬЛ НФПВН
ИФРЯЛ ТСШРФ РЫЛЬА ШЛЩНВ ЕЬЛЬР ИРФЬЧ ШАШДА ЦДЦЧШ АШЛЯФ НКЫНЫ ЦЛРВЦ ЧШЩФР ЯРЫШЫ ЦЖРФФ БФНШМ
РАЩЛЫ НХЛНА ЫНШЫЬ РЫНЭШ ГДЦШЕ НВНЛК НФЫАЩ ЛХЛНЛ РФЦАК РЕРШШ ДЕНУН ЛЩЦФП ИБАЩЛ ХЛНЩН УНЕНЫ
ЫШЩПТ ЫВШАЩ ЛКВБЯ ТИФНВ ШДЕБЗ АЩЛЯЫ РЮЫЬР ЧРЛРФ ШАЩЛК РЭРЕЦ АЩЛЩЕ НКРМР ЫЫЬРК ЯРЧРШ ЫНЧВЕ
БДББЩ ЬФЦГС РДНВЦ ЧШЫЦА ЩЛШВЕ ШВШЫЦ ЩЦФБИ РЛНЫБ СРДНВ НЕЦИФ ТАЩЛШ ДНЕЫЬ РКРЕЗ ШЫЬАЩ ЛШВФЦ
МИШСЦ АЩЛШИ ЕРМНК ЬРДЦФ ФГЖШЫ ЦЖШШЛ ЦЧКРЯ ПЧШЕЛ ЭВ
"""
azbuk = dict()
new_string = str()
for char in strng:
    if char == " " or char == "\n":
        continue
    new_string += char
    if char in azbuk:
        azbuk[char] += 1
    else:
        azbuk[char] = 1

for char, count in sorted(
    azbuk.items(), key=lambda x: x[1], reverse=True
):  # Вывод частоты букв
    print(f"{char} - {count}")

new_string = new_string.replace("ЛЭВ", ".").replace("АЩЛ", ",")
# Подсчитаем биграммы и триграммы
bigrams = analyze_bigrams(new_string)
trigrams = analyze_trigrams(new_string)
print(new_string)
# Выводим самые частые биграммы и триграммы
print("Самые частые биграммы:")
for bigram, count in bigrams.most_common(10):
    print(f"{bigram}: {count}")

print("\nСамые частые триграммы:")
for trigram, count in trigrams.most_common(10):
    print(f"{trigram}: {count}")
chars_need_change = {
    "Л": "т",  # +
    "Э": "ч",  # +
    "В": "к",  # +
    "А": "з",  # +
    "Щ": "п",  # +
    "Н": "о",
    "П": "ь",
    "Ф": "л",
    "Ш": "е",
    "Е": "р",
    "Ь": "ы",
    "Я": "с",
    "Д": "г",
    "Р": "и",
    "Ц": "а",
    "Ы": "б",
    "О": "ф",  # +
}
for i in new_string:
    if i in chars_need_change:
        new_string = new_string.replace(i, chars_need_change[i])
print("\nРезультат после подстановки символов:")
print(new_string, end="\n\n")
