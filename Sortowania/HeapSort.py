def heapify(tab, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and tab[i] < tab[l]:
        largest = l
    if r < n and tab[largest] < tab[r]:
        largest = r
    if largest != i:
        tab[i], tab[largest] = tab[largest], tab[i]
        heapify(tab, n, largest)
def BuildHeap(tab,n):
    for i in range(n, -1, -1):
        heapify(tab, n, i)
def heapSort(tab,n):
    BuildHeap(tab,n)
    for i in range(n - 1, 0, -1):
        tab[i], tab[0] = tab[0], tab[i]
        heapify(tab, i, 0)
n = int(input("Podaj ilosc liczb ziom: "))
tab=[0]*(n)
for i in range(0,n):
    tab[i]=int(input())
heapSort(tab,n)
for i in range(0,n):
    print(tab[i])

