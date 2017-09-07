import random
import evaluate
import numpy as np

class Gene():
    def __init__  (self,baseprenum,parameter,popsize,baseusingnum,choosenum,crosspro,mutepro,iterationtime):
        #parameter = [basex,basey,baseh,x,y,h,fc,Tx,G,htb,hre,Noise,rsrpthre,sinrthre,coverthre,nbaseallx,nbaseally,ncost,ocost] htb hre is useless
        self.baseprenum = baseprenum     #the num of all base could be used
        self.baseusingnum = baseusingnum #the num of base will be used
        self.popsize = popsize
        self.parameter = parameter
        self.choosenum = choosenum  #the size of chooseset
        self.crosspro = crosspro #the probability of cross
        self.mutepro = mutepro #the probability of mutation
        self.iterationtime = iterationtime
        self.pop = []
        self.F = []
        
    def individual(self):
        indexnum = [i for i in range(self.baseprenum)]
        indexnum = random.shuffle(indexnum)
        return indexnum
        
    def pop1(self):
        popultaion=[]
        for i in range(self.popsize):
            popultaion.append[self.individual()]
        return popultaion
        
        
    self.pop = self.pop1()
    
    def fitness(self):
        popfitness=[]
        for i in self.pop:      #i = [abcdefg] individual
            j = i[:self.baseusingnum]   #j: all base will be used in the individual
            parameter1 = []
            #parameter =  [basex,basey,baseh,x,y,h,fc,Tx,G,htb,hre,Noise,rsrpthre,sinrthre,coverthre,nbaseallx,nbaseally,ncost,ocost]
            for k in range(3):
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
            for k in range(1,len(self.F)):
                if choosesumpro[k-1] <= a and choosesumpro[k] > a:
                    chooseset.append(k)
            if len(set(chooseset)) == self.choosenum:
                break
        return chooseset    #return the index of pop
        
    
    
    def cross(self):
        chooseset = self.choose()
        chooseset = [str(i) for i in chooseset]  #the index of pop
        fitvalue = [self.F[j] for j in chooseset]  #the fitvalue of each individual choose from the pop
        crosspre = dict(zip(chooseset,fitvalue))  
        crolist = sorted(crosspre.items(), key = lambda x:x[1],reverse = True)
        #[('2', 6), ('1', 2.1), ('3', 1.2)]
        for k in range(0,self.choosenum,2):
            crossindex1 = int(crolist[k][1])
            crossindex2 = int(crolist[k+1][1])
            cross1 = self.pop(crossindex1)#parents of the cross individual
            cross2 = self.pop(crossindex2)
            crossnew=[]
            for u,m in enumerate(cross1[:self.choosenum]):
                if m in cross2[:self.choosenum]:
                    crossnew.append(m)#inherit the gene that all parents have
            crossnewpre = []
            crossnewpre.append(cross1[i] for i in range(self.choosenum))
            crossnewpre.append(cross2[i] for i in range(self.choosenum))
            crossnewpre = list(set(crossnewpre))
            crossnewpre.remove(crossnew[i] for i in range(len(crossnew)))#the gene that only one of the parents keep
            crossnewcan = random.sample(crossnewpre,self.choosenum - len(crossnewpre))
            crossnew.append(i for i in crossnewcan)# the base will be choose
            crossrest = list(set(cross1).difference(set(crossnew)))#the base will not be used
            crossnew.append(i for i in crossrest) #a new individual
            self.pop.append(crossnew) #add the new individual into pop
            '改变self.pop是否会影响整个类'
    
    def mutation(self):
        mutepre = self.pop[random.sample(self.choose(),1)]
        mutepos = random.sample(range(len(mutepre)),2)
        mutepre[mutepos[1]],mutepre[mutepos[2]] = mutepre[mutepos[2]],mutepre[mutepos[1]]
        self.pop.append(mutepre)
        '改变self.pop是否会影响整个类'
        
    def popleft(self):
        popnowindex = [str(i) for i in range(len(self.pop))]
        popnowfit = self.fitness()
        popnow = dict(zip(popnowindex,popnowfit))
        popnow = sorted(popnow.items(), key = lambda x:x[1],reverse = True)
        poppre = []
        for i in range(self.popsize):
            poppre.append(self.pop[int(popnow[i][0])])
        self.pop = poppre
        
    
        
    def Gene_main(self):
        maxfit = 0
        bestindividual = []
        for i in range(self.iterationtime):
            self.cross()
            self.mutation()
            self.popleft()
            #print (self.pop)
            print("the best fitness of the %d's generation is %f "%(i,max(self.F)))
            print("the best individual of the %d's generation is %f "%i)
            print(self.pop[0][:self.baseusingnum])
            print("\n\n\n")
            if max(self.F) > maxfit:
                maxfit = max(self.F)
                bestindividual = self.pop[0]
                
        print("the best fitness is %f "%maxfit)
        print("the best individual is")
        print(bestindividual[:self.baseusingnum])
        parameter1 = []
        #parameter =  [basex,basey,baseh,x,y,h,fc,Tx,G,htb,hre,Noise,rsrpthre,sinrthre,coverthre,nbaseallx,nbaseally,ncost,ocost]
        for k in range(3):
            parameter1.append([self.parameter[k][l] for l in bestindividual[:self.baseusingnum]])
        parameter2 = [parameter1,parameter[3:]]
        cost = (evaluate.cost(parameter2))
        print("the cost of this individual is %r"%cost)
        print("\n\n\n")
        return maxfit, bestindividual[:self.baseusingnum], cost