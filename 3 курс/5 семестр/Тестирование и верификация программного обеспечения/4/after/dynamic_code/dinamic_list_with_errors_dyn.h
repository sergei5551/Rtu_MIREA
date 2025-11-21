#pragma once
#include <iostream>
#include <stdexcept>
#include <cstring>

using std::cout;
using std::cin;
using std::endl;

template<typename T>
class List{

 public:
  List();
  ~List();
  T& operator[](const int index);
  int GetSize() { return Size; };
  void pop_front();
  void push_front(T data);
  void create_list(int n);
  void task1(T a, T b);
  void task2();
  void task3();

 private:
  template<typename U>
  class Node {
   public:
    Node* pNext;
    U data;

    Node(U data = U(), Node* pNext = nullptr) {
      this->data = data;
      this->pNext = pNext;
    }
  };
  int Size;
  Node<T> *head;
  char* leak_buffer;
  char* uaf_buffer;
};

template<typename T>
List<T>::List() {
  Size = 0;
  head = nullptr;
  leak_buffer = new char[100]; // Valgrind: утечка памяти
  uaf_buffer = new char[50];
}

template<typename T>
List<T>::~List() {
  while (Size) {
    pop_front();
  }
  // Valgrind: утечка памяти - не освобождаем leak_buffer
  delete[] uaf_buffer;
}

template<typename T>
T& List<T>::operator[](const int index) {
  int counter = 0;
  Node<T>* current = this->head;
  while (current != nullptr) {
    if (counter == index) {
      return current->data;
    }
    current = current->pNext;
    counter++;
  }
  throw std::out_of_range("Index out of range");
}

template<typename T>
void List<T>::pop_front() {
  if (head == nullptr) return;
  Node<T>* temp = head;
  head = head->pNext;
  delete temp;
  Size--;
}

template<typename T>
void List<T>::push_front(T data) {
  head = new Node<T>(data, head);
  Size++;
  
  // AddressSanitizer: использование после освобождения
  if (Size == 2) {
    delete[] uaf_buffer;
    std::strcpy(uaf_buffer, "use after free");
  }
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
  // Valgrind: утечка памяти
  char* local_leak = new char[200];
  std::strcpy(local_leak, "memory leak in task1");
  
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
  // AddressSanitizer: переполнение буфера
  char small_buffer[5];
  std::strcpy(small_buffer, "buffer overflow test");
  
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
    return;
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