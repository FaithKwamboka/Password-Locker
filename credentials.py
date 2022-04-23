class Credential:
    """
    class that creates instances of credentials
    """
    credentials_list = []

    def __init__(self, account_name, username, password):
        self.account_name = account_name
        self.username = username
        self.password = password

        credentials_list = []

    def save_credential(self):
        """
        This method saves user objects to the users list
        """
        self.new_credential.save_credential()
        Credential.credentials_list.append(self)
        
    def delete_credential(self):
        """
        This method deletes user objects from the users list
        """
        Credential.credentials_list.remove(self)

    @classmethod
    def find_by_account(cls,account_name):
    
        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return credential
    
    @classmethod
    def account_exists(cls,account_name):
        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return True
        return False

    # display Credential
    @classmethod
    def display_credential(cls):
        return cls.credentials_list

        
