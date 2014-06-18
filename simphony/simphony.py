#!/usr/bin/env python

class StateData(object):
    count = -1

    def __init__(self, numberDS):
        StateData.count +=5
        self._index = StateData.count 
        self._numberDS = numberDS

    def printInfo(self):
        print "StateData index=", self._index, " with number data sets ", self._numberDS

class SimpartixAdapter(object):
    classatr = "class atr"
    
    def __init__(self):
        pass;       
    
    def run(self):
        self._currentStateData = StateData(1)
           

    def getStateData(self):
        return self._currentStateData
