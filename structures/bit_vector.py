"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov
"""

from typing import Any

from structures.dynamic_array import DynamicArray
from math import ceil


class BitVector:
    """
    A compact storage for bits that uses DynamicArray under the hood.
    Each element stores up to 64 bits, making BitVector 64 times more memory-efficient
    for storing bits than plain DynamicArray.
    """

    BITS_PER_ELEMENT = 64

    def __init__(self) -> None:
        """
        We will use the dynamic array as our data storage mechanism
        """
        self._data = DynamicArray()
        # you may want or need more stuff here in the constructor
        self._numBits = 0
        self._numWords = 0
        self._startOffset = 0
        self._reverse = False
        self._flip = False

    def __str__(self) -> str:
        """
        A helper that allows you to print a BitVector type
        via the str() method.
        """
        bitVector = []

        for index in range(self._numBits):
            bitVector.append(str(self.get_at(index)))

        return '-'.join(bitVector)

    def __resize(self) -> None:
        pass

    def _resize_and_init_zero(self, n: int) -> None:
        """
        This function is exclusively for use in main_character.
        Doubles the capacity of the bitvectors until by initialising a
        number of new sets of 0s.
        """
        # Doubles number of available bitvector spaces, initialising to 0.
        for i in range(self._numWords):
            self._data.append(0)
            self._numWords += 1
            self._numBits += self.BITS_PER_ELEMENT

    def _init_zeroes(self, capacity: int) -> None:
        """
        This function is exclusively for use in main_character.
        Doubles the capacity of the bitvectors by initialising a
        number of new sets of 0s.
        """
        # Doubles number of available bitvector spaces, initialising to 0.
        self._data._init_size(capacity//self.BITS_PER_ELEMENT + 1, 0)

        self._numBits = (capacity//self.BITS_PER_ELEMENT + 1) * self.BITS_PER_ELEMENT

    def _init_unset_space(self, n: int) -> None:
        """
        Initialises space of unset bits which can hold n bits.
        """
        if n > self._numBits:
            # Calculate number of words needed to accomodate n bits.
            addWords = ceil((n - self._numBits) / 64)

            # Append words.
            for i in range(addWords):
                self._data.append(0)

            # Grow logical size of the array.
            # THIS IS ONLY FOR USE IN MAIN_CHARACTER (NO PREPENDING).
            self._numBits += addWords * self.BITS_PER_ELEMENT

    def _adjust_index(self, index: int) -> int:
        """
        Adjusts the given index for an appropriate logical index based on
        reverse flag.
        """
        adjustedIndex = index

        if self._reverse:
            # Reverse from opposite end.
            adjustedIndex = self._numBits - 1 - index

        return adjustedIndex

    def get_at(self, index: int) -> int | None:
        """
        Get bit at the given index.
        Return None if index is out of bounds.
        Time complexity for full marks: O(1)
        """
        bit = None
        
        if index >= 0 and index < self._numBits:
            # Adjust index for reversal and starting offset.
            adjustedIndex = self._adjust_index(index) + self._startOffset

            # Determine the index of set which contains the desired bit.
            arrayIndex = adjustedIndex // 64

            # Determine the index of the bit within its set of 64.
            bitPosition = adjustedIndex % 64

            # Retrieve set of 64 bits which contains the indexed bit.
            bitSet = self._data.get_at(arrayIndex)

            # Right shift the desired bit to the LSB position and bitwise AND
            # with 1 to extract it.
            # Thank you CSSE3010 for teaching me how to do this.
            bit = (bitSet >> bitPosition) & 1

        if self._flip:
            if bit == 0:
                bit = 1
            else:
                bit = 0

        return bit

    def __getitem__(self, index: int) -> int | None:
        """
        Same as get_at.
        Allows to use square brackets to index elements.
        """
        return self.get_at(index)

    def set_at(self, index: int) -> None:
        """
        Set bit at the given index to 1.
        Do not modify the vector if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if index >= 0 and index < self._numBits:
            # Adjust index for reversal and starting offset.
            adjustedIndex = self._adjust_index(index) + self._startOffset

            # Determine the index of set which contains the desired bit.
            arrayIndex = adjustedIndex // 64

            # Determine the index of the bit within its set of 64.
            bitPosition = adjustedIndex % 64

            # Retrieve set of 64 bits which contains the indexed bit.
            word = self._data.get_at(arrayIndex)

            # Create bitmask with set bit at position of bit to be set.
            setBit = 1 << bitPosition

            # Bitwise OR to set original bit.
            word |= setBit

            # Set new value in self._data.
            self._data.set_at(arrayIndex, word)

    def unset_at(self, index: int) -> None:
        """
        Set bit at the given index to 0.
        Do not modify the vector if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if index >= 0 and index < self._numBits:
            # Adjust index for reversal and starting offset.
            adjustedIndex = self._adjust_index(index) + self._startOffset

            # Determine the index of set which contains the desired bit.
            arrayIndex = adjustedIndex // 64

            # Determine the index of the bit within its set of 64.
            bitPosition = adjustedIndex % 64

            # Retrieve set of 64 bits which contains the indexed bit.
            bitWord = self._data.get_at(arrayIndex)

            # Create bitmask with set bit at position of bit to be set.
            setBit = 1 << bitPosition

            # Bitwise OR to set original bit.
            bitWord &= ~(setBit)

            # Set new value in self._data.
            self._data.set_at(arrayIndex, bitWord)

    def __setitem__(self, index: int, state: int) -> None:
        """
        Set bit at the given index.
        Treat the integer in the same way Python does:
        if state is 0, set the bit to 0, otherwise set the bit to 1.
        Do not modify the vector if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if state == 0:
            self.unset_at(index)
        else:
            self.set_at(index)

    def append(self, state: int) -> None:
        """
        Add a bit to the back of the vector.
        Treat the integer in the same way Python does:
        if state is 0, set the bit to 0, otherwise set the bit to 1.
        Time complexity for full marks: O(1*)
        """
        if not self._reverse:
            if self._numBits % self.BITS_PER_ELEMENT == 0:
                self._data.append(0)
                self._numWords += 1
        else:
            if self._startOffset == 0:
                self._data.prepend(0)
                self._numWords += 1
                self._startOffset = self.BITS_PER_ELEMENT - 1
            else:
                self._startOffset -= 1
        
        self._numBits += 1

        self.__setitem__(self._numBits - 1, state)

    def prepend(self, state: Any) -> None:
        """
        Add a bit to the front of the vector.
        Treat the integer in the same way Python does:
        if state is 0, set the bit to 0, otherwise set the bit to 1.
        Time complexity for full marks: O(1*)
        """
        if not self._reverse:
            if self._startOffset == 0:
                self._data.prepend(0)
                self._startOffset = self.BITS_PER_ELEMENT - 1
            else:
                self._startOffset -= 1
        else:
            if self._numBits % self.BITS_PER_ELEMENT == 0:
                self._data.append(0)
    
        
        self._numBits += 1

        self.__setitem__(0, state)

    def reverse(self) -> None:
        """
        Reverse the bit-vector.
        Time complexity for full marks: O(1)
        """
        self._reverse = not self._reverse

    def flip_all_bits(self) -> None:
        """
        Flip all bits in the vector.
        Time complexity for full marks: O(1)
        """
        self._flip = not self._flip

    def shift(self, dist: int) -> None:
        """
        Make a bit shift.
        If dist is positive, perform a left shift by `dist`.
        Otherwise perform a right shift by `dist`.
        Time complexity for full marks: O(N)
        """
        pass

    def rotate(self, dist: int) -> None:
        """
        Make a bit rotation.
        If dist is positive, perform a left rotation by `dist`.
        Otherwise perform a right rotation by `dist`.
        Time complexity for full marks: O(N)
        """
        pass

    def get_size(self) -> int:
        """
        Return the number of *bits* in the list
        Time complexity for full marks: O(1)
        """
        return self._numBits
