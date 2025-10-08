def sudy_nebo_lichy(cislo):
    if cislo % 2 == 0:
        return "Číslo " + str(cislo) + " je sudé"
    else:
        return "Číslo " + str(cislo) + " je liché"

def main():
    cislo = int(input("Zadej číslo: "))
    print(sudy_nebo_lichy(cislo))

    print(sudy_nebo_lichy(5))
    print(sudy_nebo_lichy(1000000))

if __name__ == "__main__":
    main()
