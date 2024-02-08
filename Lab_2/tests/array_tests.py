import pytest


class Array():
    # Constructor
    def __init__(self, initialSize):
        self.__a = [None] * initialSize # The array stored as a list
        self.__length = 0               # Start with no values in the list
        
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
    # Otherwise, do not return anything
    def get(self, idx):
      if 0 <= idx and idx < self.__length: # Check if idx is in bounds, and
         return self.__a[idx]              # only return item if in bounds
 
    # Set the value at index idx
    def set(self, idx, value):         
      if 0 <= idx and idx < self.__length: # Check if idx is in bounds, and
         self.__a[idx] = value               # only set item if in bounds
    
    # Insert value to the end of the array
    def insert(self, value):
        self.__a[self.__length] = value

        # Increment the length
        self.__length += 1   

    # Return the index of value in the array, 
    # or -1 if value is not in the array
    def search(self, value):

        # Only search the indices we've inserted
        for idx in range(self.__length): 

            # Check the value at the current index 
            if self.__a[idx] == value:  

                # Return the index  
                return idx  
            
        # Return -1 if value was not found             
        return -1                        

    # Delete the first occurrence of value in the array
    # Returns True if value was deleted, False otherwise
    def delete(self, value):
        # Find the index of the value to delete
        idx = self.search(value)
        
        # If the value was found
        if idx != -1: 

            # Decrement the array length
            self.__length -= 1

            # Shift all the remaining values 
            for j in range(idx, self.__length):
                self.__a[j] = self.__a[j+1]

            # Return that value was deleted
            return True
        
        # Return False if the value was not found
        return False
    
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