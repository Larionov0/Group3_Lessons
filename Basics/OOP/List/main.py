class Node:
    next = None
    prev = None
    value = None


class List:
    head = None
    tail = None

    def __init__(self, *values):
        for v in values:
            self.append(v)

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

    def get_node_by_i(self, index):
        i = 0

        node = self.head
        while True:
            if node is None:
                raise Exception(f'List index out of range: {index} / {self.len() - 1}')

            if i == index:
                return node
            node = node.next
            i += 1

    def get_el_by_i(self, index):  # lst[2]   ->   lst.get_el_by_i(2)
        return self.get_node_by_i(index).value

    def len(self):
        count = 0

        node = self.head  # i = 0
        while node is not None:
            count += 1
            node = node.next  # i += 1
        return count

    def remove_node(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    def remove(self, value):
        node = self.head  # i = 0
        while node is not None:
            if node.value == value:
                self.remove_node(node)
                break

            node = node.next

    def pop(self, index):
        node = self.head  # i = 0
        i = 0
        while node is not None:
            if i == index:
                self.remove_node(node)
                return node.value

            i += 1
            node = node.next

    def __getitem__(self, index):  # []
        return self.get_el_by_i(index)

    def __setitem__(self, index, value):
        node = self.get_node_by_i(index)
        node.value = value

    def __str__(self):
        text = "["

        node = self.head  # i = 0
        while node is not None:
            text += node.value.__repr__() + ', '
            node = node.next
        text = text[:-2] + ']'
        return text


lst = List('a', 'b', 'c', 'd', 'e')

lst.pop(2)

lst[2] = 'lol'
print(lst)
