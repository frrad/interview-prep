class board:

    def __init__(self, x, y, x_trie, y_trie):
        self.__x, self.__y = x, y
        self.__x_trie, self.__y_trie = x_trie, y_trie

        self.__downs, self.__rights = [], []
        for x in xrange(self.__x):
            self.__downs.append([])
            self.__rights.append([])
            for y in xrange(self.__y):
                self.__downs[x].append(False)
                self.__rights[x].append(False)

    def __str__(self):
        ans = ''
        for x in xrange(self.__x):
            for y in xrange(self.__y):
                if self.__rights[x][y]:
                    ans += str(self.__rights[x][y])
                else:
                    ans += ' '
            ans += '\n'
        return ans

    def set_state(self, downs, rights):
        for x in xrange(self.__x):
            for y in xrange(self.__y):
                self.__downs[x][y] = downs[x][y]
                self.__rights[x][y] = rights[x][y]

    def copy(self):
        new_board = board(self.__x, self.__y, self.__x_trie, self.__y_trie)
        new_board.set_state(self.__downs, self.__rights)
        return new_board

    def above(self, x, y):
        if x == 0:
            return self.__x_trie
        if self.__downs[x - 1][y]:
            return self.__downs[x - 1][y]
        return False

    def left(self, x, y):
        if y == 0:
            return self.__y_trie
        if self.__rights[x][y - 1]:
            return self.__rights[x][y - 1]
        return False

    def set_place(self, x, y, letter):
        self.__rights[x][y] = self.left(x, y).children[letter]
        self.__downs[x][y] = self.above(x, y).children[letter]

    def filled(self):
        print self
        if self.__downs[self.__x - 1][self.__y - 1] and self.__rights[self.__x - 1][self.__y - 1]:
            return self
        best_options = range(30)
        for x in xrange(self.__x):
            for y in xrange(self.__y):
                if self.above(x, y) and self.left(x, y) and not self.__rights[x][y] and not self.__downs[x][y]:
                    a, b = self.above(x, y), self.left(x, y)
                    options = set(a.children.keys()) & set(b.children.keys())
                    if len(options) == 0:
                        return False
                    if len(options) < len(best_options):
                        best_options, best_x, best_y = options, x, y

        for option in best_options:
            below = self.copy()
            below.set_place(best_x, best_y, option)
            filled = below.filled()
            if filled:
                return filled

        return False


class trie:

    def __init__(self, name='', suffix=''):
        self.__size = 0
        self.children = dict()
        self.__name = name
        self.add(suffix)

    def add(self, suffix):
        if len(suffix) == 0:
            return
        first_letter = suffix[0]
        rest = suffix[1:]
        if first_letter in self.children:
            self.children[first_letter].add(rest)
        else:
            self.children[first_letter] = trie(first_letter, rest)

    def print_all(self, level=0):
        print ' ' * level + self.__name
        for child in self.children.values():
            child.print_all(level + 1)

    def __str__(self):
        return self.__name


def word_valid(word):
    for letter in word:
        if not (97 <= ord(letter) <= 122):
            return False
    return True


def works(x, y, x_trie, y_trie):
    my_board = board(x, y, x_trie, y_trie)
    if my_board.filled():
        print str(my_board.filled())
        return True


# makes a trie from a set of words
def make_trie(in_set):
    my_trie = trie()
    for word in in_set:
        my_trie.add(word)
    return my_trie

len_keyed_dict = dict()
with open('/usr/share/dict/words', 'r') as f:
    for word in f:
        word = word.lower().strip()
        if word_valid(word):
            if len(word) not in len_keyed_dict:
                len_keyed_dict[len(word)] = set()
            len_keyed_dict[len(word)].add(word)


keys = len_keyed_dict.keys()[:]


tries = dict()
for key in keys:
    tries[key] = make_trie(len_keyed_dict[key])


max_seen = 0
for x in keys:
    for y in keys:
        if x * y < max_seen:
            continue
        if x < y or y == 1:
            continue
        print x, y
        if works(x, y, tries[x], tries[y]):
            max_seen = x * y
