"""
Author: Evan Schneider

Adapted from UCSD CSE12
"""

class MyHashMap:
    def __init__(self, load_factor=0.75, initial_capacity=16):
        self.load_factor = load_factor
        self.capacity = initial_capacity
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    def resize(self):
        self.capacity *= 2
        old_buckets = self.buckets
        self.buckets = [[] for _ in range(self.capacity)]
        for bucket in old_buckets:
            if bucket != []:
                for entry in bucket:
                    self.put(entry.getKey(), entry.getValue())

    def put(self, key, value):
        if key is None:
            raise ValueError("Key cannot be None 1")  #Number at end of this string helps me identify which part is broken
        index = hash(key) % self.capacity
        bucket = self.buckets[index]
        for entry in bucket:
            if entry.getKey() == key:
                entry.setValue(value)
                return False
        bucket.append(self.MyHashMapEntry(key, value))
        self.size += 1
        if self.size > self.load_factor * self.capacity:
            self.resize()
        return True

    def replace(self, key, newValue):
        if key is None:
            raise ValueError("Key cannot be None 2")
        index = hash(key) % self.capacity
        bucket = self.buckets[index]
        for entry in bucket:
            if entry.getKey() == key:
                entry.setValue(newValue)
                return True
        return False

    def remove(self, key):
        if key is None:
            raise ValueError("Key cannot be None 3")
        index = hash(key) % self.capacity
        bucket = self.buckets[index]
        for i, entry in enumerate(bucket):
            if entry.getKey() == key:
                del bucket[i]
                self.size -= 1
                return True
        return False

    def set(self, key, value):
        if key is None:
            raise ValueError("Key cannot be None 4")
        if self.containsKey(key):
            return self.replace(key, value)
        else:
            return self.put(key, value)

    def get(self, key):
        if key is None:
            raise ValueError("Key cannot be None 5")
        index = hash(key) % self.capacity
        bucket = self.buckets[index]
        for entry in bucket:
            if entry.getKey() == key:
                return entry.getValue()
        return None

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def containsKey(self, key):
        if key is None:
            raise ValueError("Key cannot be None 6")
        index = hash(key) % self.capacity
        bucket = self.buckets[index]
        for entry in bucket:
            if entry.getKey() == key:
                return True
        return False

    def keys(self):
        keys_list = []
        for bucket in self.buckets:
            for entry in bucket:
                keys_list.append(entry.getKey())
        return keys_list

    class MyHashMapEntry:
        def __init__(self, key, value):
            self.key = key
            self.value = value

        def getKey(self):
            return self.key

        def getValue(self):
            return self.value

        def setValue(self, new_value):
            self.value = new_value

if __name__ == "__main__":
    pass