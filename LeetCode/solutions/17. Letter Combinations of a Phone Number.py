'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
'''

class Solution:
    def __init__(self) -> None:
        self.table = {2 : 'abc',
                      3 : 'def',
                      4 : 'ghi',
                      5 : 'jkl',
                      6 : 'mno',
                      7 : 'pqrs',
                      8 : 'tuv',
                      9 : 'wxyz'}
        
    def letterCombinations(self, digits: str) -> list[str]:
        int_digits = int(digits)