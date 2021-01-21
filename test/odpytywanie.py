def zadawanie_pytan():
    import random
    import time
    import math
   
    global SciezkaPliku
    SciezkaPliku = input("Prosze podaj nazwe pliku (musi byc w tym samym folderze co ten plik,\n\
w formacie '.txt' - innych formatow nie przyjmuje), przykład: 'Pytania' ")
    SciezkaPliku = SciezkaPliku + '.txt'
    print('otwierasz plik o nazwie:', SciezkaPliku)
    lb_pytan = input('Prosze podaj ilosc pytan (musi byc cyfra): ')
    
    while lb_pytan.isdigit() == False:
        print( "error, wprowadz cyfre")
        lb_pytan = input('Prosze podaj ilosc pytan (musi byc cyfra): ')       

    lb_pytan = int(lb_pytan)
    wyrazy = []
    
    with open(SciezkaPliku, "r") as S:
        wiersze = S.readlines() #utworz liste
        miejsce = 0

        for wiersz in wiersze:
            wiersz = wiersz[:-1]
            rozdzielonyWiersz  = wiersz.split(" | ")
            nowyWiersz = [[rozdzielonyWiersz[0]] + [rozdzielonyWiersz[1]] + [rozdzielonyWiersz[2]] + rozdzielonyWiersz[3:]]           
            wyrazy.extend(nowyWiersz)
        
        random.shuffle(wyrazy)  
    
    wybrane_pytania = []
    licznik_pytan = 0
    
    if lb_pytan > len(wyrazy):
        print('\njest',len(wyrazy),'pytan dostepnych')
        
        while len(wyrazy) >= 1:
            wybrane_pytania.append(wyrazy[-1])
            wyrazy.pop()
            
    else:
        while licznik_pytan < lb_pytan: #60
            licznik_pytan += 1
            wybrane_pytania.append(wyrazy[-1])
            wyrazy.pop()
        
    global zbior_pytan
    pytanie_licznik = 0
    slownik_pytan = {}
    zbior_pytan = []
    
    for pytanie in wybrane_pytania:      
        #slownik_pytan = {nr_pytania: pytanie, wyjasnienie: wyj, poprawna_odp: popr_odp, mozliwe_odp: [mozliwe odp]}        
        Wszystkie_odpowiedzi = wybrane_pytania[pytanie_licznik][2:]       
        random.shuffle(Wszystkie_odpowiedzi)
        odpowiedzi = {'a': 0 ,'b': 0 ,'c': 0 ,'d': 0 ,'e': 0}
        licz = 0
        
        for odpowiedz in odpowiedzi:            
            odpowiedzi[odpowiedz] = Wszystkie_odpowiedzi[licz]
            #print(odpowiedz, odpowiedzi[odpowiedz])
            licz += 1
                   
        slownik_pytan = {pytanie_licznik +1: wybrane_pytania[pytanie_licznik][0],\
                         "wyjasnienie": wybrane_pytania[pytanie_licznik][1],\
                         "poprawna": wybrane_pytania[pytanie_licznik][2],\
                         "mozliwe": odpowiedzi}       
         
        #print('slownik_pytan', slownik_pytan)
        zbior_pytan.append(slownik_pytan)  
        pytanie_licznik += 1
        
    licznik = 0
    odpowiedzi = []            
    PoczatekCzasu = time.time()
    print('\nProsze podaj odpowiedz: a, b, c, d lub e')
    
    for pytanie in zbior_pytan:
        print()
        print(str(licznik+1) + ".", str(zbior_pytan[licznik][licznik+1]) + ": ")      
        licz = 0
        
        for klucz in zbior_pytan[licznik]["mozliwe"].keys():
            print(klucz + ")", zbior_pytan[licznik]["mozliwe"][klucz])
            licz += 1
        
        #odpowiedzi = ['y', 'i', 't', 'poprawna odp', 's']
        odpowiedz = input("Podaj odpowiedz: ")
        odpowiedzi.append(odpowiedz)
        licznik += 1
        
    licz = 0
    punkty = 0
    znane_odpowiedzi = []
    znane_pytania = []
    nieznane_odpowiedzi = []
    nieznane_pytania = []
    nieznane_poprawne_odpowiedzi = []
    wyjasnienia_nieznanych = []
       
    for odpowiedz in odpowiedzi:
        if odpowiedz in zbior_pytan[licz]["mozliwe"]\
        and zbior_pytan[licz]["mozliwe"][odpowiedz] == zbior_pytan[licz]["poprawna"]:                
            punkty +=1
            znane_odpowiedzi.append(odpowiedz)
            znane_pytania.append(zbior_pytan[licz][licz + 1])
            
        else:
            nieznane_odpowiedzi.append(odpowiedz)
            nieznane_poprawne_odpowiedzi.append(zbior_pytan[licz]["poprawna"])
            nieznane_pytania.append(zbior_pytan[licz][licz + 1])
            wyjasnienia_nieznanych.append(zbior_pytan[licz]["wyjasnienie"])
                    
        licz += 1
                      
    print('\nliczba punktow:', punkty, "na", len(odpowiedzi))
    print("to jest %.1f procent " %(punkty/len(odpowiedzi)*100))       
    print('\npytania i odpowiedzi dla poprawnie udzielonych odopwiedzi:')
    licznik = 0   
    
    for odpowiedz in znane_pytania:       
        print(znane_pytania[licznik], znane_odpowiedzi[licznik])
        licznik +=1
        
    print('\npytania i odpowiedzi dla NIEpoprawnie udzielonych odopwiedzi, podane:')
    licznik = 0
    
    for odpowiedz in nieznane_pytania: 
        print(nieznane_pytania[licznik], nieznane_odpowiedzi[licznik])
        licznik +=1
           
    print('\npytania, odpowiedzi i wyjasnienie czemu dla NIEpoprawnie udzielonych odopwiedzi, poprawne:')
    licznik = 0
    
    for odpowiedz in nieznane_pytania: 
        print(nieznane_pytania[licznik], ",", nieznane_poprawne_odpowiedzi[licznik], ",", wyjasnienia_nieznanych[licznik])
        licznik +=1
    
    KoniecCzasu = time.time() - PoczatekCzasu
    KoniecCzasu = int(KoniecCzasu)
    print('\nzajelo Ci to %.2f minut(y)' %(KoniecCzasu/60))
    #time.sleep(100)

anserw = 'tak'
while anserw == 'tak':
    zadawanie_pytan()
    anserw = input("wpisz 'tak' by powtorzyc: ")
    anserw.lower()
    print(anserw)    
else:
    print('to czesc, dziena za dzis')
    
