"""
Author: Evan Schneider
Modified from code provided by Prof. Kubota
"""

class DoubleNode:
    def __init__(self, value, next=None, previous=None):
        # Initializes a DoubleNode object.
        self.__value = value
        self.__next_node = next  # Store the reference to the next node
        self.__previous_node = previous  # Store the reference to the previous node

    def isFirst(self) -> bool:
        # Checks if the node is the first node in the list.
        return self.__previous_node is None

    def isLast(self) -> bool:
        # Checks if the node is the last node in the list.
        return self.__next_node is None

    def getValue(self):
        # Returns the value of the node.
        return self.__value

    def getNextNode(self):
        # Returns the next node in the list.
        return self.__next_node

    def getPreviousNode(self):
        # Returns the previous node in the list.
        return self.__previous_node

    def setValue(self, new_value) -> None:
        # Sets the value of the node to a new value.
        self.__value = new_value

    def setNextNode(self, new_next) -> None:
        # Sets the next node to a new node.
        self.__checkValidNode(new_next)
        self.__next_node = new_next

    def setPreviousNode(self, new_previous) -> None:
        # Sets the previous node to a new node.
        self.__checkValidNode(new_previous)
        self.__previous_node = new_previous

    def __checkValidNode(self, node) -> bool:
        # Checks if the input node is a valid DoubleNode or None.
        if type(node) != DoubleNode and node is not None:
            raise Exception("Error: Input must be a valid DoubleNode or None")
        return True

    def __str__(self):
        # Returns a string representation of the node.
        return str(self.__value)