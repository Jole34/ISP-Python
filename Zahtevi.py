'''

@author: Jovan
'''

def ucitajZahteve():
    for i in open("zahtevi.txt", "r").readlines():
        if len (i)>1:
            zahtev = procitajK(i)
            zahtevi.append(zahtev)
    return


def procitajK(i):
    if i[-1] =="\n":
        i = i[:-1]
    korisnik,intervencija,cena = i.split("|")
    novac = cena.strip()[1:]
    zahtev = {
        "korisnik": korisnik.strip(),
        "intervencija": intervencija.strip(),
        "novac": float(novac)
        }
    return zahtev
def toStr(zahtev):
    return " | " .join([zahtev["korisnik"], zahtev["intervencija"], zahtev["novac"]])
def ispi(zahtev):
    return "Korisnik {} ceka za {} ima  {:.2f} EUR ".format(zahtev["korisnik"], zahtev["intervencija"], zahtev["novac"])

if __name__ != "__main__":
    zahtevi = [] 
    ucitajZahteve()
