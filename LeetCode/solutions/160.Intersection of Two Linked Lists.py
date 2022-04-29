'''

문제 이름 : 160.Intersection of Two Linked Lists
문제 링크 : https://leetcode.com/problems/intersection-of-two-linked-lists/
문제 풀이 : listA 끝까지 간 후, listB를 이어 붙이고
            listB도 끝까지 간 후 listA를 이어 붙이고
            두 값이 같아질 때 까지 끝까지 가면 교차점이 나타난다
시간 복잡도 : 시간 초과
공간 복잡도 : O(N)

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
        
       
