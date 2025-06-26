class Account:
  def __init__(self):
    self.account_number = ""
    self.account_password = ""
    self.user_name = ""
    self.deposit = 0

  def InitAccount(self, account_num, account_password, user_name, deposit):
    self.account_number = account_num
    self.account_password = account_password
    self.user_name = user_name
    self.deposit = deposit

  def Show(self):
    print({
        'account number': self.account_number,
        'account password' : self.account_password,
        'user name' : self.user_name,
        'deposit' : self.deposit
    })