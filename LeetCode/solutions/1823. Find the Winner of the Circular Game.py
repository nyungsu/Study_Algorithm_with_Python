'''
문제 이름 : 1823. Find the Winner of the Circular Game
문제 링크 : https://leetcode.com/problems/find-the-winner-of-the-circular-game/
문제 풀이 : collections - deque 이용, rotate, popleft
시간 복잡도 : O(N)
공간 복잡도 : O(1)

rotate 시간 복잡도는 O(N)
https://stackoverflow.com/questions/63878383/why-does-the-rotate-method-of-collections-deque-have-a-linear-time-complexity

popleft() deque에서 시간 복잡도 O(1)
'''


from collections import deque

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        self.friends = [i+1 for i in range(n)]
        self.friends = deque(self.friends)
        
        for i in range(n):
            self.friends.rotate(-k+1)                   # O(N)
            result = self.friends.popleft()             # k>0 : 시계 / k<0 : 반시계 
        
        return result
        