# -*- coding: utf-8 -*-

import jsonpickle
import json
from PyQt4 import QtGui  # Import the PyQt4 module we'll need
from PyQt4 import QtCore
 
########################################################################
class Car(object):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.wheels = 4
        self.doors = 5
        self.name = 'Volvo'

 
    #----------------------------------------------------------------------
    def drive(self):
        """"""
        print "Driving the speed limit"
 
if __name__ == "__main__":


    s = u'åland'
    print 'Printing a-ring:', s

    my_car = Car()
    #my_car.name = QtCore.QString(u'Åäö')
    my_car.name = 'Ford'

    serialized = jsonpickle.encode(my_car)
    print 'Serialized:', serialized
 
    f = open('jsonpickle.sav', 'w')
    f.write(serialized)
    f.close()

    my_car_obj = jsonpickle.decode(serialized)
    print 'De-serialized:', my_car_obj.drive()

    f = open('jsonpickle.sav')
    json_str = f.read()
    obj = jsonpickle.decode(json_str)
    print 'Testing the file decoded object:', obj.drive()
    f.close()


    