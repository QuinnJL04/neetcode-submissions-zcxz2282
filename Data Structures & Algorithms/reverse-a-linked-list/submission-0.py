# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next

        res.reverse()
        print(res)

        reverseL = ListNode(val=res[0])
        tail = reverseL
        for i in range(1, len(res)):
            newNode = ListNode(val=res[i])
            tail.next = newNode
            tail = newNode

        return reverseL            