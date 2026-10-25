import unittest

from split_evens_odds import SplitEvensOdds


class TestSplitEvensOdds(unittest.TestCase):

    def get_nodes(self, linked_list):
        nodes = []
        current = linked_list._head

        while current is not None:
            nodes.append(current)
            current = current.next

        return nodes

    def test_mixed_values(self):
        linked_list = SplitEvensOdds()
        linked_list.build_list_forward([10, 13, 14, 18, 21])

        even_list, odd_list = linked_list.split_even_odd()

        self.assertEqual(list(even_list), [10, 14, 18])
        self.assertEqual(list(odd_list), [13, 21])

        self.assertEqual(len(even_list), 3)
        self.assertEqual(len(odd_list), 2)

        self.assertEqual(even_list._tail.data, 18)
        self.assertEqual(odd_list._tail.data, 21)

        self.assertIsNone(even_list._tail.next)
        self.assertIsNone(odd_list._tail.next)

        self.assertTrue(linked_list.is_empty())
        self.assertIsNone(linked_list._head)
        self.assertIsNone(linked_list._tail)
        self.assertEqual(len(linked_list), 0)

    def test_all_even(self):
        linked_list = SplitEvensOdds()
        linked_list.build_list_forward([2, 4, 6, 8])

        even_list, odd_list = linked_list.split_even_odd()

        self.assertEqual(list(even_list), [2, 4, 6, 8])
        self.assertEqual(list(odd_list), [])
        self.assertEqual(len(even_list), 4)
        self.assertEqual(len(odd_list), 0)

    def test_all_odd(self):
        linked_list = SplitEvensOdds()
        linked_list.build_list_forward([1, 3, 5, 7])

        even_list, odd_list = linked_list.split_even_odd()

        self.assertEqual(list(even_list), [])
        self.assertEqual(list(odd_list), [1, 3, 5, 7])
        self.assertEqual(len(even_list), 0)
        self.assertEqual(len(odd_list), 4)

    def test_single_even(self):
        linked_list = SplitEvensOdds()
        linked_list.append(10)

        even_list, odd_list = linked_list.split_even_odd()

        self.assertEqual(list(even_list), [10])
        self.assertEqual(list(odd_list), [])

    def test_single_odd(self):
        linked_list = SplitEvensOdds()
        linked_list.append(11)

        even_list, odd_list = linked_list.split_even_odd()

        self.assertEqual(list(even_list), [])
        self.assertEqual(list(odd_list), [11])

    def test_empty_list_error(self):
        linked_list = SplitEvensOdds()

        with self.assertRaises(ValueError):
            linked_list.split_even_odd()

    def test_reuses_original_nodes(self):
        linked_list = SplitEvensOdds()
        linked_list.build_list_forward([10, 13, 14, 18])

        original_nodes = self.get_nodes(linked_list)

        even_list, odd_list = linked_list.split_even_odd()

        new_nodes = self.get_nodes(even_list) + self.get_nodes(odd_list)

        self.assertEqual(len(original_nodes), len(new_nodes))

        for node in original_nodes:
            self.assertIn(node, new_nodes)


if __name__ == "__main__":
    unittest.main() 
