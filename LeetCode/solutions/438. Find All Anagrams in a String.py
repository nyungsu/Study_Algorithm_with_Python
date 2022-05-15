'''
문제 이름 : 438. Find All Anagrams in a String
문제 링크 : https://leetcode.com/problems/find-all-anagrams-in-a-string/
문제 풀이 :  
시간 복잡도 : 
공간 복잡도 :
'''

from collections import Counter

# s = "cbaebabacd"
# p = "abc"

class Solution:
    def __init__(self) -> None:
        self.window = 0
        
    def findAnagrams(self, s: str, p: str):
        p_counter = Counter(list(p)) 
        result_idx = []

        for i in range(len(s)-len(p)+1):
            s_counter = Counter(list(s[i:i+len(p)]))
            
            if s_counter == p_counter:
                result_idx.append(i)
        
        
        return result_idx
    
# a = Solution()
# result = a.findAnagrams(s,p)

# print(result)