#!/usr/bin/env python3.8
from credentials import Credential
import login
 
#create credential

def create_credentials(user_name,accountName,user_password):
        new_credential = Credential(user_name,accountName,user_password)
        return new_credential

# save credential
def save_credentials(credential):
        credential.save_credential()
        
# delete credential
def del_credential(credential):
        credential.delete_credential()
        
def find_credential(account_name):
        return Credential.find_by_account(account_name)

def check_exixting_credentials(account_name):
        return Credential.credential_exist(account_name)

def  display_credentials():
        return Credential.display_credential()