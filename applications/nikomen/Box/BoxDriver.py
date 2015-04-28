__author__ = 'angeloluna'

from BoxChild import Inbox
from Email import Email
"""self, sAddr, rAddr, subject, message, attachment"""
a = Email("2@gmail.com", "rAddr@gmail.com", "a Test Email 2", "Dear person 1,\nThis is a Test Message\n\nFrom \n-a person", 0)
b = Email("3@gmail.com", "rAddr@gmail.com", "b Test Email 3", "Dear person 2,\nThis is a Test Message\n\nFrom \n-a person", 0)
c = Email("1@gmail.com", "rAddr@gmail.com", "c Test Email 1", "Dear person 3,\nThis is a Test Message\n\nFrom \n-a person", 0)

inbox = Inbox()

inbox.retrieve_email(a)
inbox.retrieve_email(b)
inbox.retrieve_email(c)

inbox.display()

print "\nSORT BY SUBJECT\n"
inbox.sort(1)
inbox.display()

print "\nSORT BY SENDER\n"
inbox.sort(2)
inbox.display()

print "\nSORT BY DATE\n"
inbox.sort(0)
inbox.display()

print "\nFILTER BY SENDER\n"
inbox.filter(1, "2@gmail.com")

print "\nFILTER BY SUBJECT\n"
inbox.filter(0, "b Test Email 3")
