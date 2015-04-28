__author__ = 'angeloluna'

class TestClass:
    __a = 0
    __b = 0
    __c = 0
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def printValues(self):
        print self.a,self.b,self.c

    def getA(self):
        return self.a

    def setA(self, a):
        self.a = a






