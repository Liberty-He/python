import re
basic = '1'
n = int(input('Input athe number n:'))
count = 1
an = ''
p1 = re.compile(r'(\d)\1*')

while count < n:
    Lst = re.finditer(p1,basic)
    Lst = [i.group() for i in Lst]
    Lst2 = list(map(len,Lst))
    for i in range(len(Lst)):
        an += str(Lst[i][0]) + str(Lst2[i])
    basic = an
    an = ''
    count += 1
print(basic[::-1])
