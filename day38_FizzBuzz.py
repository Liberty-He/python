n = int(input('Enter n: '))
li = [i for i in range(1, n+1)]
li = list(map(str, li))
for i in range(0, n):
    if int(li[i]) % 3 == 0 and int(li[i]) % 5 != 0:
        li[i] = 'Fizz'
    elif int(li[i]) % 5 == 0 and int(li[i]) % 3 != 0:
        li[i] = 'Buzz'
    elif int(li[i]) % 3 == 0 and int(li[i]) % 5 == 0:
        li[i] = 'FizzBuzz'
print(li)
