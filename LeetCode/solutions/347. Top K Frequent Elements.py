'''
https://leetcode.com/problems/top-k-frequent-elements/
'''

from collections import Counter

class Solution:
    def topKFrequent(self,nums: list[int], k: int) -> list[int]:
        temp = Counter(nums)
        key_list = []
        
        for index, (key,val) in enumerate(temp.items()):
            key_list.append(key)
        key_list.sort()
        
        return key_list[:k]
               