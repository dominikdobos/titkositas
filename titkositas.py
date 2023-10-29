ABC = "abcdefghjklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.:?! "
titkosABC = "xyzXYZabcdefghjklmnopqrstuvwABCDEFGHIJKLMNOPQRSTUVW,.:?! "


def titkosit():
    szoveg = input("Kérek egy szöveget: ")
    titkosSzoveg = ""
    for i in range(len(szoveg)):
        match = False
        aktBetu = szoveg[i]
        poz = 0
        j = 0
        while match == False:
            if aktBetu == ABC[j]:
                poz = j
                match = True
            else:
                j += 1
        titkosBetu = titkosABC[poz]
        titkosSzoveg += titkosBetu
    print("A titkosított szöveg:", titkosSzoveg)


def dekodol():
    titkosSzoveg = input("Kérek egy TITKOS szöveget: ")
    dekodoltSzoveg = ""
    for i in range(len(titkosSzoveg)):
        match = False
        aktBetu = titkosSzoveg[i]
        poz = 0
        j = 0
        while match == False:
            if aktBetu == titkosABC[j]:
                poz = j
                match = True
            else:
                j += 1
        dekodoltBetu = ABC[poz]
        dekodoltSzoveg += dekodoltBetu
    print("A titkosított szöveg:", dekodoltSzoveg)