'''
문제 이름 : 10815. 숫자 카드
문제 링크 : https://www.acmicpc.net/problem/10815
시간 복잡도 : O(N)
공간 복잡도 : O(1)
'''
N1 = int(input())
target_nums = set(map(int,input().split()))

N2 = int(input())
nums = list(map(int,input().split()))

result = []

for i in range(max(N1,N2)):
    if nums[i] in target_nums:
        print(1,end=' ')
    else :
        print(0,end=' ')
        
