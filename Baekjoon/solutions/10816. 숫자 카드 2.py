'''
문제 이름 : 10816. 숫자 카드2 
문제 링크 : https://www.acmicpc.net/problem/10816
시간 복잡도 : O(N)
공간 복잡도 : O(1)
'''
from collections import Counter

N1 = int(input())
target_nums = Counter(map(int,input().split()))


N2 = int(input())
nums = list(map(int,input().split()))

for i in nums:
    if i in target_nums:
        print(target_nums[i], end=' ')
    else :
        print(0, end = ' ')