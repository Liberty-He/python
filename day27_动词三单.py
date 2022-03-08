import re
import os

while True:
    word = input('Enter a verb: ')

    if word == 'q' or word == 'Q':
        os._exit(0)
        
    elif word[-1] == 'y':
        letter = re.split(r'(\w)', word)
        letter[-2] = 'ies'
        for i in letter:
            if i != '':
                print(i, end ='')
        print()

    elif word[-1] == 'o' or word[-1] == 's' or word[-1] == 'x' or word[-1] == 'z':
        word = word + 'es'
        print(word)

    elif word[-2::] == 'ch' or word[-2::] == 'sh':
        word = word + 'es'
        print(word)

    else:
        word = word + 's'
        print(word)

    print()

## str.endswith(suffix, start, end)
## str.startswith(prefix, start, end)
## '-'.join(['1', '2', '3'])
    
