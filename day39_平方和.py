def fun():
    n = int(input('Enter n: '))
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i**2 + j**2 == n and i != j:
                return True
    else:
        return False
while True:
    print(fun())
