## 有一堆石头，每块石头的重量都是正整数。
## 每一回合，从中选出两块最重的石头，然后将它们一起粉碎。假设石头的重量分别为x,y，且 x <= y。那么粉碎的可能结果如下：
##    如果 x == y，那么两块石头都会被完全粉碎；
##    如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
## 最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 0。

def fun(rocks):
    broken = []
    if len(rocks) > 1:
        while len(broken) < 2:
            broken.append(max(rocks))
            rocks.remove(max(rocks))
            
        if broken[0] != broken[1]:
            rocks.append(max(broken) - min(broken))
            
        return fun(rocks)
    elif len(rocks) == 1:
        return rocks[0]
    else:
        return 0
        
print(fun([2,7,4,1,8,1]))
