n = int(input('Enter the length:')) #边长，即每条边‘*’的个数

#上半部分
space = n*2 - 1 #第二行的两个‘*’间的空格数
for i in range(1, n+1): #第1行到中间最长的那一行
    if i == 1:              #第一行单独输出
        print(' '*(n-i) + '* '*n)  #开头的空格 + ‘* ’（星号与空格看成整体）
    else:
        print(' '*(n-i) + '*' + ' '*space + '*')
        space += 2 #每个空心行的空格数依次递增2

#下半部分
space -= 4
for i in range(n+1, 2*n):
    if i == 2*n - 1:
        print(' '*(i-n) + '* '*n)
    else:
        print(' '*(i-n) + '*' + ' '*space + '*')
        space -= 2
        
