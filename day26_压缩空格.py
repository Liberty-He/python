import re

text = 'This  is  very funny and   cool.Indeed!I love this!'

# 压缩多个空格
p1 = re.compile(r' +')
a = re.sub(p1, ' ', text)
print(a)

# 若标点符号后紧跟字母，两者之间加空格
p2 = re.compile(r'([!,.:;?])(?=\w)')  # 请尝试去掉第一组括号，会得到不一样的结果
s = re.split(p2, a)

symbol = [',', '.', '!', '?', ':', ';']

for i in range(0, len(s)):
    if s[i] in symbol:
        print(s[i-1]+s[i]+' ', end = '')
        
print(s[-1])
