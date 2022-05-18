'''
문제 이름 : 98. Validate Binary Search Tree
문제 링크 : https://leetcode.com/problems/validate-binary-search-tree/
문제 풀이 :  
시간 복잡도 : 
공간 복잡도 :
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self) -> None:
        self.max_val = 0
        self.min_Val = 0
    
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return 0
        self.max_val = root
        self.min_val = root
        
        
        
        root.left = self.isValidBST(root.left)
        root.right = self.isValidBST(root.right)
        
        return False