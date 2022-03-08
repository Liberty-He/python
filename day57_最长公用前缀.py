strings = input('words = ').split(',')
strings = sorted(strings, key = lambda item: len(item))  ##
stan = strings[0]

res = {}
for i in range(1, len(stan)):
    res[stan[0:i]] = 0
    for j in range(0, len(strings)):
        if stan[0:i] == strings[j][0:i]:
            res[stan[0:i]] += 1
res = list(zip(res.values(), res.keys()))   ## 顺序！

if max(res)[0] == len(strings):
    print('\'%s\'' % max(res)[1])    ## max的查找机制
else:    
    print('\' \'')
