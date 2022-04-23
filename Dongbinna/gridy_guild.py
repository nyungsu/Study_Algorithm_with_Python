from tracemalloc import start


group=list(map(int,input().split(" ")))

sorted_group =sorted(group,reverse=True)

print(sorted_group)

# max_phobia = sorted_group[0]
# team1=[]
# for i,v in enumerate(sorted_group,start=1):
#     team1.append(v)
#     if i ==max_phobia:
#         break

# team1=[v for i,v in enumerate(sorted_group,start=1) if i<=max_phobia]
# print(team1)


team =[]
team_temp =sorted_group
max_phobia = sorted_group[0]
while True:
    for i,v in enumerate(team_temp,start=1):
        team.append(v)
        if i ==max_phobia:
            team.append(' ')
            break
    team_temp = sorted_group[max_phobia:]
    max_phobia = team_temp[0]

    if team_temp == sorted_group[4]:
        break
print(team)

    