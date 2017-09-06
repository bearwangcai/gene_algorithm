import random
import evaluate

class Gene():
    def __init__  (self,Nbasepre,parameter):
        self.Nbasepre = Nbasepre
        
    def individual(self):
        indexnum = [i for i in self.Nbasepre]
        indexnum = random.shuffle(indexnum)
        return indexnum
        
    def pop(self,size):
        popultaion=[]
        for i in range(size):
            popultaion.append[self.individual()]
        return popultaion
        
    def choose(self):
    
    def cross(self):
    
    def mutation(self):