# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        first= ListNode()
        first.next = head
        
        faster = first
        slower = first
        
        while faster is not None:
            if faster.next is not None:
                faster = faster.next
            faster = faster.next
            slower = slower.next
            
        return slower
    
        N = 0
        pointer = head
        while pointer is not None:
            pointer = pointer.next
            N += 1
        
        pointer = head
        N //= 2
        while N > 0:
            pointer = pointer.next
            N -= 1
        return pointer
        