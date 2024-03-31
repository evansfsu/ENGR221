import pytest

from ..box import Box
from entry import Entry

# Write your tests here

@pytest.fixture
def box():
    return Box()

def test_add_entry(box):
    entry1 = Entry("nickname1", "species1")
    box.add_entry(entry1)
    assert box.size() == 1
    assert box.contains_nickname("nickname1") == True

def test_remove_entry(box):
    entry1 = Entry("nickname1", "species1")
    box.add_entry(entry1)
    box.remove_entry("nickname1")
    assert box.size() == 0
    assert box.contains_nickname("nickname1") == False

def test_get_entry(box):
    entry1 = Entry("nickname1", "species1")
    box.add_entry(entry1)
    assert box.get_entry("nickname1") == entry1
    assert box.get_entry("nonexistent_nickname") == None

if __name__ == '__main__':
    pytest.main()