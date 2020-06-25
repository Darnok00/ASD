#Klasyczny algorytm sortowania przez wstawianie 
def insertion_sort (tab,n):
     for i in range(0,n):
        temp = tab[i]
        j = i
        while  j > 0  and temp < tab[j-1]:
            tab[j] = tab[j-1]
            j=j-1
        tab[j] = temp
n = int(input("Podaj ilosc liczb joł: "))
tab = [0]*n
for i in range(0,n):
    tab[i]=int(input())
insertion_sort(tab,n)
for i in range(0,n):
    print(tab[i])
