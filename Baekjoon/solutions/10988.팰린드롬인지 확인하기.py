'''
거꾸로 읽어도 똑같은 단어를 팰린드롬이라고 함.
팰린드롬인지 아닌지 출력하기
'''


string = list(str(input()))

if list(reversed(string)) == string:
    print(1)
else :
    print(0)
    
    