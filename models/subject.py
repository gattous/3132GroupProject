#!/usr/bin/env python

##with help from http://code.activestate.com/recipes/131499-observer-pattern/

class Subject():
    def __init__(self):
        self._observers = []


    def attach(self, observer):
        if not observer in self._observers:
            self._observers.append(observer)


    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

    
        
