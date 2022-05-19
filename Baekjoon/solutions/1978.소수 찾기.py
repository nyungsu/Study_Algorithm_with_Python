'''
문제 이름 : 1978.소수 찾기
문제 링크 : https://www.acmicpc.net/problem/1978
시간 복잡도 : O(N^2)
공간 복잡도 : O(N)
'''


n = int(input())

num_list = list(map(int,input().split()))

cnt = 0

for i in num_list:
    for j in range(2,i+1):
        if i%j==0:
            if i == j:
                cnt += 1
             
            break
            
print(cnt)

