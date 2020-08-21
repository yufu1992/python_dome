import time

def login():
    return "login--------welcome hahahaha to our website ......tiem: %s" % time.ctime()

def register():
    return "register--------welcome hahahaha to our website ......tiem: %s" % time.ctime()

def profile():
    return "profile--------welcome hahahaha to our website ......tiem: %s" % time.ctime()


def application(file_name):
    if file_name == "/login.py":
        return login()
    elif file_name == "/register.py":
        return register()
    else:
        return "not found you page...."