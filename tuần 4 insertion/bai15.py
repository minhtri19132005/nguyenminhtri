class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertion_sort_linked_list(head):
    if not head or not head.next: return head
    
    dummy = Node(0)
    curr = head
    
    while curr:
        next_node = curr.next
        
        prev = dummy
        while prev.next and prev.next.data < curr.data:
            prev = prev.next
            
        curr.next = prev.next
        prev.next = curr
        
        curr = next_node
        
    return dummy.next

def make_and_print_list(arr):
    dummy = Node(0)
    c = dummy
    for x in arr: c.next = Node(x); c = c.next
    res = insertion_sort_linked_list(dummy.next)
    out = []
    while res: out.append(str(res.data)); res = res.next
    return " -> ".join(out) + " -> null"

print(make_and_print_list([3, 1, 2]))