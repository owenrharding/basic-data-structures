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

from warmup.warmup import * 

def test_main_character_performance(num_elements: int):
    """
    Test the performance of the main_character function with a specified number of random integers.
    
    :param num_elements: The number of random integers to generate for the test.
    """
    # Generate a list of `num_elements` random integers in the range [0, 2^32 - 1]
    #random.seed(42)  # Seed for reproducibility
    input_list = [random.randint(0, 2**32 - 1) for _ in range(num_elements)]

    # Insert a duplicate value randomly to test finding the first repeated integer
    if num_elements > 1:
        duplicate_index = random.randint(1, num_elements - 1)
        input_list[duplicate_index] = input_list[duplicate_index - 1]

    # Start the timer
    start_time = time.time()

    # Call the main_character function
    result = main_character(input_list)

    # End the timer
    end_time = time.time()
    
    # Print the results
    print(f"First repeated integer found at index: {result}")
    print(f"Test with {num_elements} elements completed in: {end_time - start_time:.4f} seconds")

def test_missing_odds_performance(test_size: int):
    """
    Function to test the missing_odds function with different input sizes.
    
    @param test_size: the size of the test input list.
    """

    # Generate a list of random distinct integers within a reasonable range based on the test size
    if test_size <= 10_000:
        max_value = 10_000
    elif test_size <= 300_000:
        max_value = 1_000_000
    else:
        max_value = 10 ** 16

    inputs = random.sample(range(0, max_value), test_size)

    # Output for manual review
    print(f"=== Testing with {test_size} elements...")

    # Start timing
    start_time = time.time()

    # Call the missing_odds function
    result = missing_odds(inputs)

    # End timing
    end_time = time.time()

    # Basic checks with known values
    if test_size <= 10_000:
        # These checks are only applicable to small sizes for manual verification.
        assert missing_odds([1, 2]) == 0
        assert missing_odds([1, 3]) == 0
        assert missing_odds([1, 4]) == 3
        assert missing_odds([4, 1]) == 3
        assert missing_odds([4, 1, 8, 5]) == 10

    # Print the result for the large input test
    print(f"Result for {test_size} elements: {result}")

    # Calculate the time taken
    time_taken = end_time - start_time
    print(f"Time taken for {test_size} elements: {time_taken:.6f} seconds.\n")

def test_main_character():
    """
    A simple set of tests for the main character problem.
    This is not marked and is just here for you to test your code.
    """
    list = [1,2,2,3,4,5]
    print(main_character(list))

    print(main_character([60000, 120000, 654321, 999, 1337, 133731337]))

    print("===== Testing main_character performace with 10 random integers...")
    test_main_character_performance(10)

    print("===== Testing main_character performace with 1000 random integers...")
    test_main_character_performance(1000)

    print("===== Testing main_character performace with 10000 random integers...")
    test_main_character_performance(10000)

    print("===== Testing main_character performace with 300000 random integers...")
    test_main_character_performance(300000)

    print("===== Testing main_character performace with 5000000 random integers...")
    test_main_character_performance(5000000)

def test_missing_odds():
    """
    A simple set of tests for the missing odds problem.
    This is not marked and is just here for you to test your code.
    """
    test_missing_odds_performance(10000)   # It works case
    test_missing_odds_performance(300000)  # Exhaustive case
    test_missing_odds_performance(5000000)  # Welcome to COMP3506 case

def test_k_cool():
    """
    A simple set of tests for the k cool problem.
    This is not marked and is just here for you to test your code.
    """

def test_number_game():
    """
    A simple set of tests for the number game problem.
    This is not marked and is just here for you to test your code.
    """

def test_road_illumination():
    """
    A simple set of tests for the road illumination problem.
    This is not marked and is just here for you to test your code.
    """

# The actual program we're running here
if __name__ == "__main__":
    # Get and parse the command line arguments
    parser = argparse.ArgumentParser(description="COMP3506/7505 Assignment One: Testing Warmup Problems")

    parser.add_argument("--character", action="store_true", help="Test your main character sol.")
    parser.add_argument("--odds", action="store_true", help="Test your missing odds sol.")
    parser.add_argument("--kcool", action="store_true", help="Test your k-cool sol.")
    parser.add_argument("--numbergame", action="store_true", help="Test your number game sol.")
    parser.add_argument("--road", action="store_true", help="Test your road illumination sol.")
    parser.add_argument("--seed", type=int, default='42', help="Seed the PRNG.")
    args = parser.parse_args()

    # No arguments passed
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(-1)

    # Seed the PRNG in case you are using randomness
    random.seed(args.seed)

    # Now check/run the selected algorithm
    if args.character:
        test_main_character()

    if args.odds:
        test_missing_odds()

    if args.kcool:
        test_k_cool()

    if args.numbergame:
        test_number_game()

    if args.road:
        test_road_illumination()

