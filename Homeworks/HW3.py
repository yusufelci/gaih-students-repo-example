
#prime_first
def prime_second():
    for i in range(500,1001):
        if i > 1:
            asal=False
            for j in range(2,i):
                if i % j ==0:
                    asal=True
            if asal==False:
                print(i)


prime_second()

#prime_second
def prime_first():
    for i in range(0,500):
        if i > 1 :
            asal=False
            for j in range(2,i):
                if i % j == 0:
                    asal=True
            if asal==False:
                print(i)

prime_first()