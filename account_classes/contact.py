#!/usr/bin/python2.7

from account import Account

class Contact:
    """This is the contact class"""
    def __init__(self, name, emailAddress=None):
        """Contact constructor. Requires a name, address will be none if there is not address(es) specified)"""
        self.addresses = []
        self.name = name
        if emailAddress != None:
            #Iterate over input addresses
            for eAddr in emailAddress:
                tmpAddress = Address(eAddr)
                #Check to see if Email Address is valid
                if tmpAddress != None:
                    self.addresses.append(tmpAddress)

    def addAddress(emailAddress):
        """Adds an Address class to the Contact"""
        tmpAddress = Address(emailAddress)
        #tmpAddress == None if email is invalid
        if tmpAddress != None
            self.addresses.append(tmpAddress)

    def getAddresses(self):
        """Returns the Address of this Contact"""
        return self.addresses
    def deleteAddress(self, address)
        """Deletes Address of this Contact"""
        self.addresses.remove(address)
    def editAddress(self, oldAddress, newAddress)
        self.addresses.remove(address)
        self.addresses.append(newAddress)
