#suma wszystkich argumentow z wagami
def suma (*arg):
    print("=", sum(*arg))

def srednia_prosta(*arg):
    print("srednia prosta =", sum(*arg)/len(*arg) )

def srednia_wazona( suma = 1, *oceny_Waga):
    print("srednia wazona =", sum(*oceny_Waga)/suma)
    
#srednia wazona

global oceny
oceny = []
global wagi
wagi = []
global oceny_Waga
oceny_Waga = []

y = int(input("(kropki nie przecinki)\n\
ile liczb chcesz podac?: "))

for x in range(0, y):
    ocena = float(input("podaj ocene: "))
    waga = float(input("podaj wage: "))    
    print("licznik ocen -", x+1)
    
    oceny.append(ocena)
    wagi.append(waga) 
    ocena_Waga = ocena * waga
    oceny_Waga.append(ocena_Waga)
    
print()
print("oceny:",oceny)
print("wagi:",wagi)
print("oceny z wagami:",oceny_Waga)
suma_Wag = sum(wagi)
print()

print("suma:")
print("suma ocen")
suma(oceny)
print("suma wag")
print("=", suma_Wag) #, type(suma_Wag)
print("suma ocen z wagami")
suma(oceny_Waga)
print()

srednia_prosta(oceny)
srednia_wazona(suma_Wag, oceny_Waga)
