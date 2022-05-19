'''
문제 이름 : 1859. Sorting the Sentence
문제 링크 : https://leetcode.com/problems/sorting-the-sentence/
문제 풀이 :  
시간 복잡도 : O(NlogN)
공간 복잡도 : O(N)
'''
class Solution:
    def sortSentence(self, s: str) -> str:
        s = list(s.split())

        for i in range(len(s)):
            s[i] = s[i][::-1]

        s.sort()

        for i in range(len(s)):
            s[i] = s[i][::-1]
            s[i] = s[i][:-1]
            
        result = ' '.join(s)
        
        return result




# s = "is2 sentence4 This1 a3"

# s = list(s.split())

# # s[0]
# for i in range(len(s)):
#     s[i] = s[i][::-1]

# s.sort()

# for i in range(len(s)):
#     s[i] = s[i][::-1]
#     s[i] = s[i][:-1]

# result = ' '.join(s)

# print(result)