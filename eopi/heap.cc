#include "heap.h"

bool min_heap::insert(int bubble_down) {
  if (bubble_down < data) {
    int temp = data;
    data = bubble_down;
    bubble_down = temp;
  }

  if (right == nullptr) {
    min_heap insert = min_heap(bubble_down);
    right = &insert;
    return true;
  }
  if (left == nullptr) {
    min_heap insert = min_heap(bubble_down);
    left = &insert;
    return true;
  }
  right->insert(bubble_down);
  return true;
}

int min_heap::pop_min() { int to_return = get_data(); }

int min_heap::get_data() { return data; }
