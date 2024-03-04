"""
Written by Prof Kobuta
Comments by Evan.S
"""

from .doublyLinkedList import DoublyLinkedList

class Deque():
    def __init__(self):
        # Initialize a new Deque.
        self.__values = DoublyLinkedList()

    def isEmpty(self):
        # Check if the Deque is empty.
        # Returns:
        #     bool: True if the Deque is empty, False otherwise.
        return self.__values.isEmpty()
    
    def __len__(self):
        # Get the number of elements in the Deque.
        # Returns:
        # int: The number of elements in the Deque.
        return len(self.__values)
    
    def __str__(self):
        # Get a string representation of the Deque.
        # Returns:
        # str: A string representation of the Deque.
        return str(self.__values)

    def peekLeft(self):
        # Get the value at the left end of the Deque without removing it.
        # Returns:
        # Any: The value at the left end of the Deque.
        return self.__values.first()

    def peekRight(self):
        # Get the value at the right end of the Deque without removing it.
        # Returns:
        # Any: The value at the right end of the Deque.
        return self.__values.getLastNode().getValue()

    def insertLeft(self, value):
        # Insert a value at the left end of the Deque.
        # Args:
        # value (Any): The value to insert.
        self.__values.insertFront(value)
        
    def insertRight(self, value): 
        # Insert a value at the right end of the Deque.
        # Args:
        # value (Any): The value to insert.
        self.__values.insertBack(value)

    def removeLeft(self): 
        # Remove and return the value at the left end of the Deque.
        # Returns:
        # Any: The value at the left end of the Deque.
        return self.__values.deleteFirstNode()

    def removeRight(self):
        # Remove and return the value at the right end of the Deque.
        # Returns:
        # Any: The value at the right end of the Deque.
        return self.__values.deleteLastNode()
    
if __name__ == "__main__":
    pass