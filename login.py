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

 #    login   
def Login():
     print("LOGIN")
     print("-"*30)
     username = input("Enter username: ")
     userpassword = input("enter login password:  ")
     
     user = User(username,userpassword)
     if user is None:
         print("please enter a valid name and password")
     else:
         user.login
         print(f"Welcome {username}!you are logged in")
         print("\n")
         print("-"*30)
         print('What would you like to do?')
         while True:
            print("Use this short codes : cc-create a new password , dc-display passwords, fc-find a specific credential,dd-delete credential,ex -exit" )
            print("-"*50)
            user_input = input("answer: ")
            if user_input == "cc":
                            choose= input("would you like a custom password or generated password?: c = custom and g = generated password: c/g?")
                            if  choose == "c":
                                    
                                    print("*"*60)
                                    print("Account name i.e Facebook")
                                    accountName= input()
                                    
                            
                                    print("User Name")
                                    user_name= input()
                            
                                                        
                                    print("password")
                                    user_password= input()