"""
Author: Evan Schneider
Modified from code provided by ENGR 221 4/15/24
Purpose: Binary search tree functions and methods.
"""

class BinarySearchTree:
    """ DESCRIBE THE BST CLASS HERE """

    def __init__(self):
        self.__root = None # The root Node of this BST

    def insert(self, insertKey, insertValue):
        """ Inserts the given key and value into the BST.
            Inputs:
                - insertKey: (any) The key to insert
                - insertValue: (any) The value to insert
            Returns: None
        """
        # Update the root to include the inserted node
        self.__root = self.__insertHelp(self.__root, insertKey, insertValue)
    
    def __insertHelp(self, node, insertKey, insertValue):
        """ A recursive helper method to insert a new node 
            with the given key and value into the BST.
            Inputs:
                - node: (Node) The root of the subtree to insert into
                - insertKey: (any) The key to insert
                - insertvalue: (any) The value to insert
            Returns: The node to insert """
        # Base case - Insert the node as a leaf in the appropriate location
        if node == None:
            return self.__Node(insertKey, insertValue)
        # Insert the key into the left subtree if it is less than the current key
        elif insertKey < node.key:
            node.left = self.__insertHelp(node.left, insertKey, insertValue)
        # Insert the key into the right subtree if it is greater than the current key
        elif insertKey > node.key:
            node.right = self.__insertHelp(node.right, insertKey, insertValue)
        # Return the node with the node inserted
        return node

    def isEmpty(self):
        """ Check whether the BST is empty """
        return self.__root is None
    
    def getRoot(self):
        """ Get the root node of the BST """
        return self.__root

    def __searchHelp(self, node, goalKey):
        """ A recursive method to help with the search() method, which
            searches for a given key in the BST.
            Arguments:
            - node: The root node of the subtree being searched
            - goalKey: The key to search for
            Output: A tuple (found, node) where found is a Boolean representing whether 
            or not goalKey is in the BST, and node is the Node with the key goalKey """
        if node is None:
            return False, None
        if node.key == goalKey:
            return True, node
        elif goalKey < node.key:
            return self.__searchHelp(node.left, goalKey)
        else:
            return self.__searchHelp(node.right, goalKey)

    def search(self, goalKey):
        """ SEARCH DOCUMENTATION HERE """
        found, node = self.__searchHelp(self.__root, goalKey)
        return found

    def lookup(self, goal):
        """ LOOKUP DOCUMENTATION HERE """
        found, node = self.__searchHelp(self.__root, goal)
        if found:
            return node.value
        else:
            raise KeyError("Key not found")

    def __findSuccessorHelp(self, node):
        """ __FINDSUCCESSOR DOCUMENTATION HERE """
        if node.left is not None:
            return self.__findSuccessorHelp(node.left)
        return node

    def findSuccessor(self, subtreeRoot):
        """ FINDSUCCESSOR DOCUMENTATION HERE """
        return self.__findSuccessorHelp(subtreeRoot)

    def __deleteHelp(self, node, deleteKey):
        """ __DELETEHELP DOCUMENTATION HERE """
        if node is None:
            return node
        if deleteKey < node.key:
            node.left = self.__deleteHelp(node.left, deleteKey)
        elif deleteKey > node.key:
            node.right = self.__deleteHelp(node.right, deleteKey)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self.__findSuccessorHelp(node.right)
            node.key = temp.key
            node.value = temp.value
            node.right = self.__deleteHelp(node.right, temp.key)
        return node

    def delete(self, deleteKey):
        """ DELETE DOCUMENTATION HERE """
        if self.search(deleteKey):
            return self.__deleteHelp(self.__root, deleteKey)
        raise Exception("Key not in tree.")

    def __traverseHelp(self, node):
        """ __TRAVERSEHELP DOCUMENTATION HERE """
        if node is not None:
            self.__traverseHelp(node.left)
            print(node.key, node.value)
            self.__traverseHelp(node.right)

    def traverse(self) -> None:
        """ TRAVERSE DOCUMENTATION HERE """
        self.__traverseHelp(self.__root)
            

    ##############
    # NODE CLASS #
    ##############

    class __Node:
        """ Implementation of a node in a BST. Note that it is 
            private, so it cannot be accessed outside of a BST """

        def __init__(self, key, value, left=None, right=None):
            self.key = key         # The key of the root node of this tree
            self.value = value     # The value held by the root node of this tree
            self.left = left       # Points to the root of the left subtree
            self.right = right     # Points to the root of the right subtree

        def __str__(self):
            """ Represent the node as a string.
                Formats as "{key, value}" """
            return "({}, {})".format(self.key, self.value)
        
if __name__ == "__main__":
    pass