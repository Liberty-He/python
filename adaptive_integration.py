## 输出自适应间隔n的程序入口
#
def application():
    global n, error, exact                   
    f = lambda x: x**(1/2)                              
    a = 0
    b = 2
    n = 1
    eps = float(input('eps:'))
    numerical = midpoint(f, a, b, n)    
    F = lambda x: (2/3)*x**(3/2)               
    exact = F(b) - F(a)                 
    error = abs(exact - numerical)           
    n = adaptive_integration(f, a, b, eps, method=midpoint)
    print(error, n)
    return error, n

## 用midpoint方法近似计算积分
#
## f为被积函数,a为积分下限,b为积分上限,n为区间间隔
def midpoint(f, a, b, n):               
    h = float(b - a)/n                    
    result = 0                          
    for i in range (n):                 
        result += f((a+h/2)+i*h)        
    result *= h                         
    return result                       

## 找到能满足可接受的误差的间隔n
#
## f为被积函数,a为积分下限,b为积分上限,eps为可接受的误差
def adaptive_integration(f, a, b, eps, method=midpoint):
    global n, error, exact
    while error>eps:                     # 当真实误差不在可接受范围内时进入循环                                  
        n *= 2                           
        numerical = midpoint(f, a, b, n)
        error = abs(exact - numerical)       
    return n
    
## 画图程序入口,绘制eps在区间[10**-10，0.1]内关于n的图像
#
def make_plot():
    global eps, n
    import matplotlib.pyplot as plt
    from numpy import zeros
    from math import log10
    N = zeros(91)
    EPS = zeros(91)
    for i in range(10, 101):        
        eps = 10**(-i*0.1)          # 在区间[10**-10，0.1]内取得91个eps
        EPS[i-10] = log10(eps)      # 得到91个进行过对数运算的eps
        N[i-10] = plot_application()# 进行自适应运算得到对应的91个间隔n
    plt.plot(N, EPS)
    plt.xlabel('n')
    plt.ylabel('eps')
    plt.axis('auto')
    plt.show()

## 为make_plot()服务,计算一定范围内的每个eps得到的自适应间隔n
#
def plot_application():
    global n, error, exact
    f = lambda x: x**(1/2)
    a = 0
    b = 2
    n = 1
    F = lambda x: (2/3)*x**(3/2)
    numerical = midpoint(f, a, b, n)
    exact = F(b) - F(a)
    error = abs(exact - numerical)   
    n = adaptive_integration(f, a, b, eps, method=midpoint)
    return n 
    
application()
make_plot()

