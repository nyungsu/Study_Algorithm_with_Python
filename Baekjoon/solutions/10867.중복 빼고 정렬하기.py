'''
문제 이름 : 10867.중복 빼고 정렬하기
문제 링크 : https://www.acmicpc.net/problem/10867
시간 복잡도 : 
공간 복잡도 : 
'''

n = int(input())

num_list = list(map(int,input().split()))

num_list = list(set(num_list))
num_list.sort()

# num_list = list(set(num_list)).sort()
# 이거는 런타임 에러 뜨넹

for i in num_list:
    print(i, end=' ')
