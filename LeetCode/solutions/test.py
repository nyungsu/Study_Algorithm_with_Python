'''
https://leetcode.com/problems/top-k-frequent-elements/
'''

from collections import Counter

a = [4,1,-1,2,-1,2,3]
temp = Counter(a)

print(temp)
print(temp.keys())
print()


def topKFrequent(nums: list[int], k: int) -> list[int]:
        temp = Counter(nums)
        key_list = []
        print(temp)
        for key,val in temp.items():
            key_list.append([key,val])
        print(key_list)
        return key_list
        
    
result = topKFrequent(a,2)
print(result)