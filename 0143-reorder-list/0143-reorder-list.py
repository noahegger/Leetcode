# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        def find_mid(head: ListNode) -> ListNode:
            slow = head
            fast = head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def reverse(head:ListNode)->ListNode:
            prev = None
            curr = head
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        def merge_lists(l1:ListNode, l2:ListNode)-> None:
            while l2:
                l1_next = l1.next
                l2_next = l2.next

                l1.next = l2
                if not l1_next:
                    break
                l2.next = l1_next
                l1 = l1_next
                l2 = l2_next

        if not head or not head.next:
            return
        
        mid = find_mid(head)
        half2 = mid.next
        mid.next = None

        half2 = reverse(half2)
        merge_lists(head, half2)
       

