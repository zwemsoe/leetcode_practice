import sys
import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    carry = 0
    head = ListNode()
    p = head
    while l1 != None or l2 != None:
        v1 = 0 if l1 == None else l1.val
        v2 = 0 if l2 == None else l2.val
        s = v1 + v2
        if s > 9 and carry == 0:
            carry = 1
            p.val = s-10
        elif s >= 9 and carry == 1:
            p.val = s-9
        else:
            p.val = s+carry
            carry = 0
        l1 = None if l1 == None else l1.next
        l2 = None if l2 == None else l2.next
        if l1 != None or l2 != None:
            p.next = ListNode()
        elif carry:
            p.next = ListNode(1)
        p = p.next

    return head

