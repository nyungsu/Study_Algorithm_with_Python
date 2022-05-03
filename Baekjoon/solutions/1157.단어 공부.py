'''
가장 많이 사용된 알파벳 출력하기
'''

from collections import Counter

string = list(str(input()))
counter_string = Counter(string)
most_common = counter_string.most_common(1)     # [(첫 번째로 많이 쓰인), (2번째로 많이 쓰인)]
for i in len(string):
    if most_common[i][0] == most_common[i+1][0]:
        print('?')
    
print(most_common[0][0].upper())                        # [(알파벳, 갯수)]


