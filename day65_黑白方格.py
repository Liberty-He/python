##from scipy.special import comb
def fun():
    n = int(input('n = '))
    k = int(input('k = '))
    if n * n >= k >= n:
        if k == n:
            return 2 * n
        elif k == n ** 2:
            return 1
        elif k % n == 0:
            return 2 * getValue(n, k // n)
        else:
            if (k-1) % (n-1) == 0:
                return n * getValue(n, (k-1) // (n-1) - 1)
            else:
                return 0
    else:
        return 0

def helper(n):
    if n == 1:
        return n
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def getValue(n, m):
    first = helper(n)
    second = helper(m)
    third = helper(n - m)
    return first // (second * third)
print(fun())

