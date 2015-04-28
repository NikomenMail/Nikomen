#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib

from applications.nikomen.modules.account_classes.person import Person


class Account:
    def __init__(self, username, password, email):
        print "Creating Account..."
        self.username = username
        self.password = password #Add actual non-string storage of passwords
        self.person = Person(name=username, email=email)

    def logout(self):
        # Save Object to file
        self.save_account()
        print "Implement Logout"

    @staticmethod
    def login(username, password):
        """This method logs a user in and returns their associated account, or None if nothing was found"""
        # Search for Account File credentials
        path = "../../../accounts/"
        input_name = hashlib.sha224(username)
        input_file = open(path + input_name, "r")
        account_name = input_file.readline()
        account_password = input_file.readline()
        address = input_file.readline()
        image_path = input_file.readline()
        # Check Password
        if password == account_password:
            login_account = Account(username=account_name, password=account_password, email=address)
            login_account.get_person().set_image_name(image_path)
        else:
            login_account = None
        return login_account

    def save_account(self):
        """Saves the account to a file"""
        path = "../../../accounts/"
        output_name = hashlib.sha224(self.username).hexdigest()
        output_file = open(path + output_name, "w")
        output_file.write(self.password + "\n")
        output_file.write(self.username + "\n")
        output_file.write(self.person.get_email_address() + "\n")
        output_file.write(self.person.getImageName() + "\n")
        output_file.close()
        return

    def delete(self, username, password):
        # Search for Account File credentials
        # Check password
        # Delete Account
        print "Implement Account deletion!"

    def edit_account(self, **kwargs):
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
        return self.username

    def get_password(self):
        """Probs make this method private and have it encapsulated with some authorized method"""
        return self.password

    def get_person(self):
        """Returns the person object associated with this account"""
        return self.person

    def print_account(self):
        print "\t", self.username, "\t", self.password

