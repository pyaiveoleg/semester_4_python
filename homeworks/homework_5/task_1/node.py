import json
import random
from typing import Tuple, Optional, Any, Iterator
from json import JSONDecoder, JSONEncoder


class Node:
    def __init__(
        self,
        key: float,
        value: Any,
        priority: Optional[float] = None,
        left_child: Optional["Node"] = None,
        right_child: Optional["Node"] = None,
    ):
        self.key = key
        self.value = value
        if priority is None:
            self.priority = random.random()  # random distribution is the best for Cartesian tree
        else:
            self.priority = priority
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self):
        """
        String representation of node
        """
        return json.dumps(self, allow_nan=True, cls=self.NodeJSONEncoder)

    def __eq__(self, other):
        """
        Checks equality of two nodes
        """
        if isinstance(other, Node):
            return self.__dict__ == other.__dict__
        return False

    def __contains__(self, key) -> bool:
        """
        Checking if key in node or its subnodes using 'in' operator
        """
        if self.key == key:
            return True
        if self.left_child is not None and key < self.key:
            return key in self.left_child
        if self.right_child is not None and key > self.key:
            return key in self.right_child
        return False

    def __iter__(self) -> Iterator[Any]:
        """
        Generator: pre-order node transversal
        """
        yield self.value
        if self.left_child is not None:
            yield from self.left_child
        if self.right_child is not None:
            yield from self.right_child

    def __reversed__(self) -> Iterator[Any]:
        """
        Generator: post-order node transversal
        """
        if self.left_child is not None:
            yield from reversed(self.left_child)
        if self.right_child is not None:
            yield from reversed(self.right_child)
        yield self.value

    def get(self, key) -> Any:
        """
        Get value by key or None if there are no such key
        """
        if self.key == key:
            return self.value
        if self.left_child is not None and key < self.key:
            return self.left_child.get(key)
        if self.right_child is not None and key > self.key:
            return self.right_child.get(key)

    def update(self, key, new_value) -> None:
        """
        Change value of element with given key to new_value
        """
        if self.key == key:
            self.value = new_value
        if self.left_child is not None and key < self.key:
            self.left_child.update(key, new_value)
        if self.right_child is not None and key > self.key:
            self.right_child.update(key, new_value)

    def insert(self, key, value, priority: Optional[float] = None) -> "Node":
        """
        Insert new node with given parameters and return it
        """
        new_node = Node(key, value, priority)
        left_child, right_child = self.__split(key)
        if left_child is None:
            return new_node.__merge(right_child)
        left_child = left_child.__merge(new_node)
        return left_child.__merge(right_child)

    def remove(self, key) -> Optional["Node"]:
        """
        Remove node with given key if exists
        """
        left_child, right_child = self.__split(key)
        if right_child is None:
            return left_child
        right_child = right_child.__remove_smallest()
        if left_child is None:
            return right_child
        return left_child.__merge(right_child)

    def __remove_smallest(self) -> Optional["Node"]:
        if self.left_child is None:
            return self.right_child
        self.left_child = self.left_child.__remove_smallest()
        return self

    def __split(self, key) -> Tuple[Optional["Node"], Optional["Node"]]:
        if key > self.key:
            if self.right_child is None:
                return self, None
            left_child, right_child = self.right_child.__split(key)
            result = self
            result.right_child = left_child
            return result, right_child
        else:
            if self.left_child is None:
                return None, self
            left_child, right_child = self.left_child.__split(key)
            result = self
            result.left_child = right_child
            return left_child, result

    def __merge(self, other: Optional["Node"]) -> "Node":
        if other is None:
            return self

        if self.priority > other.priority:
            result = self
            if self.right_child is None:
                result.right_child = other
            else:
                result.right_child = self.right_child.__merge(other)
            return result
        else:
            result = other
            if other.left_child is None:
                result.left_child = self
            else:
                result.left_child = self.__merge(other.left_child)
            return result

    class NodeJSONEncoder(JSONEncoder):
        """
        JSON serializer for Node class
        """

        def default(self, obj):
            if isinstance(obj, Node):
                return obj.__dict__
            return JSONEncoder.default(self, obj)

    class NodeJSONDecoder(JSONDecoder):
        """
        Deserializer from JSON representation
        """

        def __init__(self, *args, **kwargs):
            JSONDecoder.__init__(self, object_hook=lambda dct: Node(**dct), *args, **kwargs)
