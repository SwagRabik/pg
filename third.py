def je_prvocislo(cislo):
    cislo = int(cislo)
    if cislo < 2:
        return False
    for i in range(2, int(cislo ** 0.5) + 1):
        if cislo % i == 0:
            return False
    return True

def vrat_prvocisla(maximum):
    maximum = int(maximum)
    vysledek = []
    for i in range(2, maximum + 1):
        if je_prvocislo(i):
            vysledek.append(i)
    return vysledek

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    print(je_prvocislo(cislo))
    maximum = input("Zadej maximum: ")
    print(vrat_prvocisla(maximum))
