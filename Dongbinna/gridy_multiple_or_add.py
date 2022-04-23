num_list = list(input(''))

result = int(num_list[0])

for i in range(1,len(num_list)):
    num = int(num_list[i])
    if num <=1 or result<=1:
        result += num
    else:
        result *= num
        
print(result)
#처음 짠 거
# result =1

# while True:
#     if not '0'in num_list:
#         break
    
#     num_list.remove('0')
    
#     if not '0'in num_list:
#         break


# for i in num_list:
#     result *=int(i)


# print(result)