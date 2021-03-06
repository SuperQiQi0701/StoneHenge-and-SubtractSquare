""" implement stack ADT
"""
from typing import Any


class Stack:
    """ Last-in, first-out (LIFO) stack.
    """

    def __init__(self) -> None:
        """ Create a new, empty Stack self.

        >>> s = Stack()
        """
        self.contains = []

    def add(self, obj: Any) -> None:
        """ Add object obj to top of Stack self.

        >>> s = Stack()
        >>> s.add(5)
        """
        self.contains.append(obj)

    def remove(self) -> Any:
        """
        Remove and return top element of Stack self.

        Assume Stack self is not emp.

        >>> s = Stack()
        >>> s.add(5)
        >>> s.add(7)
        >>> s.remove()
        7
        """
        return self.contains.pop()

    def is_empty(self) -> bool:
        """
        Return whether Stack self is empty.

        >>> s = Stack()
        >>> s.is_empty()
        True
        >>> s.add(5)
        >>> s.is_empty()
        False
        """
        return len(self.contains) == 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()
