'''
문제 이름 : 1920. 수 찾기
문제 링크 : https://www.acmicpc.net/problem/1920
시간 복잡도 : O(N)
공간 복잡도 : O(1)
'''

# # solution 1 : set + in 이용
N1 = int(input())
target_nums = set(map(int,input().split()))

N2 = int(input())
nums = list(map(int,input().split()))

for i in nums:
    if i in target_nums:
        print(1)
    else :
        print(0)
        
# -----------------------------------------------------------
        
# solution 2 : 이분탐색, 아직 안 됨
N1 = int(input())
target_nums = list(map(int,input().split()))
target_nums.sort()

N2 = int(input())
nums = list(map(int,input().split()))

result = []

def bs(target_nums,num):
    if len(target_nums) % 2 == 0:
        mid = target_nums[(len(target_nums)//2)-1]     
    else :
        mid = target_nums[len(target_nums)//2]

    if target_nums[-1] < num:
        return print(0)
    if mid == num :
        return print(1)
    
    elif num<mid :
        target_nums = target_nums[:mid]
        bs(target_nums,num)
    
    elif num>mid :
        target_nums = target_nums[mid:]
        bs(target_nums,num)



for i in nums:
    bs(target_nums,i)
    
# print(result) 


    
    