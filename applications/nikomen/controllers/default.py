from applications.nikomen.modules.account_classes.account import Account


def index():
    form = SQLFORM(db.login)
    if form.process().accepted:
        print "Logging in user"
        user_name = str(form.vars.username)
        password = str(form.vars.password)
        print password
        print "Attempting Login with:", user_name, password
        user = auth.login_bare(user_name, password)
        print "Checking login status"
        if user == False:
            print "Incorrect User login"
            redirect(URL('index.html'))
            return dict(form=form)
        else:
            print "Found User!"
            redirect(URL('email.html'))
    return dict(form=form)


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


def login_function():
    form = SQLFORM(db.users)
    if form.process().accepted:
        print "Checking Credentials"
        IS_IN_DB(db, db.auth_user.username)
    return dict(form=form)


def create_redirect():
    redirect(URL('create.html'))
    return dict()


def create():
    """This function handles the creation of a new account"""
    form = SQLFORM(db.register)
    if form.process().accepted:
        print "Creating account!"
        db.auth_user.insert(
            username=str(form.vars.username),
            password=str(form.vars.pswd),
            email=str(form.vars.email),
            first_name=str(form.vars.fname),
            last_name=str(form.vars.lastname),
        )
        print "Created Account"
        redirect(URL('index.html'))

    elif form.errors:
        response.flash = 'form has errors'
        print db.auth_user
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)


def create_function():
    #print "Creating account for realz"
    form = SQLFORM(db.register)
   # print request.vars
    check = check_registration(request.vars.fname, request.vars.lastname, request.vars.username, request.vars.pswd,
                               request.vars.repswd, request.vars.email, request.vars.empswd, request.vars.recemail,
                               request.vars.secQues, request.vars.secAns)
    if check:
        print "Registration passed!"
        new_account = Account(request.vars.username, request.vars.pswd, request.vars.email)
        print "Account Username:", new_account.get_username()
        print "Account Password:", new_account.get_password()
        print "Email address:", new_account.get_person().get_email_address()
        redirect(URL('email.html'))
        return dict(form=form)
    else:
        print "Registration rejected!"
        redirect(URL('create.html'))
    return dict()


def email():
    print db.register
    return dict()


def user():
    """User Controller"""
    return dict(form=auth())

"""The following methods check for input validity for login information"""


def check_login(username, password):
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