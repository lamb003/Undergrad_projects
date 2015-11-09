'''
Created on 13 Sep 2013

@author: chad
'''
# 
# if __name__ == '__main__':
#     pass
def DMS2dec(dms):
    ''' convert from dd.mmss to decimal degrees '''
    
    D = int(dms)
    M = int((dms - D) * 100.0)
    S = round((((dms - D) * 100.0) - M )* 100,2)
    
    DEC = D + M/60.0 + S/3600.0
    
    return DEC


    
def dec2DMS(dec):
    ''' converts decimal degrees to dms (dd.mmss)'''
    d = int(dec)
    m = int((dec - d)*60)
    s = (((dec - d)*60) - m) *60
 
    DMS = float(d + m/100.0 + s/10000.0)
 
    return DMS



##print "Approximate formula"
##
##print "S: " + str(1215417.123) + "m"
##print
##print "alpha1: " + str(dec2DMS(49.5808267))
##print
##print "alpha2: " + str(dec2DMS(44.9339529))

