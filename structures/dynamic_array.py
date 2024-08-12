"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov
"""

from typing import Any

INIT_CAPACITY = 8

class DynamicArray:
    def __init__(self) -> None:
        self._capacity = INIT_CAPACITY
        self._start = INIT_CAPACITY // 2
        self._end = self._start - 1
        self._data = [None] * INIT_CAPACITY
        self._reverse = False

    def __str__(self) -> str:
        """
        A helper that allows you to print a DynamicArray type
        via the str() method.
        """
        currentArray = []
        index = self._start
        while index <= self._end:
            currentArray.append(str(self._data[index]))
            index += 1
        return ', '.join(currentArray)

    def __resize(self) -> None:
        """
        Resizes array capacity to include more null space either size of the
        logical array.
        """
        # Double list capacity.
        self._capacity *= 2

        # Create a new (larger) list for old data to be copied into.
        dataCopy = [None] * self._capacity

        # Copy data leaving equal buffer room either side.
        arraySize = self.get_size()
        newStart = (self._capacity - arraySize) // 2
        newEnd = newStart + arraySize - 1

        index = newStart
        oldArrCursor = 0
        while index <= newEnd:
            dataCopy[index] = self._data[self._start + oldArrCursor]
            index += 1
            oldArrCursor += 1

        # Set new DynamicArray data.
        self._data = dataCopy
        self._start = newStart
        self._end = newEnd

    def get_at(self, index: int) -> Any | None:
        """
        Get element at the given index.
        Return None if index is out of bounds.
        Time complexity for full marks: O(1)
        """
        element = None
        offsetIndex = index + self._start

        if offsetIndex >= self._start and offsetIndex <= self._end:
            element = self._data[offsetIndex]

        return element

    def __getitem__(self, index: int) -> Any | None:
        """
        Same as get_at.
        Allows to use square brackets to index elements.
        """
        element = None
        offsetIndex = index + self._start

        if offsetIndex >= self._start and offsetIndex <= self._end:
            element = self._data[offsetIndex]

        return element

    def set_at(self, index: int, element: Any) -> None:
        """
        Set element at the given index.
        Do not modify the list if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        offsetIndex = index + self._start
        
        if offsetIndex >= self._start and offsetIndex <= self._end:
            self._data[index] = element

    def __setitem__(self, index: int, element: Any) -> None:
        """
        Same as set_at.
        Allows to use square brackets to index elements.
        """
        offsetIndex = index + self._start

        if offsetIndex >= self._start and offsetIndex <= self._end:
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
        self._data[self._end + 1] = element

        # Increase array size.
        self._end += 1

    def prepend(self, element: Any) -> None:
        """
        Add an element to the front of the array.
        Time complexity for full marks: O(1*)
        """
        # Resize if there is no remaining space for element to be appended.
        if self.is_full():
            self.__resize()
        
        # Set element at next available index.
        self._data[self._start - 1] = element

        # Increase array size.
        self._start -= 1

    def reverse(self) -> None:
        """
        Reverse the array.
        Time complexity for full marks: O(1)
        """
        self._reverse = not self._reverse

    def remove(self, element: Any) -> None:
        """
        Remove the first occurrence of the element from the array.
        If there is no such element, leave the array unchanged.
        Time complexity for full marks: O(N)
        """
        found = False

        # Iterate through data, comparing to given element.
        index = 0
        while (index + self._start) <= self._end:
            if self._data[index + self._start] == element:
                found = True
                break
            index += 1

        if found:
            self.remove_at(index)

    def remove_at(self, index: int) -> Any | None:
        """
        Remove the element at the given index from the array and return the 
        removed element.
        If there is no such element, leave the array unchanged and return None.
        Time complexity for full marks: O(N)
        """
        element = None
        offsetIndex = index + self._start

        if offsetIndex >= self._start and offsetIndex <= self._end:
            element = self._data[offsetIndex]

            # Replace element with following one, and repeat for all following
            # elements.
            while offsetIndex <= self._end :
                self._data[offsetIndex] = self._data[offsetIndex + 1]
                offsetIndex += 1

            # After all elements have been shifted, element at border of size
            # has been copied down and needs to be set to None.
            self._data[self._end] = None

            self._end -= 1

        return element

    def is_empty(self) -> bool:
        """
        Boolean helper to tell us if the structure is empty or not
        Time complexity for full marks: O(1)
        """
        empty = False

        if self._start == self._end:
            empty = True

        return empty

    def is_full(self) -> bool:
        """
        Boolean helper to tell us if the structure is full or not
        Time complexity for full marks: O(1)
        """
        full = False
        
        if self._start == 0 or self._end == (self._capacity - 1): # -1 for index
            full = True

        return full

    def get_size(self) -> int:
        """
        Return the number of elements in the list
        Time complexity for full marks: O(1)
        """
        return self._end - self._start + 1

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
        if self.get_size() < 2:
            return # List is already sorted.

        # Copy logical array to new list to make indexing easier.
        offset = self._start
        dataCopy = [None] * self.get_size()

        for index in range(self.get_size()):
            dataCopy[index] = self._data[index + offset]

        middle = self.get_size() // 2

        size1 = middle
        size2 = self.get_size() - middle

        # Declare two new arrays for old array to be split in half into.
        list1 = [None] * size1
        list2 = [None] * size2

        # Variables for array traversal.
        cursor = 0
        i = j = 0

        # Copy first half of logical array to list1.
        while i < size1:
            list1[i] = dataCopy[cursor]
            i += 1
            cursor += 1

        # Copy second half of logical array to list2.
        while j < size2:
            list2[j] = dataCopy[cursor]
            j += 1
            cursor += 1

        # Sort two halves recursively.
        self.sort(list1)
        self.sort(list2)

        # Merge results.
        self.merge(list1, list2, dataCopy)
            

    def merge(self, list1: list, list2: list) -> list:
        """
        Merge two sorted lists together, with the merged lists also being
        sorted.
        """
        i = j = 0

        while i + j < 
