__author__ = 'angeloluna'

from abc import ABCMeta, abstractmethod


class Box(object):
    """abstract box object used to create all the boxes to store emails in."""
    __metaclass__ = ABCMeta

    name = "Box"  # name of the Box
    emails = [ ]  # list of emails
    location = "location"  # location???

    def retrieve_email(self):
        pass

    def filter(self, list):
        pass

    def sort(self, list):
        pass

    def view_list(self):
        pass

    def create_box(self):
        pass

