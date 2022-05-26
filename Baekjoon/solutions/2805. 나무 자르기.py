'''
문제 이름 : 2805. 나무 자르기
문제 링크 : https://www.acmicpc.net/problem/2805
시간 복잡도 : O(logN)
공간 복잡도 : O(1)
'''
# # solution 1 재귀함수
# import sys
# input = sys.stdin.readline

# N,T = map(int,input().split())

# tree = list(map(int,input().split()))

# start, end = 0, max(tree)


# def bs(start,end,tree):
#     mid = (start+end)//2
#     cut = 0
#     if start>end:
#         return 0
    
#     for i in tree:
#         if i>=mid:
#             cut += i - mid
            
#     if cut == T:
#         print(mid)

#     elif cut > T :
#         start = mid + 1
#         bs(start,end,tree)
    
#     elif cut < T :
#         end = mid - 1
#         bs(start,end,tree)

# bs(start,end,tree)

# solution 2 while
import sys
input = sys.stdin.readline
N,T = map(int,input().split())
trees = list(map(int,input().split()))

start, end = 0, max(trees)
cut = 0
while (start <= end):
    mid = (start+end)//2
    cut = 0    
    
    for i in trees:
        if i >= mid:
            cut += i - mid

    if cut >= T :
        result = mid
        start = mid + 1

    if cut < T :
        end = mid - 1

print(result)