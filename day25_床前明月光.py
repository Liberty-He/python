import re

text = '床前明月光，疑是地上霜。举头望明月，低头思故乡。'
new1 = re.split(r'\W+', text)
new2 = re.split(r'(\W+)', text)
    
for i in new1:
    if i != '':
        print(i)
print()

col = 0
for i in new2:
    if i != '':
        print(i, end = '')
        col += 1
        if col % 2 == 0:
            print()
