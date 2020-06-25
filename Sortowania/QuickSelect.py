#Algorytm kalsyczny QuickSelect, ktory zwraca k-najmniejsza liczbe ze zbioru 
#Uwaga, nie mowimy o indeksie, tylko o liczbie w kolejnosci!
def partition(arr, l, r):
    x = arr[r]
    i = l
    for j in range(l, r):

        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[r] = arr[r], arr[i]
    return i
def QSelect(arr, l, r, k):
    if (k > 0 and k <= r - l + 1):
        index = partition(arr, l, r)
        if (index - l == k - 1):
            return arr[index]
        if (index - l > k - 1):
            return QSelect(arr, l, index - 1, k)
        return QSelect(arr, index + 1, r,
                           k - index + l - 1)
k = 3
n = int(input("Podaj ilosc liczb ziom: "))
tab = [0]*n
for i in range(0,n):
    tab[i]=int(input())
print(QSelect(tab, 0, n - 1, k))
