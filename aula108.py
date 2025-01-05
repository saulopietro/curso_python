from itertools import count as c
c1 = c()
r1 = range(10)

for i in c1:
    print(i)
    if i == 100:
        break
