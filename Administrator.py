'''


@author: Jovan
'''



def ucitajAdmin():
    for linija in open("administratori.txt", "r").readlines():
        if(len(linija) > 1):
            admin = procitaj(linija)
            administratori.append(admin)
    return


def procitaj(linija):
    if linija[-1]=="\n":
        linija=linija[:-1]
    korisnicko,tip,sifra =linija.split("|")  
    admin={
     "korisnicko": korisnicko.strip(),
     "tip": tip.strip(),
     "sifra": sifra.strip(),
     }
    return admin

def login(korisnicko, sifra):
    for i in administratori:
        if i ["korisnicko"] == korisnicko and i ["sifra"] == sifra:
            if (i["tip"] == "junior"):
                print ("----- Vi ste junior administrator!  \n")
               
            else:
                print ("----- Vi ste senior administrator!  \n")
            return True
    return False

def senior(korisnicko, sifra):
    for i in administratori:
        if i ["korisnicko"] == korisnicko and i ["sifra"] == sifra:
            if (i["tip"] == "junior"):
                return False
    return True
            

def toStr(admin):
    return "|".join([admin[0]["korisnicko"], admin[0]["tip"], admin[0]["sifra"]])
   



if __name__ != "__main__":
    administratori = []
    ucitajAdmin()
    



