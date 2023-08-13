import numpy as np
import random as r
import sys
import matplotlib.pyplot as plt


n = r.randint(1, 10)
m = r.randint(1, 10)
M = np.zeros((n, m))

listaocen = [u for u in np.arange(2, 6, 1/2)]
for w in range(n):
    for k in range(m):
        M[w][k] = M[w][k] + r.choice(listaocen)

#1
def niezaliczylin(M):
    niezaliczoneprzedmioty = [0 for x in range(n)]
    l = r.randint(0, m + 1)
    for w in range(n):
        for k in range(m):
            if M[w][k] < 2.5:
                niezaliczoneprzedmioty[w] = niezaliczoneprzedmioty[w] + 1
    odp = 0
    for s in niezaliczoneprzedmioty:
        if s >= l:
           odp= odp + 1
    return ("Tyle studentów niezaliczyło co najmniej n przedmiotów:", odp)


#2
def srednie(M):
    sumyocen = []
    for w in M:
        s = sum(w)
        sumyocen.append(s)
    return("Oceny studentów z najwyższą średnią to:", M[sumyocen.index(max(sumyocen))], "\n",
   "Oceny studentów z najmniejszą średnią to:", M[sumyocen.index(min(sumyocen))])


#3
def najoceny(M):
    listanajocen = [0 for c in range(m)]
    najstudenci = [0 for e in range(n)]
    for w in range(n):
        for k in range(m):
            if M[w][k] >= listanajocen[k]:
                listanajocen[k] = M[w][k]
    for i in range(m):
        for j in range(n):
            if listanajocen[i] == M[j][i]:
                najstudenci[j] +=1
    return najstudenci



#4
def histogram(M):

    for i in range(m):
        plt.hist(M[:, i], bins=10, range=(2.0, 5.5))
        plt.title(f'Histogram przedmiotu {i+1}')
        plt.xlabel('Oceny')
        plt.ylabel('Liczba studentów')
        plt.show()
        print()


#5
def sredniepow4ipol(M):
    listastud = []
    for w in range(n):
        u = sum(M[w]) / m
        if u >= 4.5:
            listastud.append(w)
    return ("Wiersze studentów, którzy mają średnią powyżej 4.5 to:", listastud)



# 2 ZADANIE
def odlmacierzy(A,B):
    sumodl = 0
    for w in range(len(B)):
        for k in range(len(B[0])):
            sumodl = sumodl + abs(A[w][k] - B[w][k])
    return sumodl


#3 Zadanie
def gauss(X):
    for i in range(len(X)):
        max = i
        for j in range(i + 1, len(X)):
            if abs(X[j, i]) > abs(X[max, i]):
                max = j
        X[[i, max], :] = X[[max, i], :]

        if X[i, i] != 0:
            X[i, :] /= X[i, i]

        for j in range(i + 1, len(X)):
            c = X[j, i] / X[i, i]
            X[j, :] -= c * X[i, :]

    for i in reversed(range(len(X))):
        for j in range(i):
            c = X[j, i] / X[i, i]
            X[j, :] -= c * X[i, :]

    X[np.abs(X) < 1e-10] = 0

    return X


#4 Zadanie
def walidacjaparagon(paragon, opistowarow):
    for w in paragon:
        c = 0
        for k in opistowarow:
            if w[1] == k[0]:
                c = 1
                if k[2] == 0 and w[2] * 10 % 10 != 0:
                    return "Produkt sprzedawany w sztukach nie jest liczbą całkowitą"
        if not c:
            return "Tego numeru nie ma na liście towarów:"
    return "paragon poprawny"


def cenaklienta(paragon, opistowarow, nr_klienta):
    cena = 0
    for w in paragon:
        if w[0] == nr_klienta:
            for k in opistowarow:
                if k[0] == w[1]:
                    cena += k[1] * w[2]
    print("Cena którą zapłacił klient ", cena)




