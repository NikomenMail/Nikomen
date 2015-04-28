from applications.nikomen.modules.Box import TestClass

__author__ = 'angeloluna'
a = 5
b = 15
c = 25

o = TestClass(a,b,c)
o.printValues()
o.setA(45)
o.printValues()
o.a = 50
o.printValues()


