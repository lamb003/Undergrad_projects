# This is the main module 

from IO import *
from Calculations import *
import matplotlib.pyplot as plt


RF = ReadFile()
OC = OrbitChecks()
DataSet1 = RF.readData("uct.orb.jason2.140510.v40.sp3")
Poslist1, Veclist1 = DataSet1[0], DataSet1[1]
##print len(Poslist1)
##print len(Veclist1)
DataSet2 = RF.readData("uctja208.b14124.e14131.sp3.001")
Poslist2, Veclist2 = DataSet2[0], DataSet2[1]


# Plotting

DifRad = []
DifAlong = []
DifCrosX = []
DifCrosY = []
DifCrosZ = []
# Determine the OrbitChecks
obs = range(0,1440)#len(Poslist1))
for i in obs :
	Radial1, Radial2 = OC.Radial(Poslist1[i]),      OC.Radial(Poslist2[i])
	Cross1, Cross2 = OC.CrossTrack(Poslist1[i], Veclist1[i]),	OC.CrossTrack(Poslist2[i], Veclist2[i])
	Along1, Along2 =  OC.AlongTrack(Poslist1[i], Veclist1[i]),	OC.AlongTrack(Poslist2[i], Veclist2[i])

	DifRad +=[Radial1 - Radial2]
	DifAlong += [Along1 - Along2]
	DifCrosX += [Cross1[0] - Cross2[0]]
	DifCrosY += [Cross1[1] - Cross2[1]]
	DifCrosZ += [Cross1[2] - Cross2[2]]


# Get means for entire dataset
DifRadM = []
DifAlongM = []
DifCrosXM = []
DifCrosYM = []
DifCrosZM = []

# RMS part
DifRadRMS = []
DifAlongRMS = []
DifCrosXRMS = []
DifCrosYRMS = []
DifCrosZRMS = []
#####

Allobs = range(0,len(Poslist1))
for i in Allobs:
	Radial1M, Radial2M = OC.Radial(Poslist1[i]),      OC.Radial(Poslist2[i])
	Cross1M, Cross2M = OC.CrossTrack(Poslist1[i], Veclist1[i]),	OC.CrossTrack(Poslist2[i], Veclist2[i])
	Along1M, Along2M =  OC.AlongTrack(Poslist1[i], Veclist1[i]),	OC.AlongTrack(Poslist2[i], Veclist2[i])

	DifRadM +=[Radial1M - Radial2M]
	DifAlongM += [Along1M - Along2M]
	DifCrosXM += [Cross1M[0] - Cross2M[0]]
	DifCrosYM += [Cross1M[1] - Cross2M[1]]
	DifCrosZM += [Cross1M[2] - Cross2M[2]]


	DifRadRMS +=[(Radial1M - Radial2M)**2]
	DifAlongRMS += [(Along1M - Along2M)**2]
	DifCrosXRMS += [(Cross1M[0] - Cross2M[0])**2]
	DifCrosYRMS += [(Cross1M[1] - Cross2M[1])**2]
	DifCrosZRMS += [(Cross1M[2] - Cross2M[2])**2]


MRad = sum(DifRadM)/len(Poslist1)
MAlong = sum(DifAlongM)/len(Poslist1)
MCrosx = sum(DifCrosXM)/len(Poslist1)
MCrosy = sum(DifCrosYM)/len(Poslist1)
MCrosz = sum(DifCrosZM)/len(Poslist1)
#RMS
RMSRad = np.sqrt(sum(DifRadM)/len(Poslist1))
RMSAlong = np.sqrt(sum(DifAlongRMS)/len(Poslist1))
RMSCrosx = np.sqrt(sum(DifCrosXRMS)/len(Poslist1))
RMSCrosy = np.sqrt(sum(DifCrosYRMS)/len(Poslist1))
RMSCrosz = np.sqrt(sum(DifCrosZRMS)/len(Poslist1))

print "The Mean for each of the Computations"
print
print "Mean Radial:       ",	MRad
print "Mean Along Track:  ",	MAlong
print "Mean Cross Track X:", MCrosx
print "Mean Cross Track Y:", MCrosy
print "Mean Cross Track Z:", MCrosz

print 
print "RMS for each of the Computation"
print "RMS Radial:       ",	RMSRad
print "RMS Along Track:  ",	RMSAlong
print "RMS Cross Track X:", RMSCrosx
print "RMS Cross Track Y:", RMSCrosy
print "RMS Cross Track Z:", RMSCrosz






# plt.subplot(2, 1, 1)
plt.title('Along Track')
plt.plot(obs, DifAlong)
plt.xlabel("time (Min)")
plt.ylabel("Along track Diferences (KM)")
plt.tight_layout()
# plt.show()
# plt.subplot(2, 1, 2)
plt.title('Radial')
plt.plot(obs, DifRad)
plt.xlabel("time (Min)")
plt.ylabel("Radial Differences (KM)")
plt.tight_layout()
# plt.show()


# plt.subplot(2,1,1)
plt.title("Cross Track")
plt.plot(obs, DifCrosX)
plt.xlabel("time (Min)")
plt.ylabel("Cross track X differences (KM)")
plt.tight_layout()
# plt.show()
# plt.subplot(2,1,2)
plt.title("Cross Track")
plt.plot(obs, DifCrosY)
plt.xlabel("time (Min)")
plt.ylabel("Cross track Y differences (KM)")
plt.tight_layout()
# plt.show()
#plt.subplot(2,1,1)
plt.title("Cross Track")
plt.plot(obs, DifCrosZ)
plt.xlabel("time (Min)")
plt.ylabel("Cross track Z differences (KM)")
plt.tight_layout()
# plt.show()

