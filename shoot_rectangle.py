## 1、玩家运行此文件，得到一个有固定位置的矩形。玩家有3次机会去射击同一个矩形。每一次尝试，玩家都被要求输入“v0”(初始速度)和“theta”(角度)的值。
## 2、用数值计算方法模拟画出一条近似于抛物线的炮弹轨迹。对v0进行分解，取固定的极短的时间段，在这个极短时间段内水平方向与竖直方向都看作匀速运动，画出轨迹；对于下一个时间段更新竖直方向的速度，继续都看做匀速运动，画出轨迹。依此类推。
## 3、判断是否打中目标。比较目标位置与每次更新的炮弹位置坐标，若在容错范围内，表示打中了目标；不在容错范围内，则继续更新下一时间段的轨迹。
## 4、要在之前尝试的轨迹基础上绘制一个新的轨迹。

from numpy import *                 # 调用数组
from math import *
import random
import matplotlib.pyplot as plt

distance=random.uniform(10,15)      # 定义全局变量distance   

def get_trajetory(v0,theta):        # 定义得到抛物线的函数
    global x,y                      # 声明全局变量
    x = [0]                         # 序列x中有一个数0
    y = [0]                         # 序列y中有一个数0
    t = 0.001                       # 赋值给t
    g = 9.81                        # 赋值给g
    rad = theta*(pi/180)            # 赋值给rad
    vx = v0*cos(rad)                # 通过公式计算出vx
    vy = v0*sin(rad)                # 通过公式计算出vy
    x.append(vx*t)                  # 在序列x的最后一个数后依次加入计算vx*t得到的数
    y.append(vy*t)                  # 在序列y的最后一个数后依次加入计算vy*t得到的数
    while (y[-1] >= 0):             # 当y[-1] >= 0的条件成立时执行
        vy -= g*t                   # vy加上g*t得到新的vy
        x.append(x[-1] + vx*t)      # 在序列x的最后一个数后依次加入计算x[-1]+vx*t得到的数
        y.append(y[-1] + vy*t)      # 在序列y的最后一个数后依次加入计算y[-1]+vy*t得到的数
    plot_trajetory(x,y)             # 调用画抛物线函数
    
def judge(x,y):                     # 定义判断函数
    n = len(x)                      # n是一系列x的长度
    a=0                             # a的初始值
    for i in range(0,n):            # 对于在0到n-1范围上的i进行以下循环
        if distance <= x[i]<= (distance+2) and 0 <= y[i] <= 1:#如果某个点的x,y值都在矩形范围内
            a+=1                    # a加上1得到新的a
    if a>0:                         # 如果a>1
        print('恭喜你，射中目标！') # 输出反馈语句1
    else:                           # 不满足a>1的条件时
        print('很遗憾，没有射中')   # 输出反馈语句2

def get_rectangle(distance):        # 定义得到矩形的函数
    x1=x2=distance                  # 赋值给x1,x2
    x3=x4=distance+2                # 赋值给x3,x4
    y1=y4=0                         # 赋值给y1,y4
    y2=y3=1                         # 赋值给y2,y3
    x=[x1,x2,x3,x4]                 # 将序列[x1,x2,x3,x4]赋给x
    y=[y1,y2,y3,y4]                 # 将序列[y1,y2,y3,y4]赋给y
    x.append(x[0])                  # 在序列x的最后一个数后再加入一个数x[0]
    y.append(y[0])                  # 在序列y的最后一个数后再加入一个数y[0]
    plot_rectangle(x,y)             # 调用画矩形函数

def plot_trajetory(x,y):            # 定义画抛物线函数
    plt.xlabel('x(m)')              # x轴名称为'x(m)'
    plt.ylabel('y(m)')              # y轴名称为'y(m)'
    plt.plot(x,y,label='Try%d' %(i))# 分别以x,y为x轴,y轴
    plt.legend()                    # 图例
    plt.draw()                      # 开始画图
    plt.pause(0.01)                 # 停顿0.01秒

def plot_rectangle(x,y):            # 定义画矩形函数
    plt.plot(x,y,label='rectangle',color='r')
    plt.xlim(0,20)                  # x轴的界限    
    plt.ylim(0,5)                   # y轴的界限
    plt.legend()                    # 图例
    plt.draw()                      # 开始画图
    plt.pause(0.01)                 # 停顿0.01秒

def main():                         # 定义主函数
    print('欢迎来到射击游戏！')     # 输出交互语句
    print('现在目标在 %.2f 米处。'% (distance))
    print('你有3次机会射击它！')
    global i                        # 声明全局变量
    get_rectangle(distance)         # 调用得到矩形函数
    for i in range(1,4):            # 对于在1到3范围上的i进行以下循环
        print('')                   # 输出空格
        print('第',i,'次射击')      # 输出交互语句      
        v0 = float(input('你想要的初速度=')) # 将用户输入的初速度转为浮点数赋给v0
        theta = float(input('你想要的角度='))# 将用户输入的角度转为浮点数赋给theta
        get_trajetory(v0,theta)     # 调用得到抛物线函数
        judge(x,y)                  # 调用判断函数
    print('')                       # 输出空格
    print('游戏结束')               # 输出反馈语句

def test_get_trajetory():           # 定义测试得到抛物线的函数
    expected = 0                    # 预期值是0
    x,y = get_trajetory(1,90)       # 将得到抛物线函数的返回值依次赋给x,y
    computed = y[-1]                # 电脑计算值是y[-1]
    tol = 1E-4                      # 误差允许范围是1E-4
    diff = abs(expected - computed) # 误差值
    assert diff < tol, 'diff = %g' %diff #假定diff<tol不成立，输出格式化的diff值

def test_get_rectangle():           # 定义测试得到矩形的函数
    computed_x,computed_y = get_rectangle(2)# 将得到矩形函数的返回值依次赋给computed_x,computed_y
    expected_x = [2,2,4,4]          # 预期值是[2,2,4,4]
    expected_y = [0,1,1,0]          # 预期值是[0,1,0,1]
    assert (expected_x,expected_y) == (computed_x,computed_y), '坐标计算错误' #假定此条件不成立，输出反馈语句

main()                              # 调用主函数
