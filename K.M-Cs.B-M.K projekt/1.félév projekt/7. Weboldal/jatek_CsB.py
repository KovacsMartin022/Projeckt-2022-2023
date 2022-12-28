import random
def eletero():
    return random.randint(1, 300)
def karak(szam):
    karakterek = ["vadmajom", "nyilas ember", "mérges kígyó"]


    kar = karakterek[szam]

    print(f"Szembe jött egy {kar} ")
    return kar
def eszkoz(ellenfel_karakter,szam):
    karakterek = ["vadmajom", "nyilas ember", "mérges kígyó"]
    eszkozok = ["éles fogak", "íj és nyilak", "méreg"]
    sebzes = [50, 65, 70]
    kar = karakterek[szam]
    eszkoz = eszkozok[szam]
    seb = sebzes[szam]
    print(f"A {kar} a következővel harcol: {eszkoz} és sebzése: {seb} %")
    return seb
def sza():
     return random.randint(0, 2)

def harc(ellenfel_karakter, ellenfel_eletero, ellenfelsebzes, fosebzes, foelet):
    ellenfel_eletero -= fosebzes
    foelet -= ellenfelsebzes
    print(f"A(z) {ellenfel_karakter} sebzése: {ellenfelsebzes} %, így neked {foelet}% életerőd maradt!")
    print(f"A(z) te sebzésed: {fosebzes} % így a {ellenfel_karakter} életereje {ellenfel_eletero} % lett!")
    if(foelet <= 0):
        print("Sajnos meghalltál. Vége a játéknak.")
        exit()
    else:
        print("Megnyerted a csatát, folytasd az utad!")
    return foelet


fokarakter = "ember"
fosebzes = 60
foelet = 700
print("Üdv a játékban!")
print("Ez a történet egy ritka gyémánt megtalálásáról szól.")
print("A feladatod: megszerezni a gyémántot úgy, hogy a pályákon közben harcolnod kell az ellenfeleiddel.")

print("Te egy ember vagy és egy bunkókalapács a fegyvered, és egy kötél a kisegítő eszközöd.")
szam = sza()
ellenfel_karakter = karak(szam)
ellenfel_eletero = eletero()
print(f"A következő tulajdonságokkal")
print(f"\tÉleterő {ellenfel_eletero} %")
ellenfelsebzes = eszkoz(ellenfel_karakter, szam)

foelet = harc(ellenfel_karakter, ellenfel_eletero, ellenfelsebzes, fosebzes, foelet)

for i in range(2,11):
    print(f"{i}. elem: {harc(ellenfel_karakter, ellenfel_eletero, ellenfelsebzes, fosebzes, foelet)}")
print("Eljutottál utad végére. A gyémántot megtaláltad! A játékot sikeresen kívégezted!")
print("GRATULÁLOK!!!")
