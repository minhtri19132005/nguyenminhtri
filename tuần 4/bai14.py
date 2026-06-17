class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def sort_linked_list(head):
    if not head: return None
    
    dummy = Node(0) 
    tail = dummy
    
    current_head = head
    while current_head:
    
        min_prev = None
        min_node = current_head
        
        prev = current_head
        curr = current_head.next
        while curr:
            if curr.data < min_node.data:
                min_node = curr
                min_prev = prev
            prev = curr
            curr = curr.next
            

        if min_node == current_head:
            current_head = current_head.next
        else:
            min_prev.next = min_node.next
            

        tail.next = min_node
        tail = min_node
        tail.next = None
        
    return dummy.next


def make_list(arr):
    dummy = Node(0)
    curr = dummy
    for x in arr:
        curr.next = Node(x)
        curr = curr.next
    return dummy.next

def print_list(head):
    res = []
    while head:
        res.append(str(head.data))
        head = head.next
    return " -> ".join(res) + " -> null"

head = make_list([3, 1, 2])
sorted_head = sort_linked_list(head)
print( print_list(sorted_head))
