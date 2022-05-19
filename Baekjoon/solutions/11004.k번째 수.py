'''
문제 이름 : 11004.k번째 수
문제 링크 : https://www.acmicpc.net/problem/11004
시간 복잡도 : O(NlogN)
공간 복잡도 : O(N)
'''

n,k = map(int,input().split())

num = list(map(int,input().split()))
num.sort()

print(num[k-1])
