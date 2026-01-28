from pwdlib import PasswordHash


password_hash = PasswordHash.recommended()

class Hash():

    @staticmethod
    def make(password):
        return password_hash.hash(password)
    
    @staticmethod
    def check(password, hashed_password):
        return password_hash.verify(password, hashed_password)
