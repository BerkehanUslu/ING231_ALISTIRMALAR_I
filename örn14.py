li = list()
for i in range(2,60606):
    if 121212%i == 0:
        li.append(i)


minval = li[int((len(li)+1)/2)] - li[int((len(li)+1)/2 - 1)]
print(minval)
