"""
现有一个列表li = [1,2,3,'a',4,'c'],有一个字典；
如果该字典没有"k1"这个键，那就创建这个"k1"键和对应的值(该键对应的值为空列表)，并将列表li中的索引位为奇数对应的元素，添加到
"k1"这个键对应的空列表中。

如果该字典中有"k1"这个键，且k1对应的value是列表类型。那就将该列表li
中的索引位为奇数对应的元素，添加到"k1"，这个键对应的值中。
"""


dic = {}
li = [1, 2, 3, 'a', 4, 'c']

if 'k1' not in dic:
    dic['k1'] = []
    for i in li:
        if li.index(i) % 2 == 1:
            dic['k1'].append(i)
        else:
            if type(dic['k1']) == list:
                for i in li:
                    if li.index(i) % 2 == 1:
                        dic['k1'].append(i)
            else:
                print('不是列表，无法追加')
                
print(dic)
