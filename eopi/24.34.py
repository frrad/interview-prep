import bst

alphabet = {'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702, 'f': 2.228, 'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.153, 'k': 0.772, 'l': 4.025, 'm': 2.406,
            'n': 6.749, 'o': 7.507, 'p': 1.929, 'q': 0.095, 'r': 5.987, 's': 6.327, 't': 9.056, 'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.150, 'y': 1.974, 'z': 0.074}


def huffman(freq_table):

    # should use min-heap for pool
    pool = [bst.bst((freq_table[key], key)) for key in freq_table.keys()]

    while len(pool) > 1:
        pool.sort(key=lambda x: -x.data[0])
        a, b = pool.pop(), pool.pop()
        weight = a.data[0] + b.data[0]
        c = bst.bst((weight, ''))
        c.left, c.right = a, b
        pool.append(c)

    return pool[0]


def decode(huffman, prefix=''):
    if huffman.left or huffman.right:
        return decode(huffman.left, prefix + '0') + decode(huffman.right, prefix + '1')
    else:
        return [(huffman.data, prefix)]


print '\n'.join(map(str, decode(huffman(alphabet))))
