'''
문제 이름 : 1448. Count Good Nodes in Binary Tree
문제 링크 : https://leetcode.com/problems/count-good-nodes-in-binary-tree/
문제 풀이 :  max 값을 업데이트 해주면서 노드와 비교했다, DFS
시간 복잡도 : O(N)
공간 복잡도 : O(N)
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self):
        self.good_node = 0
        
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.dfs(root=root,max_val=root.val)
        return self.good_node
        
    def dfs(self,node:TreeNode,max_val):
        if not node:
            return 0
     
        # max값과 현재 노드 비교 
        if node.val >= max_val:
            self.good_node += 1
            max_val = node.val
        
        
        # DFS 순회
        node.left = self.dfs(node.left,max_val)
        node.right = self.dfs(node.right,max_val)
        
    
        
        