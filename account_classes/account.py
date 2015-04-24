#!/usr/bin/python2.7

from person import Person


class Account:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password #Add actual non-string storage of passwords
        self.person = Person(name=username, email=email)

    def logout(self):
        # Save Object to file
        print "Implement Logout"

    def login(username, password):
        # Search for Account File credentials
        # Check Password
        # Open Account
        # Return Account
        print "Implement login"
        return Account()

    def delete(self, username, password):
        # Search for Account File credentials
        # Check password
        # Delete Account
        print "Implement Account deletion!"

    def editAccount(self, **kwargs):
        # Implement various methods to change various parts of the Account
        # Change username
        # Change password
        # Change image
        # Edit addresses
        print "Implment, username, password, image, and address change methods"

    def set_user_name(self, new):
        """Sets the account's username"""
        self.person.set

    def getUsername(self):
        return self.username

    def getPassword(self):
        """Probs make this method private and have it encapsulated with some authorized method"""
        return self.password

    def get_person(self):
        """Returns the person object associated with this account"""
        return self.person

    def printAccount(self):
        print "\t", self.username, "\t", self.password

