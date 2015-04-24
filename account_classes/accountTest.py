#!/usr/bin/python2.7

import string
import random
import sys
from account import Account

class AccountTester:
    def __init__(self, numberOfTrials):
        self.numberOfTrials = numberOfTrials
        self.accounts = []
        self.checks = []
        self.passwords = []
        self.usernames = []
        self.createAccounts()
        self.logFile = open('TestLog.txt', 'w')
    def testAccounts(self):
        #Edit the Accounts (*Update checks accordingly)
        self.checkAccount()
        self.logFile.close()
    def checkAccount(self):
        print "Checking Usernames"
        self.logFile.write("==USERNAME CHECKS==\n")
        successes = 0
        failures = 0
        testIteration = 1
        print len(self.checks)
        for check in self.checks:
            self.log(check.checkUsername(), "Username Check", check.getUsername())
            if check.checkUsername():
                successes += 1
            else:
                failures += 1
            testIteration += 1
        successes = 0
        failures = 0
        for check in self.checks:
            result = check.checkPassword()
            if result:
                successes += 1
            else:
                failures += 1
            self.log(result, "Password Check", check.getUsername())
        print "\n"
        self.logStat(successes, failures)

    def createAccounts(self):
        for i in range(1, self.numberOfTrials):
            accountName = self.generateRandomString()
            self.usernames.append(accountName)
            passwordString = self.generateRandomString()
            self.passwords.append(passwordString)
            emailAddress = self.generateRandomString(3)+"@"+"gmail.com"
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
    def log(self, check, checkType, accountName):
        if check == True:
            self.logFile.write("PASSED: %s %s\n" % (checkType, accountName))
        else:
            self.logFile.write("FAILED: %s %s\n" % (checkType, accountName))
    def logStat(self, numPass, numFail):
        totalTests = numPass + numFail
        successToFail = numPass / totalTests
        successToFail *= 100
        self.logFile.write("Test Results: Passed: %d, Failed %d, Success Rate %f\n" % (numPass, numFail, successToFail))

class accountCheck:
    def __init__(self, password, username, account):
        self.password = password
        self.username = username
        self.account = account

    def setPassword(self, password):
        self.password = password

    def setUsername(self, username):
        self.username = username

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def checkPassword(self):
        return self.password == self.account.getPassword()

    def checkUsername(self):
        return self.username == self.account.getUsername()
