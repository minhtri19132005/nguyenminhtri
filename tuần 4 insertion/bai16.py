class OnlineInsertionSort:
    def __init__(self):
        self.arr = []
        
    def add(self, val):
        self.arr.append(val)
        i = len(self.arr) - 1
        while i > 0 and self.arr[i - 1] > val:
            self.arr[i] = self.arr[i - 1]
            i -= 1
        self.arr[i] = val
        return list(self.arr)

online_sort = OnlineInsertionSort()

for num in [5, 2, 8, 1]:
    print(f" Thêm {num} -> {online_sort.add(num)}")