#!/usr/bin/python2.7
import re

class Address:
    """This is the address class."""
    def __init__(self, address):
        """The initialization of an address, address strings are checked for validity"""
        self.setAddress(address)
    
    def _checkFormat(self, address):
        """This method checks the validity of an address string."""
        emailCheck = re.compile('[^@]+@[^@]+\.[^@]+')
        return emailCheck.match(address)

    def getAddress(self):
        """Returns the address of this class"""
        return self.address

    def setAddress(self, address):
        """Sets the address, but the address must be valid to be set, it will return True if address was successfully set, false if otherwise"""
        if(self._checkFormat(address)):
            self.address = address
        else:
            return False
        return True
