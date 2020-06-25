def merge (tab,start,mid,end):
    p = start
    q = mid+1
    tab1=[0]*(end-start+1)
    k=0
    for i in range (start,end+1):
        if p > mid:
            tab1[k] = tab[q]
            k += 1
            q += 1
        elif  q > end:
            tab1[k] = tab[p]
            k += 1
            p += 1
        elif tab[ p ] < tab[ q ]:
            tab1[k] = tab[p]
            k += 1
            p += 1
        else:
            tab1[k] = tab[ q]
            k += 1
            q += 1
    for p in range (0,k):
        tab[start] = tab1[p]
        start += 1
def merge_sort (tab,start,end):
    if start < end :
        mid = (start + end ) // 2
        merge_sort (tab, start , mid )
        merge_sort (tab,mid+1 , end )
        merge(tab, start, mid, end)
n = int(input("Podaj ilosc liczb ziom: "))
tab = [0]*n
for i in range(0,n):
    tab[i]=int(input())
merge_sort(tab,0,n-1)
for i in range(0,n):
    print(tab[i])
