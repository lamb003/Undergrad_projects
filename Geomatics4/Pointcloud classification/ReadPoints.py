'''
Created on 02 May 2014

@author: chad
'''
class pointReader():
    
    def __init__(self):
        '''constructor'''
        
    def readpoints(self, data):  
        ''' read in data and create points list''' 
        fob = open(data,'r')
        
        points =[]
            
        for line in fob:
            sp = line.split(' ')
            points += [[float(sp[0]),float(sp[1]),float(sp[2])]]
        
                   
        fob.close()
        return points
    
    def xyzRead(self, data):
        '''Read points and output xlist, ylist, zlist'''
        fob = open(data,"r")
        
        
        xlist = []
        ylist = []
        zlist =[]
        
        for line in fob:
            sp = line.split(' ')
        
            x,y,z = float(sp[0]), float(sp[1]), float(sp[2])
            xlist += [x]
            ylist += [y]
            zlist += [z]
        
        fob.close()
        
        xyzlist = [xlist,ylist,zlist]
        
        return xyzlist
        