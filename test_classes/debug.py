#!/usr/bin/python2.7

from emailGenerator import EmailGenerator

#Stuff to know
# Send To: nikomenTest@gmail.com
# Send From: nikomenClient@gmail.com
generator = EmailGenerator('yolo@swag.org', 'nikomen@wat.com')
generator.printEmail()

generator.generateMessage(paragraph=10)
generator.printEmail()

generator.emailToFile('test')
