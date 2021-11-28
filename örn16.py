def asalMi(i):

    if i<2:
        return False
    
    n=2
    while i % (n) != 0:
        n+= 1
        if n == i:
            return True
