# 1. Jak dzia³a petla while(){ przykk³ad }

i = 0
n = 10
while i<=n:
    print(i)
    i+=1
# petla Do..While w Pyton nie istnieje

#2. prostokat ze znaków
for i in range(5):
    linia = ''
    for j in range(10):
        linia = '*' + linia
    print(linia)
#3. przechylona choinka
linia = ''
for j in range(10):
    linia = linia + '*'
    print(linia)
#4. przechylona choinka w drug¹ stronê
print("")
i = 10
while (i >= 0):
    i = i + 2
    j = i - 1
    linia = ''
    for i in range(j):
        linia = linia + '*'
    print(linia)
    linia = " " + linia
    i = i - 1