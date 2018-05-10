def tizesSZR():
    if honnan==11 or honnan==12 or honnan==13 or honnan==14 or honnan== 15 or honnan== 16:
        result = []
        for i in szam:
            if i == 'A':
                result.append('10')
            elif i == 'B':
                result.append('11')
            elif i == 'C':
                result.append('12')
            elif i == 'D':
                result.append('13')
            elif i == 'E':
                result.append('14')
            elif i == 'F':
                result.append('15')
            else:
                result.append(i)

        tmp = result[::-1]
        sum = 0
        kitevo = 0
        for j in tmp:
            sum += int(j)*(honnan**kitevo)
            kitevo += 1
        return sum

    else:
        tmp = szam[::-1]
        sum = 0
        kitevo = 0

        for i in tmp:
            sum += int(i)*(honnan**kitevo)
            kitevo += 1
        return sum

def melyikSZR():
    fgv = tizesSZR()
    eredmeny = ''
    while True:
        if fgv == 0:
            return eredmeny[::-1]
        if fgv%hova==10:
            eredmeny += 'A'
        elif fgv%hova==11:
            eredmeny += 'B'
        elif fgv%hova==12:
            eredmeny += 'C'
        elif fgv%hova==13:
            eredmeny += 'D'
        elif fgv%hova==14:
            eredmeny += 'E'
        elif fgv%hova==15:
            eredmeny += 'F'
        else:
            eredmeny += str(fgv%hova)
        fgv = fgv//hova


szam = input('Kérek egy számot: ')
honnan = int(input('Melyik számrendszerből: '))
hova = int(input('Melyik számrendszerbe: '))

print(melyikSZR())
