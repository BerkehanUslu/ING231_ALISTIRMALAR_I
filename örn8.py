counter = 0
for i in range(100,999,2):
    i = str(i)
    if i[0] == i[1] or i[0] == i[2] or i[1] == i[2]:
        counter+= 1

print(counter)
        
