"""
Author: Evan Schneider
Modified from code provided by Prof. Kubota
"""

from .doubleNode import DoubleNode 

class DoublyLinkedList:

    def __init__(self):
        self.__firstNode = None
        self.__lastNode = None 

    def isEmpty(self) -> bool:
        """
        Check whether or not the list is empty.
        """
        return self.__firstNode is None

    def first(self):
        """
        Return the value of the first node in the list. Raise an exception if the list is empty.
        """
        if self.__firstNode is None:
            raise Exception("List is empty")
        return self.__firstNode.getValue()
    
    def getFirstNode(self):
        """
        Get the first node of the list.
        """
        return self.__firstNode

    def getLastNode(self):
        """
        Get the last node of the list.
        """
        return self.__lastNode
    
    def setFirstNode(self, node) -> None:
        """
        Set the first node of the list to a new double node. If the input is not a DoubleNode or None, raise an exception.
        """
        if not isinstance(node, DoubleNode) and node is not None:
            raise Exception("Input must be a valid DoubleNode or None")
        self.__firstNode = node

    def setLastNode(self, node) -> None:
        """
        Set the last node of the list to a new double node. If the input is not a DoubleNode or None, raise an exception.
        """
        if not isinstance(node, DoubleNode) and node is not None:
            raise Exception("Input must be a valid DoubleNode or None")
        self.__lastNode = node

    def find(self, value):
        """
        Return a node in the list containing the given value. If the value is not in the list, return None.
        """
        current = self.__firstNode
        while current is not None:
            if current.getValue() == value:
                return current
            current = current.getNextNode()
        return None

    def insertFront(self, value) -> None:
        """
        Insert the given value to the front of the list.
        """
        new_node = DoubleNode(value)
        if self.isEmpty():
            self.__firstNode = self.__lastNode = new_node
        else:
            new_node.setNextNode(self.__firstNode)
            self.__firstNode.setPreviousNode(new_node)
            self.__firstNode = new_node

    def insertBack(self, value) -> None:
        """
        Insert the given value to the back of the list.
        """
        new_node = DoubleNode(value)
        if self.isEmpty():
            self.__firstNode = self.__lastNode = new_node
        else:
            new_node.setPreviousNode(self.__lastNode)
            self.__lastNode.setNextNode(new_node)
            self.__lastNode = new_node

    def insertAfter(self, value_to_add, after_value) -> bool:
        """
        Insert a value into the list after a specified value.
        """
        after_node = self.find(after_value)
        if after_node is None:
            return False
        new_node = DoubleNode(value_to_add)
        new_node.setNextNode(after_node.getNextNode())
        new_node.setPreviousNode(after_node)
        if after_node.getNextNode() is not None:
            after_node.getNextNode().setPreviousNode(new_node)
        else:
            self.__lastNode = new_node
        after_node.setNextNode(new_node)
        return True
    
    def deleteFirstNode(self):
        """
        Remove the first node from the list. If the list is empty, raise an exception.
        """
        if self.isEmpty():
            raise Exception("List is empty")
        value = self.__firstNode.getValue()
        self.__firstNode = self.__firstNode.getNextNode()
        if self.__firstNode is not None:
            self.__firstNode.setPreviousNode(None)
        else:
            self.__lastNode = None
        return value
    
    def deleteLastNode(self):
        """
        Remove the last node from the list. If the list is empty, raise an exception.
        """
        if self.isEmpty():
            raise Exception("List is empty")
        value = self.__lastNode.getValue()
        self.__lastNode = self.__lastNode.getPreviousNode()
        if self.__lastNode is not None:
            self.__lastNode.setNextNode(None)
        else:
            self.__firstNode = None
        return value
    
    def deleteValue(self, value):
        """
        Remove a node with the specified value from the list. If the list is empty, raise an exception.
        """
        node_to_delete = self.find(value)
        if node_to_delete is None:
            raise ValueError("Value not found in the list")
        if node_to_delete == self.__firstNode:
            return self.deleteFirstNode()
        elif node_to_delete == self.__lastNode:
            return self.deleteLastNode()
        else:
            prev_node = node_to_delete.getPreviousNode()
            next_node = node_to_delete.getNextNode()
            prev_node.setNextNode(next_node)
            next_node.setPreviousNode(prev_node)
            return node_to_delete.getValue()

    def forwardTraverse(self):
        """
        Print each item in the list from beginning to end.
        """
        current_node = self.__firstNode
        while current_node:
            print(current_node.getValue())
            current_node = current_node.getNextNode()

    def reverseTraverse(self):
        """
        Print each item in the list in reverse order
        """
        current_node = self.__lastNode
        while current_node:
            print(current_node.getValue())
            current_node = current_node.getPreviousNode()

    def __len__(self):
        """
        Will be run when checking the length of a DoublyLinkedList.
        """
        count = 0
        current_node = self.__firstNode
        while current_node:
            count += 1
            current_node = current_node.getNextNode()
        return count
    
    def __str__(self):
        """
        This runs when printing a DoublyLinkedList.
        """
        result = []
        current_node = self.__firstNode
        while current_node:
            result.append(str(current_node.getValue()))
            current_node = current_node.getNextNode()
        return "[" + " <-> ".join(result) + "]"

if __name__ == "__main__":
    pass