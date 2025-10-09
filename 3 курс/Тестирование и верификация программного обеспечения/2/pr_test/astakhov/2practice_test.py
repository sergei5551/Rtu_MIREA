class Matrix:
    def __init__(self, matrix_v=[], size="1x1"):
        self.matrix_v = matrix_v
        if len(matrix_v) > 0:
            self.size = f"{len(matrix_v)}x{len(matrix_v[0])}"
        else:
            self.size = size
            
    def change_element(self, index_row, index_col, element):
        if index_row >= len(self.matrix_v) or index_col >= len(self.matrix_v[0]):
            raise IndexError(f"Индекс [{index_row}][{index_col}] вне границ матрицы {self.size}")
        self.matrix_v[index_row][index_col] = element
    
    def create_matrix(self, size="3x3", matrixDefault=True) -> list():
        if not self._validate_size_format(size):
            raise ValueError(f"Неверный формат размера: {size}. Используйте формат 'NxM'")
        
        self.size = size
        self.matrix_v = []  

        if matrixDefault:
            max_var = 1
            for i in range(int(self.size[0])):
                matrix_prom = list()  
                for j in range(int(self.size[2])):  # Берем третий символ (индекс 2)
                    matrix_prom.append(max_var)
                    max_var += 1
                self.matrix_v.append(matrix_prom)
            return self.matrix_v
        
        for i in range(int(self.size[0])):
            matrix_prom = list()  
            for j in range(int(self.size[2])):  # Берем третий символ (индекс 2)
                value = int(input(f"Введите значение для элемента[{i+1}][{j+1}]:"))
                matrix_prom.append(value)
            self.matrix_v.append(matrix_prom)
        return self.matrix_v

    @staticmethod
    def _validate_size_format(size):
        """Проверяет корректность формата размера"""
        return len(size) == 3 and size[1] == 'x' and size[0].isdigit() and size[2].isdigit()

    @staticmethod
    def sum(matrix1, matrix2) -> "Matrix":
        if matrix1.size != matrix2.size:
            raise ValueError(f"Размеры матриц не совпадают: {matrix1.size} и {matrix2.size}")
        
        # ОШИБКА 1: Не проверяем, что матрицы не пустые
        if not matrix1.matrix_v or not matrix2.matrix_v:
            raise ValueError("Одна из матриц пуста")
        
        matr1 = [row[:] for row in matrix1.matrix_v]  # Создаем копию
        matr2 = matrix2.matrix_v
        
        for row in range(len(matr2)):
            for col in range(len(matr2[0])):
                matr1[row][col] += matr2[row][col]
        return Matrix(matr1)

    def transposition(self) -> "Matrix":
        if not self.matrix_v:
            raise ValueError("Матрица пуста, транспонирование невозможно")
        
        rows = len(self.matrix_v)
        cols = len(self.matrix_v[0])
        
        # Создаем новую транспонированную матрицу
        transposed = []
        for j in range(cols):
            new_row = []
            for i in range(rows):
                new_row.append(self.matrix_v[i][j])
            transposed.append(new_row)
        
        return Matrix(transposed)

    @staticmethod
    def multiplication(matrix1, matrix2) -> "Matrix":
        if len(matrix1.matrix_v[0]) != len(matrix2.matrix_v):
            raise ValueError(f"Несовместимые размеры для умножения: {matrix1.size} и {matrix2.size}")
        
        rows1 = len(matrix1.matrix_v)
        cols1 = len(matrix1.matrix_v[0])
        cols2 = len(matrix2.matrix_v[0])
        
        result = []
        for i in range(rows1):
            row = []
            for j in range(cols2):
                sum_val = 0
                for k in range(cols1):
                    # ОШИБКА 2: Может возникнуть, если элементы не числа
                    try:
                        sum_val += matrix1.matrix_v[i][k] * matrix2.matrix_v[k][j]
                    except TypeError:
                        raise TypeError("Элементы матриц должны быть числами")
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


def main():
    try:
        print("=== Тестирование матриц ===")
        
        # Тест 1: Создание матрицы по умолчанию
        mtr1 = Matrix()
        mtr1.create_matrix()
        print("Матрица 1 (3x3 по умолчанию):")
        mtr1.print()
        
        print("\n" + "="*50)
        
        # Тест 2: Создание пользовательской матрицы
        mtr2 = Matrix()
        mtr2.create_matrix("2x2")
        print("Матрица 2 (2x2):")
        mtr2.print()
        
        print("\n" + "="*50)
        
        # Тест 3: Сложение матриц
        mtr3 = Matrix()
        mtr3.create_matrix("2x2")
        mtr4 = Matrix()
        mtr4.create_matrix("2x2")
        
        print("Матрица 3:")
        mtr3.print()
        print("Матрица 4:")
        mtr4.print()
        
        try:
            result_sum = Matrix.sum(mtr3, mtr4)
            print("Результат сложения:")
            result_sum.print()
        except ValueError as e:
            print(f"Ошибка при сложении: {e}")
        
        print("\n" + "="*50)
        
        # Тест 4: Транспонирование
        print("Транспонирование матрицы 1:")
        try:
            transposed = mtr1.transposition()
            transposed.print()
        except ValueError as e:
            print(f"Ошибка при транспонировании: {e}")
        
        print("\n" + "="*50)
        
        # Тест 5: Умножение
        mtr5 = Matrix([[1, 2], [3, 4]])
        mtr6 = Matrix([[5, 6], [7, 8]])
        
        print("Умножение матриц:")
        mtr5.print()
        print("×")
        mtr6.print()
        
        try:
            result_mul = Matrix.multiplication(mtr5, mtr6)
            print("=")
            result_mul.print()
        except (ValueError, TypeError) as e:
            print(f"Ошибка при умножении: {e}")
        
        print("\n" + "="*50)

        
        print("\n=== Тестирование обработки ошибок ===")
        
        # ОШИБКА 1: Сложение с пустой матрицей
        print("1. Сложение с пустой матрицей:")
        try:
            empty_matrix = Matrix()
            Matrix.sum(mtr1, empty_matrix)
        except ValueError as e:
            print(f"   ✓ Ошибка: {e}")
            
        # ОШИБКА 2: Умножение с некорректными данными
        print("2. Умножение с некорректными данными:")
        try:
            mtr9 = Matrix([["a", "b"], ["c", "d"]])  # Строки вместо чисел
            mtr10 = Matrix([[1, 2], [3, 4]])
            Matrix.multiplication(mtr9, mtr10)
        except TypeError as e:
            print(f"   ✓ Ошибка: {e}")

    except Exception as e:
        print(f"Неожиданная ошибка: {e}")


if __name__ == "__main__":
    main()