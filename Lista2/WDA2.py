import timeit
import numpy as np
import plotly.graph_objects as go
import math
import random

#zad1
def babelkowe(lista):
    for j in range(len(lista) - 1):
        for i in range(0, len(lista) - 1 - j):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
    return lista

def wstawianie(lista):
    for i in range(1, len(lista)):
        k = lista[i]
        j = i - 1
        while j >= 0 and k < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = k

    return lista



def wybieranie(lista):
    for i in range(len(lista)):
        idx = i
        for j in range(i + 1, len(lista)):
            if lista[idx] > lista[j]:
                idx = j

        lista[i], lista[idx] = lista[idx], lista[i]
    return lista




#zad2
# obliczamy czas sortowania babelkowego
def czas_babelkowego(n):
    SETUP_CODE = '''
from __main__ import babelkowe
from random import randint'''

    TEST_CODE = f'''
mylist = [x for x in range({n})]
babelkowe(mylist)
    '''

    czas = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          number=10)


    return np.mean(czas), max(czas)



# obliczamy czas sortowania wybieranie
def czas_wybierania(n):
    SETUP_CODE = '''
from __main__ import wybieranie
from random import randint'''

    TEST_CODE = f'''
mylist = [x for x in range({n})]
wybieranie(mylist)'''


    czas = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          number=10)


    return np.mean(czas), max(czas)


# obliczamy czas sortowania wstawianie
def czas_wstawiania(n):
    SETUP_CODE = '''
from __main__ import wstawianie
from random import randint'''

    TEST_CODE = f'''
mylist = [x for x in range({n})]
wstawianie(mylist)
    '''

    czas = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          number=10)

    return np.mean(czas), max(czas)




#zad3
def wykresy():
    #wykres sortowania babelkowego
    babelkowe_średnie = []
    babelkowe_max = []
    x = [10,  20,  50,  100,  200,  500,  1000]
    for n in x:
        średni_czas, max_czas = czas_babelkowego(n)
        babelkowe_średnie.append(średni_czas)
        babelkowe_max.append(max_czas)




    #wykres sortowania przez wybieranie

    wybieranie_średnie = []
    wybieranie_max = []
    x = [10,  20,  50,  100,  200,  500,  1000]
    for n in x:
        średni_czas, max_czas = czas_wybierania(n)
        wybieranie_średnie.append(średni_czas)
        wybieranie_max.append(max_czas)



    #wykres sortowania przez wstawianie

    wstawianie_średnie = []
    wstawianie_max = []
    x = [10,  20,  50,  100,  200,  500,  1000]
    for n in x:
        średni_czas, max_czas = czas_wybierania(n)
        wstawianie_średnie.append(średni_czas)
        wstawianie_max.append(max_czas)


    fig = go.Figure(data = go.Scatter (x = x, y = babelkowe_średnie, name='Średni czas sortowania bąbelkowego'))
    fig.add_trace(go.Scatter(x=x, y=babelkowe_max, name='Max czas sortowania bąbelkowego'))
    fig.add_trace(go.Scatter(x = x, y = wybieranie_średnie, name='Średni czas sortowania przez wybieranie'))
    fig.add_trace(go.Scatter(x=x, y=wybieranie_max, name='Max czas sortowania przez wybieranie'))
    fig.add_trace(go.Scatter(x = x, y = wstawianie_średnie, name='Średni czas sortowania przez wstawianie'))
    fig.add_trace(go.Scatter(x=x, y=wstawianie_max, name='Max czas sortowania przez wstawianie'))
    fig.update_layout(title='Sorting time', xaxis_title='List length', yaxis_title='Time (seconds)')
    fig.show()

#zad4
#babelkowe zatrzymuje się jeśli nie ma zamiany
def babelkowe2(lista):
    for j in range(len(lista) - 1):
        zamiana = False
        for i in range(0, len(lista) - 1 - j):
            if lista[i] > lista[i + 1]:
                zamiana = True
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
        if not zamiana:
            return lista
    return lista
#babelkowe porównuje do końca ciągu
def babelkowe3(lista):
    for j in range(len(lista) - 1):
        for i in range(0, len(lista) - 1):
            if (lista[j] > lista[j + 1]):
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
    return lista
#zad4
def czas_babelkowego2(n):
    SETUP_CODE = '''
from __main__ import babelkowe2
from random import randint'''

    TEST_CODE = f'''
mylist = [x for x in range({n})]
babelkowe2(mylist)
    '''

    czas = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          number=10)


    return np.mean(czas), max(czas)

def czas_babelkowego3(n):
    SETUP_CODE = '''
from __main__ import babelkowe3
from random import randint'''

    TEST_CODE = f'''
mylist = [x for x in range({n})]
babelkowe3(mylist)
    '''

    czas = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          number=10)


    return np.mean(czas), max(czas)
#zad5
def porównanie_czasów():
    print(babelkowe(100))
    print(babelkowe2(100))
    print(babelkowe3(100))
#zad6
def testy_wydajnościowe():
    #babelkowe
    for n in [10, 100, 1000]:
        l = [random.randint(0, 1000) for i in range(n)]
        t = timeit.timeit(lambda: babelkowe(l), number=1)
        r = (n * math.log(n)) / t
        print(f"babelkowe | {n} | {t:.6f}s | {r:.6f}")
    # babelkowe2
        l = [random.randint(0, 1000) for i in range(n)]
        t = timeit.timeit(lambda: babelkowe2(l), number=1)
        r = (n * math.log(n)) / t
        print(f"babelkowe2 | {n} | {t:.6f}s | {r:.6f}")
    # babelkowe3
        l = [random.randint(0, 1000) for i in range(n)]
        t = timeit.timeit(lambda: babelkowe3(l), number=1)
        r = (n * math.log(n)) / t
        print(f"babelkowe3 | {n} | {t:.6f}s | {r:.6f}")
    # wybieranie
        l = [random.randint(0, 1000) for i in range(n)]
        t = timeit.timeit(lambda: wstawianie(l), number=1)
        r = (n * math.log(n)) / t
        print(f"wybieranie | {n} | {t:.6f}s | {r:.6f}")
    # wstawianie
        l = [random.randint(0, 1000) for i in range(n)]
        t = timeit.timeit(lambda: wybieranie(l), number=1)
        r = (n * math.log(n)) / t
        print(f"wstawianie | {n} | {t:.6f}s | {r:.6f}")

