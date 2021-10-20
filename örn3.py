toplam = 0

for n in range(0,1000):   
    if n > 1:
        fact = n
        for i in range(n,1,-1):                        
            fact = fact * (i-1) 
    else:
        fact = 1

    toplam = toplam + (1/fact)

print(toplam)
