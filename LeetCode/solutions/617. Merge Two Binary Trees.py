'''
문제 이름 : 617. Merge Two Binary Trees
문제 링크 : https://leetcode.com/problems/merge-two-binary-trees/
문제 풀이 : 재귀 함수를 이용해 root1에 덮어서 연산
시간 복잡도 : O(N)
공간 복잡도 : O(N)

'''

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def mergeTrees(self, root1, root2):
        if root1 is None:
            return root2            
        if root2 is None:
            return root1
            
        root1.val += root2.val
        
        ##### 여기까지 val 합치는 부분 ###
                
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        
        # 재귀함수 돌면서 root1에 덮어씌움
        return root1
