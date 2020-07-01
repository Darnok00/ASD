def LS(tab,n):
    for i in range(n):
        tab[i] = []
    k = int(input("wprowadz liczbę krawedzi"))
    for i in range (0,k):
        tab[int(input())].append(int(input()))
    print(tab)
def DFS(tab):
    n=len(tab)
    LS(tab, n)
    visited=[False]*n
    exit=[0]*n
    exit0=[0]*n
    tabu=[]
    def DFSVisit(u,tab):
        nonlocal time
        nonlocal visited
        nonlocal exit
        nonlocal exit0
        nonlocal tabu
        visited[u]=True
        tabu.append(u)
        for i in range(0,len(tab[u])):
            v = tab[u][i]
            if visited[tab[u][i]]==False:
                DFSVisit(v,tab)
        time+=1
        exit[u]=time
    time = 0
    for i in range(0,len(tab)):
        v = i
        visited[v]=False
    for i in range(0,len(tab)):
        v = i
        if visited[v]==False:
            DFSVisit(v,tab)
    print(exit)
    #zmiana kierunku krawedzi
    tab1=[0]*n
    for i in range(n):
        tab1[i] = []
    for i in range (0,n):
        for j in range (0,len(tab[i])):
            s=tab[i][j]
            tab1[s].append(i)
    print(tab1)
    #kolejny DFS
    exit0=[0]*n

    for i in range(0,n):
        exit0[i]=exit[i]
    for i in range(0,n):
        v = i
        visited[v]=False
    for i in range(0,n):
        tabu=[]
        maks=0
        id=-1
        for j in range(0,n):
            if exit0[j]>maks and visited[j]==False:
                maks=exit0[j]
                id=j
        v=id
        if visited[v]==False:
            DFSVisit(v,tab1)
        print(tabu)
n = int(input("podaj liczbę wierzcholkow ziomek:"))
tab2=n*[0]
DFS(tab2)
