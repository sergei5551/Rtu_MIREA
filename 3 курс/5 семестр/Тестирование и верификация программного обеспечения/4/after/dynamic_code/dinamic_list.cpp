// test_auto.cpp
#include "dinamic_list_with_errors_dyn.h"

int main() {
    List<int> list;
    
    list.push_front(3);
    list.push_front(2);
    list.push_front(1);
    
    std::cout << "Size: " << list.GetSize() << std::endl;
    
    for (int i = 0; i < list.GetSize(); i++) {
        std::cout << "list[" << i << "] = " << list[i] << std::endl;
    }
    
    list.task1(10, 20);
    list.task2();
    list.task3();
    
    list.push_front(-5);
    list.task2();
    
    return 0;
}