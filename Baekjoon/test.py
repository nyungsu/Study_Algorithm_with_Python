def bs(start, end, target, nums):
    if start> end:
        return 0
    
    mid = (start + end)//2
    
    if target == nums[mid] :
        return print(1)
    
    elif target > nums[mid] :
        start = mid +1
        bs(start,end,target,nums)
    
    elif target < nums[mid] :
        end = mid-1
        bs(start,end,target,nums)
        
a = [1,2,3,4,5]


bs(start = 0,end = len(a)-1,target = 1 ,nums=a)
