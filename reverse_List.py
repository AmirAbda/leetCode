class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head: ListNode) -> ListNode:
    prev = None
    curr = head

    while curr is not None:
        next_temp = curr.next  
        curr.next = prev       
        prev = curr            
        curr = next_temp       

    return prev  
