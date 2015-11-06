from IO import *
import math
pr = pointReader()

from Pval import *
class getN():
	
	def calcN(self,stnData, data):
		
		G = Pval()
		P = G.Pn(stnData[1],G.PValue(stnData[1]))
		lat = math.radians(stnData[1])
		lng = math.radians(stnData[2])
		
		GM = 3986005e8 					#Geocentric gravitational constant
		f = 0.00335281068118				#flattening
		a = 6378137. 							#semiMajor axis of the earth
		b = a*(1-f)						#semiMinor axis of the earth
		w = 7292115e-11					#angular velocity of earth
		e = math.sqrt(a**2 - b**2) / a
		e2 = math.sqrt(a**2 - b**2) / b 	#second eccentricity 
		
		m = ((w**2)*(a**2)*b)/GM 
		
		lata = (GM /(a*b)) * ( 1 - 3./2. * m - 3./14. * e2*m) #gravity acc. at equator
		latb = (GM/a**2) * ( 1 + m +3./7. * e2*m)
		k = (b * latb - a*lata)/(a*lata)
		ngrav = lata * ( 1 + k*(math.sin(lat))**2)/(math.sqrt(1-e**2*(math.sin(lat))**2)) #normal gravity phi_o
		ler = a * math.sqrt(1 - (e**2*(1-e**2)*(math.sin(lat))**2)/(1 - e**2*(math.sin(lat))**2))	#local ellipsoidal radius r(phi)

		outer = GM /(ngrav * ler) #outer part of N eqn, i.e left of the double summation
		
		#Normalise J's
		J2 =  108263e-8
		J4 = -0.00000237091222
		J6 =  0.00000000608347
		J8 = -0.00000000001427
		
		gcLat = math.atan(((b/a)**2 )* math.tan(lat))
			#Second part
		FullSum = 0
		
		for deg_n in range(2,85):
			totaln = 0
			for ord_m in range(0,deg_n+1):
				datlist = data[str(deg_n) + "_" + str(ord_m) ]
				
				if deg_n == 2 and ord_m ==0:
					jn = J2*math.sqrt(1/(2.*deg_n + 1.))
					C = datlist[0] + jn
					
				elif deg_n==4 and ord_m ==0:
					jn = J4*math.sqrt(1/(2.*deg_n + 1.))
					C = datlist[0] + jn 
					
				elif deg_n ==6 and ord_m ==0:
					jn = J6*math.sqrt(1/(2.*deg_n + 1.))
					C = datlist[0] + jn 
							
				elif deg_n==8 and ord_m ==0:
					jn = J8*math.sqrt(1/(2.*deg_n + 1.))
					C = datlist[0] + jn 
						
				else:
					C = datlist[0]
					
				S = datlist[1]
				getKey = "Pn_" + str(deg_n) + "_" + str(ord_m)
				totaln += (C * math.cos(ord_m*lng) + S*math.sin(ord_m*lng)) *\
				P[getKey] * math.cos(gcLat)
			
			totaln = (a/ler)**deg_n *totaln
			FullSum +=totaln
		N = outer * FullSum
		print stnData[0] + "			", N
		return N

