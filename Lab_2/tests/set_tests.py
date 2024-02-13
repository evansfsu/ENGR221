"""
Author: Evan Schneider

Modified from doc given by Prof. Kubota

MySet part 2, code from pseudo code in same file as test to fix issues.
"""

import pytest

class MySet:
    def __init__(self, values=[]): #Constructer for MySet
        self.__s = []       # Initialize an empty list to store values in the set
        self.__size = 0     # Initialize the size of the set to 0
        for value in values:
            if value not in self.__s:
                # Add unique values from input list to the set
                self.__s.append(value)
                self.__size += 1

    def search(self, value):
        for item in self.__s:
            if item == value:
                return True
        return False

    def insert(self, value):
        if not self.search(value):
            # Add value to the set if it's not already present
            self.__s.append(value)
            self.__size += 1

    def delete(self, value):
        for item in self.__s:
            if item == value:
                # Remove the value from the set if found
                self.__s.remove(value)
                self.__size -= 1
                return True
        return False

    def traverse(self):
        for item in self.__s:
            print(item)

    def size(self):
        return self.__size #return suze

    def vals(self):
        return self.__s #return set values


# Doing same correction as array_tests.py by having code and tests in same file.
            

@pytest.mark.settest1
def test_init_set(vals=[1, 2, 3]):
    s = MySet(vals)
    assert (s.size() == 3 and set(s.vals()) == set([1, 2, 3]))

@pytest.mark.settest1
def test_init_set_dups(vals=[0, 0, 0, 0]):
    s = MySet(vals)
    assert (s.size() == 1 and set(s.vals()) == set([0]))

@pytest.mark.settest2
def test_search_set(vals=['E', 'N', 'G', 'R', 2, 1]):
    s = MySet(vals)
    assert s.search('E')

@pytest.mark.settest2
def test_search_set_absent(vals=['E', 'N', 'G', 'R', 2, 1]):
    s = MySet(vals)
    assert not s.search(0)

@pytest.mark.settest3
def test_insert_set():
    s = MySet(['E', 'N', 'G', 'R', 2, 1])
    s.insert('!')
    assert (s.size() == 7 and set(s.vals()) == set(['E', 'N', 'G', 'R', 2, 1, '!']))

@pytest.mark.settest3
def test_insert_set_empty():
    s = MySet([])
    s.insert(0)
    assert (s.size() == 1 and set(s.vals()) == set([0]))

@pytest.mark.settest3
def test_insert_set_dups():
    s = MySet(['E', 'N', 'G', 'R', 2, 1])
    s.insert(2)
    assert (s.size() == 6 and set(s.vals()) == set(['E', 'N', 'G', 'R', 2, 1]))

@pytest.mark.settest4
def test_delete_set():
    s = MySet(['E', 'N', 'G', 'R', 2, 1])
    s.delete(2)
    assert (s.size() == 5 and set(s.vals()) == set(['E', 'N', 'G', 'R', 1]))

@pytest.mark.settest4
def test_delete_set_absent():
    s = MySet(['E', 'N', 'G', 'R', 2, 1])
    s.delete(0)
    assert (s.size() == 6 and set(s.vals()) == set(['E', 'N', 'G', 'R', 2, 1]))

@pytest.mark.settest5
def test_traverse_set(capfd):
    s = MySet(['E', 'N', 'G', 'R', 2, 1])
    s.traverse()
    out, err = capfd.readouterr()
    assert out == "E\nN\nG\nR\n2\n1\n"