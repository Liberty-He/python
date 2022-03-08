import re

code = []
code_new = []
print('Enter q or Q to exit.\n')
while True:
    label = str(input('Enter codes of HTML/XML: '))    
    if label == 'q' or label == 'Q':
        break
    else:
        code.append(label)

pattern1 = re.compile(r'<')
pattern2 = re.compile(r'>')
pattern3 = re.compile(r'</\w*>')

for i in code:
    code_new.append(pattern1.sub('', pattern2.sub(':', pattern3.sub('', i))))


for i in code_new:
    print(i)

