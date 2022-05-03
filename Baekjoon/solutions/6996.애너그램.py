'''
a의 알파벳의 순서를 바꾸어 b를 만들 수 있다면
애너그램
'''
from collections import Counter

T = int(input())

for i in range(T):
    a1,a2 = map(str,input().split())
    a1_counter = Counter(a1)
    a2_counter = Counter(a2)
    
    if a1_counter == a2_counter:
        print(f'{a1} & {a2} are anagrams.')
    else:
        print(f'{a1} & {a2} are NOT anagrams.')

    
    
    


