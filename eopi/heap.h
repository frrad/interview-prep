class min_heap {

private:
  int data;

public:
  min_heap(int x) : data(x){};

  min_heap *left = nullptr;
  min_heap *right = nullptr;

  int get_data();
  int pop_min();

  bool insert(int x);
};
