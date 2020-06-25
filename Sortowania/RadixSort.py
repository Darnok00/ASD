#RadixSort standardowy Algorytm
def countsort(tab,n,place):
        tab1=[0]*10
        tab2=[0]*n
        for i in range(0,n):
            tab1[(tab[i]//place)%10]+=1
        for i in range (1,10):
            tab1[i]+=tab1[i-1]
        for i in range (n-1,-1,-1):
            tab2[tab1[(tab[i]//place)%10]-1]=tab[i]
            tab1[(tab[i]//place)%10]-=1
        for i in range (0,n):
            tab[i]=tab2[i]
def maxx(tab,n):
    K=0
    for i in range(0,n):
        if K < tab[i]:
            K=tab[i]
    return K
def radixsort(tab,n,maks):
        mul=1
        while maks>0:
            countsort(tab,n,mul)
            mul*=10
            maks//=10
n = int(input("Podaj ilosc liczb ziom: "))
tab = [0]*n
for i in range(0,n):
    tab[i]=int(input())
maks=maxx(tab,n)
radixsort(tab,n,maks)
for i in range(0,n):
    print(tab[i])
