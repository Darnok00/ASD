#klasyczny algorytm sortowania przez wybieranie
def selection_sort (tab,n):
        for i in range (0,n-1):
            minimum = i
            for j in range(i+1,n):
                if tab[j] < tab[minimum]:
                    minimum = j
            tab[minimum], tab[i] = tab[i], tab[minimum]
n = int(input("Podaj ilosc liczb ziom: "))
tab = [0]*n
for i in range(0,n):
    tab[i]=int(input())
selection_sort(tab,n)
for i in range(0,n):
    print(tab[i])
