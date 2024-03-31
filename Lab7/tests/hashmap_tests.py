import pytest

from ..myHashMap import MyHashMap

# Write your tests here

@pytest.fixture
def hashmap():
    return MyHashMap()

def test_put_and_get(hashmap):
    hashmap.put("key1", "value1")
    assert hashmap.get("key1") == "value1"

def test_remove(hashmap):
    hashmap.put("key1", "value1")
    assert hashmap.remove("key1") == True
    assert hashmap.get("key1") == None

def test_containsKey(hashmap):
    hashmap.put("key1", "value1")
    assert hashmap.containsKey("key1") == True
    assert hashmap.containsKey("key2") == False