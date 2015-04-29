#!/usr/bin/python2.7

from applications.nikomen.modules.account_classes.contact import Contact


class Person(Contact):
    def __init__(self, name, email, imageName="/"):
        """Constructor for the person class"""
        super(Person, self).__init__(name=name, emailaddress=email)
        self.imageName = imageName

    def set_name(self, new):
        """Aaaahhhh"""
        print "hello"

    def set_image_name(self, path):
        """Sets the image path"""
        self.imageName = path

    def get_image_name(self):
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
