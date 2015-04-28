from applications.nikomen.modules.Box import Email

__author__ = 'angeloluna'

from applications.nikomen.modules.Box.BoxChild import *

"""self, sAddr, rAddr, subject, message, attachment"""
a = Email("2@gmail.com", "rAddr@gmail.com", "a Test Email 2", "this is a test message", 0)
b = Email("3@hotmail.com", "rAddr@gmail.com", "b Test Email 3", "this is a test message", 0)
c = Email("1@gmail.com", "rAddr@gmail.com", "c Test Email 1", "this is a test message", 0)

inbox = Inbox()
drafts = Drafts()
sent = Sent()
trash = Trash()

inbox.add_email(a)
inbox.add_email(b)
inbox.add_email(c)

print "PRINT INBOX\n"
inbox.display()

print "\nPRINT DRAFTS\n"
drafts.display()


print "\nSORT BY SUBJECT\n"
inbox.sort(1, False)
inbox.display()

print "\nSORT BY SENDER\n"
inbox.sort(2, False)
inbox.display()

print "\nSORT BY DATE\n"
inbox.sort(0, False)
inbox.display()

print "\nFILTER BY SENDER\n"
inbox.filter(1, "@gmail")

print "\nFILTER BY SUBJECT\n"
inbox.filter(0, "b Test Email 3")


print "\nWRITE EMAIL AND MOVE DRAFT\n"
inbox.save_draft(Email.write("1@gmail.com", "rAddr@gmail.com", "Test Write", "this is a test write", 0), drafts)
drafts.display()