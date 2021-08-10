class Bank_account: 
  @property
  def password(self):
    return 'Password: 123'
  
andy = Bank_account()
print(andy.password)

#If we try to change andy.password, an error will occur, which is @property 's characteristic

class Bank_acount:
    def __init__(self):
        self._password = '0000'

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @password.deleter
    def password(self):
        del self._password
        print('del complite')
        
andy = Bank_acount()
print(andy.password)
andy.password = '1234'
print(andy.password)
del andy.password
print(andy.password)