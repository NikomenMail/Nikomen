#!/usr/bin/python2.7

from contact import Contact


class Person(Contact):
    def __init__(self, name, email, imageName=None):
        """Constructor for the person class"""
        super(Person, self).__init__(name=name, emailaddress=email)
        self.imageName = imageName

    def set_name(self, new):
        """Aaaahhhh"""
        print "hello"

    def set_image_name(self, path):
        self.imageName = path

    def getImageName(self):
        """Returns the image file name"""
        return self.imageName

    def get_email_address(self):
        """Returns the Person's email address"""
        addresses = self.get_addresses()
        return addresses[0].get_address()

    def deleteImage(self):
        """Deletes associated image"""
        self.imageName = None
        #ADD ACTUAL DELETION OF IMAGE FILE HERE
