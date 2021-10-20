import random
statement = True


while statement == True:
    r1 = random.randint(10,100)
    r2 = random.randint(10,100)
    new = str(r1)+str(r2)
    if (r1 + r2)*11 == int(new):
        print(r1)
        print(r2)
        statement = False

