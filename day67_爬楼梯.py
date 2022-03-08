def main():
    global count
    count = 0
    n = int(input('Total steps: '))
    climb(0, n)
    
def climb(pre, total):
    global count
    if pre == total:
        count += 1
        return None
    elif pre < total:
        climb(pre+1, total)
        climb(pre+2, total)

main()
print(count)
