__author__ = 'William'


class Checker:
    """This class checks for validty of input"""
    @staticmethod
    def check_login(username, password):
        if username == None or password == None:
            return False
        return True

    @staticmethod
    def check_registration(fname, lastname, pswd, repswd, email, empswd, recemail, secQues, secAns):
        if fname == None or lastname == None or pswd == None or email == None or empswd == None or recemail == None or secQues == None or secAns == None:
            return False
        if pswd != repswd:
            return False
        return True