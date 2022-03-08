stu =[['张飞  ', 78, 75],
['李大刀', 92, 67],
['李墨白', 84, 88],
['王老虎', 50, 50],
['雷小米', 99, 98]]

##sorted返回与原列表格式相同的一个列表，排列顺序不同
stu_new = sorted(stu, key = lambda a: a[1] + a[2], reverse = True)

for i in stu_new:
    for j in i:
        print(j, end = '  ')
    print()

print("This is a test string from Andrew".split())
