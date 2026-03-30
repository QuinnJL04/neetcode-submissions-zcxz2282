# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        curr2 = head
        while curr and curr.next:
            curr = curr.next.next
            curr2 = curr2.next
            if curr2 == curr:
                return True

        return False