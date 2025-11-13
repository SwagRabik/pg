def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    start_r, start_s = figurka["pozice"]
    cil_r, cil_s = cilova_pozice
    typ = figurka["typ"]

    if not (1 <= cil_r <= 8 and 1 <= cil_s <= 8):
        return False

    if cilova_pozice in obsazene_pozice:
        return False

    dr = cil_r - start_r
    ds = cil_s - start_s
    abs_dr = abs(dr)
    abs_ds = abs(ds)

    if typ == "pěšec":
        if ds != 0:
            return False
        
        if dr == 1:
            return True

        if dr == 2 and start_r == 1:
            mezilehle_pole = (start_r + 1, start_s)
            if mezilehle_pole not in obsazene_pozice:
                return True
        
        return False

    elif typ == "jezdec":
        if (abs_dr == 2 and abs_ds == 1) or (abs_dr == 1 and abs_ds == 2):
            return True
        return False

    elif typ == "král":
        if abs_dr <= 1 and abs_ds <= 1:
            return True
        return False
    
    step_r = (dr > 0) - (dr < 0)
    step_s = (ds > 0) - (ds < 0)

    if typ == "věž":
        if dr != 0 and ds != 0:
            return False
        
        r, s = start_r + step_r, start_s + step_s
        while (r, s) != cilova_pozice:
            if (r, s) in obsazene_pozice:
                return False
            r += step_r
            s += step_s
        return True

    elif typ == "střelec":
        if abs_dr != abs_ds:
            return False

        r, s = start_r + step_r, start_s + step_s
        while (r, s) != cilova_pozice:
            if (r, s) in obsazene_pozice:
                return False
            r += step_r
            s += step_s
        return True

    elif typ == "dáma":
        is_vez_move = (dr == 0 or ds == 0)
        is_strelec_move = (abs_dr == abs_ds)

        if not (is_vez_move or is_strelec_move):
            return False

        r, s = start_r + step_r, start_s + step_s
        while (r, s) != cilova_pozice:
            if (r, s) in obsazene_pozice:
                return False
            r += step_r
            s += step_s
        return True

    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))