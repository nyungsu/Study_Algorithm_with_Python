change = int(input('얼마를 거슬러 주나요 ?'))
change_copy = change

#for문으로 정리
coin_list = [500,100,50,10]
count = 0
for i in coin_list:
    count += change // i
    change -=i*(change//i)

print(count)

#처음 짠 거
# num_of_500 = change_copy//500
# change_copy = change_copy - 500*num_of_500

# num_of_100 = change_copy //100
# change_copy = change_copy - 100*num_of_100

# num_of_50 = change_copy //50
# change_copy = change_copy - 50*num_of_50

# num_of_10 = change_copy //10

# print(num_of_10+num_of_50+num_of_100+num_of_500)


