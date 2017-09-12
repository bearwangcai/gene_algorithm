import numpy as np
from math import sqrt, log10
from scipy.spatial import cKDTree
class Evaluate:
	def __init__(self,parameter):
		#parameter = [basex,basey,baseh,x,y,h,fc,Tx,G,htb,hre,Noise,rsrpthre,sinrthre,coverthre,obaseallx,obaseally,ncost,ocost]
		#print(parameter)
		self.Nsample = len(parameter[3])
		self.Nbase = len(parameter[0])
		self.basex = parameter[0]
		self.basey = parameter[1]
		self.x = parameter[3]
		self.y = parameter[4]
		self.baseh = parameter[2]
		self.h = parameter[5]
		self.fc = parameter[6]
		self.Tx = parameter[7]
		self.G = parameter[8]
		self.htb = parameter[9]
		self.hre = parameter[10]
		self.L1 = 46.33+33.9*log10(self.fc)-13.82*log10(self.htb)-((1.1*log10(self.fc)-0.7)*self.hre-1.56*log10(self.fc)+0.8)+3
		self.L2 = 44.9-6.55*log10(self.htb)
		self.Noise = parameter[11]
		self.rsrpthre = parameter[12]
		self.sinrthre = parameter[13]
		self.coverthre = parameter[14]
		self.obaseallx = parameter[15]
		self.obaseally = parameter[16]
		self.ncost = parameter[17]
		self.ocost = parameter[18]
		#print("self.basex is %r"%self.basex)
	
	def loss(self,d):
		if abs(d - 0) < 0.5:
			L=0
		else:
			L = self.L1 + self.L2*log10(d)
		return L 
	
	def R(self,rsrp,sinrpr):
		sinr = rsrp/sinrpr
		if rsrp >= self.rsrpthre and sinr >= self.sinrthre:
			return 1
		else:
			return 0
	'''	
	def coverage(self):
		sinrp=np.ones(self.Nsample)*(self.rsrp-10)	
		rsrp=np.ones(self.Nsample)*self.sinrthre
		coverv=np.zeros(self.Nsample)
		basexy = list(zip(self.basex,self.basey))
		basexycd = cKDTree(basexy)
		for i in range(self.Nsample):
			corsample = list(zip(self.basex[i],self.basey[i]))
			nearbase = basexycd.query_ball_point(corsample,2)
			for j in nearbase:
				d = sqrt((self.basex[j]-self.x[i])**2+(self.basey[j]-self.y[i])**2)
				L = loss(self,d)
				rsrp1 = self.Tx + self.G - L
				if rsrp1 > rsrp[i]:
					rsrp[i] = rsrp1
				else:
					sinr[i] += rsrp1
			coverv[i] = R(rsrp[i],sinr[i])
		cover = sum(coverv)/self.Nsample
	return cover
	'''
	def coverage(self):
		sinr=np.ones(self.Nsample)*pow(10,self.Noise/10)
		rsrp=np.ones(self.Nsample)*pow(10,(self.rsrpthre-10)/10)
		coverv=np.zeros(self.Nsample)
		for i in range(self.Nsample):
			for j in range(self.Nbase):
				d = sqrt((self.basex[j]-self.x[i])**2+(self.basey[j]-self.y[i])**2)
				#print(d)
				L = self.loss(d)
				rsrp1 = self.Tx + self.G - L
				#print("the %d sample, the %d base loss = %f" %(i,j,rsrp1))
				rsrp1 = pow(10,rsrp1/10)
				if rsrp1 > rsrp[i]:
					rsrp[i] = rsrp1
				else:
					sinr[i] += rsrp1
			coverv[i] = self.R(10*log10(rsrp[i]),10*log10(sinr[i]))
		cover = sum(coverv)/self.Nsample
		return cover
	
	
	def cost(self):
		j=0
		basexy = list(zip(self.basex,self.basey))
		#print("basexy is %r"%basexy)
		baseallxy = list(zip(self.obaseallx,self.obaseally))
		#print("baseallxy is %r"%baseallxy)
		for i in range(self.Nbase):
			if basexy[i] in baseallxy:
				j+=1
		#print("j = %d"%j)
		costvalue = j*self.ocost + (self.Nbase-j)*self.ncost
		return costvalue
	
	
	def Evaluate_main(self):
		cover = self.coverage()
		costvalue = self.cost()
		#print("cover = %f" %cover)
		if cover >= self.coverthre:
			evalute = costvalue * (1+cover)
		else :
			evalute = self.Nsample * self.ncost#if coverage is less than threshold, then return a much larger value than normal evalutae num
		return evalute
