#!/usr/bin/env python

from simphony import *

simPar = SimpartixAdapter()
# configure simpartix with a model with
#  CM, SD, BC, SP


# configure CM (solver and paramters) so that 
# it would output 

#for i in range(200):
#        simPar.run() # runs for 5 steps
#        savefile('myfile.simphy' + str(i), simPar.getStateData())
	#or 
        # simphony.saveStateData(filename='myfile.simphy', timestep=i, simPar.getStateData())



#savefile('myfile.simphy', simPar)

p = Point(1, 2, 3, 43)
print p.uuid
p = Point(1, 2, 3, 43)
#print p.data
#print p.data.foo
print p.data.velocity
