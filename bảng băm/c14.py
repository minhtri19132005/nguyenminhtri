class LazyDeleteHashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        self.TOMBSTONE = "DELETED" 
    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        idx = self._hash(key)
        first_deleted_idx = None
        start_idx = idx
        
        while self.keys[idx] is not None:
            if self.keys[idx] == key:
                self.values[idx] = value
                return
            if self.keys[idx] == self.TOMBSTONE and first_deleted_idx is None:
                first_deleted_idx = idx 
            idx = (idx + 1) % self.capacity
            if idx == start_idx: break
                
        insert_idx = first_deleted_idx if first_deleted_idx is not None else idx
        self.keys[insert_idx] = key
        self.values[insert_idx] = value

    def get(self, key):
        idx = self._hash(key)
        start_idx = idx
        while self.keys[idx] is not None:
            if self.keys[idx] == key:
                return self.values[idx]
            idx = (idx + 1) % self.capacity
            if idx == start_idx: break
        return None

    def remove(self, key):
        idx = self._hash(key)
        start_idx = idx
        while self.keys[idx] is not None:
            if self.keys[idx] == key:
                self.keys[idx] = self.TOMBSTONE 
                self.values[idx] = None
                return True
            idx = (idx + 1) % self.capacity
            if idx == start_idx: break
        return False