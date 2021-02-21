
#Generating  3x3 matrix with 9 random prime numbers.


import random as rnd

a = [[0] * 3 for i in range(3)]

for i in range(3):
    for j in range(3):
        a[i][j] = rnd.randint(1,100)

for row in a:
    print(' '.join([str(x) for x in row]))
