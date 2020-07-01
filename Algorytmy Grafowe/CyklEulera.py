#Reprezenetacja macierzowa
def MS(tab,n):
    for i in range (0,n):
        for j in range (0,n):
            tab[i][j]=int(input())
    print(tab)
def DFS_Euler(tab,n):
    MS(tab, n)
    f=True
    for i in range(0,n):
        k=0
        for j in range(0,n):
            if tab[i][j]==1:
                k+=1
        if k%2!=0:
            f=False
            print("BRAK CYKLU EULERA")
            break
    if(f==True):
        print("GRAF POSIADA CYKL EULERA")
        S=[]
        tabb=[]
        S.append(0)

        def DFSVisit(u):
            nonlocal tab
            nonlocal S
            nonlocal tabb
            for i in range(0,n):
                if tab[u][i]==1:
                    S.append(i)
                    tab[i][u]=0
                    tab[u][i]=0
                    v=i
                    DFSVisit(v)
                if i==(n-1) and tab[u][i]==0:
                    tabb.append(S.pop())
        DFSVisit(0)
        tabbb=[0]*len(tabb)
        for i in range (0,len(tabb)):
            tabbb[i]=tabb[len(tabb)-1-i]
        print(tabbb)
    #tabbb to cykl EUlera jezeli istnieje

n = int(input("podaj liczbę wierzcholkow ziomek:"))
tab1=[[0]*n for i in range(n)]
DFS_Euler(tab1,n)
