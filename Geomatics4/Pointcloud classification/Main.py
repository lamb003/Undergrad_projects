'''
Created on 28 Apr 2014

@author: chad
'''
from PlaneFit import *
from TilingPointCloud import *
from EigenValues import *
if __name__ == '__main__':
    print "************"
    print "Begin"
    print "************"
    print 
    print "Tiling point cloud"
#     data = 'W55A - Cloud.xyz'
    data = 'jameson.xyz'
    read =  pointReader()
    TileData = tiling()
    AngleCalc = Angles()
    EigCalc = EigenCalc()
    tiles = TileData.tile(read.xyzRead(data))
    print 
    print "Finished tiling point cloud"
    print 
    print "To calculate the angle by planefitting type p"
    print "To calculate the angel by eigenvectors type e"
    print 
    method = raw_input("Method to use: ")
    print
    
#loop to run through all the tiles and output data
    if method == 'p' or method == 'P':  
        print "Calculating normal angle to the vertical"
        print  
        for i in range(1,int(tiles)):
             
            infile = 'tile' + str(i) + '.xyz'
            AngleCalc.LsNormals(read.readpoints(infile))
            print str(i) +' of ' + str(int(tiles)) + ' done'
#    
    elif method == 'e' or method == "E":     
#    calculating data using eigen values
        print "Calculating normal angle to the vertical"
        print
        for i in range(1,int(tiles)):
            
            infile = 'tile' + str(i) + '.xyz'
            EigCalc.eigen(read.readpoints(infile))
            print str(i) +' of ' + str(int(tiles)) + ' done'
    else:
        print "Sorry, command not understood"
    print "************"
    print "End"
    print "************"
    