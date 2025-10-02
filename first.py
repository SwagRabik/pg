def sudy_nebo_lichy(cislo):
    return cislo % 3 == 0

def main():
  cislo = int(input("Zadej číslo: "))
    if cislo % 2 == 0:
        return "Číslo (cislo) je sudé"
    else:
        return "Číslo (cislo je liché)"


if __name__ == "__main__":
    main() 
sudy_nebo_lichy(5)
sudy_nebo_lichy(1000000)