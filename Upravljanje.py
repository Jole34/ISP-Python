'''

@author: Jovan
'''

from UKIM import Usluge
from UKIM import Zahtevi


def ucitajAdrese():
    for i in open("adrese.txt", "r").readlines():
        if len (i)>1:
            adresa = procitajA(i)
            ip.append(adresa)
    return


def procitajA(i):
    if i[-1] =="\n":
        i = i[:-1]
    ip,prefiks= i.split("|")
    klasa = ip.strip()[:3]
    maska = "255.255.255.255"
    if (float(klasa) < 127 ):
        maska = "255.0.0.0"
    if ((float(klasa) > 128) & (float(klasa) < 191) ):
        maska = "255.255.0.0"
    if ((float(klasa) > 191) & (float(klasa) < 223) ):
        maska = "255.255.255.0"
    adresa = {
        "ip": ip.strip(),
        "prefiks": prefiks.strip(),
        "klasa": klasa.strip(),
        "maska": maska.strip()
        }
    return adresa


def odradiZahtev(zahtev):
    cena = 0
    usluga = Usluge.pronadjiUsluguS(zahtev)
    if (usluga!= -1):
        if (Zahtevi.zahtevi[0]["novac"] >= usluga["cena"]):
            if (zahtev == "Novi korisnik"):
                dhcp()
                cena = cena+usluga["cena"]
                del Zahtevi.zahtevi[0]
                print("Novi korisnik uspesno dodat")
            else:
                cena = cena + usluga["cena"]
                del Zahtevi.zahtevi[0]
                print ("Uspesno obavljena intervencija")
        else:
            if (zahtev == "Novi korisnik"):
                dhcp()
                zaduzeni.append(Zahtevi.zahtevi[0])
                del Zahtevi.zahtevi[0]
                print ("Novi korisnik je zaveden u knjigu duznika")
            else:
                zaduzeni.append(Zahtevi.zahtevi[0])
                del Zahtevi.zahtevi[0]
                print ("Korisnik je zaveden u knjigu duznika")
    else:
        del Zahtevi.zahtevi[0]
        print ("Korisnik je zahtevao intervenciju koju nije moguce izvrsiti")
    return cena   
def dhcp():
    adresa = ""
    javnaA = ""
    maska = ""
    javnaAmaska = ""
    for i in ip:
        if (i["maska"] == "255.255.255.0"):
            adresa = i
            maska = i["maska"]
            break
    for i in ip:
        if (i["maska"] == "255.0.0.0"):
            javnaA = i["ip"]
            javnaAmaska = i["maska"]
            break
    javnaA = str(javnaA)        
    definisana = str(adresa["ip"[0:7]])
    pocetna = definisana.replace("0", "168", 1)
    poslednja  = pocetna.replace("0", "9")
    ssid = "UKIM20190"
    broj = str(len(noviKorisnici)+1)
    wpa = "AsdF20190"
    if len(noviKorisnici) == 0:
        ssid = "UKIM20191"
    else:
        ssid = str("UKIM2019"+broj) 
        javnaA = javnaA.replace("0", broj, 1)
    if len(noviKorisnici) == 0:
        wpa = "AsdF20191"
    else:
        wpa = str("AsdF2019"+broj)         
    korisnik = {
        "pocetna": pocetna,
        "poslednja": poslednja,
        "javna": javnaA,
        "javnaMaska": javnaAmaska,
        "maska": maska,
        "ssid": ssid,
        "wpa": wpa
        }
    noviKorisnici.append(korisnik)
def unosNovog(novi):
    return " | " .join([novi["pocetna"], novi["poslednja"], novi["javna"], novi["javnaMaska"], novi["maska"], novi["javna"], novi["ssid"], novi["wpa"]])
def hitnaInt(korisnik, intervencija, novac):
    zahtev = {"korisnik": korisnik, "intervencija": intervencija, "novac": float(novac)}
    Zahtevi.zahtevi.append(Zahtevi.zahtevi[0])
    Zahtevi.zahtevi.insert(0, zahtev)
    return          

if __name__ != "__main__":
    ip = []
    noviKorisnici = []
    zaduzeni = []
    ucitajAdrese()