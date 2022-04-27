from collections import deque

# n = 5

# friends = [i+1 for i in range(n)]

# friends = deque(friends)

# for i in range(5):
#     friends.rotate(-1)
#     result = friends.popleft()
#     print(friends)
#     print(result)
#     print()

def findTheWinner(n: int, k: int) -> int:
        friends = [i+1 for i in range(n)]
        friends = deque(friends)
        # 둘 중에 뭐가 나을지
        for i in range(n):
            friends.rotate(-(k)+1)
            result = friends.popleft()
            print(friends)
            print(result)
            print()
        return result
        
a = findTheWinner(5,2)
print(a)