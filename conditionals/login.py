# Apply these rules:
# - If the username is "admin" and the password is "python123", print "Login successful".
# - If the username is correct but the password is wrong, print "Incorrect password".
# - Otherwise, print "Invalid username".



def main():
    username = input("Enter username: ")
    password = input("Enter password: ")
    admin_login(username,password);

def admin_login(username,password):
    if username=="admin" and password=="python123":
        print("login successful")
    elif username=="admin":
        print("incorrect password ")
    else:
        print("invaild user");


main()