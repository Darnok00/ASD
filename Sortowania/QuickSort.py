#klasyczny algorytm sortowania szybkiego
def partition ( tab, start ,end):
    i = start + 1
    piv = tab[start]
    for j in range (start + 1,end+1):
        if  tab[ j ] < piv:
            tab[ i ],tab[ j ]=tab[j],tab[i]
            i += 1
    tab[start],tab[ i-1]=tab[i-1],tab[start]
    return i-1
def quick_sort ( tab,start,end):
   if start < end:
         piv_pos = partition(tab,start,end )
         quick_sort (tab,start , piv_pos -1)
         quick_sort ( tab,piv_pos +1 , end)
n = int(input("Podaj ilosc liczb ziom: "))
tab = [0]*n
for i in range(0,n):
    tab[i]=int(input())
quick_sort(tab,0,n-1)
for i in range(0,n):
    print(tab[i])
