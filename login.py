from user import User
import run
from random import randint
from password import generate_password

def register():
    print("REGISTER")
    print("-"*30)
    username = input("enter username:  ")
    userpassword = input("enter password:  ")
    confirm_pass=input("confirm password:   ")
    
    #  validation
    if userpassword == confirm_pass:
        user = User(username,userpassword)
        user.save_user
        print(f"Welcome {username}!you are now registered")
        print("Lets Login")
        
    else:
       repeat= input("Something has gone wrong. Try again. y/n")
       if repeat == "y":
           print(register())
       else:
           print(exit())