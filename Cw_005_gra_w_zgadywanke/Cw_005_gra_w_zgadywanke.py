from random import randint
import time #biblioteka obsluguj¹ca czas w Python

print("Gra w zgadywanke liczby") 
imie = input('''Podaj swoje imie: ''')
losowanie = ""
print("Prosze czekac. Trwa losowanie liczby:")
for i in range(5):  
    losowanie = losowanie + "."
    print(losowanie)
    time.sleep(1) #czas w sekundach
los = randint(0,100)
#print(los)
licznik = 0
liczba = -1
while los != int(liczba):
    liczba = input(" Podaj liczbe: ")
    licznik +=1
    if int(liczba) > los:
        print("Podales za duzo")
    elif int(liczba) < los:
        print("poadales za malo")
    else:
        print("BRAWO "+ imie + " udalo ci sie odgadnac za " + str(licznik) + " razem")