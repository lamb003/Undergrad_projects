#Geodesy prac4
#Read in an SB3 file

import UserString

class ReadFile():

	def __init__(self):
		'''constructor'''

	def readHeader(self, file):
		fob = open(file,"r")
		linelist = []

		for line in fob:
			line = UserString.MutableString(line)
			llist = [] #data in the line for the header
			sym = line[0]+line[2]
			if len(linelist) == 0:	#we are on the first line
				Ver = line[:2]
				datFlag = line[2]	#position only, or pos and velocity data
				year = line[3:7]
				month = line[8:10]
				day = line[11:13]
				hour = line[14:16]
				minute = line[17:19]
				second = line[20:31]
				Epochs = line[32:39]	#number of epochs observed in file
				datatype = line[40:45]	# type of data (slr, doris etc)
				cdSys = line[46:51]		#coord system
				orbType = line[52:55]
				Agency = line[56:60]	#Who provided the data
			
			elif len(linelist)==1:	#we are on line 2
				GPSw = line[3:7]
				SoW = line[8:23]	#seconds of the week
				epInt = line[24:38]	#epoch intervals
				MJD = line[39:44]	#Modified julian date
				Fday = line[45:60]	#fractional day
			

			else:
				continue



	def readData(self, file):
		fob = open(file, "r")
		VelList = []
		PosList = []

		for line in fob:
			line = UserString.MutableString(line)
			if line[0] == "P":
				# This is position data
				x = float(line[5:19])
				y = float(line[19:33])
				z = float(line[33:47])
				PosList +=[[x,y,z]]

			elif line[0] == "V":
				# This is velocity data
				xv = float(line[5:19])	/10000. #~ Transform from dm/s to KM/s?
				yv = float(line[19:33])/10000.
				zv = float(line[33:47])/10000.
				VelList += [[xv,yv,zv]]
			else:
				continue

		Dat = [PosList, VelList]
		return Dat