"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov

NOTE: This file is not used for assessment. It is just a driver program for
you to write your own test cases and execute them against your data structures.
"""

# Import helper libraries
import random
import sys
import time
import argparse

# Import our data structures
from structures.linked_list import Node, DoublyLinkedList
from structures.dynamic_array import DynamicArray 
from structures.bit_vector import BitVector

def test_linked_list():
    """
    A simple set of tests for the linked list implementation.
    This is not marked and is just here for you to test your code.
    """
    print ("==== Executing Linked List Tests ====")

    # Consider expanding these tests into your own methods instead of
    # just doing a bunch of stuff here - this is just to get you started
    
    # OK, let's add some strings to a list
    my_list = DoublyLinkedList()
    assert(my_list.get_size() == 0)

    my_list.insert_to_front("hello")
    assert(my_list.get_size() == 1)

    my_list.insert_to_back("algorithms")
    assert(my_list.get_size() == 2)

    # Have a look - we can do this due to overriding __str__ in the class
    print(str(my_list))

    # Now lets try to find a node
    print("Searching for element containing \"algorithms\"...")
    elem = my_list.find_element("algorithms")
    if elem is not None:
        print ("Found node with data \"algorithms\"")

    # And try to delete one
    print("Searching for element containing \"1337\"...")
    elem = my_list.find_and_remove_element("1337")
    if elem is not None:
        print ("Deleted node with data \"1337\"")
    else:
        print ("Didn't find element = 1337")

    # And try to delete another one
    print("Searching for element containing \"hello\"...")
    elem = my_list.find_and_remove_element("hello")
    if elem is not None:
        print ("Deleted node with data \"hello\"")
    else:
        print ("Didn't find element = hello")

    # Have another look
    print(str(my_list))

    # OK, now check size
    print("Checking list is size 1...")
    assert(my_list.get_size() == 1)

    # Check reverse.
    print("Checking reverse cases...")
    print("Unreversed list:", str(my_list))
    my_list.reverse()
    print("Reversed list:", str(my_list))
    my_list.reverse() # Return list to original state.

    # Add to list to observe reversing.
    my_list.insert_to_back("first")
    my_list.insert_to_back("second")
    my_list.insert_to_back("third")
    print(str(my_list))

    # Reverse and check.
    my_list.reverse()
    print("Reversed:", str(my_list))

    # Check insert_to_front/back with reversal.
    print("Inserting to front of reversed list...")
    my_list.insert_to_front("Front")
    print(str(my_list))

    print("Inserting to back of reversed list...")
    my_list.insert_to_back("Back")
    print(str(my_list))

    # Re-reverse and check insert_to_front/back.


def test_dynamic_array():
    """
    A simple set of tests for the dynamic array implementation.
    This is not marked and is just here for you to test your code.
    """
    print ("==== Executing Dynamic Array Tests ====")
    
##### INITIALISE TEST ##########################################################
    print("Initialising Dynamic Array...")
    arr = DynamicArray()
    if arr is not None:
        print("  -> Successfully initialised.")

##### APPEND TEST ##############################################################
    appending = ['a', 'b', 'c', 'd', 'e']
    print("Appending the elements:", end=" ")
    for element in appending:
        if element is not appending[-1]:
            print('\'' + element + '\',', end=" ")
    print('\'' + appending[-1] + '\'...')
    
    for element in appending:
        arr.append(element)
        print("  -> Successfully appended", '\'' + element + '\'.')

    print("Current array:")
    print(str(arr))

##### PREPEND TEST #############################################################
    prepending = ['1', '2', '3']
    print("Prepending the elements:", end=" ")
    for element in prepending:
        if element is not prepending[-1]:
            print('\'' + element + '\',', end=" ")
    print('\'' + prepending[-1] + '\'...')

    for element in prepending:
        arr.prepend(element)
        print("  -> Successfully prepended", '\'' + element + '\'.')

    print("Current array:")
    print(str(arr))

def test_bitvector():
    """
    A simple set of tests for the bit vector implementation.
    This is not marked and is just here for you to test your code.
    """
    print ("==== Executing Bit Vector Tests ====")



# The actual program we're running here
if __name__ == "__main__":
    # Get and parse the command line arguments
    parser = argparse.ArgumentParser(description="COMP3506/7505 Assignment One: Testing Data Structures")

    parser.add_argument("--linkedlist", action="store_true", help="Test your linked list.")
    parser.add_argument("--dynamicarray", action="store_true", help="Test your dynamic array.")
    parser.add_argument("--bitvector", action="store_true", help="Test your bit vector.")
    parser.add_argument("--seed", type=int, default='42', help="Seed the PRNG.")
    
    args = parser.parse_args()

    # No arguments passed
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(-1)

    # Seed the PRNG in case you are using randomness
    random.seed(args.seed)

    # Now check/run the selected algorithm
    if args.linkedlist:
        test_linked_list()

    if args.dynamicarray:
        test_dynamic_array()

    if args.bitvector:
        test_bitvector()

