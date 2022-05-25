'''
문제 이름 : 1920. 수 찾기
문제 링크 : https://www.acmicpc.net/problem/1920
시간 복잡도 : O(N)
공간 복잡도 : O(1)
'''

# solution 1 : set + in 이용
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

start = 0
end = N1-1

def bs(start, end, target, nums):
    if start >= end:
        return print(0)
                
    mid = (start + end)//2
    
    if target == nums[mid] :
        return print(1)
    
    elif target > nums[mid] :
        start = mid +1
        bs(start,end,target,nums)
    
    elif target < nums[mid] :
        end = mid-1
        bs(start,end,target,nums)

for i in nums:
    bs(start=0, end=N1, target=i, nums=target_nums)

    