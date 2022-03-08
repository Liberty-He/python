def main():
    s = str(input('String: '))
    subs = []
    for end in range(1, len(s)):
        subs.append(s[0:end])
    for item in subs:
        for count in range(1, len(s) + 1):
            if item * count == s:
                return True
    else:
        return False
print(main())