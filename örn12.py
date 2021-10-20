for i in range(1900,2005):
    i = str(i)
    comp = int(i[0]) + int(i[1]) + int(i[2]) + int(i[3])
    if (2005 - int(i)) == comp:
        print(i)
