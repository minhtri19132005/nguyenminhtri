import random

class UniversalHashFamily:
    def __init__(self, m, p=1000003): 
        self.m = m
        self.p = p
        self.a = random.randint(1, p - 1)
        self.b = random.randint(0, p - 1)

    def hash(self, k):
        """
        h(k) = ((a*k + b) mod p) mod m
        Chống tấn công từ chối dịch vụ (DoS) cố ý đưa vào dữ liệu xấu.
        """
        return ((self.a * k + self.b) % self.p) % self.m