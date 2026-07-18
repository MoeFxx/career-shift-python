username = input("Username")
password = input("Password")
def access (username,password):
    if username == "ftwmido" and password == "1231":
        print ("Access granted")
    else:
        print("Access denied")
access(username,password)