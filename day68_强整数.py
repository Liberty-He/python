x = int(input('x = '))
y = int(input('y = '))
bound = int(input('bound = '))

xs = [x**i for i in range(0, bound+1) if x**i <= bound]
ys = [y**i for i in range(0, bound+1) if y**i <= bound]
res = []
for i in xs:
    for j in ys:
        if i+j <= bound:
            res.append(i+j)
print(set(res))
