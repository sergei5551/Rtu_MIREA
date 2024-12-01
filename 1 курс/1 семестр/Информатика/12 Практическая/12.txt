import random # Добавление библиотеки для рандомных чисел


def sortir(): # Функция сортировки
    for i in range(len(matr)):
        for j in range(len(matr)):
            matr[i].sort(reverse=True)
        matr.sort(reverse=True)

def letter(): # Функция для добавления чисел
    for i in range(len(matr)):
        for j in range(len(matr)):
            if question == 1:
                matr[i].append(random.randint(1, 100))
            elif question == 2:
                letter_per = "a"
                while (type(letter_per) != int):
                    try:
                        letter_per = int(input("Число: "))
                    except:
                        print("Введенно не целое число!")

                matr[i].append(letter_per)


matr = [] # Создание матрицы
answer = question = 0
while not((2 <= answer <= 8) and (answer % 2 == 0) and (question == 1 or question == 2)):
    try: # Проверяет на наличие ошибок написании тип данных
        if (not((2 <= answer <= 8) and (answer % 2 == 0))):
            answer = int(input("Введите четное число матрицы MxM интервалом [2,8]: "))
        if not ((2 <= answer <= 8) and (answer % 2 == 0)):
            print("Неверно")
            continue
        question = int(input("1)Случайные числа \n2)Ввести самому \nВвод:"))
        if not (question == 1 or question == 2):
            print("Неверно")
            continue
    except: # Если выдает ошибку, заканчивает программу
        print("Введенно не целое число!")


for i in range(answer): # Создание столбцов для матрицы
    matr.append([])

letter() # Вызываем функцию для добавления элементов в матрицу
sortir() # Вызываем функцию, чтоб отсортировать матрицу по строкам и столбцам

for i in matr: # Вывод отсортированной матрицы
    print(i)

# Далее мы поменяем местами первую половину старших элементов
# с половиной младших (поменяем первых 3 столбца на последние три столбца)
infor = 0
for i in range(len(matr)):
    for j in range(len(matr[i])//2):
        infor = matr[i][j]
        matr[i][j] = matr[i][ (len(matr[i])//2) + j ]
        matr[i][ (len(matr[i])//2) + j ] = infor




print("\n")

for i in matr: # Вывод итоговой матрицы
    print(i)

o = input("Нажмите Enter для закрытия программы...") # Чтоб программа не вылетала в консоли
