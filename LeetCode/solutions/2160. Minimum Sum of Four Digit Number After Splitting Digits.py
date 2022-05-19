'''
문제 이름 : 2160. Minimum Sum of Four Digit Number After Splitting Digits
문제 링크 : https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/
문제 풀이 : 와 개어이없다 이거
시간 복잡도 : O(NlogN)
공간 복잡도 : O(N)

'''

class Solution:
    def minimumSum(self, num: int) -> int:
        num = list(str(num))
        num.sort()
        num = list(map(int,num))

    
        return num[0]*10 + num[2] + num[1]*10 + num[3]

