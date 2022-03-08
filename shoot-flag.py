## 射击游戏

from math import *              #调用math模组中的任一子模块
from numpy import *             #调用numpy模组中的任一子模块
import random                   #调用random模组
import matplotlib.pyplot as plt #调用matplotlib.pyplot作为plt

distance=random.uniform(10,15)  #将random.uniform(10,15)得到的值赋给参数distance

print('欢迎来到射击小旗游戏！') #输出'欢迎来到射击小旗游戏！'
print('现在小旗在 %.2f 米处。'% (distance))#输出'现在小旗在距离为distance米处。'%(distance)
print('你有3次机会射击它！')    #输出'你有3次机会射击它！'

## 主要函数
#
#  这个程序的入口点
def main():                         #定义主要函数  
    get_flag(distance)              #调用get_flag(distance)函数

    i = 1                           #i的初始值

    while i <= 3:                   #当i<=3成立执行此条件内容
        print('第',i,'次射击')             #输出'第i次射击'
        v0 = float(input('你想要的初速度=')) #将玩家输入的初速度转为浮点数
        theta = float(input('你想要的角度='))#将玩家输入的角度转为浮点数
        print('')             #输出空行                
        get_trajetory(v0,theta)#调用get_trajetory(v0,theta)函数
        i+=1                   #i加上1
    else:                      #当i<=3不成立时执行此内容
        print('游戏结束了！')  #输出'游戏结束了！'

## 这个函数可以得到一系列的相对应的x，y
#
#  参数v0、theta分别是玩家输入的射击初速度和角度
def get_trajetory(v0,theta): #定义一个以v0,theta为参数的函数
    g=9.81                   #重力加速度
    t=linspace(0,10,1001)    #区间[0,10]里的1001个等间隔的数
    rad=pi*theta/180         #把玩家输入的角度转换为弧度制
    x=v0*(cos(rad))*t        #由运动学公式得出一系列x
    y=v0*(sin(rad))*t-0.5*g*t**2   #由运动学公式得出一系列y
    plot_trajetory(x,y)      #调用plot_trajetory(x,y)函数
    print(x,y)
    return x,y               #返回一系列x、y的值

## 这个函数负责画出轨迹图
#
#参数为x、y   
def plot_trajetory(x,y):           #定义一个以x、y为参数的函数 
    plt.xlabel('x(m)')             #x轴名称为x(m)
    plt.ylabel('y(m)')             #y轴名称为y(m)
    plt.plot(x,y) #使用默认线样式和颜色绘制 x 和 y，设置图例标签
                     #显示图例
    plt.draw()                     #绘制出当前图形但不改变之前的图形
    plt.pause(0.1)                 #暂停间隔的0.1秒

##得到旗子的坐标（x，y）
#
#参数distance:10-15的随机数
#输出x，y：两个lists
def get_flag(distance):#定义一个参数为distance的函数
    x1=x2=x4=distance  #为x1，x2，x4赋值
    x3=x1+1            #为x4赋值
    y1=0               #为y1赋值
    y2=1               #为y2赋值
    y3=y4=0.6          #为y3，y4赋值
    x=[x1,x2,x3,x4]    #x输出为包含四个元素的list
    y=[y1,y2,y3,y4]    #y输出为包含四个元素的list
    plot_flag(x,y)     #调用画旗函数
    return x,y         #输出x，y

##根据坐标画出旗子图像
#
#参数(x,y):旗子坐标
def plot_flag(x,y):                     #定义一个参数为x，y的函数
    plt.plot(x,y,label='flag',color='r')#画‘x为x轴数据，y为y轴数据，图例标签为flag，颜色为红色’的图像
    plt.xlim(0,20)                      #x轴界限为0-20
    plt.ylim(0,5)                       #y轴界限为0-5
    plt.legend()                        #显示图例
    plt.draw()                          #绘制出当前图形但不改变之前的图形
    plt.pause(0.01)                     #停顿的间隔为0.01秒
    
main()               #调用主要函数

