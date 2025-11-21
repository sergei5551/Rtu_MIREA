from Matrix import Matrix

def matrix_operations():
    m1 = Matrix()
    m2 = Matrix()
    
    m1.create_matrix("2x2", True)
    m2.create_matrix("2x2", True)
    
    print("Матрица 1:")
    m1.print()
    
    print("\nМатрица 2:")
    m2.print()
    
    print("\nСложение матриц:")
    try:
        result_sum = Matrix.sum(m1, m2)
        result_sum.print()
    except Exception as e:
        print(f"Ошибка сложения: {e}")
    
    print("\nТранспонирование матрицы 1:")
    try:
        transposed = m1.transposition()
        transposed.print()
    except Exception as e:
        print(f"Ошибка транспонирования: {e}")
    
    print("\nУмножение матриц:")
    try:
        result_mul = Matrix.multiplication(m1, m2)
        result_mul.print()
    except Exception as e:
        print(f"Ошибка умножения: {e}")
    
    print("\nИзменение элемента:")
    try:
        m1.change_element(0, 0, 99)
        m1.print()
    except Exception as e:
        print(f"Ошибка изменения: {e}")

if __name__ == "__main__":
    matrix_operations()