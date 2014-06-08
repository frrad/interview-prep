class linkedlist:
    '''a singly linked list'''
    def __init__(self):
        self.next = None
        self.data = 0

    def show(self, number = 0):
        print number, ":", self.data
        if not self.next is None:
            self.next.show(number +1)

    def removeNext(self):
        if self.next is None: return
        self.next = self.next.next

    def addTail(self, number):
        end = linkedlist()
        end.data = number
        pointer = self
        while not pointer.next is None:
            pointer = pointer.next
        pointer.next = end

def linkify(array):
    last = None
    while len(array) > 0:
        link = linkedlist()
        link.data = array.pop()
        link.next = last
        last = link
    return last

def deDuplicate(llist):
    seen = set([llist.data])
    if llist.next is None: return
    forward = llist.next

    while not forward is None:
        if forward.data in seen:
            llist.removeNext()
            forward = llist.next
        else:
            seen.add(forward.data)
            llist = llist.next
            forward = llist.next


def kthToLast(start, k):
    end = start
    for i in xrange(k):
        if end.next is None: return None
        end = end.next
    while not end is None:
        start = start.next
        end = end.next
    return start


example = linkify([234,234,3,32,1,56,234,7887,56])
example.show()
print "========"
print kthToLast(example, 5).data
