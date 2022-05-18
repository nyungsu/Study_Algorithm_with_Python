# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def __init__(self):
        self.num = []
    
    def DFS(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        
        self.num.append(root.val)
        
        root.left = self.DFS(root.left)
        root.right = self.DFS(root.right)
    
        return self.num
    