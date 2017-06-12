class bst:

    def __init__(self, data='', left=None, right=None):
        self.data, self.left, self.right = data, left, right

    def insert_list(self, data_list):
        for datum in data_list:
            self.insert(datum)

    def insert(self, data):
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = bst(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = bst(data)

    def string(self, level=0, prefix=''):
        ans = prefix + '`--'
        ans += str(self.data)
        if self.left:
            ans += '\n' + self.left.string(level + 1, prefix + '  |')
        if self.right:
            ans += '\n' + self.right.string(level + 1, prefix + '   ')
        return ans

    def __str__(self):
        return self.string()
