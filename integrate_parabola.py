## 核心函数
#
#  参数为f,a,b,n
def trapezoidal(f, a, b, n):            #定义trapezoidal函数
    h = float(b-a)/n                    #(b-a)/n运算得到的值转为浮点数后赋值给h
    result = 0.5*f(a) + 0.5*f(b)        #result初始值为(0.5*f(a)+0.5*f(b))
    for i in range(1, n):               #for循环开始
        result += f(a + i*h)            #result初始值加上f(a+i*h)
    result *= h                         #for循环结束后的result乘以h
    return result                       #返回新的result值

## 核心函数
#
#  参数为f,a,b,n
def midpoint(f, a, b, n):               #定义midpoint函数
    h = float(b-a)/n                    #(b-a)/n运算得到的值转为浮点数后赋值给h
    result = 0                          #0赋值给result
    for i in range (n):               #for循环开始
        result += f((a+h/2)+i*h)          #result初始值加上f(a+h/2+i*h)
    result *= h                         #for循环结束后的result乘以h
    return result                       #返回新的result值

## 应用函数
#
#  这个程序的入口点
def application():                      #定义application函数
    y = lambda x: x**2-x                #定义y函数
    n = int(input('n: '))               #将用户输入的数转为整数赋给n
    tra_numerical = trapezoidal(y, 2, 6, n) #tra_numerical的值是函数trapezoidal(y,2,6,n)的结果
    mid_numerical = midpoint(y, 2, 6, n)    #mid_numerical的值是函数midpoint(y,2,6,n)的结果

    # 与精确结果比较         
    Y = lambda x: (1/3)*x**3-0.5*x**2   #定义Y函数
    exact = Y(6) -  Y(2)                #将Y(2)-Y(6)的值赋给exact
    tra_error = exact - tra_numerical   #将exact - tra_numberical的值赋给tra_error
    mid_error = exact - mid_numerical   #将exact - mid_numberical的值赋给mid_error
    tra_real_error = (tra_error) / (exact)
    mid_real_error = (mid_error) / (exact)
    
    print('n=%d: trapezoidal: %.16f  error: %.5g  real_error: %.5g' % \
          (n, tra_numerical, tra_error, tra_real_error))                   #格式化输出
    print('n=%d:    midpoint: %.16f  error: %.5g  real_error: %.5g' % \
          (n, mid_numerical, mid_error, mid_real_error))                   #格式化输出

if __name__ == '__main__':              #运行应用函数application()
    application()
