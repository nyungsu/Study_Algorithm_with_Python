'''
https://leetcode.com/problems/find-the-winner-of-the-circular-game/
'''


from collections import deque

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        self.friends = [i+1 for i in range(n)]
        self.friends = deque(self.friends)
        
        for i in range(n):
            self.friends.rotate(-k+1)
            result = self.friends.popleft()
        
        return result
        