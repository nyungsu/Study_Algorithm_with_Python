'''
문제 이름 : 324. Wiggle Sort II
문제 링크 : https://leetcode.com/problems/wiggle-sort-ii/
문제 풀이 :
시간 복잡도 : 
공간 복잡도 :
'''

nums = [1,5,1,1,6,4]

nums.sort()

if len(nums) % 2 ==0:
    idx = len(nums) // 2 
    front = nums[:idx]
    back = nums[idx:]
    print(front)
    print(back)

result = []
  
for i in range(len(nums)//2):
    result.append(front[i])
    result.append(back[-i])
    
print(result)
    

# else :
#     idx = len(nums) // 2
#     front = nums[:idx]
    




