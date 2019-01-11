'''


@author: Jovan
'''

from UKIM import Administrator, Upravljanje, Usluge, Zahtevi

odradjeno = []
def login():
    print(">>> Ulogujte se kao administrator <<<\n")
    global korisnicko
    korisnicko = input("Korisnicko ime: ")
    global sifra
    sifra = input("Lozinka: ")
    return Administrator.login(korisnicko, sifra)


def main():
    print("____________________________")
    print("____________________________")
    print("                            ")
    print("-----   UKIM company   -----")
    print("____________________________")
    print("____________________________")

    
    if not login():
        print("\nNeispravno korisnicko ime ili lozinka!!! \nPonovo pokrenite program i pokusajte ponovo...")
        return
    izbor = 0
    if not Administrator.senior(korisnicko, sifra):
        print ("        DOBRO DOSLI        \n")
        while (izbor != "k"):
            izbor = meni1()
            if izbor == "1":
                ipisibrZahteva()
            if (izbor == "2"):
                ispisiIntervencije()
            if (izbor == "3"):
                ispisiZad()    
            if (izbor == "4"):
                odradiZahJ()
            if (izbor == "k"):
                zavrsi()
    else:
        print ("        DOBRO DOSLI        \n")
        while (izbor != "k"):
            izbor = meni2()
            if izbor == "1":
                ipisibrZahteva()
            if (izbor == "2"):
                ispisiIntervencijeS()
            if (izbor == "3"):
                ispisiZad()    
            if (izbor == "4"):
                odradiZahS()
            if (izbor == "5"):
                zaradjenaSuma()
            if (izbor == "6"): 
                odradiHitno()  
            if (izbor == "k"):
                zavrsi()
                
    
    print("____________________________")
    print("____________________________")
    print("                            ")
    print("-----   UKIM company   -----")
    print("____________________________")
    print("__________JG________________")
    
    
    
    
    
               
def meni1():
    stampajMeni1()
    izbor = input ("\nIzaberite odredjenu opciju:")
    while izbor.lower() not in ('1', '2', '3', '4', 'k'):
        print ("Niste uneli pravilnu opciju! \n")
        izbor = input ("Izaberite odredjenu opciju:")
    return izbor.lower()

def meni2():
    stampajMeni2()
    izbor = input ("\nIzaberite odredjenu opciju:")
    while izbor.lower() not in ('1', '2', '3', '4', '5','6','k'):
        print ("Niste uneli pravilnu opciju! \n")
        izbor = input ("Izaberite odredjenu opciju:")
    return izbor.lower()



    
def stampajMeni1():
    print ("----- Ponudjene opcije su: \n")
    print ("----- (1) | Broj zahteva | ")
    print ("----- (2) | Intervencije (zahtevi) koji su mi dopusteni |")    
    print ("----- (3) | Proveri i ispisi zaduzena lica | ")
    print ("----- (4) | Odradi zahtev | ")
    print ("----- (k) | Zavrsi i upisi u fajl odradjene tikete(zahteve)|")
    
def stampajMeni2():
    print ("----- Ponudjene opcije su: \n")
    print ("----- (1) | Broj zahteva | ")
    print ("----- (2) | Intervencije (zahtevi) koji su mi dopusteni |")    
    print ("----- (3) | Proveri i ispisi zaduzena lica | ")
    print ("----- (4) | Odradi zahtev | ")
    print ("----- (5) | Prikazi zaradjen novac! |  ")
    print ("----- (6) | Postavi novu hitnu intervenciju ! |  ")
    print ("----- (k) | Zavrsi i upisi u fajl odradjene tikete(zahteve)|")    
    
    
def odradiHitno():
    korisnik = input("Ime korisnika: ")
    intervencija = input ("Intervencija: ")
    novac = eval(input("Cena hitnosti: "))
    if intervencija.lower() == "Izlazak terenaca".lower():
        Upravljanje.hitnaInt(korisnik, intervencija, novac)
        print ("Intervencija stavljena na prvo mesto!")
    else:
        print ("Intervencija nije hitna i nece se staviti na prvo mesto!")

    
def ipisibrZahteva():
    print ("Broj zahteva je: ", len(Zahtevi.zahtevi))
    
def ispisiIntervencije():
    print ("----- Sortirana lista usluga: ")
    Usluge.sortirajJ()
    for i in Usluge.uslugeJunior:
        print (Usluge.pregledUFajl(i))    


def ispisiIntervencijeS():
    print ("----- Sortirana lista usluga: ")
    Usluge.sortirajJ()
    for i in Usluge.uslugeSenior:
        print (Usluge.pregledUFajl(i))

def ispisiZad():
    print ("Zaduzenih korisnika je: ", len(Upravljanje.zaduzeni))

def zaradjenaSuma():
    print("\n Zaradjen novac je ")
    print("{:.2f} EUR".format(zarada))


def odradiZahJ():
    print("----- Odradi zahtev")
    global zarada
    if  len(Zahtevi.zahtevi) == 0 :
        print("Nema zahteva!") 
        return
    naziv = str(Zahtevi.zahtevi[0]["intervencija"])
    usluga = Usluge.pronadjiUsluguJ(naziv)
    if (usluga  == -1):
        print ("\n Pokusali ste da pristupite opciji za seniora\n")
        return
    zaradaInt = Upravljanje.odradiZahtev(naziv)
    if(zarada != (zarada+zaradaInt)):
        zarada += zaradaInt
        odradjeno.append({"intervencija": naziv, "cena": usluga["cena"]})
    return



def odradiZahS():
    print("----- Odradi zahtev")
    global zarada
    if  len(Zahtevi.zahtevi) == 0 :
        print("Nema zahteva!") 
        return
    naziv = Zahtevi.zahtevi[0]["intervencija"]
    zaradaInt = Upravljanje.odradiZahtev(naziv)
    usluga = Usluge.pronadjiUsluguS(naziv)
    if(zarada != (zarada+zaradaInt)):
        zarada += zaradaInt
        odradjeno.append({"intervencija": naziv, "cena": usluga["cena"]})
    return


def zavrsi():
    f = open('ZavrseniTiketi.txt', 'a')
    f.write("Odradjeni tiketi: \n")
    for odradjen in odradjeno:
        f.write("%s\n" % Usluge.pregledUFajl(odradjen))





if __name__ == "__main__":
    zarada = 0
    main()
        
            

            
            
            
            
