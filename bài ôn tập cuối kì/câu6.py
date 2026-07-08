class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_cycle_start(head):
    if not head or not head.next:
        return None
    slow = head 
    fast = head 
    met_node = None

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            met_node = slow 
            break

    if not met_node:
        print("Danh sách liên kết không có chu trình.")
        return None

    print(f"-> Giai đoạn 1: Rùa và Thỏ gặp nhau tại Node có giá trị: {met_node.data}")

    slow = head  
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow

head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node5.next = node3 
cycle_start = find_cycle_start(head)

if cycle_start:
    print(f"-> Giai đoạn 2: Điểm bắt đầu chu trình tìm được là Node: {cycle_start.data}")