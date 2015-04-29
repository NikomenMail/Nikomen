# -*- coding: utf-8 -*-

db = DAL('sqlite://webform.sqlite', fake_migrate_all=True)
# This defines the input fields for logging into an existing account
db.define_table('login',
    Field('username', requires=IS_NOT_EMPTY()),
    Field('password', requires=IS_NOT_EMPTY(), type="password"))
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


from gluon.tools import Auth
auth = Auth(db, hmac_key=Auth.get_or_create_key())
auth.define_tables(username=True, signature=False)
auth.settings.profile_next = URL('email.html')
