
# implement linked list

class Node(object):
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList(object):
    def __init__(self, data=None) -> None:
        self.head = None
        self.tail = None

        if(data is not None):
            curr_node = None
            for d in data:
                if(self.head is None):
                    curr_node = Node(d)
                    self.head = curr_node
                    self.tail = self.head
                else:
                    new_node = Node(d)
                    new_node.prev = curr_node
                    curr_node.next = new_node
                    curr_node = new_node
                    self.tail = curr_node

    def __repr__(self):
        
        node = self.head
        if(node is None):
            return "None"

        repr_str = ""
        while node is not None:
            repr_str += str(node.data) + " -> "
            node = node.next

        repr_str += " None "

        return repr_str

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        if(self.head is not None):
            self.head.prev = node
            node.next = self.head
            self.head = node
        else:
            self.head = node
            self.tail = node

    def add_last(self, node):
        if(self.tail is not None):
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            self.head = node
            self.tail = node

    def remove_first(self):
        if(self.head is None):
            raise Exception("list is empty")
        
        node = self.head
        self.head = node.next
        self.head.prev = None
        return node

    def remove_last(self):
        if(self.tail is None):
            raise Exception("list is empty")
        
        node = self.tail
        self.tail = node.prev
        self.tail.next = None
        return node

    def remove(self, node):
        if(self.head is None):
            raise Exception("list is empty")

        for n in self:
            if(n.data==node.data):
                if (n==self.head):
                    return self.remove_first()
                elif (n==self.tail):
                    return self.remove_last()
                else:
                    n.prev.next = n.next
                    n.next.prev = n.prev
                    return n

        raise Exception("Node is not in the list")

# answer questions
def remove_dups(L):

    # data_count = dict()
    # for n in L:
    #     if(n.data in data_count):
    #         data_count[n.data] += 1
    #     else:
    #         data_count[n.data] = 1

    # for n in L:
    #     if(data_count[n.data]>1):
    #         L.remove(n)
    #         data_count[n.data] -= 1

    n = L.head
    while n is not None:
        next_node = n.next
        while next_node is not None:
            if(next_node.data==n.data):
                next_node.prev.next = next_node.next
                if(next_node.next is not None):
                    next_node.next.prev = next_node.prev
                next_node = next_node.next
            else:
                next_node = next_node.next

        n = n.next

    return L

# test code for questions
if (__name__ == "__main__"):

    # create list
    L = LinkedList([1, 2, 3, 4])
    print(L)

    L.add_first(Node(12))
    print(L)
    L.add_first(Node(22))
    print(L)

    L.add_last(Node(122))
    print(L)
    L.add_last(Node(123))
    print(L)

    L.remove(Node(22))
    print(L)
    L.remove(Node(3))
    print(L)
    L.remove(Node(123))
    print(L)

    # test the questions
    L = LinkedList([1, 2, 2, 3, 4, 7, 7])
    print(L)

    L2 = remove_dups(L)
    print(L2)