import vector
import numpy as np

def getPos(source, phase, distance):
	phase *= 2*np.pi
	t = vector.obj(rho=distance, phi=phase)
	s = source+t
	print((s.x, s.y))

from time import sleep
for i in np.arange(0, 1, .01):
	getPos(vector.obj(x=0, y=0), i, 1)
	sleep(.1)
