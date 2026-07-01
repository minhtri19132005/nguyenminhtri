class RehashHashTable:
    def __init__(self, capacity=4, load_factor_threshold=0.75):
        self.capacity = capacity
        self.threshold = load_factor_threshold
        self.size = 0
        self.table = [None] * self.capacity

    def _hash(self, key, capacity):
        return hash(key) % capacity

    def _resize(self):
        new_capacity = self.capacity * 2
        new_table = [None] * new_capacity
        
        for item in self.table:
            if item:
                for key, value in item:
                    idx = self._hash(key, new_capacity)
                    if new_table[idx] is None:
                        new_table[idx] = []
                    new_table[idx].append((key, value))
                    
        self.capacity = new_capacity
        self.table = new_table

    def put(self, key, value):
        if (self.size + 1) / self.capacity > self.threshold:
            self._resize()
            
        idx = self._hash(key, self.capacity)
        if self.table[idx] is None:
            self.table[idx] = []
            
        for i, kv in enumerate(self.table[idx]):
            if kv[0] == key:
                self.table[idx][i] = (key, value)
                return
                
        self.table[idx].append((key, value))
        self.size += 1