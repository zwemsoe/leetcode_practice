import sys
import math


def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    t1 = headA
    t2 = headB
    hm = {}
    while t1 != None:
        hm[t1] = t1.val
        t1 = t1.next
    while t2 != None:
        if t2 in hm:
            return t2
        t2 = t2.next

    return None


def main():
    pass


main()
