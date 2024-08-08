"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov
"""

from typing import Any

INIT_CAPACITY = 8

class DynamicArray:
    def __init__(self) -> None:
        self._size = 0
        self._capacity = INIT_CAPACITY
        self._data = [None] * INIT_CAPACITY

    def __str__(self) -> str:
        """
        A helper that allows you to print a DynamicArray type
        via the str() method.
        """
        pass

    def __resize(self) -> None:
        # Double list capacity.
        self._capacity *= 2

        # Create a new (larger) list for old data to be copied into.
        dataCopy = [None] * self._capacity

        # Copy data.
        for index, element in enumerate(self._data):
            dataCopy[index] = element

        # Set new DynamicArray data.
        self._data = dataCopy

    def get_at(self, index: int) -> Any | None:
        """
        Get element at the given index.
        Return None if index is out of bounds.
        Time complexity for full marks: O(1)
        """
        element = None

        if index < self._size:
            element = self._data[index]

        return element

    def __getitem__(self, index: int) -> Any | None:
        """
        Same as get_at.
        Allows to use square brackets to index elements.
        """
        element = None

        if index < self._size:
            element = self._data[index]

        return element

    def set_at(self, index: int, element: Any) -> None:
        """
        Set element at the given index.
        Do not modify the list if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if index < self._size:
            self._data[index] = element

    def __setitem__(self, index: int, element: Any) -> None:
        """
        Same as set_at.
        Allows to use square brackets to index elements.
        """
        if index < self._size:
            self._data[index] = element

    def append(self, element: Any) -> None:
        """
        Add an element to the back of the array.
        Time complexity for full marks: O(1*) (* means amortized)
        """
        # Resize if there is no remaining space for element to be appended.
        if self.is_full():
            self.__resize()
        
        # Set element at next available index.
        self._data[self._size] = element

        # Increase array size.
        self._size++

    def prepend(self, element: Any) -> None:
        """
        Add an element to the front of the array.
        Time complexity for full marks: O(1*)
        """
        pass

    def reverse(self) -> None:
        """
        Reverse the array.
        Time complexity for full marks: O(1)
        """
        pass

    def remove(self, element: Any) -> None:
        """
        Remove the first occurrence of the element from the array.
        If there is no such element, leave the array unchanged.
        Time complexity for full marks: O(N)
        """
        found = None

        # Iterate through data, comparing to given element.
        for index, item in enumerate(self._data):
            if item == element:
                found = index

        if found is not None:
            self.remove_at(index)

    def remove_at(self, index: int) -> Any | None:
        """
        Remove the element at the given index from the array and return the removed element.
        If there is no such element, leave the array unchanged and return None.
        Time complexity for full marks: O(N)
        """
        element = None

        if index < self._size:
            element = self._data[index]

            # Replace element with following one, and repeat for all following
            # elements.
            while index < (self._size - 1):
                self._data[index] = self._data[index + 1]
                index++

            # After all elements have been shifted, element at border of size
            # has been copied down and needs to be set to None.
            self._data[self._size] = None

            self._size--

        return element

    def is_empty(self) -> bool:
        """
        Boolean helper to tell us if the structure is empty or not
        Time complexity for full marks: O(1)
        """
        empty = False

        if self._size == 0:
            empty = True

        return empty

    def is_full(self) -> bool:
        """
        Boolean helper to tell us if the structure is full or not
        Time complexity for full marks: O(1)
        """
        full = False
        
        if self._size == self._capacity:
            full = True

        return True

    def get_size(self) -> int:
        """
        Return the number of elements in the list
        Time complexity for full marks: O(1)
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the total capacity (the number of slots) of the list
        Time complexity for full marks: O(1)
        """
        return self._capacity

    def sort(self) -> None:
        """
        Sort elements inside _data based on < comparisons.
        Time complexity for full marks: O(NlogN)
        """
        pass
