class MyHashSet:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.table = [[] for _ in range(self.capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def add(self, key):
        idx = self._hash(key)
        if key not in self.table[idx]:
            self.table[idx].append(key)

    def contains(self, key):
        idx = self._hash(key)
        return key in self.table[idx]

    def remove(self, key):
        idx = self._hash(key)
        if key in self.table[idx]:
            self.table[idx].remove(key)