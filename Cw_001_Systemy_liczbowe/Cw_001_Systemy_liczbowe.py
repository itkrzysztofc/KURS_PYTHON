print("Cwiczenie 1")
print("Zamiana liczby dziesietnej dodatniej na liczbe binarna")
print("======================================================")
print("Wprowadz liczbe, ktora chcesz zamienic na liczbe binarna:")
n = int(input())
print("Wybrales liczbe: " + str(n))
print("uzycie funkcji bin()") # funkcja wbudowana
print(bin(n))
print("------------------\n Wlasny algorytm:\n------------------")
#i = 0 #iteratory tablicy - niewymagany
tab = []
napis = ""
while n != 0:
    tab = int(n%2)
    n = (n - tab)/2
    #print(str(i) + " " + str(tab) + " " + str(n))
    napis += str(tab)
    #i+=1
print((napis))
#odwrocenie napisu
dlugosc = len(napis)
napis2 = ""
for i in range(dlugosc):
    napis2 += napis[dlugosc-i-1]
print(napis2)
print("Dlugosc liczby binarnej to " + str(dlugosc) + " znakow")

