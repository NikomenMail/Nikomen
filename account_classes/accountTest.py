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
        self.create_accounts()
        self.logFile = open('TestLog.txt', 'w')

    def test_accounts(self):
        # Edit the Accounts (*Update checks accordingly)
        self.check_account()
        self.logFile.close()

    def check_account(self):
        print "Checking Usernames"
        self.logFile.write("==USERNAME CHECKS==\n")
        successes = 0
        failures = 0
        test_iteration = 1
        # Check Username
        for check in self.checks:
            self.log(check.checkUsername(), "Username Check", check.getUsername())
            if check.checkUsername():
                successes += 1
            else:
                failures += 1
            test_iteration += 1
        self.logStat(successes, failures)
        successes = 0
        failures = 0
        # Check passwords
        for check in self.checks:
            result = check.checkPassword()
            if result:
                successes += 1
            else:
                failures += 1
            self.log(result, "Password Check", check.getUsername())
        self.logStat(successes, failures)
        successes = 0
        failures = 0
        # Check addresses
        for check in self.checks:
            result = check.checkperson()
            if result:
                successes += 1
            else:
                failures += 1
            self.log(result, "Person Check", check.getUsername())
        print ""
        self.logStat(successes, failures)

    def create_accounts(self):
        """This method creates a select number of accounts for testing"""
        for i in range(1, self.numberOfTrials):
            account_name = self.generate_random_string()
            password_string = self.generate_random_string()

            email_address = self.generate_random_string(3)+"@"+"gmail.com"
            new_account = Account(account_name, password_string, email_address)
            new_check = AccountCheck(password_string, account_name, email_address, new_account)
            #Create Account with corresponding Check
            self.accounts.append(new_account)
            self.checks.append(new_check)

    def generate_random_string(self, size=10, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
        """Creates a random string of 'size' and from an optional set of given characters"""
        """Implentation grabbed from: stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python"""
        return ''.join(random.choice(chars) for _ in range(size))

    def print_accounts(self):
        """This method prints out an account"""
        print "Printing Account Test accounts:"
        print "Details: Username       Password"
        for a in self.accounts:
            a.printAccount()

    def log(self, check, checkType, accountName):
        """This method logs a test to a file"""
        if check == True:
            self.logFile.write("PASSED: %s %s\n" % (checkType, accountName))
        else:
            self.logFile.write("FAILED: %s %s\n" % (checkType, accountName))

    def logStat(self, numPass, numFail):
        """This method logs the statistics of a test run"""
        totalTests = numPass + numFail
        successToFail = numPass / totalTests
        successToFail *= 100
        self.logFile.write("Test Results: Passed: %d, Failed %d, Success Rate %f\n" % (numPass, numFail, successToFail))


class AccountCheck:
    """This class holds a representation of what an attributes an account should have"""
    def __init__(self, password, username, email, account):
        self.password = password
        self.username = username
        self.email = email
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

    def checkperson(self):
        account_email = self.account.get_person().get_email_address()
        reference_email = self.email
        return account_email == reference_email