class Useraccount:
    def __init__(self, username, email, password):
        self._username = username
        self.email = email
        self.__password = password
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self):
        if self.email.count("@") > 1:
            raise ValueError("Invalid email")
    def change_password(self, old_password, new_password):
        if self._Useraccount__password != old_password:
            raise ValueError("Incorrect password")
        if len(new_password) < 6:
            raise ValueError("Password must be at least 6 characters")
        self._Useraccount__password = new_password