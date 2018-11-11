MAX_KEY_SIZE = 26

def getMode():
     while True:
        print('Sezar Şifreleme Algoritması')
        mode = input().lower()
        if mode in 'şifreleme s çözme c'.split():
            return mode
        else:
            print('Komut giriniz: "sifreleme" , "s" ya da "cozme" , "c".')

def getMessage():
    print('Mesajı girin:')
    return input()

def getKey():
    key = 0
    while True:
        print('(1-%s) arasında sayı girin' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            if symbol.isupper():
                if num > ord('Z'):      #90
                    num -= 26
                elif num < ord('A'):    #65
                    num += 26

            elif symbol.islower():
                if num > ord('z'):      #122
                    num -= 26
                elif num < ord('a'):    #97
                    num += 26
            translated += chr(num)
        else:
            translated += symbol
    return translated


mode = getMode()
message = getMessage()
key = getKey()

print('Çevrilmiş mesajınız:')
print(getTranslatedMessage(mode, message, key))
