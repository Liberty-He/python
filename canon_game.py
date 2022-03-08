'''
榴弹炮游戏
'''


## 得到抛物线上各点的坐标
#  @参数 v0 - 抛出速度
#  @参数 theta - 抛出角度
def get_trajetory(v0,theta):
    from math import sin, cos, pi
    x = []                          # 空列表x
    y = []                          # 空列表y
    t = 0.001                       # 赋值给时间t
    g = 9.81                        # 赋值给重力加速度g
    rad = theta*(pi/180)            # 赋值给弧度rad
    vx = v0*cos(rad)                # 通过公式计算出水平速度vx
    vy = v0*sin(rad)                # 通过公式计算出竖直速度vy
    x.append(vx*t)                  # 在空列表x中加入计算vx*t得到的结果
    y.append(vy*t)                  # 在空列表y中加入计算vy*t得到的结果
    while y[-1] >= 0:               # 当y[-1] >= 0的条件成立时执行
        vy -= g*t                   # vy减去g*t得到新的vy
        x.append(x[-1] + vx*t)      # 在列表x中依次加入计算x[-1]+vx*t得到的结果
        y.append(y[-1] + vy*t)      # 在列表y中依次加入计算y[-1]+vy*t得到的结果
    return x,y                      # 返回两个列表x,y

## 画抛物线
#  @参数 x - 抛物线上各点的横坐标
#  @参数 y - 抛物线上各点的纵坐标
def plot_trajetory(x,y):
    import matplotlib.pyplot as plt
    plt.xlabel('x(m)')              # x轴名称为x(m)
    plt.ylabel('y(m)')              # y轴名称为y(m)
    plt.plot(x,y)                   # 分别以x,y为x轴,y轴
    plt.draw()                      # 开始画图
    plt.pause(0.5)                  # 停顿0.5秒
    plt.savefig('plot_trajetory.png')

## 得到布景一坐标 
def get_1():
    global x_cord, y_cord, x_oval, y_oval, x_center, y_center, a, b, L  # 声明全局变量
    
    import random
    from numpy import arange
    from math import sin, cos, pi
    # 随机生成椭圆(热气球)
    x_center = random.uniform(120, 140)  # 椭圆中心横坐标           
    y_center = random.uniform(45, 50)    # 椭圆中心纵坐标        
    a = random.uniform(7, 10)            # 椭圆半长轴
    b = random.uniform(6, a)             # 椭圆半短轴
    x_oval = [ ]                         # 存储构成椭圆的点的横坐标 
    y_oval = [ ]                         # 存储构成椭圆的点的纵坐标
    for rad in arange(0,2*pi, 0.01):
        x_oval.append( x_center + a*cos(rad) )   
        y_oval.append( y_center + b*sin(rad) )
        
    # 随机生成线段(绳子)             
    L = random.uniform(10, 13)                  # 线段(绳子)长度                          
    x_cord = [x_center, x_center]               # 端点横坐标  
    y_cord = [y_center - b, y_center - b - L]   # 端点纵坐标

## 画布景一
def plot_1():
    import matplotlib.pyplot as plt
    # 画椭圆(热气球)
    plt.plot(x_oval, y_oval, color = 'r')
    plt.fill(x_oval, y_oval, 'r', alpha = 0.5)
    
    # 画线段(绳子，目标)
    plt.plot(x_cord, y_cord, color = 'k')

    # 画圆(目标)
    circle = plt.Circle( ( x_center, y_center - b - L - 1 ), 2.5, color = 'k', fill = 'k', alpha = 0.8 )
    plt.gcf().gca().add_artist(circle)
    plt.xlabel('x(m)')              
    plt.ylabel('y(m)')
    plt.title('Background 1')
    plt.axis('equal')
    plt.axis('scaled')
    plt.axis( [0, 160, 0, 60] )
    plt.savefig('plot_1.png')
    plt.pause(0.1)
    plt.draw()
    
## 得到三角形(山,障碍物)的坐标集合
def get_mountain():
    global X_M, Y_M               # 声明全局变量
    
    import random    
    e = random.uniform(50,60)     # 定义随机数e,f,g,h
    f = random.uniform(10,40)       
    g = random.uniform(40,70)
    h = random.uniform(30,40)
    x1 = e                        # 赋值给x1,x2,x3,y1,y2,y3  
    x2 = x1 + f
    x3 = x1 + g
    y1 = 0
    y2 = h
    y3 = 0
    X_M = [x1, x2, x3]            # 山的端点横坐标集合
    Y_M = [y1, y2, y3]            # 山的端点纵坐标集合
    
    X_M.append( X_M[0] )          # 加长数组X_M, Y_M       
    Y_M.append( Y_M[0] )
    return X_M, Y_M               # 返回X_M, Y_M

## 画山
def plot_mountain():
    import matplotlib.pyplot as plt
    plt.fill(X_M, Y_M, 'c')
    plt.plot(X_M, Y_M, color='c')   # 用线条绘制出y关于x的图像    

## 得到柱子坐标集合
def get_pillar():
    global X_M,Y_M,X_P,Y_P              # 声明全局变量
    
    import random
    p = random.uniform(10,Y_M[1])       # 定义随机数p,q
    q = random.uniform(10,20)
    x_1 = random.uniform(X_M[0],X_M[2]) # 柱子的坐标在山的范围内随机生成
    x_2 = x_1                           # 柱子两端点的横坐标数值相同

    if x_1 < X_M[1]:              # 当柱子底端在山的左侧时
        y_1 = ( (Y_M[1] - Y_M[0])*(x_1 - X_M[0]) )/( X_M[1] - X_M[0] )    # 相似三角形比例法计算柱子端点纵坐标
        y_2 = y_1 + p             # 可击中范围(存在误差)

    else:                         # 当柱子底端在山的右侧时
        y_1 = ( (Y_M[1] - Y_M[2])*(X_M[2] - x_1) )/( X_M[2] - X_M[1] )    # 相似三角形比例法计算柱子端点纵坐标
        y_2 = Y_M[1] + q          # 可击中范围(存在误差)
        
    X_P = [x_1,x_2]               # 柱子的端点横坐标集合
    Y_P = [y_1,y_2]               # 柱子的端点纵坐标集合
    return X_P, Y_P               # 返回X_P, Y_P
    
## 画柱子
def plot_pillar():
    import matplotlib.pyplot as plt
    plt.plot(X_P, Y_P, color = 'm')  # 用线条绘制出y关于x的图像

## 画目标圆
def plot_target():
    global R        # 声明全局变量

    import matplotlib.pyplot as plt
    R = 5 
    circle = plt.Circle( ( X_P[0], Y_P[1] + R ), R ) 
    plt.gcf().gca().add_artist(circle)
    plt.xlabel('x(m)')              
    plt.ylabel('y(m)')
    plt.title('Background 2')
    plt.axis('equal')                  
    plt.axis('scaled')              
    plt.axis( [0, 160, 0, 100] )
    plt.pause(0.01)
    plt.draw()                         

## 画布景二
def plot_2():
    import matplotlib.pyplot as plt
    get_mountain()              
    get_pillar()
    plot_mountain()
    plot_pillar()
    plot_target()
    plt.savefig('plot_2.png')
    
## 判断在布景一中榴弹炮打中情况
#  @参数 x - 抛物线上点的横坐标
#  @参数 y - 抛物线上点的纵坐标
def judge_1(x, y):
    global score, non       # 声明全局变量
    
    n = len(x)              # 抛物线上点的个数
    c = 0                   # 中间变量，用于什么都没有打中的情况下
    for i in range(0, n):   # 对抛物线上的每个点都进行以下语句
        
        # 打中圆(目标)
        if ( x[i] - x_center )**2 + (y[i] - ( y_center - b - L - 1 ) )**2 <= 2.5**2:
            situ_1 = 1           # 打中目标的情况记为1 
            score += 1           # 加一分
            non = 0              # 连续没有打中目标/障碍物0次
            print('Succeed')     # 显示Succeed即告诉玩家打中了目标
            break                # 如果此条件满足且运行完毕,跳出整个循环
        
        # 打中绳子(目标)
        elif x_center - 0.1 < x[i] < x_center + 0.1 and y_center - b - L < y[i] < y_center - b:
            situ_1 = 1           # 打中目标的情况记为1 
            score += 1           # 加一分
            non = 0              # 连续没有打中目标/障碍物0次
            print('Succeed')     # 显示Succeed即告诉玩家打中了目标
            break                # 如果此条件满足且运行完毕,跳出整个循环
        
        # 打中椭圆(障碍物)
        elif (x[i] - x_center)**2 / a**2 + ( y[i] - y_center )**2 / b**2 <= 1:
            situ_1 = -1      # 打中障碍物的情况记为-1
            score -= 1       # 减一分
            non += 1         # 累加连续没有打中目标/障碍物的次数
            print('Fail')    # 显示Fail即告诉玩家打中了障碍物
            break            # 如果此条件满足且运行完毕,跳出整个循环
        
    # 什么都没有打中
        else:
            situ_1 = 0       # 什么都没有打中的情况记为0
            c += 1           # 对中间变量c进行累加
    if c == n:               # 如果抛物线上每个点都没有打中
        print('No result')   # 显示No result即告诉玩家什么都没有打中
        non += 1             # 累加连续没有打中目标/障碍物的次数
    return situ_1            # 返回situ_1

## 用于布景二下的计分函数  
def scoring():                            
    global a, score, situ_2, non  # 声明全局变量
    
    if a > 0:                   # 布景二中打中目标
        situ_2 = 1              # 打中目标的情况记为1
        score += 1              # 加一分
        non = 0                 # 连续没有打中目标/障碍物0次
    elif a < 0:                 # 布景二中打中障碍物
        situ_2 = -1             # 打中障碍物的情况记为-1
        score -= 1              # 减一分
        non += 1                # 累加连续没有打中目标/障碍物的次数
    else:                       # 布景二中什么都没有打中
        situ_2 = 0              # 什么都没有打中的情况记为0
        score += 0              # 分数不变
        non += 1                # 累加连续没有打中目标/障碍物的次数
    return situ_2               # 返回situ_2

## 判断在布景二中榴弹炮打中情况
#  @参数 x - 抛物线上点的横坐标 
#  @参数 y - 抛物线上点的纵坐标
def judge_2(x, y):
    global X_M, Y_M, X_P, Y_P, a, score, R  # 声明全局变量
    
    n = len(x)                          # 抛物线上点的个数
    for i in range(0, n):
        a = 0                           # a的初始值
        
        # 当柱子底端在山的左侧时
        if X_P[0] < X_M[1]:           
            if 0 < x[i] < X_M[0]:       # 如果抛物线上的点的横坐标小于山左顶点横坐标
                if y[i] <= 0:           # 且该点的纵坐标小于0
                    print('No result')  # 显示No result即告诉玩家什么都没有打中
                    a += 0              # a不变
                    scoring()           # 调用计分函数
                    break               # 如果此条件满足且运行完毕,跳出整个循环
                else:
                    continue            # 如果不满足上面的条件,继续往下搜寻合适的条件
                
            elif X_M[0] < x[i] < X_P[0] - R:  # 如果抛物线上某点横坐标介于山左顶点横坐标和柱子左边(不包括柱子即在目标的左边)之间
                if Y_M[0] < y[i] < Y_P[0]:    # 且该点的纵坐标介于山左顶点纵坐标和柱子的底部纵坐标之间
                    print('Fail')             # 显示Fail即告诉玩家打中了障碍物
                    a -= 1                    # a减去1得到新的a
                    scoring()                 # 调用计分函数
                    break                     # 如果此条件满足且运行完毕,跳出整个循环
                else:
                    continue                  # 如果不满足上面的条件,继续往下搜寻合适的条件
                
            elif X_P[0] - R <= x[i] <= X_P[0] + R:    # 如果抛物线上某点横坐标在目标水平直径范围内
                if Y_M[0] <= y[i] < Y_P[1] - 0.05:    # 且该点纵坐标介于山左顶点纵坐标和柱子的顶部纵坐标之间
                    print('Fail')                     # 显示Fail即告诉玩家打中了障碍物
                    a -= 1                            # a减去1得到新的a
                    scoring()                         # 调用计分函数
                    break                             # 如果此条件满足且运行完毕,跳出整个循环
                elif (x[i] - X_P[0])**2 + ( y[i] - (Y_P[1] + R) )**2 <= ( R + 0.05 )**2:   # 如果抛物线上某点在圆内(上),0.05是击中误差范围
                    print('Succeed')                  # 显示Succeed即告诉玩家打中了目标
                    a += 1                            # a加上1得到新的a
                    scoring()                         # 调用计分函数
                    break                             # 如果此条件满足且运行完毕,跳出整个循环
                else:
                    continue                          # 如果不满足上面的条件,继续往下搜寻合适的条件
                
            elif X_P[0] + R < x[i] < X_M[1]:          # 如果抛物线上某点横坐标介于柱子右边(不包括柱子即在目标的右边)到山右顶点横坐标之间
                if Y_P[0] < y[i] < Y_M[1]:            # 且该点纵坐标介于柱子的底部纵坐标(实际坐标更高)和山上顶点纵坐标之间
                    print('Fail ')                    # 显示Fail即告诉玩家打中了障碍物
                    a -= 1                            # a减去1得到新的a
                    scoring()                         # 调用计分函数
                    break                             # 如果此条件满足且运行完毕,跳出整个循环
                else:
                    continue                          # 如果不满足上面的条件,继续往下搜寻合适的条件
            elif X_M[1] < x[i] < X_M[2]:              # 如果抛物线上某点横坐标介于山上顶点横坐标到山右顶点横坐标之间
                if Y_M[2] < y[i] < Y_M[1]:            # 且该点纵坐标介于山右顶点纵坐标和山上顶点纵坐标之间
                    print('Fail')                     # 显示Fail即告诉玩家打中了障碍物
                    a -= 1                            # a减去1得到新的a
                    scoring()                         # 调用计分函数
                    break                             # 如果此条件满足且运行完毕,跳出整个循环
                else:
                    print('No result')                # 显示No result即告诉玩家什么都没有打中
                    a += 0                            # a不变
                    scoring()                         # 调用计分函数
                    break                             # 如果此条件满足且运行完毕,跳出整个循环(柱子在山的左边的情况到此判断结束)

        #当柱子底端在山的右侧时                               
        else:                       
            if 0 < x[i] < X_M[0]:                     # 如果抛物线上的点的横坐标小于山左顶点横坐标
                if y[i]<=0:                           # 且该点的纵坐标小于0
                    print('No result')                # 显示No result即告诉玩家什么都没有打中
                    a += 0                            # a不变
                    scoring()                         # 调用计分函数
                    break                             # 如果此条件满足且运行完毕,跳出整个循环
                else:
                    continue                          # 如果不满足上面的条件,继续往下搜寻合适的条件
            elif X_M[0] < x[i] < X_P[0] - R:          # 如果抛物线上的点的横坐标介于山左顶点横坐标和柱子左边(即在目标的左边)之间
                if Y_M[0] < y[i] < Y_M[1]:            # 且该点纵坐标介于山左顶点纵坐标和山上顶点纵坐标之间(与第一种情况不同之处)
                    print('Fail')                     # 显示Fail即告诉玩家打中了障碍物
                    a -= 1                            # a减去1得到新的a
                    scoring()                         # 调用计分函数
                    break                             # 如果此条件满足且运行完毕,跳出整个循环
                else:
                    continue                          # 如果不满足上面的条件,继续往下搜寻合适的条件
            elif X_P[0] - R <= x[i] <= X_P[0] + R:    # 如果抛物线上某点横坐标在目标水平直径范围内
                    if 0 <= y[i] < Y_P[1] - 0.05:     # 且该点纵坐标小于柱子顶部纵坐标
                        print('Fail')                 # 显示Fail即告诉玩家打中了障碍物
                        a -= 1                        # a减去1得到新的a
                        scoring()                     # 调用计分函数
                        break                         # 如果此条件满足且运行完毕,跳出整个循环
                    elif ( x[i] - X_P[0] )**2 + ( y[i] - (Y_P[1] + R) )**2 <= ( R + 0.05 )**2:     # 如果抛物线上某点在圆内(上),0.05是击中误差范围
                        print('Succeed')              # 显示Succeed即告诉玩家打中了目标
                        a += 1                        # a加上1得到新的a
                        scoring()                     # 调用计分函数
                        break                         # 如果此条件满足且运行完毕,跳出整个循环
                    else:
                        continue                      # 如果不满足上面的条件,继续往下搜寻合适的条件
            elif X_P[0] + R < x[i] < X_M[2]:          # 如果抛物线上某点横坐标介于目标的右边和山右顶点横坐标之间
                    if Y_M[2] < y[i] < Y_P[0]:        # 且该点纵坐标介于山右顶点纵坐标和柱子底部纵坐标之间
                        print('Fail')                 # 显示Fail即告诉玩家打中了障碍物
                        a -= 1                        # a减去1得到新的a
                        scoring()                     # 调用计分函数
                        break                         # 如果此条件满足且运行完毕,跳出整个循环
                    else:
                        print('No result')            # 显示No result即告诉玩家什么都没有打中
                        a += 0                        # a不变
                        scoring()                     # 调用计分函数
                        break                         # 如果此条件满足且运行完毕,跳出整个循环
                    
## 布景一的入口点            
def application_1():
    print('===============================场景一=====================================')
    get_1()                     # 得到布景一组成元素的坐标
    plot_1()                    # 画出布景一
    v0 = 42                     # 给定榴弹炮的发射速度
    theta = float(input('theta ='))    # 让玩家输入角度并转为浮点数
    x, y = get_trajetory(v0,theta)     # 调用函数get_trajetory(v0,theta)得到一系列坐标
    plot_trajetory(x,y)                # 调用函数plot_trajetory(x,y)画出抛物线
    situ_1 = judge_1(x,y)              # 判断在布景一中榴弹炮打中情况
    print('Final score: %d' %(score))
    change_1(situ_1)                   # 调用函数change_1(situ_1)根据榴弹炮打中情况判断布景一是否转换为布景二

## 布景二的入口点
def application_2():
    print('===============================场景二=====================================')
    plot_2()                    # 画出布景二
    v0 = 42                     # 给定榴弹炮的发射速度
    theta = float(input('theta ='))   # 让玩家输入角度并转为浮点数
    x, y = get_trajetory(v0,theta)    # 调用函数get_trajetory(v0,theta)得到一系列坐标
    plot_trajetory(x,y)               # 调用函数plot_trajetory(x,y)画出抛物线
    situ_2 = judge_2(x,y)             # 判断在布景二中榴弹炮打中情况
    print('Final score: %d' %(score))

## 根据榴弹炮打中情况判断布景一是否转换为布景二
#  @参数 situ_1 - 布景一中榴弹炮打中情况
def change_1(situ_1):
    import matplotlib.pyplot as plt
    if situ_1 == 1:         # 如果在布景一中打中目标 
        plt.pause(1.0)      # 停顿1.0秒
        plt.close()         # 关闭布景一
        application_2()     # 调用application_2()进入布景二的新一局游戏
    else:                   # 如果在布景一中打中障碍物或什么都没有打中
        if non < 3:         # 如果连续没有打中目标/障碍物的次数小于3
            plt.clf()           # 清除目前图像不清除坐标轴
            application_1()     # 调用application_1()重新进入布景一的新一局游戏
            
## 根据榴弹炮打中情况判断布景二是否转换为布景一
#  @参数 situ_2 - 布景二中榴弹炮打中情况
def change_2(situ_2):
    import matplotlib.pyplot as plt
    plt.pause(1.0)          # 停顿1.0秒
    plt.close()             # 关闭上一个布景
    if situ_2 == 1:         # 如果在布景二中打中目标 
        application_1()     # 调用application_1()进入布景一的新一局游戏
    else:
        application_2()     # 调用application_2()重新进入布景二的新一局游戏
        
## 程序入口点
def main():
    global score,non        # 声明全局变量

    print('==========================欢迎来到射击榴弹炮游戏================================')
    print('游戏初始分数为 0；榴弹炮发射速度固定为 42 m/s；共有两个场景。')
    print('打中目标加 1 分并且切换至另一场景')
    print('打中障碍物扣 1 分继续当前场景')
    print('什么都没有打中分数不变继续当前场景')
    print('')
    print('若连续三次未打中目标或分数小于 0 则游戏结束')
    print('如果你足够幸运可以一直玩下去！（Ctrl+C可停止游戏）')
    print('')
    print('场景一中热气球为障碍物，绳子以及悬挂的物体为目标。')
    print('场景二中山和柱子为障碍物，柱子上的物体为目标。')
    print('')
    non = 0                 # 连续没有打中目标/障碍物的次数初始值为0
    score = 1               # 初始分数为1
    while non < 3:          # 当连续没有打中目标/障碍物的次数小于3时
        application_1()         # 进入布景一
        while score >= 0:   # 当分数大于等于0时
            change_2(situ_2)    # 调用函数change_2(situ_2)
            if non >= 3:        # 如果连续没有打中目标/障碍物的次数大于等于3
                break           # 跳出循环
    print('Game is over')       # 显示游戏结束了

if __name__ == "__main__":
    main()

