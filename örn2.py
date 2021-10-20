t = 0

for n in range(1,100000000):
    t = t + 1/(n**2)

pi = (6*t)**(1/2)
print(pi)
