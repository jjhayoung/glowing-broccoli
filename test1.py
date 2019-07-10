def fyoon(n):
    i=0 #
    while i<n:
        i=i+1
        print("yoon")


def gugudan(k):
    for i in range(1,10):
        ans = k*i
        print("%s * %s = %s" %(k, i, ans))

def gugudanAll():
    for i in range (2,10):
        for k in range (1,10):
           ans = i*k
           print("%s * %s = %s" %(i, k, ans))
        print('\n')

def gugudanHori():
    for i in range (1,10):
        for k in range (2,10):
           ans = i*k
           print("%s * %s = %s" %(k, i, ans), end="\t")
        print()

def gugudanEvenH():
    for i in range (1,10):
        for k in range (2,10,2):
           ans = i*k
           print("%s * %s = %s" %(k, i, ans), end="\t")
        print()

def gugudanInput(n):
    for i in range (1,10):
        for k in range (n,10,2):
           ans = i*k
           print("%s * %s = %s" %(k, i, ans), end="\t")
        print()

