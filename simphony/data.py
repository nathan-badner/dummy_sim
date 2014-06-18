#!/usr/bin/env python

class Data(object):   
    def __init__(self):
        self.myData = dict()
        self.myData['velocity'] = 0.0
        self.myData['foo'] = 42.0

    def __getattr__(self, name):
        if name  in self.myData:
            return self.myData[name]
        else:
            raise AttributeError