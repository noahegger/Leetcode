# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        first = dummy
        second = dummy 

        # Symmetry argument: If list is like m, then nth from the end is the same
        # as m-nth from the beginning
        # Have first pointer go like n
        # Have second and first continue until m
        # First pointer reachers n + (m-n), second pointer goes m-n

        for _ in range(n+1):
            first = first.next
        
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
