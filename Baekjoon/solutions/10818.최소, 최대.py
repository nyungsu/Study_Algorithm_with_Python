'''
문제 이름 : 10818.최소, 최대
문제 링크 : https://www.acmicpc.net/problem/10818
시간 복잡도 : O(1)
공간 복잡도 : O(1)
'''

n = int(input())

num = [int(input()) for _ in range(n)]

    
print(f'{min(num)} {max(num)}')