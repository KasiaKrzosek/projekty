#definicja wybierz pole jakiej figury chcesz obliczyc

figury = {1: "prostokata", 2: "kwadrata", 3: "trojkata", 4: "trapeza", 5: "kola"}


z = 0
liczby = {"1","2","3","4","5","6","7","8","9","0","."," "}
zmienne = []
napis = []

#test wszystkiego
testInput = [None, "Python", "0,1", "0 1", 1+2j]

for eachItem in testInput:   
    try:
        if isinstance(eachItem, str):
            print("float('{}') = {}".format(eachItem, float(eachItem)))
        else:
            print("float({}) = {}".format(eachItem, float(eachItem)))
    except Exception as ex:
        print("float({}) = {}".format(eachItem, ex))

#check for 1/0
try:
    print("float(1/0) = {}".format(float(1/0)))
except Exception as ex:
    print("float(1/0) = {}".format(ex))

from enum import IntEnum 

Menu_Figury = IntEnum('Menu_Figury', "Prostokat Kwadrat Trojkat Trapez Kolo") 

def wybierz_figure(lp):
#wstepne informacje         
    lp = input("wybierz figure, wpisz\n\
1 - prostokat\n2 - kwadrat\n3 - trojkat\n4 - trapez\n5 - kolo:\n")
#w razie bledu

    while lp.isdigit() == False:
        lp = input("wybierz figure, wpisz\n\
1 - prostokat\n2 - kwadrat\n3 - trojkat\n4 - trapez\n5 - kolo:\n")
#gdy poprawne        
    lp = int(lp)        
    if lp == Menu_Figury.Prostokat:
        h = 0

        a = input("wprowadz a: ")
        b = input("wprowadz b: ")       
        zmiana =[a,b]
        for eachItem in zmiana:   
            try: 
                if isinstance(eachItem, str):
                    print("float('{}') = {}".format(eachItem, float(eachItem)))
                else:
                    print("float({}) = {}".format(eachItem, float(eachItem)))
            except Exception as ex:
                    #print("float({}) = {}".format(eachItem, ex))
                print( "blad, wprowadz liczby (zamiast przecinka uzyj kropki '.')")
                h = 0
            h = 1

        
                               
        a = float(a)
        b = float(b)
        wynik = a*b
        
    elif lp == Menu_Figury.Kwadrat:
        a = input("wprowadz a: ")
        while a.isdigit() == False:
            print( "blad, wprowadz liczbe")
            a = input("wprowadz a: ")
            
        if a == 0:
            return
        
        a = int(a)
        wynik = a**2
        
    elif lp == Menu_Figury.Trojkat:
        a = input("wprowadz a: ")
        h = input("wprowadz h: ")
        while (a.isdigit() and h.isdigit()) == False:
            print ("blad, wprowadz liczby")
            a = input("wprowadz a: ")
            h = input("wprowadz h: ")
            
        if (a or h) == 0:
            return
        
        a = int(a)
        h = int(h)
        wynik = a*h/2
        
    elif lp == Menu_Figury.Trapez:
        a = input("wprowadz a: ")
        b = input("wprowadz b: ")
        h = input("wprowadz h: ")       
        while (a.isdigit() and b.isdigit() and h.isdigit()) == False:
            print( "blad, wprowadz liczby")
            a = input("wprowadz a: ")
            b = input("wprowadz b: ")
            h = input("wprowadz h: ")
            
        if (a or b or h) == 0:
            return
        
        a = int(a)
        b = int(b)
        h = int(h) 
        wynik = ((a+b)*h)/2
        
    elif lp == Menu_Figury.Kolo:
        r = input("wprowadz r:")
        while r.isdigit() == False:
            return "wprowadz liczbe"
            r = input("wprowadz r:")
            
        if r == 0:
            return
        
        r = int(r)      
        wynik = 3.1416 *(r**2)

    else:
        print ("error")
        lp = "l"
        
    print ("pole", figury[lp], "=",wynik,"\n")
    lp = "o" 








start = 1
print("Czesc! Wybierz figure ktorej pole chcesz obliczyc")
lp = "l"
while start == True:
    wybierz_figure(lp)
    
