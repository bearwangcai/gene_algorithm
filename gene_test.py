#coding: utf-8
import evaluate
import gene
import random

'''
def __init__  (self,baseprenum,parameter,popsize,baseusingnum,choosenum,crosspro,mutepro,iterationtime):
#parameter = [basex,basey,baseh,x,y,h,fc,Tx,G,htb,hre,Noise,rsrpthre,sinrthre,coverthre,nbaseallx,nbaseally,ncost,ocost]
TERM_HEIGHT = 1.5
TX_POWER = 38.2
FREQ = 2600
NOISE = -110.0
center_x = 103.75  # 兰州的中心点（保留2位小数）
center_y =  36.09
'''

x=[0]*100
for i in range(10):
	for j in range(10):
		x[i*10+j] = j

y=[0]*100		
for i in range(10):
	for j in range(10):
		y[i*10+j] = i
		
        
basex=[]
basey=[]
for i in range(30):
    basex.append(random.randint(0,9))
    basey.append(random.randint(0,9))
#print("basex is %r"%basex)
baseh = [10]*30
h = [1.7]*100
fc = 2900
Tx = 80.2
#TX = 38.2 ...
G = 16.34
htb = 10
hre = 1.7
Noise = -110
rsrpthre = -88
sinrthre = -3
coverthre = 0.7
obaseallx = []
obaseally = []
obaseallx.extend(random.sample(basex,10))
obaseally.extend(random.sample(basey,10))
ncost = 300
ocost = 100
parameter1 = [basex,basey,baseh,x,y,h,fc,Tx,G,htb,hre,Noise,rsrpthre,sinrthre,coverthre,obaseallx,obaseally,ncost,ocost]
baseprenum = 30
parameter = parameter1
popsize = 8
baseusingnum = 4
choosenum =6
crosspro = 0.9
mutepro = 0.1
iterationtime = 10
#print("a's basex is %r"%parameter[0])
a = gene.Gene(baseprenum,parameter,popsize,baseusingnum,choosenum,crosspro,mutepro,iterationtime)
maxfit, bestindividual, cost = a.Gene_main()
