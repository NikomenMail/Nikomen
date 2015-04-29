#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib

from applications.nikomen.modules.account_classes.person import Person


class Account:
    """This class handles account creation, alteration, and destruction"""
    def __init__(self, username, password, email, email_password):
        self.username = username
        self.password = password
        self.person = Person(name=username, email=email)
        self.email_password = email_password

    def logout(self):
        """This method logs a user out"""
        """Still requires implementation"""
        # Save Object to file
        self.save_account()
        print "Implement Logout"

    @staticmethod
    def login(username, password):
        """This method logs a user in and returns their associated account, or None if nothing was found"""
        # Search for Account File credentials
        print username, password
        path = "./accounts/"
        """hash input name"""
        input_name = str(hashlib.sha224(username).hexdigest())
        print input_name
        try:
            input_file = open(path + input_name, "r")
        except IOError:
            print "File not found!"
            return None
        """read in file"""
        print "reading file"
        account_password = input_file.readline().rstrip('\n')
        account_name = input_file.readline().rstrip('\n')
        address = input_file.readline().rstrip('\n')
        e_password = input_file.readline().rstrip('\n')
        image_path = input_file.readline().rstrip('\n')
        # Check Password
        if password == account_password:
            print "Passwords matched!"
            login_account = Account(username=account_name, password=account_password, email=address, email_password=e_password)
            login_account.get_person().set_image_name(image_path)
        else:
            login_account = None
        return login_account

    def save_account(self):
        """Saves the account to a file"""
        path = "./accounts/"
        output_name = str(hashlib.sha224(self.username).hexdigest())
        final_path = path + output_name
        print self.password, self.username
        output_file = open(path + output_name, "w")
        output_file.write(self.password + "\n")
        output_file.write(self.username + "\n")
        output_file.write(self.person.get_email_address() + "\n")
        output_file.write(self.email_password + "\n")
        output_file.write(self.person.get_image_name())
        output_file.close()
        return

    def delete(self, username, password):
        """This method deletes an account"""
        """Still requires implementation"""
        # Search for Account File credentials
        # Check password
        # Delete Account
        print "Implement Account deletion!"

    def edit_account(self, **kwargs):
        """Edits an account's settings"""
        """Still requires implementation"""
        # Implement various methods to change various parts of the Account
        # Change username
        # Change password
        # Change image
        # Edit addresses
        print "Implment, username, password, image, and address change methods"

    def set_user_name(self, new):
        """Sets the account's username"""
        self.person.set

    def get_username(self):
        """Returns the username of an account"""
        return self.username

    def get_password(self):
        """Probs make this method private and have it encapsulated with some authorized method"""
        return self.password

    def get_e_password(self):
        """Returns the password for the account's email service"""
        return self.email_password

    def get_person(self):
        """Returns the person object associated with this account"""
        return self.person

    def print_account(self):
        """Debug method for printing an account"""
        print "\t", self.username, "\t", self.password

