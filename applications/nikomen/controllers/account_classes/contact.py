#!/usr/bin/python2.7

from address import Address


class Contact(object):
    """This is the contact class"""
    def __init__(self, name, emailaddress=None):
        """Contact constructor. Requires a name, address will be none if there is not address(es) specified)"""
        self.addresses = []
        self.name = name
        self.add_address(emailaddress)

    def add_address(self, emailAddress):
        """Adds an Address class to the Contact"""
        tmpAddress = Address(emailAddress)
        #tmpAddress == None if email is invalid
        if tmpAddress != None:
            self.addresses.append(tmpAddress)

    def get_addresses(self):
        """Returns the Address of this Contact"""
        return self.addresses

    def deleteAddress(self, address):
        """Deletes Address of this Contact"""
        self.addresses.remove(address)

    def editAddress(self, oldAddress, newAddress):
        self.addresses.remove(oldAddress)
        self.addresses.append(newAddress)
