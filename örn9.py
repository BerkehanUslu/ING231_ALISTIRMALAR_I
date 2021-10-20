for i in range(1,1000):
    i = str(i)
    n = len(i)
    if n==1 and int(i)<9:
        print(i,end=" ")
    elif n==2 and (int(i[0]) + int(i[-1]) ) < 9:
        print(i,end=" ")
    elif n==3 and (int(i[0]) + int(i[1]) + int(i[-1]) ) < 9:
        print(i,end=" ")
        
        
