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

def gugudanPrime():
    for i in range (1,10):
        prime = [2,3,5,7]
        for k in prime:
            ans = i *k
            print("%s * %s = %s" %(k, i, ans), end="\t")
        print()

def gugudanDic():
    dic = {'2dan':'hello','3dan':'hi'}

    for i in dic.values():
        print(i)

def gugudanD():
    dic = {'2dan':7,'3dan':2,'4dan':4}
    key = input("2dan, 3dan, 4dan 중 하나를 입력하세요(잘못입력시 5단이 출력됩니다):")
    
    i=dic.get(key, 5)  #i=dic[key]라고 해도 되지만, 디폴트값을 설정하기 위해 dic.get(key,5)를 사용함. 
    for k in range (1,10):
        result = k*i
        print("%s * %s = %s" %(i, k, result))
    print()
        
def listNum():
    allNum=[]
    for i in range(100):
        allNum.append(i+1)
    print("모든 숫자들의 목록 : %s " %(allNum))                    
    oddNum=allNum[0::2]
    print("홀수의 목록 : %s " %(oddNum))
    evenNum=allNum[1::2]
    print("짝수의 목록 : %s " %(evenNum))

def listTextNum():
    allNum =[]
    for i in range(100):
        allNum.append(i+1)
    SList = [str(x) for x in allNum]
    print(SList)
    oddNum=SList[0::2]
    print(oddNum)
    evenNum=SList[1::2]
    print(evenNum)

def NewListNum():
    evenNum=[]
    oddNum=[]
    x=1
    while x<100:
        if x%2 ==0:
            evenNum.append(x)
        else:
            oddNum.append(x)
        x+=1
    evenNum=[str(x) for x in evenNum]
    oddNum=[str(x) for x in oddNum]
    print(evenNum)
    print(oddNum)

def List():#List Comprehension
    L = [x+1 for x in range(100)]
    L1=[x for x in L if x%2==0]
    L2=[x for x in L if x%2==1]
    S = [str(x+1) for x in range(100)]
    S1=[str(x) for x in S if int(x)%2==0]
    S2=[str(x) for x in S if int(x)%2==1]
    print(L)
    print(L1)
    print(L2)
    print(S)
    print(S1)
    print(S2)

def ListPrac():
    L=list(range(1,100))
    print(L)
#파일 읽어들인 후 숫자 판별하고 그것들의 합 리턴하기 과제
def isNum():
    
    
def findNum():
    file=open('aa.txt','r')
    Numfiles=file.readlines()
    Numfiles=[line.rstrip('\n')for line in Numfiles]
    
    return Numfiles
