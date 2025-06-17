# x=123
# for i in x:
#     print(i)


vehicles = ['Car','Cycle','Bus','Tempo','Bike']
print(vehicles)
for i in vehicles:
    if i.startswith('B'):
        print(i)
    if not i.startswith('B'):
        print(i)
    if i=='Bus':
        break