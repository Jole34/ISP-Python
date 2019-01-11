'''


@author: Jovan
'''


def ucitajUslugeJunior():
    for i in open("usluge1.txt", "r").readlines():
        if len (i)>1:
            uslugaJ = procitajJ(i)
            uslugeJunior.append(uslugaJ)
    return


def procitajJ(i):
    if i[-1] =="\n":
        i = i[:-1]
    intervencija,cena = i.split("|")
    cena = cena.strip()[1:]
    usluga = {
        "intervencija": intervencija.strip(),
        "cena": float(cena.replace(',', '.'))
        }
    return usluga
def ucitajUslugeSenior():
    for i in open("usluge2.txt", "r").readlines():
        if len (i)>1:
            uslugaS = procitajS(i)
            uslugeSenior.append(uslugaS)
    return 


def procitajS(i):
    if i[-1] =="\n":
        i = i[:-1]
    intervencija,cena = i.split("|")
    cena = cena.strip()[1:]
    usluga = {
        "intervencija": intervencija.strip(),
        "cena": float(cena.replace(',', '.'))
        }
    return usluga     

def pronadjiUsluguS(naziv):
    for usluga in uslugeSenior:
        if usluga["intervencija"].lower() == naziv.lower():
            return usluga
    return -1    
def pronadjiUsluguJ(naziv):
    
    for usluga in uslugeJunior:
        u = usluga["intervencija"]
        if u.lower() == naziv.lower():
            return usluga
    return -1       

    
def sortirajJS():
    minPos = 0
    for i in range (0, len(uslugeSenior)):
        minPos = i
        mini = uslugeSenior[i]
        for j in range(i+1, len(uslugeSenior)):
            if uslugeSenior[j]["cena"] < mini["cena"]:
                mini = uslugeSenior[j]
                minPos = j
        uslugeSenior[i], uslugeSenior[minPos] = uslugeSenior[minPos], uslugeSenior[i]
    return

def sortirajJ():
    minPos = 0
    for i in range (0, len(uslugeJunior)):
        minPos = i
        mini = uslugeJunior[i]
        for j in range(i+1, len(uslugeJunior)):
            if uslugeJunior[j]["cena"] < mini["cena"]:
                mini = uslugeJunior[j]
                minPos = j
        uslugeJunior[i], uslugeJunior[minPos] = uslugeJunior[minPos], uslugeJunior[i]
    return




def pregledUFajl(usluga):
    u = usluga["intervencija"]
    c = usluga["cena"]
    return  "Intervencija {} po ceni od {:.2f} EUR".format(u, c)
    ## ippis float sa dve decimale



if __name__ != "__main__":
    uslugeJunior = []
    uslugeSenior = []
    ucitajUslugeJunior()
    ucitajUslugeSenior()
    
     
    
    
    
