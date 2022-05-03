'''
2중 for문과 최댓값 찾기
'''

T = int(input())

for i in range(T):
    N = int(input())
    max = 0
    maxName = ""
    for _ in range(N):
        name, num = input().split()
        num = int(num)
        if(num > max):
            max = num
            maxName = name
            print(maxName)
