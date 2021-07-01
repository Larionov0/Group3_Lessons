class Node:
    next = None
    prev = None
    value = None


class List:
    head = None
    tail = None

    def append(self, value):
        new_node = Node()
        new_node.value = value

        if self.head is None:  # Якщо наш список був пустим
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def get_el_by_i(self, index):  # lst[2]   ->   lst.get_el_by_i(2)
        i = 0

        node = self.head
        while True:
            if i == index:
                return node.value

            node = node.next
            i += 1

    def len(self):
        count = 0

        node = self.head  # i = 0
        while node is not None:
            count += 1
            node = node.next  # i += 1
        return count


n1 = Node()
n1.value = 'a'

n2 = Node()
n2.value = 'b'

n3 = Node()
n3.value = 'c'

n1.next = n2
n2.next = n3

n3.prev = n2
n2.prev = n1


lst = List()
lst.head = n1
lst.tail = n3


lst.append('d')
lst.append('e')


lst2 = List()
lst2.append('lol')
lst2.append('kek')


# i = 0
# while i < lst.len():
#     print(lst.get_el_by_i(i))
#     i += 1
