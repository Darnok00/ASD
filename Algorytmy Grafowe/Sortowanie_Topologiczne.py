def LS(tab,n):
    for i in range(n):
        tab[i] = []
    k = int(input("wprowadz liczbę krawedzi"))
    for i in range (0,k):
        tab[int(input())].append(int(input()))
    print(tab)
#DFS Z SORTOWANIEM TOPOLOGICZNYM
def DFS(tab):
    n=len(tab)
    LS(tab, n)
    visited=[False]*n
    parent=[None]*n
    entry=[0]*n
    exit=[0]*n
    tabsort=[]
    def DFSVisit(u):
        nonlocal time
        nonlocal visited
        nonlocal exit
        nonlocal tab
        nonlocal tabsort
        time+=1
        visited[u]=True
        entry[u]=time
        for i in range(0,len(tab[u])):
            v = tab[u][i]
            if visited[tab[u][i]]==False:
                parent[v]=u
                DFSVisit(v)
        time+=1
        exit[u]=time
        tabsort.append(u)
    time = 0
    for i in range(0,len(tab)):
        v = i
        visited[v]=False
        parent[v]=None
    for i in range(0,len(tab)):
        v = i
        if visited[v]==False:
            DFSVisit(v)
    tabsort1=[0]*n
    for i in range(0,n):
        tabsort1[i]=tabsort[n-1-i]
    print(tabsort1)

n = int(input("podaj liczbę wierzcholkow ziomek:"))
tab2=n*[0]
DFS(tab2)
