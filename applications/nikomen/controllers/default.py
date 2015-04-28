from input_check import Checker


def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))


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
    form = SQLFORM(db.login)
    username = request.vars.username
    password = request.vars.password
    print "Username:", username
    print "Password:", password
    if Checker.check_login(username, password):
        print "Valid checks"

    return dict(form=form)

def create_redirect():
    redirect(URL('create.html'))
    return dict()

def create():
    print "Creating account"
    form = SQLFORM(db.login)
    return dict()

def create_function():
    print "Creating account for realz"
    form = SQLFORM(db.register)
    print request.vars
    return dict()