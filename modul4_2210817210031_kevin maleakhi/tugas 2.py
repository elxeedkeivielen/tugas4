angka=int(input())

for n in range(1,angka+1) :
    if n%2!=0 :
        print(n, end=' ')
    else :
        pass
print('')
for n in reversed(range(2,angka+1)) :
    if n%2==0 :
        print(n, end=' ')
    else :
        pass
