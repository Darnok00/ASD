def LS(tab,n):
    for i in range(n):
        tab[i] = []
    k = int(input("wprowadz liczbę krawedzi"))
    for i in range (0,k):
        tab[int(input())].append(int(input()))
    print(tab)
def BFS(tab,s):
    n=len(tab)
    LS(tab,n)
    d=[0]*n
    visited=[False]*n
    parent=[None]*n
    queue=[]
    visited[s]=True
    queue.append(s)
    while len(queue)!=0:
        v=queue.pop(0)
        for i in range(0,len(tab[v])):
            u=tab[v][i]
            if visited[u]!=True:
                visited[u] = True
                d[u]=d[v]+1
                parent[u]=v
                queue.append(u)
    print(d)
n = int(input("podaj liczbę wierzcholkow ziomek:"))
tab2=n*[0]
BFS(tab2,0)
