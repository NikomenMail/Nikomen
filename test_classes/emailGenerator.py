#!/usr/bin/python2.7

import loremipsum

class EmailGenerator:
    """This class generates emails to test the Email Client"""
    def __init__(self, senderAddress, recipientAddresses, **kwargs):
        """This method intializes an email generator class"""
        #Initialize Lists for instance
        self.recipientAddresses = []
        self.ccAddresses = []
        self.bccAddresses = []
        self.message = []
        #set specified addresses
        self.senderAddress = senderAddress
        self.recipientAddresses.append(recipientAddresses)
        ###Further assignments are optional
        if ('ccAddresses' in kwargs):
            self.ccAddresses.append(kwargs['ccAddresses'])
        if ('bccAddresses' in kwargs):
            self.bccAddresses.append(kwargs['bccAddresses'])
        #Set the subject
        if ('subject' in kwargs):
            self.subject = kwargs['subject']
        #Get the Message
        if ('message' in kwargs):
            self.message = kwargs['message']

    def generateMessage(self, **kwargs):
        """This method generates a lorem ipsum message of a specified size"""
        numParagraphs = kwargs['paragraph']
        if (numParagraphs < 1):
            print 'Warning! Number of paragraphs must be over than 0. Defaulting to 1...'
            numParagraphs = 1
        self.message = loremipsum.get_paragraphs(numParagraphs)
    
    def printEmail(self):a
        """For debugging purposes, this method prints a generator's attributes to standard out"""
        print "Sender:", self.senderAddress
        print "Recipients:", self.recipientAddresses
        print "cc:", self.ccAddresses
        print "bcc:", self.bccAddresses
        print "message:", self.message

    def emailToFile(self, filename):
        """This method prints a generated email to a file for unit comparison"""
        path = './emailTests/' + filename
        out = open(path, "w")
        out.write('===SENDER ADDRESS===\n')
        out.write(self.senderAddress + '\n')
        out.write('===RECIPIENT ADDRESSES===\n')
        for recipient in self.recipientAddresses:
            out.write(recipient + '\n')
        out.write('===CC ADDRESSES===\n')
        for cc in self.ccAddresses:
            out.write(cc + '\n')
        out.write('===BCC ADDRESSES===\n')
        for bcc in self.bccAddresses:
            out.write(bcc + '\n')
        out.write('===MESSAGES===\n')
        for message in self.message:
            out.write(message)

    #Define Setters/Getters/Removers
    def setSender(self, senderAddress):
        self.senderAddress = senderAddress
    
    def setSubject(self, subject):
        self.subject = subject
    
    def addRecipient(self, recipient):
        self.recipientAddresses.append(recipient)
    
    def addCC(self, ccAddress):
        self.ccAddresses.append(ccAddress)
    
    def addBCC(self, bccAddress):
        self.bccAddresses.append(bccAddress)
    
    def removeRecipient(self, recipient):
        self.recipientAddresses.remove(recipient)
    
    def removeCC(self, ccAddress):
        self.ccAddresses.remove(ccAddress)
    
    def removeBCC(self, bccAddress):
        self.ccAddresses.remove(bccAddress)
    
    def getSender(self):
        return self.senderAddress
    
    def getRecipients(self):
        return self.recipientAddresses
    
    def getCC(self):
        return self.ccAddresses
    
    def getBCC(self):
        return self.bccAddresses
    
    def getSubject(self):
        return self.subject

