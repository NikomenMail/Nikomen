# -*- coding: utf-8 -*-
db = DAL('sqlite://webform.sqlite')
#This defines the input fields for logging into an existing account
db.define_table('login',
    Field('username', requires=IS_NOT_EMPTY()),
    Field('password', requires=IS_NOT_EMPTY()))
#This defines the input fields for creating a new account
db.define_table('register',
    Field('fname', requires=IS_NOT_EMPTY()),
    Field('lastname', requires=IS_NOT_EMPTY()),
    Field('username', requires=IS_NOT_EMPTY()),
    Field('pswd', requires=IS_NOT_EMPTY()),
    Field('repswd', requires=IS_NOT_EMPTY()),
    Field('email', requires=IS_NOT_EMPTY()),
    Field('empswd', requires=IS_NOT_EMPTY()),
    Field('recemail', requires=IS_NOT_EMPTY()),
    Field('secQues', requires=IS_NOT_EMPTY()),
    Field('secAns', requires=IS_NOT_EMPTY()))