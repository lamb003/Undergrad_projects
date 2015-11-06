import math
class Pval():
    
    def __init__(self):
        '''constructor'''
   
    def PValue(self, theta):
		t = math.sin(math.radians(theta))
		
		PvalDic = {}
		for n in range(2, 85):
			
			for m in range(0, n+1):
				
				r = (n-m) / 2.
				if (n-m)%2.0 != 0.:
					r = (n-m-1)/2.
				else:
					pass
					
				su = 0
			
				for k in range(0,int(r+1)):
					k = float(k)
					thisLoop = float(((-1)**k) * (float(math.factorial((2.*n - 2.*k)))/((float(math.factorial(k))\
					 * float(math.factorial((n - k))) * float(math.factorial((n - m - 2. *k)))))) *t**(n-m-2.*k))
					su = su + thisLoop
					
				pnm = (2.**-n) *(1. - t**2.)**(m/2.)
				pnm = pnm * su
				
				key  = "P_" + str(n) + "_" + str(m)

				PvalDic[key] = pnm
		return PvalDic
	
    def Pn(self,theta,Pv):
		t = math.sin(math.radians(theta))
		
		Pn = {}
		
		for n in range(2,85):
			for m in range(0, n+1):
				if m ==0:
					k=1.
				else:
					k=2
				
				getKey = "P_" + str(n) + "_" + str(m)
				key = "Pn_" + str(n) +"_" + str(m)
				pnm = float(math.sqrt((k * (2*n + 1) * float((math.factorial((n-m))) / float(math.factorial((n+m))))))) * Pv[getKey]
				
				Pn[key] = pnm
	
		return Pn


