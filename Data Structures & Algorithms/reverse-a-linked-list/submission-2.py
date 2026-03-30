# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev, curr = None, head

        while curr:
            tmp = curr.next # stores the next node to reverse before we break the link
            curr.next = prev # reverses the pointer
            prev = curr # points the prev head to the reversed list
            curr = tmp # updates curr to the next node to reverse

        return prev
