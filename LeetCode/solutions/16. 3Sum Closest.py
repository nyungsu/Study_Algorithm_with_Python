'''
문제 이름 : 16. 3Sum Closest
문제 링크 : https://leetcode.com/problems/3sum-closest/
문제 풀이 :
시간 복잡도 : 
공간 복잡도 :

'''
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int: 
        from itertools import combinations
        
        three_sum = combinations(nums,3)
        temp = set(list(map(sum,three_sum)))
        temp = list(temp)
        
        result = [abs(target - int(i)) for i in temp]
        min_val = min(result)
        min_idx = result.index(min_val)
        
        return temp[min_idx]


# from itertools import combinations
# from collections import Counter

# nums = [-1,2,1,-4]
# target = 1

# three_sum = combinations(nums,3)
# temp = set(list(map(sum,three_sum)))
# temp = list(temp)
# print(temp)


# result = [abs(target - int(i)) for i in temp]
# print(result)

# min_val = min(result)
# min_idx = result.index(min_val)

# print(temp[min_idx])











