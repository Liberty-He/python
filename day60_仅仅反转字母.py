## ab-cde-hijk
string = list(str(input('String: ')))
letter = []
for i in string:
    if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
        letter.append(i)

for i in range(0, len(string)):
    if 65 <= ord(string[i]) <= 90 or 97 <= ord(string[i]) <= 122:
        string[i] = letter[-1]
        del letter[-1]
for i in string:
    print(i, end = '')
