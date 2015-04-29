from applications.nikomen.modules.account_classes.account import Account
from applications.nikomen.modules.account_classes.person import Person
from applications.nikomen.modules.Box.Email import Email
from gluon.tools import Mail
mail = Mail()
mail.settings.server = 'smtp.gmail.com:587'
mail.settings.sender = 'nikomentest@gmail.com'
mail.settings.login = 'nikomentest:nikomenTest1'
user_account = None


def index():
    """This controller handles the input fields for the index"""
    form = SQLFORM(db.login)

    if form.process().accepted:
        user_account = Account.login(form.vars.username, form.vars.password)
        if user_account != None:
            mail = Mail()
            mail.settings.server = 'smtp.gmail.com:587'
            mail.sender = user_account.get_person().get_email_address()
            mail.settings.login = user_account.username + ":" + user_account.get_e_password()
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
    """represents a user session"""
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
    sender_addr = mail.settings.sender
    recipient_addr = 'jbrand@nmt.edu'
    cc_addr = ['ineal@nmt.edu', 'smanzana@nmt.edu']
    mail_subject = 'An Email Subject'
    mail_message = 'It works. It freaking works***'
    new_email = Email.write(sender_addr, recipient_addr, mail_subject, mail_message, None)
    attachment = mail.Attachment('./attach_tests/image.png', content_id="photo")
    mail.send(
        new_email.rAddr,
        new_email.subject,
        new_email.message,
        cc=cc_addr,
        attachments=attachment
    )
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