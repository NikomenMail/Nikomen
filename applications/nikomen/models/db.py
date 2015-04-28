# -*- coding: utf-8 -*-
<<<<<<< HEAD
db = DAL('sqlite://webform.sqlite', fake_migrate_all=True)
# This defines the input fields for logging into an existing account
db.define_table('users',
=======
db = DAL('sqlite://webform.sqlite')
#This defines the input fields for logging into an existing account
db.define_table('login',
>>>>>>> eebf424a01d6c1ffe364136c734c44d0e2e9980d
    Field('username', requires=IS_NOT_EMPTY()),
    Field('password', requires=IS_NOT_EMPTY()))
#This defines the input fields for creating a new account
db.define_table('register',
    Field('fname', requires=IS_NOT_EMPTY()),
    Field('lastname', requires=IS_NOT_EMPTY()),
    Field('username', requires=IS_NOT_EMPTY()),
    Field('pswd', requires=IS_NOT_EMPTY(), type="password"),
    Field('repswd', requires=IS_NOT_EMPTY(), type="password"),
    Field('email', requires=IS_NOT_EMPTY()),
    Field('empswd', requires=IS_NOT_EMPTY(), type="password"),
    Field('recemail', requires=IS_NOT_EMPTY()),
    Field('secQues', requires=IS_NOT_EMPTY()),
    Field('secAns', requires=IS_NOT_EMPTY()))
