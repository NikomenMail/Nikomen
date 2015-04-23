#!/usr/bin/python2.7

from contact import Contact

class Person(Contact):
    def __init__(self, name, imageName=None):
        """Constructor for the person class"""
        super(Contact, self).__init__(name)
        if (imageName != None):
            self.imageName = imageName
    def getImageName(self):
        """Returns the image file name"""
        return self.imageName
    def deleteImage(self):
        """Deletes associated image"""
        self.imageName = None
        #ADD ACTUAL DELETION OF IMAGE FILE HERE
