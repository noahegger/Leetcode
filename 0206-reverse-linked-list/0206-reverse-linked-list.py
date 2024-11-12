# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        next = None
        curr = head

        while curr:
            # save next node
            next = curr.next
            # reverse curr link
            curr.next = prev
            # move prev and curr forward
            prev = curr
            curr = next

        return prev

        