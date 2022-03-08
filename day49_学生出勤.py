from collections import Counter
def award():
    att = str(input('Attendance record: '))
    dic = dict(Counter(att))
    if dic['A'] > 1:
        return False
    else:
        for i in range(1, len(att)-1):
            if att[i-1] == att[i] == att[i+1]:
                return False
        else:
            return True
print(award())
