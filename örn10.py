counter = 0
for i in range(10000,100000):
    i = str(i)
    if i[0:2] == i[-2:]:
        counter+=1
        print(i)

print(counter)
    
