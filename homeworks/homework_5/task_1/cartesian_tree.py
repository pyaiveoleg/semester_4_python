from collections.abc import MutableMapping
from typing import Optional, Iterator, Any

from homeworks.homework_5.task_1.node import Node


class CartesianTree(MutableMapping):
    def __init__(self):
        self.size: int = 0
        self.root: Optional[Node] = None

    def __getitem__(self, key) -> Any:
        """
        Get value by key, raises error if no such key
        """
        if self.root is None:
            raise KeyError("Tree is empty")
        if key not in self:
            raise KeyError("There is no such key in the tree")
        return self.root.get(key)

    # MutableMapping interface
    def __setitem__(self, key: Any, value: Any) -> None:
        """
        Add pair of key-value to tree
        """
        if self.root is None:
            self.root = Node(key, value)
        if key in self:
            self.root.update(key, value)
        else:
            self.root = self.root.insert(key, value)
            self.size += 1

    def __delitem__(self, key) -> None:
        """
        Delete pair of key-value by key
        """
        if self.root is None:
            raise KeyError("Tree is empty")
        if key not in self:
            raise KeyError(f"There is no such key in the tree")
        self.root = self.root.remove(key)
        self.size -= 1

    # Iterators
    def __iter__(self) -> Iterator[Any]:
        """
        Generator: pre-order tree transversal
        """
        if self.root is None:
            return
        yield from self.root

    def __reversed__(self) -> Iterator[Any]:
        """
        Generator: post-order tree transversal
        """
        if self.root is None:
            return
        yield from reversed(self.root)

    # Checking key with 'in' operator
    def __contains__(self, key) -> bool:
        """
        Checking if key in tree using 'in' operator
        """
        return self.root is not None and key in self.root

    def __str__(self) -> str:
        """
        String representation of tree
        """
        return str(self.root)

    def __len__(self) -> int:
        """
        Size of tree
        """
        return self.size

    def insert_with_priority(self, key, value, priority) -> None:
        """
        Insert key-value pair with priority. Cannot be achieved using __setitem__, so there is another function for
        add priority
        """
        if key in self:
            raise KeyError("This key is already in the tree")
        if self.root is None:
            self.root = Node(key, value, priority)
        else:
            self.root = self.root.insert(key, value, priority)
        self.size += 1
