import json
import unittest
from pathlib import Path

from homeworks.homework_5.task_1.node import Node

answers_folder = Path("tests/homework_5/task_1/answers")


def complicated_node() -> Node:
    node = Node(1, "val1", 5)
    node = node.insert(2, "val2", 4)
    node = node.insert(3, "3", 1)
    node = node.insert(4, "123", 11)
    node = node.insert(5, "text", 1)
    node = node.insert(6, 6, 6)
    node = node.insert(7, 0.1, 3)
    return node


class NodeTest(unittest.TestCase):
    def test_contains_key_not_in_node(self):
        node = complicated_node()
        self.assertFalse(0 in node)

    def test_contains_key_in_node(self):
        node = complicated_node()
        self.assertTrue(1 in node)

    def test_insert_no_children(self):
        with open(answers_folder / "no_children.json") as answer_file:
            self.assertEqual(json.loads(answer_file.read(), cls=Node.NodeJSONDecoder), Node(1, "value", 1))

    def test_insert_only_left_child(self):
        root = Node(1, 0, 1).insert(0, 0, 0)
        with open(answers_folder / "only_left_child.json") as answer_file:
            self.assertEqual(json.loads(answer_file.read(), cls=Node.NodeJSONDecoder), root)

    def test_insert_only_right_child(self):
        root = Node(0, 0, 0).insert(-1, 0, 1)
        with open(answers_folder / "only_right_child.json") as answer_file:
            self.assertEqual(json.loads(answer_file.read(), cls=Node.NodeJSONDecoder), root)

    def test_insert_both_children(self):
        with open(answers_folder / "complicated_tree.json") as answer_file:
            self.assertEqual(json.loads(answer_file.read(), cls=Node.NodeJSONDecoder), complicated_node())

    def test_update(self):
        node = complicated_node()
        node.update(3, 4)
        self.assertNotEqual(node.get(3), "123")
        self.assertEqual(node.get(3), 4)

    def test_remove(self):
        node = complicated_node()
        node = node.remove(1)
        self.assertFalse(1 in node)

    def test_get(self):
        node = complicated_node()
        self.assertEqual(node.get(7), 0.1)

    def test_iterator_no_children(self):
        node = Node(1, 1, 1)
        self.assertEqual(list(node), [1])

    def test_iterator(self):
        node = complicated_node()
        self.assertEqual(list(node), ['123', 'val1', 'val2', '3', 6, 'text', 0.1])

    def test_reversed_no_children(self):
        node = Node(1, 1, 1)
        self.assertEqual(list(reversed(node)), [1])

    def test_reversed(self):
        node = complicated_node()
        self.assertEqual(list(reversed(node)), ['3', 'val2', 'val1', 'text', 0.1, 6, '123'])
