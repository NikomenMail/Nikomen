#!/usr/bin/python2.7

from person import Person

class Account:
    def __init__(self, username, password, person):
        self.username = username
        self.password = password #Add actual non-string storage of passwords
        self.person = person
    def logout(self):
        #Save Object to file
        print "Implement Logout"
    def login(username, password)
        #Search for Account File credentials
        #Check Password
        #Open Account
        #Return Account
        print "Implement login"
        return Account()
    def delete(self, username, password)
        #Search for Account File credentials
        #Check password
        #Delete Account
        print "Implement Account deletion!"
    def editAccount(self, **kwargs)
        #Implement various methods to change various parts of the Account
        #Change username
        #Change password
        #Change image
        #Edit addresses
        print "Implment, username, password, image, and address change methods"