"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov

WARMUP PROBLEMS

 Each problem will be assessed on three sets of tests:

1. "It works":
       Basic inputs and outputs, including the ones peovided as examples, with generous time and memory restrictions.
       Large inputs will not be tested here.
       The most straightforward approach will likely fit into these restrictions.

2. "Exhaustive":
       Extensive testing on a wide range of inputs and outputs with tight time and memory restrictions.
       These tests won't accept brute force solutions, you'll have to apply some algorithms and optimisations.

 3. "Welcome to COMP3506":
       Extensive testing with the tightest possible time and memory restrictions
       leaving no room for redundant operations.
       Every possible corner case will be assessed here as well.

There will be hidden tests in each category that will be published only after the assignment deadline.
"""

"""
You may wish to import your data structures to help you with some of the
problems. Or maybe not. We did it for you just in case.
"""
from structures.bit_vector import BitVector
from structures.dynamic_array import DynamicArray
from structures.linked_list import DoublyLinkedList, Node
import math


def main_character(instring: list[int]) -> int:
    """
    @instring@ is an array of integers in the range [0, 2^{32}-1].
    Return the first position a repeat integer is encountered, or -1 if
    there are no repeated ints.

    Limitations:
        "It works":
            @instring@ may contain up to 10'000 elements.

        "Exhaustive":
            @instring@ may contain up to 300'000 elements.

        "Welcome to COMP3506":
            @instring@ may contain up to 5'000'000 elements.

    Examples:
    main_character([1, 2, 3, 4, 5]) == -1
    main_character([1, 2, 1, 4, 4, 4]) == 2
    main_character([7, 1, 2, 7]) == 3
    main_character([60000, 120000, 654321, 999, 1337, 133731337]) == -1
    """
    bv = BitVector()
    bv._init_zeroes(2**32)

    # By default position of a repeated character is -1.
    pos = -1

    for index, element in enumerate(instring):
        if bv.get_size() < element:
            bv._init_unset_space(element)

        if bv.get_at(element) != 0:
            pos = index
            break
        else:
            # Set it so that there exists an element at the index of the value
            # of the element. Next time that this index is checked, it will not
            # none so we will have found a match.
            bv.set_at(element)
    
    return pos

def missing_odds(inputs: list[int]) -> int:
    """
    @inputs@ is an unordered array of distinct integers.
    If @a@ is the smallest number in the array and @b@ is the biggest,
    return the sum of odd numbers in the interval [a, b] that are not present in @inputs@.
    If there are no such numbers, return 0.

    Limitations:
        "It works":
            @inputs@ may contain up to 10'000 elements.
            Each element is in range 0 <= inputs[i] <= 10^4
        "Exhaustive":
            @inputs@ may contain up to 300'000 elements.
            Each element is in range 0 <= inputs[i] <= 10^6
        "Welcome to COMP3506":
            @inputs@ may contain up to 5'000'000 elements.
            Each element is in range 0 <= inputs[i] <= 10^16

    Examples:
    missing_odds([1, 2]) == 0
    missing_odds([1, 3]) == 0
    missing_odds([1, 4]) == 3
    missing_odds([4, 1]) == 3
    missing_odds([4, 1, 8, 5]) == 10    # 3 and 7 are missing
    """
    max, min = inputs[0], inputs[0]
    inputSumOfOdds = 0

    for element in inputs:
        # Determine max and min elements in the list.
        if element > max:
            max = element
        elif element < min:
            min = element
        
        if element % 2 == 1:
            # Element is odd.
            inputSumOfOdds += element

    # Determine if min and max are odd.
    a, b = min, max
    if min % 2 == 0:
        # Min is even, start at odd number immediately following max.
        a = min + 1
    if max % 2 == 0:
        # Max is even, end at odd number immediately preceding max.
        b = max - 1

    # Calculate what sum of all odds (with none missing) should've been.
    expectedNumOdds = (b - a) / 2 + 1

    expectedSumOfOdds = ((expectedNumOdds) / 2) * (a + b)

    # Sum of missing odds = expected sum of odds - sum of existing odds.
    return int(expectedSumOfOdds - inputSumOfOdds)

def number_game(numbers: list[int]) -> tuple[str, int]:
    """
    @numbers@ is an unordered array of integers. The array is guaranteed to be of even length.
    Return a tuple consisting of the winner's name and the winner's score assuming that both play optimally.
    "Optimally" means that each player makes moves that maximise their chance of winning
    and minimise opponent's chance of winning.
    You are ALLOWED to use a tuple in your return here, like: return (x, y)
    Possible string values are "Alice", "Bob", and "Tie"

    Limitations:
        "It works":
            @numbers@ may contain up to 10'000 elements.
            Each element is in range 0 <= numbers[i] <= 10^6
        "Exhaustive":
            @numbers@ may contain up to 100'000 elements.
            Each element is in range 0 <= numbers[i] <= 10^16
        "Welcome to COMP3506":
            @numbers@ may contain up to 300'000 elements.
            Each element is in range 0 <= numbers[i] <= 10^16

    Examples:
    number_game([5, 2, 7, 3]) == ("Bob", 5)
    number_game([3, 2, 1, 0]) == ("Tie", 0)
    number_game([2, 2, 2, 2]) == ("Alice", 4)

    For the second example, if Alice picks 2 to increase her score, Bob will pick 3 and win. Alice does not want that.
    The same happens if she picks 1 or 0, but this time she won't even increase her score.
    The only scenario when Bob does not win immediately is if Alice picks 3.
    Then, Bob faces the same choice:
    pick 1 to increase his score knowing that Alice will pick 2 and win, or pick 2 himself.
    The same happens on the next move.
    So, nobody picks any numbers to increase their score, which results in a Tie with both players having scores of 0.
    """
    da = DynamicArray()

    # Initialise space for the array.
    da._init_size(len(numbers), None)

    # Copy numbers over to dynamic array.
    for index, element in enumerate(numbers):
        da[index] = element
    
    # Sort dynamic array.
    da.sort()
    
    # Arrange in descending order.
    da.reverse()

    aliceScore, bobScore = 0, 0

    aliceTurn = True
    for i in range(len(numbers)):
        if aliceTurn:
            if da[i] % 2 == 0:
                # Even number.
                aliceScore += da[i]
        else:
            if da[i] % 2 == 1:
                # Odd number.
                bobScore += da[i]

        aliceTurn = not aliceTurn
    
    result = None
    if aliceScore > bobScore:
        result = ("Alice", aliceScore)
    elif bobScore > aliceScore:
        result = ("Bob", bobScore)
    else:
        result = ("Tie", aliceScore)
    
    return result


def road_illumination(road_length: int, poles: list[int]) -> float:
    """
    @poles@ is an unordered array of integers.
    Return a single floating point number representing the smallest possible radius of illumination
    required to illuminate the whole road.
    Floating point numbers have limited precision. Your answer will be accepted
    if the relative or absolute error does not exceed 10^(-6),
    i.e. |your_ans - true_ans| <= 0.000001 OR |your_ans - true_ans|/true_ans <= 0.000001

    Limitations:
        "It works":
            @poles@ may contain up to 10'000 elements.
            0 <= @road_length@ <= 10^6
            Each element is in range 0 <= poles[i] <= 10^6
        "Exhaustive":
            @poles@ may contain up to 100'000 elements.
            0 <= @road_length@ <= 10^16
            Each element is in range 0 <= poles[i] <= 10^16
        "Welcome to COMP3506":
            @poles@ may contain up to 300'000 elements.
            0 <= @road_length@ <= 10^16
            Each element is in range 0 <= poles[i] <= 10^16

    Examples:
    road_illumination(15, [15, 5, 3, 7, 9, 14, 0]) == 2.5
    road_illumination(5, [2, 5]) == 2.0
    """
    da = DynamicArray()

    # Initialise dynamic array to hold road_length elements.
    da._init_size(len(poles), None)

    # Copy poles over to dynamic array.
    for index, pole in enumerate(poles):
        da[index] = pole
    
    da.sort()

    # Find distance from 0 to first pole.
    distFromZero = da[0]

    # Find distance from last pole to end of road.
    distFromEnd = road_length - da[len(poles) - 1]

    # Find the maximum distance between two poles.
    maxDist = 0
    for i in range(len(poles) - 1):
        if (da[i + 1] - da[i]) > maxDist:
            maxDist = da[i + 1] - da[i]
    
    radius = distFromZero

    if distFromEnd > radius:
        radius = distFromEnd

    if (maxDist / 2) > radius:
        radius = (maxDist / 2)
    
    return radius