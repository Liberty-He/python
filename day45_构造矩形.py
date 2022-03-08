## 给定面积，输出最合适的长和宽（因为可能会有多组长和宽都符合该面积）
## 最合适的长和宽是指长大于宽，长和宽的差最小

square = int(input('Enter the square: '))
width_length = []
solu = {}
for width in range(1, square+1):
    for length in range(1, square+1):
        if width * length == square and length >= width:
            width_length.append(width)
            width_length.append(length)

for i in range(0, len(width_length)-1, 2):
    diff = width_length[i+1] - width_length[i]
    solu[diff] = [width_length[i], width_length[i+1]]

print('[width, length] =', solu[min(solu)])
