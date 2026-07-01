import hashlib

class ConsistentHashing:
    def __init__(self, replicas=3):
        self.replicas = replicas 
        self.ring = {}           
        self.sorted_keys = []    

    def _hash(self, key):

        return int(hashlib.md5(key.encode('utf-8')).hexdigest(), 16)

    def add_server(self, server):
        for i in range(self.replicas):
            virtual_node_key = f"{server}-node-{i}"
            val = self._hash(virtual_node_key)
            self.ring[val] = server
            self.sorted_keys.append(val)
        self.sorted_keys.sort()

    def remove_server(self, server):
        for i in range(self.replicas):
            virtual_node_key = f"{server}-node-{i}"
            val = self._hash(virtual_node_key)
            if val in self.ring:
                del self.ring[val]
                self.sorted_keys.remove(val)

    def get_server(self, key):
        if not self.ring:
            return None
        val = self._hash(key)
        
        import bisect
        idx = bisect.bisect_right(self.sorted_keys, val)
        
        if idx == len(self.sorted_keys):
            idx = 0
        return self.ring[self.sorted_keys[idx]]

# Ví dụ mẫu:
ch = ConsistentHashing()
ch.add_server("Server_A")
ch.add_server("Server_B")
print(ch.get_server("my_user_photo_123")) 