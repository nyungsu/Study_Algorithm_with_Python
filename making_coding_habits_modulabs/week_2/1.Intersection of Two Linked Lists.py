'''
https://leetcode.com/problems/intersection-of-two-linked-lists/
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        intersectVal = 0
        skipA, skipB = 0
        
        return intersectVal, skipA, skipB
    

a0 = ListNode(4)
a1 = ListNode(1)
a2 = ListNode(8)
a3 = ListNode(4)
a4 = ListNode(5)
a0.next = a1
a1.next = a2
a2.next = a3
a3.next = a4

a0.next = a4


print(a3.next)
print(a0.next)

print(a3.next is a0.next)

a = [4,1,8,4,5]
b = [5,6,1,8,4,5]

print(a[2] is b[3])
