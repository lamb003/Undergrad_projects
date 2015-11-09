'''
Created on 23 Sep 2013

@author: chad
'''
#===============================================================================
# 2D helmert transformation parameters by least squares
#===============================================================================


import numpy as np
from DMS import dec2DMS


class Helmert():


#    Reduce the coords to their centre of gravity form

        

    
#===============================================================================
#     To  set up the least squares for this problem the observation equations are as follows:
#     Vxi = a*xi + b*yi - Xi
#     Vyi = a*yi - b*xi - Yi    , where x,y are source system and X,Y are target parameters a,b
#
#    note: parameters Xo and Yo should reduce to 0
#===============================================================================
    
    def leastSquares(self, source, target):
        sum_source = np.sum(source, 0, dtype = float)
        sum_target = np.sum(target, 0, dtype = float)
        
        xc_s = sum_source[0,1] / len(source)
        yc_s = sum_source[0,0] / len(source)
        
        xc_t = sum_target[0,1] / len(target)
        yc_t = sum_target[0,0] / len(target)
        
        CG_s = np.matrix([]).reshape(0,2)
    #===============================================================================
    # generate the centre of gravity matrices for the source and target systems
    #===============================================================================
        
        for coords_s in source:
            Nxi_s = coords_s[0,1] - xc_s
            Nyi_s = coords_s[0,0] - yc_s
            CG_sRow = np.matrix([Nyi_s, Nxi_s])
            
            CG_s = np.row_stack([CG_s,CG_sRow])
    
            
        CG_t = np.matrix([]).reshape(0,2)
        
        for coords_t in target:
            Nxi_t = coords_t[0,1] - xc_t
            Nyi_t = coords_t[0,0] - yc_t
            CG_tRow = np.matrix([Nyi_t, Nxi_t])
            
            CG_t = np.row_stack([CG_t, CG_tRow])

    # the above method returns  the centre of gravity coords as a list containing a matrix of the source
    # centre of gravity and the target centre of gravity            
            
#         CG_s = CentreOfGravityCoords[0]
#         CG_t = CentreOfGravityCoords[1]
        #=======================================================================
        #     Setup the A matrix so that Vx is delt with then Vy
        #=======================================================================
        
        VxiMatrix = np.matrix([]).reshape(0,4)
        VyiMatrix = np.matrix([]).reshape(0,4)
        
        for  i in CG_s:
            
            vxi_row = np.matrix([[0,1,i[0,1],i[0,0]]])
            VxiMatrix = np.row_stack((VxiMatrix, vxi_row))
            
            
            vyi_row = np.matrix([[1,0,i[0,0],-1.0*i[0,1]]])
            VyiMatrix = np.row_stack((VyiMatrix, vyi_row))
            
        #===================================================================
        # define the A matrix
        #===================================================================
        A = np.vstack((VxiMatrix,VyiMatrix))
        #=======================================================================
        # define the l vector 
        #=======================================================================
        
        
        
        lx = CG_t[:,1]
        ly = CG_t[:,0]
        
        l = np.vstack((lx,ly))
        
        X = (A.T * A).I * A.T * l 
        # X = Yo, Xo, a, b   
        
        V = A*X - l
        # residuals

        a = X[2,0]
        b = X[3,0]
               
        Sigma0hat = np.sqrt((V.T * V)/(len(A) - len(X) ))
        Sigma_X = (Sigma0hat[0,0]**2)*((A.T * A).I)
        
        k  = np.sqrt(a**2 + b**2)
        #Scale factor
        theta_rad = np.arctan(b/a)
        #rotation in radians
        theta = dec2DMS(np.degrees(theta_rad)) *10000.0
        
        # Rotation in seconds
        
        #=======================================================================
        # Standard deviations of k and Theta
        #=======================================================================
        
        
        dkda = a / k
        dkdb = b / k
        
        dtda = 1.0 / (a*b + b**2)
        dtdb = 1.0 /(b/(a**2) + (b**2)/(a**2)) 
        
        B = np.matrix([[dkda,dkdb],[dtda,dtdb]])
        
        E_x = Sigma_X[2:,2:]
        
       
        E_kt = B* E_x * B.T
        
        Sig_k = np.sqrt(E_kt[0,0])
        Sig_t = np.sqrt(E_kt[1,1])
        
        
        Sig_a = np.sqrt(E_x[0,0])
        Sig_b = np.sqrt(E_x[1,1])
        
        print "data"
        print "Source System"
        print source
        print
        print "Target System"
        print target
        print 
        print "Results\nX: " 
        print X
        print
       
        print "Residuals\nV: " 
        print V
        print
        print "Standard deviation of observation of unit weight\nSigma0 hat: " 
        print Sigma0hat
        print "Covariance matrix of the unknowns of the unknowns\nSigma X: " 
        print Sigma_X
        print
        print "Xo ~ Yo ~ 0.000m"
        print 
        print "a = " + str(a) + "    b = " + str(b)
        print "Std dev a = " + str(Sig_a) + "    Std dev b = " + str(Sig_b)
        print
        
        print "Scale factor\nk: "
        print k
        print "Rotation angle\ntheta: "
        print theta 
        print
        print "Covariance matrix of K and theta"
        print  E_kt
        print
        print "Std dev k = " + str(Sig_k) + "    Std dev theta = " +str(Sig_t)
         
# test data from the notes pg42
##Cape_datum = np.matrix([[50687.27,3757999.54],[50931.08,3762898.83],[51662.73,3758471.22]])
##Hart94 = np.matrix([[50750.11,3758299.80],[50993.71,3763199.16],[51725.57,3758771.46]])
##test = Helmert()
##test.leastSquares(Cape_datum, Hart94)

##
Cape_datum = np.matrix([[50687.27,3757999.54],[50931.08,3762898.83],[51662.73,3758471.22],[48748.66,3759562.29],[48492.69,3758949.11],[54223.03,3763109.39],[52888.92,3760506.79],[49845.03,3758917.80]])
Hart94 = np.matrix([[50750.11,3758299.8],[50993.71,3763199.16],[51725.57,3758771.46],[48811.38,3759862.58],[48555.50,3759249.26],[54285.72,3763409.75],[52951.68,3760807.08],[49907.87,3759218.00]])

H = Helmert()
H.leastSquares(Cape_datum, Hart94)
