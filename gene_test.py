#coding: utf-8
import evaluate
import gene

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
		
basex = [3,7,7,5,6,6,5]
basey = [5,3,7,2,7,8,4]
baseh = [10]*7
h = [1.7]*100
fc = 2900
Tx = 38.2
G = 10
htb = 10
hre = 1.7
Noise = -110
rsrpthre = -88
sinrthre = 0.7
coverthre = 0.7
nbaseallx = [3]
nbaseally = [5]
ncost = 300
ocost = 100
parameter1 = [basex,basey,baseh,x,y,h,fc,Tx,G,htb,hre,Noise,rsrpthre,sinrthre,coverthre,nbaseallx,nbaseally,ncost,ocost]
baseprenum = 7
parameter = parameter1
popsize = 4
baseusingnum = 4
choosenum =2
crosspro = 0.7
mutepro = 0.1
iterationtime = 10
a = gene.Gene(baseprenum,parameter,popsize,baseusingnum,choosenum,crosspro,mutepro,iterationtime)
maxfit, bestindividual, cost = a.Gene_main()