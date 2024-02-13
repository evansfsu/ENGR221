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