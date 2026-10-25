import unittest

from singly_linked_list import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):

    def test_append(self):
        linked_list = SinglyLinkedList()

        linked_list.append(10)
        linked_list.append(20)
        linked_list.append(30)

        self.assertEqual(list(linked_list), [10, 20, 30])
        self.assertEqual(len(linked_list), 3)
        self.assertEqual(linked_list._head.data, 10)
        self.assertEqual(linked_list._tail.data, 30)
        self.assertIsNone(linked_list._tail.next)

    def test_prepend(self):
        linked_list = SinglyLinkedList()

        linked_list.prepend(10)
        linked_list.prepend(20)
        linked_list.prepend(30)

        self.assertEqual(list(linked_list), [30, 20, 10])
        self.assertEqual(len(linked_list), 3)
        self.assertEqual(linked_list._head.data, 30)
        self.assertEqual(linked_list._tail.data, 10)
        self.assertIsNone(linked_list._tail.next)

    def test_forward_builder(self):
        values = [10, 20, 30, 40, 50]
        original = values.copy()

        linked_list = SinglyLinkedList()
        linked_list.build_list_forward(values)

        self.assertEqual(list(linked_list), [10, 20, 30, 40, 50])
        self.assertEqual(values, original)
        self.assertEqual(len(linked_list), 5)

    def test_backward_builder(self):
        values = [10, 20, 30, 40, 50]
        original = values.copy()

        linked_list = SinglyLinkedList()
        linked_list.build_list_backward(values)

        self.assertEqual(list(linked_list), [50, 40, 30, 20, 10])
        self.assertEqual(values, original)
        self.assertEqual(len(linked_list), 5)

    def test_contains_is_empty_len_and_iteration(self):
        linked_list = SinglyLinkedList()

        self.assertTrue(linked_list.is_empty())
        self.assertEqual(len(linked_list), 0)

        linked_list.append(10)
        linked_list.append(20)
        linked_list.append(30)

        self.assertFalse(linked_list.is_empty())
        self.assertTrue(linked_list.contains(20))
        self.assertFalse(linked_list.contains(100))
        self.assertEqual(len(linked_list), 3)
        self.assertEqual(list(linked_list), [10, 20, 30])

    def test_insert_after(self):
        linked_list = SinglyLinkedList()
        linked_list.build_list_forward([10, 20, 30])

        linked_list.insert_after(20, 25)
        self.assertEqual(list(linked_list), [10, 20, 25, 30])

        linked_list.insert_after(30, 40)
        self.assertEqual(list(linked_list), [10, 20, 25, 30, 40])
        self.assertEqual(linked_list._tail.data, 40)
        self.assertIsNone(linked_list._tail.next)

    def test_insert_after_missing_value(self):
        linked_list = SinglyLinkedList()
        linked_list.build_list_forward([10, 20, 30])

        with self.assertRaises(ValueError):
            linked_list.insert_after(100, 200)

    def test_remove(self):
        linked_list = SinglyLinkedList()
        linked_list.build_list_forward([10, 20, 30, 40])

        linked_list.remove(10)
        self.assertEqual(list(linked_list), [20, 30, 40])

        linked_list.remove(30)
        self.assertEqual(list(linked_list), [20, 40])

        linked_list.remove(40)
        self.assertEqual(list(linked_list), [20])
        self.assertEqual(linked_list._tail.data, 20)

        linked_list.remove(20)
        self.assertTrue(linked_list.is_empty())
        self.assertIsNone(linked_list._head)
        self.assertIsNone(linked_list._tail)
        self.assertEqual(len(linked_list), 0)

    def test_remove_missing_value(self):
        linked_list = SinglyLinkedList()
        linked_list.build_list_forward([10, 20, 30])

        with self.assertRaises(ValueError):
            linked_list.remove(100)

    def test_remove_all(self):
        linked_list = SinglyLinkedList()
        linked_list.build_list_forward([20, 20, 10, 20, 30, 20, 20])

        removed = linked_list.remove_all(20)

        self.assertEqual(removed, 5)
        self.assertEqual(list(linked_list), [10, 30])
        self.assertEqual(len(linked_list), 2)
        self.assertEqual(linked_list._head.data, 10)
        self.assertEqual(linked_list._tail.data, 30)
        self.assertIsNone(linked_list._tail.next)

    def test_remove_all_no_match(self):
        linked_list = SinglyLinkedList()
        linked_list.build_list_forward([10, 20, 30])

        removed = linked_list.remove_all(100)

        self.assertEqual(removed, 0)
        self.assertEqual(list(linked_list), [10, 20, 30])
        self.assertEqual(len(linked_list), 3)

    def test_invariants(self):
        linked_list = SinglyLinkedList()
        linked_list.build_list_forward([10, 20, 30, 40])

        count = 0
        current = linked_list._head

        while current is not None:
            count += 1

            if current.next is None:
                self.assertIs(current, linked_list._tail)

            current = current.next

        self.assertEqual(count, len(linked_list))
        self.assertIsNone(linked_list._tail.next)


if __name__ == "__main__":
    unittest.main() 