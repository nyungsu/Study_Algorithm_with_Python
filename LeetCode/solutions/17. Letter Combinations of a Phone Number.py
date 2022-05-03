'''
문제 이름 : 17. Letter Combinations of a Phone Number
문제 링크 : https://leetcode.com/problems/letter-combinations-of-a-phone-number/
문제 풀이 : dict로 알파벳 맵핑하고
시간 복잡도 : 
공간 복잡도 :

'''

class Solution:
    def __init__(self) -> None:
        self.table = {2 : 'a b c',
                      3 : 'd e f',
                      4 : 'g h i',
                      5 : 'j k l',
                      6 : 'm n o',
                      7 : 'p q r s',
                      8 : 't u v',
                      9 : 'w x y z'}
        
    def letterCombinations(self, digits: str) -> list[str]:
        int_digits = list(map(int,digits))
        
        if int_digits == None:
            return None
        
        dict2list = [self.table[int_digits[i]] for i in range(len(int_digits))]
        print(dict2list)
        
        