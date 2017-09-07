import random
import evaluate
import numpy as np

class Gene():
    def __init__  (self,baseprenum,parameter,popsize,baseusingnum,choosenum,crosspro,mutepro):
        #parameter = [basex,basey,baseh,x,y,h,fc,Tx,G,htb,hre,Noise,rsrpthre,sinrthre,coverthre,nbaseallx,nbaseally,ncost,ocost] htb hre is useless
        self.baseprenum = baseprenum     #the num of all base could be used
        self.baseusingnum = baseusingnum #the num of base will be used
        self.popsize = popsize
        self.parameter = parameter
        self.choosenum = choosenum  #the size of chooseset
        self.crosspro = crosspro #the probability of cross
        self.mutepro = mutepro #the probability of mutation
        
    def individual(self):
        indexnum = [i for i in range(self.baseprenum)]
        indexnum = random.shuffle(indexnum)
        return indexnum
        
    def pop1(self):
        popultaion=[]
        for i in range(self.popsize):
            popultaion.append[self.individual()]
        return popultaion
        
    pop = pop1()
    self.pop = pop
    
    def fitness(self):
        popfitness=[]
        for i in self.pop:      #i = [abcdefg] individual
            j = i[:self.baseusingnum]   #j: all base will be used in the individual
            parameter1 = []
            #parameter =  [basex,basey,baseh,x,y,h,fc,Tx,G,htb,hre,Noise,rsrpthre,sinrthre,coverthre,nbaseallx,nbaseally,ncost,ocost]
            for k in range(3)
                parameter1.append([self.parameter[k][l] for l in j])
            parameter2 = [parameter1,parameter[3:]]
            popfitness.append(evaluate.Evaluate(parameter2))
        fmax = max(popfitness)
        popfitness = np.array(popfitness)
        popfitness = -popfitness + fmax
        popfitness = list(popfitness)
        return popfitness   #fitness value of each individual in pop
    
    
    self.F = self.fitness()     
    
    def choose(self):
        chooseset=[]
        sumfitness = sum(self.F)
        choosepro = [i/sumfitness for i in self.F]
        choosesumpro = [self.F[0]]*len(self.F)
        for j in range(1,len(self.F)):
            choosesumpro[j] = choosesumpro[j-1]+self.F[j]
        while 1:
            a=random.uniform(0,1)
            if a < choosesumpro[0]:
                choose.append(0)
            for k in range(1,len(self.F))
                if choosesumpro[k-1] <= a and choosesumpro[k] > a:
                    chooseset.append(k)
            if len(set(chooseset)) == self.choosenum:
                break
        return chooseset    #return the index of pop
        
    
    
    def cross(self):
        chooseset = self.chooseset()
        chooseset = [str(i) for i in chooseset]
        crosspre = dict(zip(chooseset,self.F))
        sorted(crosspre.items, key = crosspre.values)
        
    
    def mutation(self):