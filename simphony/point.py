#!/usr/bin/env python
import data

class Point(object):
    guuid = -1

    @staticmethod
    def uniqueId():
        Point.guuid = Point.guuid+1
        return Point.guuid
    
    def __dummyinit__(self):
        self.uuid = Point.uniqueId()
        self._x_ = 0.0
        self._y = 0.0
        self._z = 0.0
        self.data = data.Data()
        print self.data
        
    def __init__(self, x, y, z, id):
        self.uuid = id
        self._x_ = x
        self._y = y
        self._z = z
        self.data = data.Data()
        print self.data

    def printInfo(self):
        print "StateData index=", self._index, " with number data sets ", self._numberDS


    def __getattr__(self, name):
        if name  in self.myData:
            return self.myData[name]
        else:
            raise AttributeError