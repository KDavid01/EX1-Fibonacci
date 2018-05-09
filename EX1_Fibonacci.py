def Fibonacci():
    elso_szam=1
    masodik_szam=1
    print(elso_szam,end=' ')
    print(masodik_szam,end=' ')
    for i in range(98):
        osszeg=elso_szam+masodik_szam
        print(osszeg,end=' ')
        elso_szam=masodik_szam
        masodik_szam=osszeg
        
Fibonacci()
