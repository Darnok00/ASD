#Reprezenetacja macierzowa
def MS(tab,n):
    for i in range (0,n):
        for j in range (0,n):
            tab[i][j]=int(input())
    print(tab)
#Reprezentacja List Sąsiedztwa
def LS(tab,n):
    for i in range(n):
        tab[i] = []
    k = int(input("wprowadz liczbę krawedzi"))
    for i in range (0,k):
        tab[int(input())].append(int(input()))
    print(tab)
n = int(input("podaj liczbę wierzcholkow ziomek:"))
tab1=[[0]*n for i in range(n)]
tab2=n*[0]
MS(tab1,n)
LS(tab2,n)

