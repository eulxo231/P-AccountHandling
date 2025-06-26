import Account

"""
CRUD
"""
class AccountDB:
  def __init__(self):
    self.account_list = []

  def Show(self):
    for account in self.account_list: account.Show()

  def Create(self, account_number, account_password, user_name, deposit):
    res = self.FindIndexByAccountNumber(account_number)
    if res['status'] == 'fail':
        newAccount = Account()
        newAccount.InitAccount(account_number, account_password, user_name, deposit)
        self.account_list.append(newAccount) # list append
        return {'status': 'success'}
      
    return {'status': 'fail', 'msg': '중복된 계좌 생성'}

  def FindIndexByAccountNumber(self, account_number):
    for i in range(len(self.account_list)):
      if account_number == self.account_list[i].account_number:
        return {'status':'success', 'index': i}
    return {'status' : 'fail'}
  
  def Update(self, account_number, amount):
    res = self.FindIndexByAccountNumber(account_number)
    
    if res['status'] == 'success':
      if self.account_list[res['index']].deposit + amount >= 0:
        self.account_list[res['index']].deposit += amount
        return {'status':'success'}
      else:
        return {'status':'fail', 'msg':'잔액 부족'}
    else:
      return {'status':'fail', 'msg':'계좌가 존재하지 않음'}