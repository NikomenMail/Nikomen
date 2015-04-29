from applications.nikomen.modules.account_classes.account import Account
from gluon.tools import Mail
mail = Mail()
mail.settings.server = 'smtp.gmail.com:587'
mail.settings.sender = 'nikomentest@gmail.com'
mail.settings.login = 'nikomentest:nikomenTest1'

def index():
    """This controller handles the input fields for the index"""
    form = SQLFORM(db.login)

    if form.process().accepted:
        user_account = Account.login(form.vars.username, form.vars.password)
        if user_account != None:
            redirect(URL('email.html'))
        else:
            redirect(URL('index.html'))
    return dict(form=form)


def account_debug():
    """Debug function for listing accounts"""
    grid = SQLFORM.grid(db.auth_user)
    print grid
    return locals()

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


def create_redirect():
    """Redirects to the account creation page"""
    redirect(URL('create.html'))
    return dict()


def create():
    """This function handles the creation of a new account"""
    form = SQLFORM(db.register)
    if form.process().accepted:
        user_name = str(form.vars.username)
        password = str(form.vars.pswd)
        email = str(form.vars.email)
        e_pass = str(form.vars.empswd)
        new_account = Account(user_name, password, email, e_pass)
        new_account.save_account()
        redirect(URL('index.html'))

    elif form.errors:
        response.flash = 'form has errors'
        print db.auth_user
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)


def email():
    print "Made it to email handler!"
    mail.send(to=['jbrandt@nmt.edu'],
          subject='Hey John',
          # If reply_to is omitted, then mail.settings.sender is used
          reply_to='nikomenttest@gmail.com',
          message='This is most definitely not spam. Do not delete. This is the best feeling ever. It works*')
    return dict()


def user():
    """User Controller"""
    return dict(form=auth())

"""The following methods check for input validity for login information"""


def check_login(username, password):
    """This method checks the login for username and password validity"""
    if username == None or password == None:
        return False
    return True


def check_registration(fname, lastname, username, pswd, repswd, email, empswd, recemail, secQues, secAns):
    """print "First Name:", fname, "\nLast Name:", lastname, "\nPassword:", pswd, "\nCPassword:", repswd, "\nEmail:", email, \
        "\nEmail Password:", empswd, "\nRecovery Email:", recemail, "\nSecurity Question:", secQues, "\nSecurity Answer:", secAns"""
    if fname == None or lastname == None or username == None or pswd == None or email == None or empswd == None or recemail == None or secQues == None or secAns == None:
        print "Missing fields!"
        return False
    if pswd != repswd:
        print "Passwords do not match!"
        return False
    return True