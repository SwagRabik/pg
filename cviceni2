def cislo_na_slovo(x):
    x = int(x)

    j = [
        "nula",
        "jedna",
        "dva",
        "tři",
        "čtyři",
        "pět",
        "šest",
        "sedm",
        "osm",
        "devět"
    ]

    t = [
        "deset",
        "jedenáct",
        "dvanáct",
        "třináct",
        "čtrnáct",
        "patnáct",
        "šestnáct",
        "sedmnáct",
        "osmnáct",
        "devatenáct"
    ]

    d = [
        "",
        "",
        "dvacet",
        "třicet",
        "čtyřicet",
        "padesát",
        "šedesát",
        "sedmdesát",
        "osmdesát",
        "devadesát"
    ]

    if x < 10:
        slovo = j[x]
    else:
        if x < 20:
            slovo = t[x - 10]
        else:
            if x < 100:
                deset = x // 10
                jed = x % 10
                if jed == 0:
                    slovo = d[deset]
                else:
                    slovo = d[deset] + " " + j[jed]
            else:
                if x == 100:
                    slovo = "sto"
                else:
                    slovo = "mimo rozsah"

    return slovo


if __name__ == "__main__":
    cis = input("Zadej číslo: ")
    vysl = cislo_na_slovo(cis)
    print("Slovně je to:", vysl)
