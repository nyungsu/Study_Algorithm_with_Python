'''

문제 이름 : 104. Maximum Depth of Binary Tree
문제 링크 : https://leetcode.com/problems/maximum-depth-of-binary-tree/
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
    def maxDepth(self, root: TreeNode) -> int:
        if root == None : 
            return 0
        root.left = self.maxDepth(root.left)
        root.right = self.maxDepth(root.right)
        
        return max(root.left,root.right)+1

f = TreeNode(val=7,left=None,right=None)
e = TreeNode(val=7,left=None,right=f)
d = TreeNode(val=15,left=None,right=None)
c = TreeNode(val=20,left=d,right=e)
b = TreeNode(val=9,left=None,right=None)
a = TreeNode(val=3,left=b,right=c)


solution = Solution()

result = solution.maxDepth(a)

print(result)

'''
리트코드 출력값에 class 이름이 출력 되는거 보고 생각한 아이디어
str으로 바꿔서 'TreeNode'라는 글자수가 몇 개 인지 세는 걸로
depth 계산해보려 한건데 좀 더 생각해보면 괜찮아 질지도 ..?

from collections import deque
class Solution:
    def maxDepth(self, root) -> int:
        queue = str(deque([root])) 
        count = queue.count('Tree')
        depth = 0
        
        if root == None:
            return depth
        
        for i in range(count):
            depth += 1
            count -= 2**i
            if count<=0:
                return depth
'''

