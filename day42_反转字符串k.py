## 输入字符串s和整数k，对每2k个字符的前k个字符进行反转

def main():
    string = input('Enter a string: ')
    k = int(input('Enter k: '))
    rev = []
    nonrev = []

    # 把2k中的前k个（rev）和后k个（nonrev）分开存放
    for i in range(0, len(string), 2*k):
        rev.append(string[i:i+k])
        nonrev.append(string[i+k:i+2*k])

    # 反转每2k的前k个（rev）字符
    for i in range(0, len(rev)):
        rev[i] = rev[i][::-1]

    # 拼接rev和nonrev，输出
    for i in range(0, len(rev)):
        print(rev[i]+nonrev[i], end = '')

main()
