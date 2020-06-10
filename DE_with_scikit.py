  
'''
max f(x1, x2) = 100*(x1^2 - x2)^2+(1-x1)^2
s.t.

    -2.048 <= x1, x2 <= 2.048
'''


def obj_func(p):
    x1, x2 = p
    return -(100*(x1**2-x2)**2+(1-x1)**2)


# %% Do DifferentialEvolution
from sko.DE import DE

de = DE(func=obj_func, n_dim=2, size_pop=30, max_iter=100, lb=[-2.048, -2.048], ub=[2.048, 2.048])
     

best_x, best_y = de.run()
print('best_x:', best_x, '\n', 'best_y:', best_y)