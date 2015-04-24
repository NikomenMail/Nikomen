#!/usr/bin/python2.7

import string
import random
from account import Account

class AccountTester:
    def __init__(self, numberOfTrials):
        self.numberOfTrials = numberOfTrials
        self.accounts = []
        self.checks = []
        self.passwords = []
        self.usernames = []
        self.logFile = "d"
    def testAccounts(self):
        self.createAccounts()
        #Edit the Accounts (*Update checks accordingly)

    def checkAccount(self):
        print "Checking Usernames"
        for check in self.checks:
            if check.checkUsername:
                print "Check for account:", check.getUsername, "passed!"
            else:
                print "Check for account:", check.getUsername, "failed!!!"

    def createAccounts(self):
        for i in range(1, self.numberOfTrials):
            accountName = self.generateRandomString()
            self.usernames.append(accountName)
            passwordString = self.generateRandomString()
            self.passwords.append(passwordString)
            emailAddress = self.generateRandomString(3)+"@"+"gmail.com"
            print "Creating account with: ", accountName, passwordString, emailAddress
            newAccount = Account(accountName, passwordString)
            newCheck = accountCheck(passwordString, accountName, newAccount)
            #Create Account with corresponding Check
            self.accounts.append(newAccount)
            self.checks.append(newCheck)

    def generateRandomString(self, size=10, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
        """Creates a random string of 'size' and from an optional set of given characters"""
        """Implentation grabbed from: stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python"""
        return ''.join(random.choice(chars) for _ in range(size))
    def printAccounts(self):
        print "Printing Account Test accounts:"
        print "Details: Username       Password"
        for a in self.accounts:
            a.printAccount()
    def log(self, check, type, accountName):
        if check == True:
            print ";ol"

class accountCheck:
    def __init__(self, password, username, account):
        self.password = password
        self.username = username
        self.account = account

    def setPassword(self, password):
        self.password = password

    def setUsername(self, username):
        self.username = username

    def checkPassword(self):
        return self.password == self.account.getPassword()

    def checkUsername(self):
        return self.username == self.account.getUsername()