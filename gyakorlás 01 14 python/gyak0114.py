print("Hello World")
#Kérjen be egy számot és 10-szer írja ki hogy: szám;"almafa" tabulátorral elválasztva
szam=int(input("Kérek egy számot"))
for _ in range(10):
    print(szam,"almafa",sep=';',end='\t')
print()

for cv2 in range (1,11):
    for cv in range (1,11):
        print(cv*cv2,end='\t')

    print()

    #100* generáljunk 345 és 999 közötti számot
 #irassas ki a páros és hárommal osztható számokat
import random
print("3mal osztható páros számok")
for _ in range(100):
    szam=random.randint(345,999)
    if szam%2==0 and szam%3==0:
        print(szam,end='\t')
    print(szam)
    
    
 








print("")


szam=int(input("Kérek egy számot"))
while szam<10 or szam>50:
    print("Ez nem jó,kérek egy másikat")
    szam=int(input("Kérek egy másik számot"))
    print("ez már jó")










