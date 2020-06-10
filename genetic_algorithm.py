import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

SCORE=-1

class life(object):
    #个体类
    def __init__(self,gene):
        self.gene=gene
        self.score=SCORE

class GA(object):
    #遗传算法类
    def __init__(self,acrossprob,amutationprob,alifeamount,agenelength,amatchfunc):
        self.crossprob=acrossprob
        self.mutationprob=amutationprob
        self.lifeamount=alifeamount
        self.genelength=agenelength
        self.matchfunc=amatchfunc
        self.lives= []
        self.best=None
        self.generation=0
        self.crossamount=0
        self.mutationamount=0
        self.bounds=0

        self.initpop()
    
    def initpop(self):
        #初始化种群
        self.lives=[]
        for i in range(self.lifeamount):
            gene=[x for x in range(self.genelength)]
            np.random.shuffle(gene)
            lifei=life(gene)
            self.lives.append(lifei)

    def assess(self):
        #评价函数，计算适应度
        self.bounds=0
        self.best=self.lives[0]
        for life in self.lives:
            life.score=self.matchfunc(life.gene)
            self.bounds += life.score
            if self.best.score < life.score:
                self.best = life
    
    def cross(self,parent1,parent2):
        #交叉
        index1 = np.random.randint(0,self.genelength-1)
        index2 = np.random.randint(index1,self.genelength-1)
        tempgene = parent2.gene[index1:index2]
        newgene = []
        p1len = 0
        for g in parent1.gene:
            if p1len == index1:
                newgene.extend(tempgene)
                p1len +=1
            if g not in tempgene:
                newgene.append(g)
                p1len += 1
        self.crossamount += 1
        return newgene

    def mutation(self,gene):
        #变异
        index1 = np.random.randint(0,self.genelength-1)
        index2 = np.random.randint(0,self.genelength-1)
        newgene = gene
        newgene[index1],newgene[index2] = newgene[index2],newgene[index1]
        self.mutationamount += 1
        return newgene

    def select(self):
        #选择一个个体
        r=np.random.uniform(0,self.bounds)
        for life in self.lives:
            r -= life.score
            if r <= 0:
                return life

        raise Exception("选择错误",self.bounds)

    def generate(self):
        #产生新后代
        parent1 = self.select()
        probability = np.random.random()

        #交叉
        if probability < self.crossprob:
            parent2 = self.select()
            gene = self.cross(parent1,parent2)
        else:
            gene = parent1.gene
        
        #变异
        if probability < self.mutationprob:
            gene = self.mutation(gene)
        
        return life(gene)

    def next(self):
        #产生下一代种群
        self.assess()
        newlives = []
        newlives.append(self.best)
        while len(newlives) < self.lifeamount:
            newlives.append(self.generate())
        self.lives = newlives
        self.generation += 1


class tsp(object):
    #旅行商问题类
    def __init__(self,root):
        self.data=np.loadtxt(root,delimiter=';',usecols=(1,2),encoding='gbk')
        self.matchfunc=lambda gene : 1.0 / self.distance(gene)
        self.ga = GA(acrossprob = 0.7 , amutationprob = 0.05 , alifeamount = 10 , agenelength = self.data.shape[0] , amatchfunc=self.matchfunc)
        
    def distance(self,gene):
        distance = 0.0
        for i in range(self.ga.genelength-1):
            distance += np.linalg.norm(self.data[gene[i]]-self.data[gene[i+1]])
        return distance
    
    def vision(self):
        e_1=[]
        for i in range(self.ga.genelength-1):
            e_1.append((self.ga.best.gene[i],self.ga.best.gene[i+1]))
        e_1.append((self.ga.best.gene[-1],self.ga.best.gene[0]))
        n=self.ga.best.gene
        pos={}
        for i in range(self.ga.genelength):
            pos[i]=self.data[i]
        graph1=nx.Graph()
        graph2=nx.Graph()
        graph1.add_nodes_from(n)
        graph2.add_nodes_from(n)
        graph2.add_edges_from(e_1)
        return [graph1,graph2,pos]


    def main(self,gener):
        self.ga.next()
        self.vision()
        plt.figure(1)
        nx.draw(tsp279.vision()[0],pos=tsp279.vision()[2])
        plt.title("GENERATION 0,DISTANCE:%f"%(1.0/self.ga.lives[-1].score),fontdict={'size':20,'color':'red'}) 
        plt.show()
        plt.figure(2)
        plt.ion()
        plt.show()
        while gener > 0:
            self.ga.next()
            gener -= 1
            if gener%10 ==0:
                self.vision()
                plt.cla()
                nx.draw(tsp279.vision()[1],pos=tsp279.vision()[2])
                plt.title("GENERATION %d,DISTANCE:%f"%(self.ga.generation,1.0/self.ga.best.score),fontdict={'size':20,'color':'red',})
                plt.pause(0.5)
                plt.show()
                
        plt.ioff()
        plt.show()


tsp279=tsp("china.csv")
tsp279.main(3000)
