#!/usr/bin/env python
# coding: utf-8

# In[135]:


import numpy as np
# target funciton

def target(x):
    return 100*(x[0]**2-x[1])**2+(1-x[0])**2

size=30 #编码个数
dimen=2 #编码维数

x_max=np.array([2.048,2.048])
x_min=np.array([-2.048,-2.048])

gener=500 #进化次数
F=1.2  #变异因子
cr=0.6*np.ones(dimen) #交叉因子


# In[136]:


# initial x
p=x_min+(x_max-x_min)*np.random.rand(size,dimen)
# global best


# In[142]:


# evolution
x_argmax=[]
target_max=[]
for g in range(gener):
    # the g th generation
    v=h=np.empty((size,dimen))

    for s in range(10):
        # the s th x
        
        # aberrance
        r1=r2=r3=0
        while r1==r2 or r1==r3 or r2==r3 or r1==s or r2==s or r3==s :
            r1=int(size*np.random.rand(1)[0])
            r2=int(size*np.random.rand(1)[0])
            r3=int(size*np.random.rand(1)[0])
        h[s]=p[r1]+F*(p[r2]-p[r3])
        h[s]=np.where(h[s]<x_max,h[s],x_max)
        h[s]=np.where(h[s]>x_min,h[s],x_min)
        
        #interact
        temp=np.random.rand(dimen)
        v[s]=np.where(temp<cr,h[s],p[s])
        
        #select
        p[s]=np.where(target(v[s])>target(p[s]),v[s],p[s]) 
        
        #update


# In[143]:


r=np.around(size*np.random.random((size,3))).T
r_index=np.array([range(size),range(size),range(size)])
#(r==r_index or r.T[0]==r.T[1]  or r.T[0]==r.T[2] or r.T[1]==r.T[2]).any()
sum(r[0]==r[1]) 
sum(r[0]==r[2])

(r[0]==r[1]).any()


# In[144]:


target(v[0])>target(p[0])


# In[145]:


p


# In[141]:


ppp=np.zeros(p.shape)
#ppp=np.where(target(v.T)>target(p.T),v,p)
target(v.T).shape


# In[64]:


v[0]


# In[ ]:




