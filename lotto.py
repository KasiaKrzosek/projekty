import random
import time
"""
def choose_random_number (amount, total_amount):
    return random.sample(range(total_amount + 1), amount)

wybrane_liczby = []
ile_razy = 50
for i in range (ile_razy):
    wybrane_liczby.append(choose_random_number(6, 49))
    print(i + 1, wybrane_liczby[i])

print()
print(wybrane_liczby)
"""

def losuj_liczby (ile, liczba_koncowa):
    liczby = set()
    print("losuje liczby")
    a = 1
    while len(liczby) < ile:
        a = a + 0.25
        nowa_liczba = random.choice(range(1, liczba_koncowa + 1))
        liczby.add(nowa_liczba)
        time.sleep(a)
        print(nowa_liczba)
    else:
        return liczby

def wybierz_liczbe(ile, liczba_koncowa):
    wybrane_liczby = set()
    print("zakres od 1 do", liczba_koncowa)
    
    while len(wybrane_liczby) < ile:       
        nowa_liczba = int(input("wpisz liczbe: "))
        wybrane_liczby.add(nowa_liczba)
    else:
        return wybrane_liczby


def porownaj_zbiory_liczb(liczby, wybrane_liczby):
    if liczby == wybrane_liczby:
        return "Gratulacje! udalo Ci sie zgadnac wszystkie liczby"
    elif wybrane_liczby.intersection(liczby):
        zgadniete_liczby = wybrane_liczby.intersection(liczby)
        return "Gratulacje! udalo Ci sie zgadnac",len(zgadniete_liczby), "nastepujace liczby:", zgadniete_liczby
    else:
        return "Przykro mi, nie udalo Ci sie zgadnac zadnej z wylosowanych liczb"
    
global wybrane_liczby
wybrane_liczby = wybierz_liczbe(6, 49)
print("Twoje liczby:", wybrane_liczby)
global liczby
liczby = (losuj_liczby(6,49))
print("Wylosowane liczby:", liczby)

print(porownaj_zbiory_liczb(liczby,wybrane_liczby))

        

