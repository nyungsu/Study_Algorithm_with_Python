'''
문제 이름 : 1943.최소공배수
문제 링크 : https://www.acmicpc.net/problem/1934
시간 복잡도 : 
공간 복잡도 : 
'''

n = int(input())

def gcd(a,b): 
    while b>0:
        a,b = b, a%b
    return a
def lcm(a,b): 
    return a * b // gcd(a,b) 

for i in range(n): 
    a,b = map(int, input().split())
    print(lcm(a,b))