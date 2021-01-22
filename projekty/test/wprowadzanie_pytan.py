def zapis_pytania_odp (pytanie, wyjasnienie, poprawna_odpowiedz, odpowiedzi):
    print('wyglada to tak:', pytanie, wyjasnienie, poprawna_odpowiedz, odpowiedzi)
    zapis = (pytanie + " | " +  wyjasnienie + " | " + odpowiedzi[0] + " | " + odpowiedzi[1] + \
             " | " + odpowiedzi[2] + " | " + odpowiedzi[3] + " | " + odpowiedzi[4] )
    zapis = zapis + ("\n")
  
    with open(SciezkaPliku, "a", encoding="utf-8") as S: 
        S.write(zapis)
        
def wprowadzanie_pytan_odp():
    odpowiedzi = []
    licznik_odpowiedzi = 0
    
    pytanie = input("\nwprowadz pytanie: ")
    wyjasnienie = input("wprowadz wyjasnienie (mozna, nie trzeba): ")
    poprawna_odpowiedz = input("wprowadz poprawna odpowiedz: ")
    odpowiedzi.append(poprawna_odpowiedz)

    while licznik_odpowiedzi < 4:
        licznik_odpowiedzi += 1
        odpowiedz = input("wprowadz odpowiedz: ")
        odpowiedzi.append(odpowiedz)

    zapis_pytania_odp(pytanie, wyjasnienie, poprawna_odpowiedz, odpowiedzi)


SciezkaPliku = input("podaj nazwe pliku (bedzie w tym samym folderze co ten plik, w formacie '.txt',\n\
mozna dopisywac do pliku istniejacego lub tworzyc nowy plik), przykład: 'Pytania' ")
SciezkaPliku = SciezkaPliku + '.txt'
print(SciezkaPliku)
Ile_pytan = int(input('ile pytan chcesz wprowadzic(musi byc cyfra)'))
licz = 0

while licz < Ile_pytan:
    wprowadzanie_pytan_odp()
    licz += 1
