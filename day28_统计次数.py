content = 'google.com'
count = {}

for i in content:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for i in count.items():
    print(i)

print(count)

for i in count.keys():
    print(i, ':', count[i])
    
