mylist1 = list()
mylist2 = list()

for x in range(2,125):    
    if 125%x==200%x==350%x:
        mylist1 += [x]
        mylist2 += [125%x]

mylist2.sort()
print("En büyük kalan: {0}".format(mylist2[-1]))  
 

