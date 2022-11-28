angka1=int(input())
angka2=int(input())

n1=angka1
n2=angka2

if angka1>angka2 :
    while n1>=angka2 :
        print(n1,n2, end=' ')
        n1=n1-1; n2=n2+1
        if n1>angka2-1 :
            print(end=' - ')
        elif n2<angka2-1 :
            print(end=' - ')
else :
    while n1<=angka2 :
        print(n1,n2, end=' ')
        n1=n1+1; n2=n2-1
        if n1<angka2+1 :
            print(end=' - ')
        elif n2>angka2+1 :
            print(end=' - ')
