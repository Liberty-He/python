def convert(char):    
        if 65 <= ord(char) <= 90:
            print(chr(ord(char) + 32))
        elif 97 <= ord(char) <= 122:
            print(chr(ord(char) - 32))
        else:
            print(char)

def main():
    while True:
        char = input('Enter a character from keyboard: ')
        convert(char)

main()
