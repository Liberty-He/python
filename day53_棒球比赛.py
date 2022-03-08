## C -> 上一轮无效；D -> 上一轮两倍；+ -> 前两轮之和

record = input('Record = ').split(',')
score = []
for i in range(0, len(record)):
    if record[i] == 'C':
        del score[-1]
    elif record[i] == 'D':
        score.append(2*score[-1])
    elif record[i] == '+':
        score.append(score[-1]+score[-2])
    else:
        score.append(int(record[i]))
print('Total:', sum(score))
