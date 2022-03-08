def main():
    each = input('Number:\n')    # 按一次回车输入下一个数，按两次回车结束输入
    stopword = ''
    each1 = each + '\n'
    for line in iter(input, stopword):
        each1 += line + '\n'
    num = each1.splitlines()
        
    print('The numbers you entered: ', num)
    print('The third largest number is: %s' %sort(num))

def sort(num):
    num = list(map(eval, num))
    for i in range(0, len(num)-1):
        for j in range(i+1, len(num)):
            if num[j] > num[i]:
                temp = num[i]
                num[i] = num[j]
                num[j] = temp
    print(num)
    return num[2]
            
main()
