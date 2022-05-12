'''
문제 이름 : 1427.소트인사이드
문제 링크 : https://www.acmicpc.net/problem/1427
시간 복잡도 : O(NlogN)
공간 복잡도 : O(1)
'''

N = list(map(int,input()))
N.sort(reverse=True)

for i in N:
    print(i,end='')



