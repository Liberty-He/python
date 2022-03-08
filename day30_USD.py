import re

while True:
    price = str(input('Dollars: '))

    s = re.match('^\$[1-9]{1,3}(,\d{3})*(\.\d{2})?$', price)

    if s == None:
        print('Invalid! Enter again!')
    else:
        print('Valid!')
        break
    
