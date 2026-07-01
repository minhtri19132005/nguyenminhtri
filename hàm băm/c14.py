import hashlib

class BloomFilter:
    def __init__(self, size=1000, hash_count=3):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * self.size

    def _hashes(self, item):
        positions = []
        for i in range(self.hash_count):
            encoded = f"{item}-{i}".encode('utf-8')
            digest = int(hashlib.md5(encoded).hexdigest(), 16)
            positions.append(digest % self.size)
        return positions

    def add(self, item):
        for pos in self._hashes(item):
            self.bit_array[pos] = 1

    def contains(self, item):
        return all(self.bit_array[pos] == 1 for pos in self._hashes(item))