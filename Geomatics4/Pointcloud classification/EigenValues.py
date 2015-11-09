'''
Created on 01 May 2014

@author: chad
'''
import numpy as np
from scipy.spatial import cKDTree


class EigenCalc():
    
    def __init__(self):
        '''constructor'''
        
        
 
    
    def eigen(self,points_list):
        
            # generate the KD Tree
            
        tree = cKDTree(points_list) 
        ####
        i = 0
        pointAngle_eig = open('PointAngle_eig.xyz','a')
       
        #####
        for p in points_list:
                #retrieves indeces of points in the neighbourhood of point P 
                n_indeces = tree.query(p, 15)[1]
                lA = []


                for index in list(n_indeces):
                    point = points_list[index]

                    lA += [[ point[0], point[1], point[2]]]
                    
          
                A = np.matrix(lA)
                
#        Get covariance matrix of A
                
                Cov_A = np.cov(A.T)
               # print Cov_A
                
#           determine the eigen values and corrosponding vectors for the Covariance matrix of A

                eig_value, eig_vector = np.linalg.eig(Cov_A)
#                 print eig_value
#                 print eig_vector
                
#                 extract the min eigen value
                min_eig = min(eig_value)
#                 print min_eig
                index_eigmin = np.where(eig_value == min_eig)[0]
#                 print index_eigmin
                normal = eig_vector[:,index_eigmin]
#                 note eigen vectors are already normalized by the nplinalg.eig function
                
                angle = np.degrees(np.arccos(normal[2])) 
                #print angle[0]
                pointAngle_eig.write(str(p[0]) + ' ' + str(p[1]) + ' ' + str(p[2]) + ' ' + str(angle[0]) + '\n')
                
                
        pointAngle_eig.close()
        