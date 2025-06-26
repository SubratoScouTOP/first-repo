user_id = ("subrato","aditya")
password = ("1234","234")
login_user = input("\nEnter your user ID to login: ")
login_pass = input("Enter your password: ")
if login_user == user_id[0]and login_pass == password[0]:
     print(" Login successful!")
elif login_user == user_id[1]and login_pass == password[1]:
     print(" Login successfull!")
else:
    print("invalid user id and passwords")
    

"""def check_password(username, password):
    for i in range(0, len(user_id)):
        if user_id[i] == username and password[i] == login_pass:
            return True
            
        
    return False

status = check_password(login_user, login_pass)
if (status):
    print("Logged in")
else:
    print("Wrong creds")"""