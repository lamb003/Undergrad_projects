'''
Created on 28 Apr 2014

@author: chad
'''
from scipy.spatial import cKDTree
import sympy as sp
import numpy as np

class Angles():
    
    def __init__(self):
        '''Constructor'''

    
    def LsNormals(self,points_list):
        
            # generate the KD Tree
            
        tree = cKDTree(points_list) 
        ####
        i = 0
        pointAngle = open('PointAngle.xyz','a')
       
        #####
        for p in points_list:
                #retrieves indeces of points in the neighbourhood of point P 
                n_indeces = tree.query(p, 15)[1]
                lA = []
                lL = []

                for index in list(n_indeces):
                    point = points_list[index]

                    lA += [[ -point[0], -point[1], -1]]
                    lL += [[(point[2])]]
          
                A = np.matrix(lA)
                L = np.matrix(lL)
                if np.linalg.det(A.T*A) != 0.0:
                    

                    x = (A.T*A).I*A.T*L
    
                    normal = [float(x[0]),float(x[1]),1]
                    ln = np.linalg.norm(normal)
                    uvNormal = normal / ln
    
                    angle = np.degrees(np.arccos(uvNormal[2])) #calculates angle between normal and vertical
                    
                    pointAngle.write(str(p[0]) + ' ' + str(p[1]) + ' ' + str(p[2]) + ' ' + str(angle) + '\n')
                    
                    
                    
                    i+=1
                    #done = i/250000.0 *100.00
    #                 print str(np.round(done, 2)) + "% done"
                else:
                    pointAngle.write(str(p[0]) + ' ' + str(p[1]) + ' ' + str(p[2]) + ' ' + str(90.0) + '\n')

        pointAngle.close()
            
        