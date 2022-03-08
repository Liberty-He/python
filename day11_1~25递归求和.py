def sum_recursion(num):
    if num == 1:
        return 1
    else:
        return num + sum_recursion(num-1)

print(sum_recursion(25))
