#!/usr/bin/python2.7

import string
import random
from account import Account

class AccountTester:
    def __init__(self, numberOfTrials):
        self.numberOfTrials = numberOfTrials
        self.accounts = []
        self.passwords = []
        self.usernames = []
    def testAccounts(self):
        self.createAccounts()
        
    def checkAccount(self):
        print "Checkinggg"
    def createAccounts(self):
        for i in range(1, self.numberOfTrials):
            accountName = self.generateRandomString()
            self.usernames.append(accountName)
            passwordString = self.generateRandomString()
            self.passwords.append(passwordString)
            emailAddress = self.generateRandomString(3)+"@"+"gmail.com"
            print "Creating account with: ", accountName, passwordString, emailAddress
            newAccount = Account(accountName, passwordString)
            self.accounts.append(newAccount)
    def generateRandomString(self, size=10, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
        """Creates a random string of 'size' and from an optional set of given characters"""
        """Implentation grabbed from: stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python"""
        return ''.join(random.choice(chars) for _ in range(size))
    def printAccounts(self):
        print "Printing Account Test accounts:"
        print "Details: Username       Password"
        for a in self.accounts:
            a.printAccount()
