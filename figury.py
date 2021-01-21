
def wybierz_figure(lp): 
    while lp.isdigit() == False or lp == 0:
        lp = input("wybierz figure, wpisz\n\
1 - prostokat\n2 - kwadrat\n3 - trojkat\n4 - trapez\n5 - kolo:\n")
        
    lp = int(lp)
        
    if lp == 1:
        a = input("wprowadz a: ")
        b = input("wprowadz b: ")
        while (a.isdigit() and b.isdigit()) == False:
            print( "error, wprowadz liczby")
            a = input("wprowadz a: ")
            b = input("wprowadz b: ")
                           
        a = int(a)
        b = int(b)
        wynik = a*b
        
    elif lp == 2:
        a = input("wprowadz a: ")
        while a.isdigit() == False:
            print( "error, wprowadz liczbe")
            a = input("wprowadz a: ")
            
        if a == 0:
            return
        
        a = int(a)
        wynik = a**2
        
    elif lp == 3:
        a = input("wprowadz a: ")
        h = input("wprowadz h: ")
        while (a.isdigit() and h.isdigit()) == False:
            print ("error, wprowadz liczby")
            a = input("wprowadz a: ")
            h = input("wprowadz h: ")
            
        if (a or h) == 0:
            return
        
        a = int(a)
        h = int(h)
        wynik = a*h/2
        
    elif lp == 4:
        a = input("wprowadz a: ")
        b = input("wprowadz b: ")
        h = input("wprowadz h: ")       
        while (a.isdigit() and b.isdigit() and h.isdigit()) == False:
            print( "error, wprowadz liczby")
            a = input("wprowadz a: ")
            b = input("wprowadz b: ")
            h = input("wprowadz h: ")
            
        if (a or b or h) == 0:
            return
        
        a = int(a)
        b = int(b)
        h = int(h) 
        wynik = ((a+b)*h)/2
        
    elif lp == 5:
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
        
    print (wynik)
    lp = "o" 



start = True
lp = "7"          
print("hi what do You want to calculate? (prostokat, kwadrat, trojkat, trapez, kolo), licz pole 1-4")
lp = input("wybierz figure, wpisz\n\
1 - prostokat\n2 - kwadrat\n3 - trojkat\n4 - trapez\n5 - kolo:\n")
while start == True:
    wybierz_figure(lp)
    lp = "k"

