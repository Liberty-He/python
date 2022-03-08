import re

def main():
    name = str(input('Enter the name: '))
    camel_case(name)
    
def camel_case(name):
    # 去掉 '-'
    s = re.split(r'-', name)

    # 把单个字母小写转成大写
    first = re.findall(r'(?<=-)\w(?=\w)', name)
    for i in range(0, len(first)):
        first[i] = chr(ord(first[i]) - 32)   # 此处必须用下标迭代

    # 把两个要求结合起来
    for i in range(1, len(s)):
        s[i] = re.sub(r'^\w', first[i-1], s[i])

    for i in s:
        print(i, end ='')
        
while True:
    main()
    print()

