"""
Author: Evan Schneider
Modified off of code from Prof. Kabuta 
"""

class Stack():
    def __init__(self):
        self.__items = []

    # Returns True if the Stack is empty, false if not
    def isEmpty(self):
        return len(self.__items) == 0

    # For stack, "push" item to the top
    def add(self, item):
        self.__items.append(item)

    def remove(self):
        if not self.isEmpty():
            return self.__items.pop()
        else:
            return None
    
# Implementation of a Queue
class Queue():
    def __init__(self):
        self.__items = []

    # Returns True if empty, or False if not empty
    def isEmpty(self):
        return len(self.__items) == 0

    # Should "enqueue" item to the end of the Queue
    def add(self, item):
        self.__items.append(item)

    # For Queue, should "dequeue" an item and return it
    def remove(self):
        if not self.isEmpty():
            return self.__items.pop(0)
        else:
            return None
    