#include "heap.h"
#include <iostream>

int main() {

  min_heap joe = min_heap(15);
  joe.insert(3);
  joe.insert(-1);
  joe.insert(31);

  std::cout << joe.get_data() << std::endl;
}
