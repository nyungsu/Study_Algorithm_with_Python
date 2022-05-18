'''
문제 이름 : 2609.최대공약수와 최소공배수
문제 링크 : https://www.acmicpc.net/problem/2609
시간 복잡도 : 
공간 복잡도 : 
'''

a,b = map(int,input().split())

def gcd(a,b): 
    while b>0:
        a,b = b, a%b
    return a
def lcm(a,b): 
    return a * b // gcd(a,b) 

print(gcd(a,b))
print(lcm(a,b))
