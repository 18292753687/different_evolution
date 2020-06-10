import numpy as np

A=np.array([[0.24,0.19,0.16,0.12,0.29],
[0.22,0.16,0.33,0.18,0.11],
[0.31,0.09,0.18,0.37,0.05],
[0.25,0.38,0.17,0.13,0.07],
[0.6,0.15,0.11,0.08,0.06],
[0.23,0.17,0.21,0.25,0.14],
[0.19,0.13,0.13,0.51,0.04]]).T

A1=A**2
A2=-2*A

def object_function(p):
    x1,x2,x3,x4,x5=p
    return np.sum(A1)+np.sum(A2,1)[0]*x1+np.sum(A2,1)[1]*x2+np.sum(A2,1)[2]*x3+np.sum(A2,1)[3]*x4+np.sum(A2,1)[4]*x5+x1**2+x2**2+x3**2+x4**2+x5**2

constraint_eq=[
    lambda x:1-sum(x)
]

from sko.DE import DE

de=DE(func=object_function,n_dim=5,size_pop=100,max_iter=1000,lb=[0.19,0.09,0.11,0.08,0.04],ub=[0.31,0.19,0.21,0.37,0.14],constraint_eq=constraint_eq)

best_x,best_y=de.run()
print('best_x:', best_x, '\n', 'best_y:', best_y)
