class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._count = 0



    def append(self, value):
        new_node = Node(value)

        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

        self._count += 1

    def prepend(self, value):
        new_node = Node(value)

        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head = new_node

        self._count += 1



    def is_empty(self):
        return self._count == 0

    def __len__(self):
        return self._count

    def contains(self, value):
        current = self._head

        while current is not None:
            if current.data == value:
                return True
            current = current.next

        return False



    def __iter__(self):
        current = self._head

        while current is not None:
            yield current.data
            current = current.next

    def __str__(self):
        values = []
        current = self._head

        while current is not None:
            values.append(str(current.data))
            current = current.next

        if values:
            return "Head -> " + " -> ".join(values) + " -> None"

        return "Head -> None"


if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)


    print(linked_list)

    print("Length:", len(linked_list))
    print("Contains 20:", linked_list.contains(20))
    print("Contains 100:", linked_list.contains(100)) 