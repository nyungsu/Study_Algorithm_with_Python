'''
https://leetcode.com/problems/top-k-frequent-elements/
'''

from collections import Counter

class Solution:
    def topKFrequent(self,nums: list[int], k: int) -> list[int]:
        temp = Counter(nums)
        most_common = temp.most_common(k)
        result = [most_common[i][0] for i in range(k)]
        return result
               
