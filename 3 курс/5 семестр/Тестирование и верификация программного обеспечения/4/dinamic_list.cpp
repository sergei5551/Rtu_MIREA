#include "dinamic_list.h"

int main(){
	setlocale(0, "Rus");
	List<double> L;
	int choice = 1;
	double a, b;
	// 4-6 Пункты доп задачи
	while (choice != 0) {
		puts("Интерфейс");
		puts("1) Вставка узла в начало списка");
		puts("2) Создание списка из n узлов, используя функцию вставки узла перед первым узлом");
		puts("3) Вывод списка в консоль");
		puts("4) Вставить перед последним узлом два новых узла с заданными значениями");
		puts("5) Удалить из списка L первое отрицательное значение, если оно присутствует в списке");
		puts("6) Найти в списке L максимальное значение и перенести узел с этим значением в конец списка");
		puts("0) Чтоб выйти");
		cout << "Ввод: "; cin >> choice;

		switch (choice) {
		case 1:
			int data;
			cout << "Введите данные: "; cin >> data;
			L.push_front(data);
			break;
		case 2:
			int n;
			cout << "Введите колл-во(n) элементов списка для создания: "; cin >> n;
			
			L.create_list(n);
			break;
		case 3:
			for (int i = 0; i < L.GetSize(); i++) {
				cout << L[i] << " ";
			}
			cout << endl;
			break;
		case 4:
			cout << "Введите два значения для вствки в предпоследний узел(через пробел): ";
			cin >> a >> b;
			L.task1(a, b);
			break;
		case 5:
			L.task2();
			break;
		case 6:
			L.task3();
			break;
		}
	}
}