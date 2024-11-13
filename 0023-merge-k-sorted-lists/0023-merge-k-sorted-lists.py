# Definition for singly-linked list.
import heapq
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = []
        dummy = ListNode(0)

        for node in lists:
            while node:
                values.append(node.val)
                node = node.next
        
        if not values:
            return None

        heapq.heapify(values)
        curr = dummy
        while values:
            val = heapq.heappop(values)
            curr.next = ListNode(val)
            curr = curr.next
        
        return dummy.next


