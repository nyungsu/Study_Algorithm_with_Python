'''
a의 알파벳의 순서를 바꾸어 b를 만들 수 있다면
애너그램
'''
from collections import Counter
a = 'aba'
b = 'aab'

a = Counter(a)
b = Counter(b)

print(a == b)
