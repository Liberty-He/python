import re

while True:
    name = str(input('User name: '))
    qq = str(input('QQ: '))

    p1 = re.compile(r'^[a-z0-9A-Z_]{6,20}$')
    p2 = re.compile(r'^[1-9]\d{4,11}$')

    res1 = re.match(p1, name)
    res2 = re.match(p2, qq)

    if res1 is None:
        print('Invalid name! Enter again!')        
    if res2 is None:
        print('Invalid qq number! Enter again!')
    print()
    if res1 is not None and res2 is not None:
        print('Valid! ')
        break
