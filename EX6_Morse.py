morseABC={'A': '.-', 'B': '-...', 'C': '-.-.',
          'D': '-..', 'E': '.', 'F': '..-.',
          'G': '--.', 'H': '....', 'I': '..',
          'J': '.---', 'K': '-.-', 'L': '.-..',
          'M': '--', 'N': '-.', 'O': '---',
          'P': '.--.', 'Q': '--.-', 'R': '.-.',
          'S': '...', 'T': '-', 'U': '..-',
          'V': '...-', 'W': '.--', 'X': '-..-',
          'Y': '-.--', 'Z': '--..',

          '0': '-----', '1': '.----', '2': '..---',
          '3': '...--', '4': '....-', '5': '.....',
          '6': '-....', '7': '--...', '8': '---..',
          '9': '----.', '!':'--.--', ',':'--..--',
          '.':'.-.-.-','?':'..--..', '/':'-..-.',
          '-':'-....-','(':'-.--.', ')':'-.--.-'}

def forditoMorse(input):
    tmp=''
    szoveg=input.upper()
    for szo in szoveg:
        for s1,s2 in morseABC.items():
            if szo == s1:
                tmp +=s2
        tmp += ' '
    print(tmp)

def forditoABC(input2):
    newTmp = ''
    for karakter in input2.split(' '):
        if karakter=='':
            newTmp += ' '
        for s1,s2 in morseABC.items():
            if karakter == s2:
                newTmp += s1
    print(newTmp.capitalize())

def main():
    x=input("Mire forditsak(morze/abc)?: ")
    if x=='morze':
        return forditoMorse(input("Irja be a szoveget: "))
    else:
        return forditoABC(input("Irja be a morzet: "))
main()
