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

        # Tortoise & Hare Two-pointer to find mid
        def find_mid(head: ListNode) -> ListNode:
            slow = head
            fast = head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        # Reverse second half
        def reverse(head:ListNode)->ListNode:
            prev = None
            curr = head
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        # Merge first half, reversed second half
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

        # Return if head is None or list is 1 val
        if not head or not head.next:
            return
        
        # Find midpoint
        mid = find_mid(head)
        # Define second half starting node
        half2 = mid.next
        # Disconnect First from second
        mid.next = None

        # Reverse second
        half2 = reverse(half2)
        # Merge back
        merge_lists(head, half2)
       

