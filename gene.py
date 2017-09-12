#coding: utf-8
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
        self.pop = self.pop1()
        #print(self.pop)
        self.E,self.F = self.fitness()
        
    def individual(self):
        indexnum = [i for i in range(self.baseprenum)]
        random.shuffle(indexnum)
        return indexnum
        
    def pop1(self):
        popultaion=[]
        for i in range(self.popsize):
            popultaion.append(self.individual())
        return popultaion
        
        
    
    
    def fitness(self):
        popfitness=[]
        #print(self.pop)
        #print("fitness")
        for i in self.pop:      #i = [abcdefg] individual
            #print("individual is %r"%i)
            j = i[:self.baseusingnum]   #j: all base will be used in the individual
            #print("all base will be used in the individual is %r"%j)
            parameter1 = []
            #parameter =  [basex,basey,baseh,x,y,h,fc,Tx,G,htb,hre,Noise,rsrpthre,sinrthre,coverthre,nbaseallx,nbaseally,ncost,ocost]
            #print("j is %r"%j)
            for k in range(3):
                parameter10 = []
                for l in j:
                    parameter10.append(self.parameter[k][l])
                    #print("l is %d"%l)
                    #print("self.parameter[k][l] is %r"%self.parameter[k][l])
                    #print("parameter10 is %r"%parameter10)
                parameter1.append(parameter10)
                #print("%d step parameter1 is should be basex or y or h of %d size: %r"%(k,self.baseusingnum,parameter1))
            #print("parameter1 %r is should be basex, basey and baseh of %d size"%(parameter1,self.baseusingnum))
            parameter2 = []
            parameter2.extend(parameter1)
            parameter2.extend(self.parameter[3:])
            popfitness.append(evaluate.Evaluate(parameter2).Evaluate_main())
        fmax = max(popfitness)
        #print('fmax = %d'%fmax)
        #print("popfitness is %r"%popfitness)
        popfitness1 = popfitness[:]
        popfitness2 = np.array(popfitness)
        popfitness2 = -popfitness2 + fmax + 5 
        popfitness2 = list(popfitness2)
        #print("self.F is %r"%popfitness)
        return popfitness1, popfitness2   #fitness value of each individual in pop
    
    
    
    
    def choose(self):
        #print("choose")
        chooseset=[]
        sumfitness = sum(self.F)
        #print("sumfitness = %f"%sumfitness)
        #print("self.F is %r" %self.F)
        #choosepro = [i/sumfitness for i in self.F]
        choosesumpro = [self.F[0]]*len(self.F)
        #print("location 1")
        for j in range(1,len(self.F)):
            choosesumpro[j] = choosesumpro[j-1]+self.F[j]
        #print("location 2")
        #print("step1 finished")
        choosesumpro = np.array(choosesumpro)
        #print(choosesumpro)
        choosesumpro = choosesumpro/sumfitness
        #print(sumfitness)
        #print(choosesumpro)
        #for i in range(3):
        while 1:
            a=random.uniform(0,1)
            
            if a < choosesumpro[0]:
                chooseset.append(0)
            for k in range(1,len(self.F)):
                if choosesumpro[k-1] <= a and choosesumpro[k] > a:
                    chooseset.append(k)
                #print("a is %f, k is %f\n, chooseset is %r\n, choosesumpro is %r\n"%(a,k,chooseset,choosesumpro))        
            
            if len(set(chooseset)) == self.choosenum:
                break
            #print(a,chooseset,self.choosenum)
        chooseset = list(set(chooseset))
        #print("chooseset is %r ,pop length is %d, pop now is %r"%(chooseset,len(self.pop),self.pop))
        return chooseset    #return the index of pop
        
    
    
    def cross(self):
        #print("cross")
        chooseset = self.choose()
        fitvalue = []
        #print("cross choose finished")
        chooseset = [str(i) for i in chooseset]  #the index of pop
        for j in chooseset:
            fitvalue.append(self.E[int(j)])   #the fitvalue of each individual choose from the pop
        #print("location 3")
        crosspre = dict(zip(chooseset,fitvalue))  
        crolist = sorted(crosspre.items(), key = lambda x:x[1],reverse = False)
        #[('2', 6), ('1', 2.1), ('3', 1.2)]
        #print("crolist is %r"%crolist)
        for k in range(0,self.choosenum,2):
            crossindex1 = int(crolist[k][0])
            crossindex2 = int(crolist[k+1][0])
            #print("self.pop is %r"%self.pop)
            #print(crossindex1)
            cross1 = self.pop[crossindex1]#parents of the cross individual
            cross2 = self.pop[crossindex2]
            crossnew=[]
            for u,m in enumerate(cross1[:self.baseusingnum]):
                if m in cross2[:self.baseusingnum]:
                    crossnew.append(m)#inherit the gene that all parents have
            #print("crossnew is %r"%crossnew)
            #print("cross1 is %r"%cross1)
            #print("cross2 is %r"%cross2)
            crossnewpre = []
            #crossnewpre.append(cross1[i] for i in range(self.baseusingnum))
            #crossnewpre.append(cross2[i] for i in range(self.baseusingnum))
            crossnewpre.extend(cross1[:self.baseusingnum])
            crossnewpre.extend(cross2[:self.baseusingnum])
            crossnewpre = list(set(crossnewpre))
            #print("crossnewpre is %r"%crossnewpre)
            for i in range(len(crossnew)):
                crossnewpre.remove(crossnew[i] )#the gene that only one of the parents keep
            crossnewcan = random.sample(crossnewpre,self.baseusingnum - len(crossnew))
            #print("crossnewcan is %r"%crossnewcan)
            crossnew.extend(crossnewcan)# the base will be choose
            #print("crossnew1 is %r"%crossnew)
            crossrest = list(set(cross1).difference(set(crossnew)))#the base will not be used
            #print("crossnew2 is %r"%crossnew)
            crossnew.extend(crossrest) #a new individual
            #print("the crossnew of 'self.pop.append(crossnew)' is %r"%crossnew)
            self.pop.append(crossnew) #add the new individual into pop
            #print("location 1")
        self.E,self.F = self.fitness()
            #print("location 2")
    
    def mutation(self):
        #print("mutation")
        mutepre = self.pop[random.sample(self.choose(),1)[0]]
        #print("mutepre is %r"%mutepre)
        mutepos = random.sample(range(len(mutepre)),2)
        #print("mutepos is %r"%mutepos)
        mutepre[mutepos[0]],mutepre[mutepos[1]] = mutepre[mutepos[1]],mutepre[mutepos[0]]
        #print("the mutepre of 'self.pop.append(mutepre)' is %r"%mutepre)
        self.pop.append(mutepre)
        self.E,self.F = self.fitness()
        
        
    def popleft(self):
        #print("popleft")
        #print("self.pop unchanged is %r"%self.pop)
        popnowindex = [str(i) for i in range(len(self.pop))]
        popnowfit,unum = self.fitness()
        popnow = dict(zip(popnowindex,popnowfit))
        popnow = sorted(popnow.items(), key = lambda x:x[1],reverse = False)
        poppre = []
        
        #for i in range(len(self.pop)):
        for i in range(self.popsize):
            poppre.append(self.pop[int(popnow[i][0])])
        #print("poppre is %r"%poppre)
        self.pop = poppre
        #print("here2")
        self.E,self.F = self.fitness()
        
    
        
    def Gene_main(self):
        minfit = len(self.parameter[3] * self.parameter[17])
        bestindividual = []
        for i in range(self.iterationtime):
            self.cross()
            self.mutation()
            self.popleft()
            #print("here1")
            #print (self.pop)
            print("the best fitness of the %d's generation is %f "%(i,min(self.E)))
            print("the best individual of the %d's generation is"%i)
            print(self.pop[0][:self.baseusingnum])
            print("\n\n\n")
            if min(self.E) < minfit:
                minfit = min(self.E)
                bestindividual = self.pop[0]
                
        print("the best fitness is %f "%minfit)
        print("the best individual is")
        print(bestindividual[:self.baseusingnum])
        parameter1 = []
        #parameter =  [basex,basey,baseh,x,y,h,fc,Tx,G,htb,hre,Noise,rsrpthre,sinrthre,coverthre,nbaseallx,nbaseally,ncost,ocost]
        for k in range(3):
            parameter10 = []
            for l in bestindividual[:self.baseusingnum]:
                parameter10.append(self.parameter[k][l])
            parameter1.append(parameter10)
        print("parameter1 is %r"%parameter1)
        parameter2 = []
        parameter2.extend(parameter1)
        parameter2.extend(self.parameter[3:])
        cost = (evaluate.Evaluate(parameter2).cost())
        cover = (evaluate.Evaluate(parameter2).coverage())
        print("the cost of this individual is %r"%cost)
        print("the cover of this individual is %r"%cover)
        print("\n\n\n")
        return minfit, bestindividual[:self.baseusingnum], cost