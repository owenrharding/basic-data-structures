"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov
"""

# so we can hint Node get_next
from __future__ import annotations

from typing import Any


class Node:
    """
    A simple type to hold data and a next pointer
    """

    def __init__(self, data: Any) -> None:
        self._data = data  # This is the payload data of the node
        self._next = None  # This is the "next" pointer to the next Node
        self._prev = None  # This is the "previous" pointer to the previous Node

    def set_data(self, data: Any) -> None:
        self._data = data

    def get_data(self) -> Any:
        return self._data

    def set_next(self, node: Node, reverse: bool) -> None:
        if reverse is not True:
            self._next = node
        else:
            self._prev = node

    def get_next(self, reverse: bool) -> Node | None:
        if reverse is not True:
            return self._next
        else:
            return self._prev

    def set_prev(self, node: Node, reverse: bool) -> None:
        if reverse is not True:
            self._prev = node
        else:
            self._next = node

    def get_prev(self, reverse: bool) -> Node | None:
        if reverse is not True:
            return self._prev
        else:
            return self._next


class DoublyLinkedList:
    """
    Your doubly linked list code goes here.
    Note that any time you see `Any` in the type annotations,
    this refers to the "data" stored inside a Node.

    [V3: Note that this API was changed in the V3 spec] 
    """

    def __init__(self) -> None:
        # You probably need to track some data here...
        self._size = 0
        self._head = None
        self._tail = None
        self._reverse = False

    def __str__(self) -> str:
        """
        A helper that allows you to print a DoublyLinkedList type
        via the str() method.
        """
        list = []
        cursor = self.get_head()

        while cursor is not None:
            list.append(str(cursor.get_data()))
            cursor = cursor.get_next(self._reverse)

        return "<->".join(list)

    """
    Simple Getters and Setters below
    """

    def get_size(self) -> int:
        """
        Return the size of the list.
        Time complexity for full marks: O(1)
        """
        return self._size

    def set_size(self, size: int) -> int:
        """
        Set the size of the list.
        Unassessed function.
        """
        self._size = size

    def mod_size(self, mod: int) -> int:
        """
        Modifies (increment/decrements) the size of the list by a given value.
        Unassessed function.
        """
        self._size += mod

    def get_head_node(self) -> Any | None:
        """
        Returns a pointer to the current head node.
        """
        if self._reverse is not True:
            return self._head
        else:
            return self._tail

    def get_tail_node(self) -> Any | None:
        """
        Returns a pointer to the current tail node.
        """
        if self._reverse is not True:
            return self._tail
        else:
            return self._head

    def get_head(self) -> Any | None:
        """
        Return the data of the leftmost node in the list, if it exists.
        Time complexity for full marks: O(1)
        """
        if self._reverse is not True:
            return self._head
        else:
            return self._tail

    def set_head(self, data: Any) -> None:
        """
        Replace the leftmost node's data with the given data.
        If the list is empty, do nothing.
        Time complexity for full marks: O(1)
        """
        if self.get_head() is not None: # Only set data if a node exists.
            self.get_head().set_data(data)

    def get_tail(self) -> Any | None:
        """
        Return the data of the rightmost node in the list, if it exists.
        Time complexity for full marks: O(1)
        """
        if self._reverse is not True:
            return self._tail
        else:
            return self._head

    def set_tail(self, data: Any) -> None:
        """
        Replace the rightmost node's data with the given data.
        If the list is empty, do nothing.
        Time complexity for full marks: O(1)
        """
        if self.get_tail() is not None: # Only set data if a node exists.
            self.get_tail().set_data(data)

    def toggle_reverse_flag(self) -> None:
        """
        Toggles the class local reverse flag (on -> off / off -> on).
        """
        self._reverse = not self._reverse

    """
    More interesting functionality now.
    """

    def insert_to_front(self, data: Any) -> None:
        """
        Insert the given data to the front of the list.
        Hint: You will need to create a Node type containing
        the given data.
        Time complexity for full marks: O(1)
        """
        newHead = Node(data)
        oldHead = self.get_head()

        # Modify the previous head to reference the new head.
        if oldHead is not None:
            oldHead.set_prev(newHead, self._reverse)
            newHead.set_next(oldHead, self._reverse)
        else:
            self._head = newHead
            self._tail = newHead

        # Set new head node.
        if self._reverse is not True:
            self._head = newHead
        else:
            self._tail = newHead
        self.mod_size(1)

    def insert_to_back(self, data: Any) -> None:
        """
        Insert the given data (in a node) to the back of the list
        Time complexity for full marks: O(1)
        """
        newTail = Node(data)
        oldTail = self.get_tail()

        # Modify the previous tail to reference the new tail.
        if oldTail is not None:
            oldTail.set_next(newTail, self._reverse)
            newTail.set_prev(oldTail, self._reverse)
        else:
            self._head = newTail
            self._tail = newTail

        # Set new tail node.
        if self._reverse is not True:
            self._tail = newTail
        else:
            self._head = newTail
        self.mod_size(1)

    def remove_from_front(self) -> Any | None:
        """
        Remove the front node, and return the data it holds.
        Time complexity for full marks: O(1)
        """
        data = None

        if self.get_head() is not None:
            oldHead = self.get_head()

            # Remove reference to original head.
            if oldHead.get_next() is not None:
                newHead = oldHead.get_next()
                newHead.set_prev(None, self._reverse)
                # Set new head.
                if self._reverse is not True:
                    self._head = newHead
                else:
                    self._tail = newHead
            else:
                if self._reverse is not True:
                    self._head = None
                else:
                    self._tail = None

            # Return original head data.
            data = oldHead.get_data()

            # Decrease list size by 1.
            self.mod_size(-1)

        return data


    def remove_from_back(self) -> Any | None:
        """
        Remove the back node, and return the data it holds.
        Time complexity for full marks: O(1)
        """
        data = None

        if self.get_tail() is not None:
            oldTail = self.get_tail()

            # Remove reference to original tail.
            if oldTail.get_prev(self._reverse) is not None:
                newTail = oldTail.get_prev(self._reverse)
                newTail.set_next(None, self._reverse)
                # Set new tail.
                if self._reverse is not True:
                    self._tail = newTail
                else:
                    self._head = newTail
            else:
                if self._reverse is not True:
                    self._tail = None
                else:
                    self._head = None

            # Return original tail data.
            data = oldTail.get_data()

            # Decrease list size by 1.
            self.mod_size(-1)

        return data

    def find_element(self, elem: Any) -> bool:
        """
        Looks at the data inside each node of the list and returns True
        if a match is found; False otherwise.
        Time complexity for full marks: O(N)
        """
        elementFound = False
        nodeCursor = self.get_head()

        # Loop through all nodes and see if data matches desired elem.
        while elementFound is not True and nodeCursor is not None: # Cursor = None = End
            if nodeCursor.get_data() == elem:
                elementFound = True
                break
            # Set cursor as next node in the sequence.
            nodeCursor = nodeCursor.get_next(self._reverse)

        return elementFound

    def find_and_remove_element(self, elem: Any) -> bool:
        """
        Looks at the data inside each node of the list; if a match is
        found, this node is removed from the linked list, and True is returned.
        False is returned if no match is found.
        Time complexity for full marks: O(N)
        """
        elementFound = False
        nodeCursor = self.get_head()

        # Loop through all nodes and see if data matches desired elem.
        while elementFound is not True and nodeCursor is not None:

            if nodeCursor.get_data() == elem:
                elementFound = True

                # Overwrite references to to-be-removed node with references to
                # the nodes either side of it (rejoining linked list).
                nodeToLeft = nodeCursor.get_prev(self._reverse)
                nodeToRight = nodeCursor.get_next(self._reverse)

                if nodeToLeft is not None:
                    nodeToLeft.set_next(nodeToRight, self._reverse)
                else:
                    self._head = nodeToRight

                if nodeToRight is not None:
                    nodeToRight.set_prev(nodeToLeft, self._reverse)
                else:
                    self._tail = nodeToLeft

                # Decrease list size by 1.
                self.mod_size(-1)
            
                # Break out of search loop.
                break

            # Set cursor as next node in the sequence.
            nodeCursor = nodeCursor.get_next(self._reverse)

        return elementFound

    def reverse(self) -> None:
        """
        Reverses the linked list
        Time complexity for full marks: O(1)
        """
        self.toggle_reverse_flag()
