#pragma once
#include <iostream>

using std::cout;
using std::cin;
using std::endl;

template<typename T>
class List{

 public:
  List();
  ~List();
  T& operator[](const int index);
  int GetSize() { return Size; };  // Получение размера
  void pop_front();  // Удаление первого элемента
  void push_front(T data);
  void create_list(int n);
  void task1(T a, T b);
  void task2();
  void task3();

 private:
  template<typename T>
  class Node {
   public:
    Node* pNext;
    T data;

    Node(T data = T(), Node* pNext = nullptr) {
      this->data = data;
      this->pNext = pNext;
    }
  };
  int Size;
  Node<T> *head;
};

// В отдельный файл нельзя вынести шаблонные методы класса

template<typename T>
List<T>::List() {
  Size = 0;
  head = nullptr;
}

template<typename T>
List<T>::~List() {
  while (Size) {
    pop_front();
  }
}

template<typename T>
T& List<T>::operator[](const int index) {
  int counter = 0;
  Node<T>* current = this->head;
  while (current != nullptr) {
    if (counter == index)
    {
      return current->data;
    }

    current = current->pNext;
    counter++;
  }
}

template<typename T>
void List<T>::pop_front() {
  Node<T>* temp = head;
  head = head->pNext;
  delete temp;
  Size--;
}

template<typename T>
void List<T>::push_front(T data) {
  head = new Node<T>(data, head);
  Size++;
}

template<typename T>
void List<T>::create_list(int n) {
  T data;

  for (int i = 0; i < n; i++) {
    cout << "Введите данные: "; cin >> data;
    push_front(data);
  }
}

template<typename T>
void List<T>::task1(T a, T b) {
  Node<T>* current = head;

  if (current == nullptr || current->pNext == nullptr) {
    return;
  }

  while (current->pNext->pNext != nullptr) {
    current = current->pNext;
  }

  current->pNext = new Node<T>(a, current->pNext);
  current->pNext->pNext = new Node<T>(b, current->pNext->pNext);
  Size += 2;
}

template<typename T>
void List<T>::task2() {
  Node<T>* current = head;
  Node<T>* prev = nullptr;
  while (current != nullptr && current->data >= 0) {
    prev = current;
    current = current->pNext;
  }

  if (current != nullptr && prev != nullptr) {
    prev->pNext = current->pNext;
    delete current;
    Size--;
  }
  else if (current != nullptr) {
    pop_front();
  }
}
template<typename T>
void List<T>::task3() {
  if (head == nullptr || head->pNext == nullptr) {
    return;  // List is empty or has only one node.
  }
  Node<T>* current = head;
  Node<T>* maxNodePrev = nullptr;
  Node<T>* maxNode = head;
  Node<T>* prev = nullptr;
  T maxValue = head->data;

  while (current != nullptr) {
    if (current->data > maxValue) {
      maxValue = current->data;
      maxNodePrev = prev;
      maxNode = current;
    }
    prev = current;
    current = current->pNext;
  }

  if (maxNode->pNext == nullptr) {
    return;
  }

  if (maxNodePrev == nullptr) {
    head = maxNode->pNext;
  }
  else {
    maxNodePrev->pNext = maxNode->pNext;
  }

  prev->pNext = maxNode;
  maxNode->pNext = nullptr;
}