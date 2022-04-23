'''
https://leetcode.com/problems/intersection-of-two-linked-lists/
'''

from operator import is_not


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        intersectVal = 0
        skipA, skipB = 0
        
        return intersectVal, skipA, skipB
    

a = [4,1,8,4,5]
b = [5,6,1,8,4,5]


a0 = ListNode(4)
a1 = ListNode(1)
a2 = ListNode(8)
a3 = ListNode(4)
a4 = ListNode(5)
a0.next = a1
a1.next = a2
a2.next = a3
a3.next = a4

b0 = ListNode(5)
b1 = ListNode(6)
b2 = ListNode(1)
b3 = ListNode(8)
b4 = ListNode(4)
b5 = ListNode(5)
b0.next = b1
b1.next = b2
b2.next = b3
b3.next = b4
b4.next = b5

# def get_solution(headA,headB):
intersectVal = 0
skipA = 0
skipB = 0
a_i = a0
b_i = b0

# while(a_i is not b_i):
#     if a_i is b_i:
#         intersectVal = a_i.val
#     else:
#         b_i = b_i.next
    
    # return intersectVal, skipA, skipB

# a0 = ListNode(4)
a_i = a0
print(a0.next)
print(a_i.next)

