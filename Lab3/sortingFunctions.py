"""
sortingFunctions.py
Description: Implementation of sorting algorithms.
"""

import time, random

# Implementation of insertionSort algorithm
def insertionSort(list_to_sort:list) -> list:
    for i in range(len(list_to_sort)):
        # Store the current element at index i
        current_element = list_to_sort[i]
        # Initialize j to i
        j = i
        # Move the element to its correct position in the sorted part of the list
        while j > 0 and list_to_sort[j - 1] > current_element:
        # Shift elements to the right to make space for the current element
            list_to_sort[j] = list_to_sort[j - 1]
        # Move to the previous index
            j -= 1
        # Place the current element in its correct position
        list_to_sort[j] = current_element
    # Return the sorted list (although in-place sorting modifies the original list)
    return list_to_sort

# Implementation of bubbleSort algorithm
def bubbleSort(list_to_sort:list) -> list:
    # Length of the list
    n = len(list_to_sort)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place, so we don't need to traverse them
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if list_to_sort[j] > list_to_sort[j + 1]:
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]
    return list_to_sort

# Returns a random list of the given length
def createRandomList(length:int) -> list:
    return random.sample(range(max(100, length)), length)
    
# Returns the length of time (in seconds) that it took
# for the function_to_run to sort a list of length list_length
def getRuntime(function_to_run, list_length) -> float:
    # Create a new list to sort
    list_to_sort = createRandomList(list_length)
    # Get the time before running
    start_time = time.time()
    # Sort the given list
    function_to_run(list_to_sort)
    # Get the time after running
    end_time = time.time()
    # Return the difference
    return end_time - start_time


if __name__ == '__main__':
    # Test insertionSort() with diff lengths
    print("Insertion Sort:")
    print("100 items:", getRuntime(insertionSort, 100)) #Outcome: 0
    print("1,000 items:", getRuntime(insertionSort, 1000)) #Outcome:0.0378
    print("10,000 items:", getRuntime(insertionSort, 10000)) #Outcome: 3.4986
    
    # Test bubbleSort() with diff lengths
    print("\nBubble Sort:")
    print("100 items:", getRuntime(bubbleSort, 100)) #Outcome: 0.0010
    print("1,000 items:", getRuntime(bubbleSort, 1000)) #Outcome: 0.0668
    print("10,000 items:", getRuntime(bubbleSort, 10000)) #Outcome: 6.5035

    pass