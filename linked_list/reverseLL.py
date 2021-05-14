# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p = None
        c = head
        while c != None:
            n = c.next
            c.next = p
            p = c
            c = n
        return p
            