#klasyczny algorytm sortowania bąbelkowego
def bubble_sort(tab, n):
    for k in range(0,n-1):
        for i in range(0,n-k-1):
            if tab[i] > tab[i+1]:
                tab[i], tab[i+1] = tab[i+1], tab[i]
#input i output
n = int(input("Podaj ilosc liczb: "))
tab = [0]*n
for i in range(0,n):
    tab[i]=int(input())
bubble_sort(tab,n)
for i in range(0,n):
    print(tab[i])
