from myHashMap import MyHashMap
from entry import Entry

class Box:
    def __init__(self):
        self.nicknameMap = MyHashMap()

    def populate_box(self, inputFile):
        with open(inputFile, 'r') as file:
            for line in file:
                nickname, species = line.strip().split(',')
                entry = Entry(nickname, species)
                self.add_entry(entry)

    def add_entry(self, entry):
        if not self.nicknameMap.containsKey(entry.nickname):
            self.nicknameMap.put(entry.nickname, entry)
        else:
            raise ValueError("Nickname '{}' already exists in the Box.".format(entry.nickname)) #same as non error in myHashMap.py

    def remove_entry(self, nickname):
        if self.nicknameMap.containsKey(nickname):
            self.nicknameMap.remove(nickname)
        else:
            raise ValueError("Nickname '{}' does not exist in the Box.".format(nickname))

    def get_entry(self, nickname):
        if self.nicknameMap.containsKey(nickname):
            return self.nicknameMap.get(nickname)
        else:
            return None

    def size(self):
        return self.nicknameMap.size()

    def is_empty(self):
        return self.nicknameMap.isEmpty()

    def contains_nickname(self, nickname):
        return self.nicknameMap.containsKey(nickname)

if __name__ == "__main__":
    # Box object
    my_box = Box()

    # Populate the box
    my_box.populate_box("entries.txt")

    # Test adding an entry
    new_entry = Entry("nickname2", "species2")
    my_box.add_entry(new_entry)
    print("Added new entry:", my_box.get_entry("nickname2"))

    # Test removing an entry
    my_box.remove_entry("nickname1")
    print("After removing entry:", my_box.get_entry("nickname1"))

    # Test getting an entry
    print("Entry for nickname2:", my_box.get_entry("nickname2"))

    # Print the size of the box
    print("Size of the box:", my_box.size())

    # Check if the box is empty
    print("Is the box empty?", my_box.is_empty())

    # Check if a nickname exists in the box
    print("Does 'nickname1' exist?", my_box.contains_nickname("nickname1"))
    pass

