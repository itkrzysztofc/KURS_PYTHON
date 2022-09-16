import math
from random import randint
#Cz.1 wprowadzenie
tab = []
print(tab)
dlugosc = 5
for i in range(dlugosc):
    tab.append(2*i+1) #dopisuje wartoœæ na koñcu tablicy
print(tab)
tab.insert(3,999) #wstawia w czaery index tablicy wartosc '999'
print(tab)
tab[5] = 2**10 #potegowanie
print(tab)
#pierwiastek
print(2**(1/2)) #zadzia³a pierwiastek lub
print(math.sqrt(2)) #konieczny import modu³u `math`
print(tab[3]) #wyswietla element o indeksie `3`
#============================================
#tablica z losowanymi elementami
tab2 = []
for i in range(dlugosc):
    tab2.append(randint(-10,10))
print(tab2)
print(sum(tab2)) #suma elementu tablicy `tab2`

# cz.2 operacje na tablicachliczbowych
# - wylosowanie tablicy oraz posortowanie jej bez metody append
tabLos = []
for i in range(10):
    tabLos.insert(i,randint(-50,50))
print(tabLos) # tablica przed sortowaniem
# - znalezienie minimum i maximum
minimum = 0
maksimum = 0
for i in range(len(tabLos)):
    if (tabLos[i] > maksimum):
        maksimum = tabLos[i]
    if (tabLos[i] < minimum):
        minimum = tabLos[i]
print('MIN = ' + str(minimum))
print('MAX = ' + str(maksimum))
# posortowanie tablicy malej¹co
for i in range(len(tabLos)-1, 0, -1):
    for j in range(i):
        if tabLos[j] > tabLos[j+1]:
            #tabLos[j], tabLos[j+1] = tabLos[j+1], tabLos[j]
            bufor = tabLos[j]
            tabLos[j] = tabLos[j+1]
            tabLos[j+1] = bufor
print(tabLos)