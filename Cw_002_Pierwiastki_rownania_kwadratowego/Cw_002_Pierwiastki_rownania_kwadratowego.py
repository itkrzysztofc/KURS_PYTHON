#Program obliczaj¹cy pierwiaski rownania kwadratowego
# 1. w celu stworzenia rownania kwadratoweggo losujemy wspolczynniki a,b,c
# 2. sprawdzamy dzy jest to rownanie kwadratowe, czy liniowe, czy liczba
# 3. obliczmy pierwiaski rownaia kwadratowego

#========= poczatek kodu ===========#
from pickletools import float8
from random import randint

imie = input('Podaj swoje imie:  ')
print('Witaj ' + imie)
print('\n Wlasnie zostaly wylosowane wspolczynniki rownania kwadratowego a, b, c')
a = randint(-10,10)
b = randint(-10,10)
c = randint(-10,10)
delta = b**2 - 4*a*c
print("Rownanie ma postac: y = " + str(a) + "x^2 + " + str(b) + "x + " + str(c))
print('Delta = ' + str(delta))
if (a == 0):
    print('To nie jest rownianie kwadratowe')
elif (a == 0 and b == 0):
    print('ani rownanie liniowe')
elif(delta == 0):
    print('rownanie kwadratowe ma jedno rozwiazanie')
    x = -b/(2*a)
    print ('x  = '  + str(x))
elif (delta < 0):
    print('rownanie NIE ma rozwiazania')
else:
    print ('Rownanie ma dwa rozwiazania')
    x1 = (-b-delta)/(2*a)
    x2 = (-b+delta)/(2*a)
    print ('x1 = ' + str(x1))
    print ('x2 = ' + str(x2))
