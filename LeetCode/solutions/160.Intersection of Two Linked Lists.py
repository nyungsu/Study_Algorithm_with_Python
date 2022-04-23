'''
https://leetcode.com/problems/intersection-of-two-linked-lists/
'''
# 나의 풀이 : 시간 초과
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        temp_a = headA
        temp_b = headB
        intersectVal = None
        
        while temp_a:
            
            while temp_b:
                if temp_a == temp_b:
                    intersectVal = temp_a
                    return intersectVal
                
                else:
                    intersectVal = None
                
                temp_b = temp_b.next
            
            temp_a = temp_a.next
            temp_b = headB
        return intersectVal
        
# 모범 답안
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        pA = headA
        pB = headB

        while not pA==pB:
            pA = pA.next if pA!=None else headB
            pB = pB.next if pB!=None else headA
        

        return pA
        
       
