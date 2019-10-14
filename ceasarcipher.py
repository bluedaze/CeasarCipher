import time

def main():
    mode = modeChoice()
    message = my_message()
    my_key = key()
    ceasar_cipher(mode, message, my_key)

def modeChoice():
    mode = None
    while (mode==None):
        mode = input("\n1: Encrypt\n" +
    "2: Decrypt\n\n" +
    "Press a number to make your selection: ")
        if mode == "1":
            return "encrypt"
        elif mode == "2":
            return "decrypt"
        else:
            print()
            invalid = "Invalid selection. Make a valid selection."
            for i in invalid:
                print(i, end = "")
                time.sleep(.1)
            print()
            mode = None

def my_message():
    message = input("What is your message? ")
    return message

def key():
    key = None
    while (key==None):
        key = input("What is your key? ")
        print()
        if key.isdigit():
            return int(key)
        else:
            print()
            invalid = "Invalid selection. Make a valid selection."
            for i in invalid:
                print(i, end = "")
                time.sleep(.1)
            print()
            key = None


def ceasar_cipher(mode, message, key):
    SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."
    translated = ""

    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            if mode == "encrypt":
                translatedIndex = symbolIndex + key
            elif mode == "decrypt":
                translatedIndex = symbolIndex - key

            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex == 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol

    print(translated)
