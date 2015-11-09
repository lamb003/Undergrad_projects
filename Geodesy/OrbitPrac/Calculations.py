#this is a bunch of kak and i dont feel like doing it
import numpy as np
class OrbitChecks():

	def __init__(self):
		"""constructor"""

	def Radial(self, Pvec):
		return np.linalg.norm(Pvec)

	def CrossTrack(self, Pvec, Vvec):
		v = np.linalg.norm(Vvec)
		Vvec = (Vvec[0]/v,Vvec[1]/v,Vvec[2]/v)
		return np.cross(Pvec,Vvec)

	def AlongTrack(self, Pvec, Vvec):
		v = np.linalg.norm(Vvec)
		Vvec = (Vvec[0]/v,Vvec[1]/v,Vvec[2]/v)
		return np.vdot(Pvec,Vvec)



