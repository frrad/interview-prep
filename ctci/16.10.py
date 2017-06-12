class graph:

    lookup = dict()

    def __init__(self, name):
        self.name = name
        graph.lookup[name] = self
        self.neighbors = list()

    def __str__(self):
        return self.name + '=' + ";".join([x.name for x in self.neighbors])

    def add_neighbor(self, neighbor):
        for already in self.neighbors:
            if already.name == neighbor.name:
                return

        self.neighbors.append(neighbor)
        # all are two-way
        neighbor.neighbors.append(self)


def word_valid(word):
    for letter in word:
        if not (97 <= ord(letter) <= 122):
            return False
    return True


def connect(graph_1, graph_2):
    consider = [(0, graph_1, [])]
    added_ptrs = set()
    while len(consider) > 0:
        distance, pointer, record = consider.pop()
        if pointer == graph_2:
            return distance, record + [pointer.name]
        for neighbor in pointer.neighbors:
            if neighbor.name not in added_ptrs:
                consider.insert(
                    0, (distance + 1, neighbor, record + [pointer.name]))
                added_ptrs.add(pointer.name)

    return False

start_word = 'damp'
target_word = 'like'

assert len(start_word) == len(target_word)
word_length = len(start_word)


wordlist = list()
with open('/usr/share/dict/words', 'r') as f:
    for word in f:
        word = word.lower().strip()
        if word_valid(word) and len(word) == word_length:
            wordlist.append(word)


# map from masked words to their nodes
masks = dict()
for word in wordlist:
    node = graph(word)
    for i in xrange(len(word)):
        mask = word[:i] + '*' + word[i + 1:]

        if mask in masks:
            for neighbor in masks[mask]:
                neighbor.add_neighbor(node)
            masks[mask].append(node)
        else:
            masks[mask] = [node]

print connect(graph.lookup[start_word], graph.lookup[target_word])
