import unittest
from pathlib import Path

from homeworks.homework_5.task_1.cartesian_tree import CartesianTree

resources = Path("tests/homework5/resources")


def complicated_tree() -> CartesianTree:
    tree = CartesianTree()
    tree.insert_with_priority(1, "val1", 5)
    tree.insert_with_priority(2, "val2", 4)
    tree.insert_with_priority(3, "3", 1)
    tree.insert_with_priority(4, "123", 11)
    tree.insert_with_priority(5, "text", 1)
    tree.insert_with_priority(6, 6, 6)
    tree.insert_with_priority(7, 0.1, 3)
    return tree


class CartesianTreeTest(unittest.TestCase):
    def test_contains_key_in_tree(self):
        self.assertTrue(1 in complicated_tree())

    def test_contains_key_not_in_tree(self):
        self.assertFalse(0 in complicated_tree())

    def test_add_check_key(self):
        tree = CartesianTree()
        tree[1] = 2
        self.assertTrue(1 in tree)

    def test_add_check_value_key_not_in_tree(self):
        tree = complicated_tree()
        tree[15] = 2
        self.assertEqual(tree[15], 2)

    def test_add_check_value_key_in_tree(self):
        tree = complicated_tree()
        tree[1] = 2
        self.assertEqual(tree[1], 2)

    def test_delete_empty_tree(self):
        tree = CartesianTree()
        with self.assertRaises(KeyError):
            del tree[0]

    def test_delete_key_not_in_tree(self):
        tree = complicated_tree()
        with self.assertRaises(KeyError) as context:
            del tree[-1]

    def test_delete_key_in_tree(self):
        tree = complicated_tree()
        del tree[3]
        self.assertTrue(3 not in tree)

    def test_get_empty_tree(self):
        tree = CartesianTree()
        with self.assertRaises(KeyError):
            value = tree[0]

    def test_get_key_not_in_tree(self):
        tree = complicated_tree()
        with self.assertRaises(KeyError):
            value = tree[0]

    def test_get_key_in_tree(self):
        tree = complicated_tree()
        result = tree[1]
        self.assertEqual(result, "val1")

    def test_len_empty_tree(self):
        tree = CartesianTree()
        self.assertEqual(len(tree), 0)

    def test_len_complicated_tree(self):
        self.assertEqual(len(complicated_tree()), 7)

    def test_iterator_empty_tree(self):
        tree = CartesianTree()
        self.assertEqual(list(tree), [])

    def test_iterator_complicated_tree(self):
        tree = complicated_tree()
        self.assertEqual(list(tree), ['123', 'val1', 'val2', '3', 6, 'text', 0.1])

    def test_reversed_empty_tree(self):
        tree = CartesianTree()
        self.assertEqual(list(reversed(tree)), [])

    def test_reversed_complicated_tree(self):
        tree = complicated_tree()
        self.assertEqual(list(reversed(tree)), ['3', 'val2', 'val1', 'text', 0.1, 6, '123'])
