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