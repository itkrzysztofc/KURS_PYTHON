#Cw 4
#from math import factorial


 #program wyznacza liczby pierwsze od poczatku zakresu do `n`
n = input("Podaj liczbe calkowita `n` tworzaca gorny zakres liczb pierwszych: ")
n = int(n)
#funkcja `sito`
def sito(n):
    kandydat = [1 for k in range(n+1)]
    pierwsze = []
    for i in range(2,n+1):
        if kandydat[i] != 0:
            pierwsze.append(i)
            for j in range(2*i,n+1,i):# range(start,stop,krok)
                kandydat[j]=0
    return pierwsze

print(sito(n))