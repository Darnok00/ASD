def LS(tab,n):
    for i in range(n):
        tab[i] = []
    k = int(input("wprowadz liczbę krawedzi"))
    for i in range (0,k):
        tab[int(input())].append(int(input()))
    print(tab)
def DFS_Bridge(tab,n):
    LS(tab,n)
    visited=[False]*n
    entry=[-1]*n
    low=[-1]*n
    time=0
    S=[]*n
    def DFS(v,p):
        nonlocal entry
        nonlocal tab
        nonlocal visited
        nonlocal low
        nonlocal time
        nonlocal S
        visited[v]=True
        entry[v] = low[v]=time
        time+=1
        for i in range(0,len(tab[v])):
            u=tab[v][i]
            if u==p:
                continue
            if visited[u]==True:
                low[v]=min(low[v],entry[u])
            else:
                DFS(u,v)
                low[v]=min(low[v],low[u])
                if low[u]>entry[v]:
                    S.append([u,v])
    for i in range(0,n):
        if visited[i]==False:
            DFS(i,-1)
    
    print(low)
    print(S)
n = int(input("podaj liczbę wierzcholkow ziomek:"))
tab1=[[0]*n for i in range(n)]
DFS_Bridge(tab1,n)
