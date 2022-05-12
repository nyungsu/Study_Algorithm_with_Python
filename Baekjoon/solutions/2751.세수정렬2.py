'''
문제 이름 : 2751.세수정열2
문제 링크 : https://www.acmicpc.net/problem/2751
시간 복잡도 : O(NlogN)
공간 복잡도 : O(1)
2750과 테스트케이스의 길이가 다르다
input() 함수보다
sys.stdin.readline() 함수가 더 빠르다고한다
'''

import sys
N = int(input())
num = [int(sys.stdin.readline()) for _ in range(N)]
    
for i in sorted(num):
    sys.stdout.write(str(i)+'\n')