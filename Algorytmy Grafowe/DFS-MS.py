#Reprezenetacja macierzowa
def MS(tab,n):
    for i in range (0,n):
        for j in range (0,n):
            tab[i][j]=int(input())
    print(tab)
def DFS(tab,n):
    MS(tab, n)
    visited=[False]*n
    parent=[None]*n
    entry=[0]*n
    exit=[0]*n
    def DFSVisit(u):
        nonlocal time
        nonlocal visited
        nonlocal exit
        nonlocal parent
        nonlocal entry
        time+=1
        visited[u]=True
        entry[u]=time
        for i in range(0,n):
            if tab[u][i]==1:
                v=i
                if visited[v]==False:
                    parent[v]=u
                    DFSVisit(v)
        time+=1
        exit[u]=time
    time = 0
    for i in range(0,n):
        v = i
        visited[v]=False
        parent[v]=None
    for i in range(0,n):
        v = i
        if visited[v]==False:
            DFSVisit(v)
    print(exit)
n = int(input("podaj liczbę wierzcholkow ziomek:"))
tab1=[[0]*n for i in range(n)]
DFS(tab1,n)
