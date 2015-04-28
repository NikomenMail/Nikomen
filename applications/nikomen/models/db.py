# -*- coding: utf-8 -*-
db = DAL('sqlite://webform.sqlite', fake_migrate_all=True)
# This defines the input fields for logging into an existing account
db.define_table('users',
    Field('username', requires=IS_NOT_EMPTY()),
    Field('password', requires=IS_NOT_EMPTY()))
# This defines the input fields for creating a new account
db.define_table('register',
    Field('fname', requires=IS_NOT_EMPTY()),
    Field('lname', requires=IS_NOT_EMPTY()),
    Field('username', requires=IS_NOT_EMPTY()),
    Field('pswd', requires=IS_NOT_EMPTY(), type="password"),
    Field('repswd', requires=IS_NOT_EMPTY(), type="password"),
    Field('email', requires=IS_NOT_EMPTY()),
    Field('empswd', requires=IS_NOT_EMPTY(), type="password"),
    Field('recemail', requires=IS_NOT_EMPTY()),
    Field('secQues', requires=IS_IN_SET(['What is your birthplace?', 'What is your favorite color?', 'Will you remember this security question?'])),
    Field('secAns', requires=IS_NOT_EMPTY()))

# Settings for User Access Control
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Service, PluginManager

auth = Auth(db)
service = Service()
plugins = PluginManager()
## create all tables needed by auth if not custom tables
auth.define_tables(username=True, signature=False)
"""
## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else myconf.take('smtp.sender')
mail.settings.sender = myconf.take('smtp.sender')
mail.settings.login = myconf.take('smtp.login')"""