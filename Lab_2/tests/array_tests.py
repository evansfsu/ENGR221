"""
Author: Evan Schneider

Modified from Prof. Kubota's original 

Array testing from Lab_2
"""

import pytest


class Array():
    # Constructor
    def __init__(self, initialSizeOrValues):
        if isinstance(initialSizeOrValues, int):  # If an integer is provided
            self.__a = [None] * initialSizeOrValues
            self.__length = 0
        elif isinstance(initialSizeOrValues, list):  # If a list is provided
            self.__a = initialSizeOrValues.copy()
            self.__length = len(initialSizeOrValues)
        else:
            raise ValueError("failed on else") # debug helper

    ########
    # Methods
    ########

    # Return the current length of the array
    def length(self):
        return self.__length

    # Return a list of the current array values
    def values(self):
        return self.__a

    # Return the value at index idx
    def get(self, idx):
        if 0 <= idx < self.__length:
            return self.__a[idx]

    # Set the value at index idx
    def set(self, idx, value):
        if 0 <= idx < self.__length:
            self.__a[idx] = value

    # Insert value to the end of the array
    def insert(self, value):
        if self.__length == len(self.__a):  # If the array is full, extend it
            self.__a.append(value)
        else:
            self.__a[self.__length] = value
        self.__length += 1

    # Return the index of value in the array,
    # or -1 if value is not in the array
    def search(self, value):
        for idx in range(self.__length):
            if self.__a[idx] == value:
                return idx
        return -1

    # Delete all occurrences of value in the array
    def delete(self, value):
        deleted = False
        i = 0
        while i < self.__length:
            if self.__a[i] == value:
                self.__length -= 1
                del self.__a[i]
                deleted = True
            else:
                i += 1
        return deleted

    # Print all items in the list
    def traverse(self):
        for i in range(self.__length):
            print(self.__a[i])


## These are pytests for now 
@pytest.mark.arraytest1
def test_init_array_len(len=0):
    a = Array(len)
    assert (a.length() == 0 and a.values() == [])

@pytest.mark.arraytest1
def test_init_array_length_vals(vals=['E', 'N', 'G', 'R', 2, 2, 1]):
    a = Array(vals)
    assert (a.length() == len(vals) and a.values() == vals)

@pytest.mark.arraytest2
def test_insert_array():
    a = Array(['E', 'N', 'G', 'R', 2, 2, 1])
    a.insert('!')
    assert (a.get(7) == '!' and a.length() == 8)

@pytest.mark.arraytest2
def test_insert_empty_array():
    a = Array(0)
    a.insert('Hello')
    assert (a.get(0) == 'Hello' and a.length() == 1)

@pytest.mark.arraytest3
def test_delete_array():
    a = Array(['E', 'N', 'G', 'R', 2, 2, 1])
    a.delete(2)
    assert (a.values() == ['E', 'N', 'G', 'R', 1] and a.length() == 5)

@pytest.mark.arraytest3
def test_delete_array_absent():
    a = Array(['E', 'N', 'G', 'R', 2, 2, 1])
    a.delete(0)
    assert (a.values() == ['E', 'N', 'G', 'R', 2, 2, 1] and a.length() == 7)