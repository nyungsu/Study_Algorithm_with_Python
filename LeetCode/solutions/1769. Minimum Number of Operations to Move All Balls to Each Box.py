
'''
문제 이름 : 1769. Minimum Number of Operations to Move All Balls to Each Box
문제 링크 : https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
문제 풀이 :  
시간 복잡도 : 
공간 복잡도 :
'''

class Solution:
    def minOperations(self, boxes :str) :
        output = []
        tmp = 0
        
        for i in range(len(boxes)):
            for j in range(len(boxes)):
                if boxes[j] =='1':
                    tmp += abs(j-i)
            output.append(tmp)
            tmp = 0
        return output