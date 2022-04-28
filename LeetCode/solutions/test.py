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
        most = temp.most_common(k)
        result = []
        for i in range(k):
            result.append(most[i][0])
        print(result)
        return 
        
    
result = topKFrequent(a,2)
print(result)