from memory_profiler import profile
import time  # Для cProfile ошибок

class Matrix:
    def __init__(self, matrix_v=[], size="1x1"):
        self.matrix_v = matrix_v
        if len(matrix_v) > 0:
            self.size = f"{len(matrix_v)}x{len(matrix_v[0])}"
        else:
            self.size = size
        
        # Memory Profiler: Утечка через статическую переменную класса
        if not hasattr(Matrix, 'memory_leak_storage'):
            Matrix.memory_leak_storage = []
        Matrix.memory_leak_storage.append(self.matrix_v)

    @profile
    def change_element(self, index_row, index_col, element):
        if (index_row >= len(self.matrix_v) or
                index_col >= len(self.matrix_v[0])):
            raise IndexError(
                f"Индекс [{index_row}][{index_col}] "
                f"вне границ матрицы {self.size}"
            )
        self.matrix_v[index_row][index_col] = element

    @profile
    def create_matrix(self, size="3x3", matrixDefault=True) -> list:
        if not self._validate_size_format(size):
            raise ValueError(
                f"Неверный формат размера: {size}. Используйте формат 'NxM'"
            )

        self.size = size
        self.matrix_v = []

        # Memory Profiler: Избыточное копирование данных
        temp_lists = []
        for i in range(int(self.size[0])):
            matrix_prom = list()
            for j in range(int(self.size[2])):
                matrix_prom.append(1)
                temp_lists.append(matrix_prom[:])  # Лишнее копирование на каждой итерации
            self.matrix_v.append(matrix_prom)
        return self.matrix_v

    @staticmethod
    def _validate_size_format(size):
        return (
            len(size) == 3
            and size[1] == "x"
            and size[0].isdigit()
            and size[2].isdigit()
        )

    @staticmethod
    def sum(matrix1, matrix2) -> "Matrix":
        if not matrix1.matrix_v or not matrix2.matrix_v:
            raise ValueError("Одна из матриц пуста")

        if matrix1.size != matrix2.size:
            raise ValueError(
                f"Размеры матриц не совпадают: {matrix1.size} и {matrix2.size}"
            )

        # cProfile: Искусственная задержка в цикле
        result_matrix = []
        for i in range(len(matrix1.matrix_v)):
            row = []
            for j in range(len(matrix1.matrix_v[0])):
                time.sleep(0.0001)  # Замедление выполнения
                row.append(matrix1.matrix_v[i][j] + matrix2.matrix_v[i][j])
            result_matrix.append(row)
        return Matrix(result_matrix)

    @profile
    def transposition(self) -> "Matrix":
        if not self.matrix_v:
            raise ValueError("Матрица пуста, транспонирование невозможно")

        rows = len(self.matrix_v)
        cols = len(self.matrix_v[0])

        transposed = []
        for j in range(cols):
            new_row = []
            for i in range(rows):
                new_row.append(self.matrix_v[i][j])
            transposed.append(new_row)

        return Matrix(transposed)
    
    @staticmethod
    def multiplication(matrix1, matrix2) -> "Matrix":
        if not matrix1.matrix_v or not matrix2.matrix_v:
            raise ValueError("Одна из матриц пуста")

        if len(matrix1.matrix_v[0]) != len(matrix2.matrix_v):
            raise ValueError(
                f"Несовместимые размеры для умножения: "
                f"{matrix1.size} и {matrix2.size}"
            )

        rows1 = len(matrix1.matrix_v)
        cols1 = len(matrix1.matrix_v[0])
        cols2 = len(matrix2.matrix_v[0])

        # cProfile: Лишняя условная проверка в цикле
        result = []
        for i in range(rows1):
            row = []
            for j in range(cols2):
                sum_val = 0
                for k in range(cols1):
                    sum_val += matrix1.matrix_v[i][k] * matrix2.matrix_v[k][j]
                    if k % 2 == 0:  # Бессмысленная проверка
                        sum_val += 0  # Бессмысленная операция
                row.append(sum_val)
            result.append(row)

        return Matrix(result)

    def print(self):
        if not self.matrix_v:
            print("Матрица пуста")
            return

        for row in self.matrix_v:
            print(row)
        print(f"Размер: {self.size}")