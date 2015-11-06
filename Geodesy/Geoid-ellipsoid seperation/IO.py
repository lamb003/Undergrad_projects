
import UserString

class pointReader():
    
    def __init__(self):
        '''constructor'''
        
    def readData(self, data):  
        ''' read in data ''' 
        fob = open(data,'r')

        allDataList = []
        allDat = {}
        
        for line in fob:
            lineList = []
            line = UserString.MutableString(line)
            linelist = []

            del line[:6]
            lineList1 =  [line[0] + line[1] + line[2]] 
            lineList2 =  [line[3] + line[4] + line[5]]

            del line[:6]
            sp = line.split()
            allData = lineList1 + lineList2 + sp

            newDataList = []
            for i in allData:
                io = float(i.replace('D','E'))
                newDataList += [io]
            key = str(int(newDataList[0])) + "_" + str(int(newDataList[1]))
             
            del newDataList[0]
            del newDataList[0]
            allDat[key] = newDataList

        return allDat
        
    def readStationData(self, data):
		'''read station data'''
		fob = fob = open(data,'r')
		allStations = []
		for line in fob:
			sp = line.split(' ')
			name,lat,lng = str(sp[0]), float(sp[1]), float(sp[2])
			station = [name,lat,lng]
			allStations += [station]

		return allStations


