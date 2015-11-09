'''
Created on 04 Apr 2014

@author: chad
'''
from numpy import ceil
from ReadPoints import *

class tiling():
    def __init__(self):
        '''constructor'''
        
    def tile(self, xyzlist):
#         fob = open(data,"r")
#         
#         
#         xlist = []
#         ylist = []
#         zlist =[]
#         
#         for line in fob:
#             sp = line.split(' ')
#         
#             x,y,z = float(sp[0]), float(sp[1]), float(sp[2])
#             xlist += [x]
#             ylist += [y]
#             zlist += [z]
        
        
        
#         fob.close() 
       
           
        xlist = xyzlist[0]
        ylist = xyzlist[1]
        zlist = xyzlist[2]
        ppt = 250000.0
        numTiles = ceil(len(xlist)/ppt)
        #     print numTiles
        print "The Number of tiles to be made is: " + str(numTiles)
        print 
        
        for i in range(1, int(numTiles)):
            # iterate over the tiles
            tileDoc = open('tile' + str(i) + '.xyz', 'w')
            for coord in range(int((i-1)*ppt), int(i*ppt)):
                tileDoc.write(str(xlist[coord]) + ' ' + str(ylist[coord]) + ' ' + str(zlist[coord]) + '\n')
            
            tileDoc.close()
            complete = round(i / float(round(numTiles)) *100, 3) 
            
            print str(i) + " of " + str(numTiles) + " complete"
#         print "DONE"
        return numTiles
        
        
        
            
            
        
        
        
        
    
    
