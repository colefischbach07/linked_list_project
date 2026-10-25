from singly_linked_list import SinglyLinkedList


class SplitEvensOdds(SinglyLinkedList):

    def split_even_odd(self):
        if self.is_empty():
            raise ValueError("Cannot split an empty list")

        even_list = SinglyLinkedList()
        odd_list = SinglyLinkedList()

        current = self._head

        self._head = None
        self._tail = None
        self._count = 0

        while current is not None:
            next_node = current.next
            current.next = None

            if current.data % 2 == 0:
                destination = even_list
            else:
                destination = odd_list

            if destination._head is None:
                destination._head = current
                destination._tail = current
            else:
                destination._tail.next = current
                destination._tail = current

            destination._count += 1

            current = next_node

        return even_list, odd_list