## 给定边长数组，返回由其中三条边组成的面积不为零的三角形的最大周长
## 若不能形成任何面积不为零的三角形，返回0
def main():
    length = sorted(list(map(int, input('Nums = ').split(','))))    ##
    res = []
    for i in range(0, len(length)-2):
        for j in range(i+1, len(length)-1):
            for k in range(j+1, len(length)):
                if is_triangle([length[i], length[j], length[k]]):
                    res.append(sum([length[i], length[j], length[k]]))

    if len(res) == 0:
        return 0
    else:
        return max(res)

def is_triangle(lis):
    if lis[0] + lis[1] > lis[2]:
        return True
    else:
        return False
print(main())
