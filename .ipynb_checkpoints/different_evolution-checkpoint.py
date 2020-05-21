import numpy as np
# target funciton

def target(x):
    return 100*(x[0]**2-x[1])**2+(1-x[0])**2

size=30 #编码个数
dimen=2 #编码维数

x_max=[2.048,2.048]
x_min=[-2.048,-2.048]

evo=50 #进化次数
F=1.2  #变异银子
cr=0.9 #交叉因子
p=np.random.rand_samples(x_min[0],x_max[0])
print(p)