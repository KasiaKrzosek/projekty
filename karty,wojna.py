import random

cardList = ['joker','joker']
cards = ['9','10','walet','dama','krol','as']

for card in cards:
    count = 0
    while count < 4:
        count += 1
        cardList.append(card)

#print('cardlist =',cardList)

random.shuffle(cardList)

#print('\nshuffle cardlist =',cardList)

karta = cardList.pop()
#print('\nwielkosc pozostalej talii =',len(cardList))
#print('\nkarta =',karta)

gracze = ['gracz_1', 'gracz_2']
talie = { 1: [], 2: []}
#print('klucze talie =',talie.keys())
#print('zawartosc talie =',talie[1])

for key in talie:
    count_kart = 0
    #talia = []
    while count_kart < 5:
        count_kart += 1
        karta = cardList.pop()
        talie[key].append(karta)
    #print (talia)
print ('talia 1 =',talie[1])
print ('talia 2 =',talie[2])

#print ('\nwielkosc pozostalej talii =',len(cardList))

#print(talie)

##########wartosci = cards

n = 0
for karta1 in talie[1]: #and karta2 in talie[2]:
    print('\nrunda',n+1)
    print(talie[1][n],"przeciwko",talie[2][n])
    
    if talie[1][n] == talie[2][n]:
        print('wojna')
    
    n +=1
    






