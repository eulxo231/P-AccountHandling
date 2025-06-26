db = AccountDB()

# initial info
account_number = '1234'
account_password = '5678'
user_name = '강서안'
deposit = 1000000

res = db.Create(account_number, account_password, user_name, deposit)

account_number = '1235'
account_password = '1234'
user_name = '홍길동'
deposit = 1500000

res = db.Create(account_number, account_password, user_name, deposit)

while True:
    print("=== Bank Menu ===")
    print(" 1. Create ")
    print(" 2. Deposit")
    print(" 3. Withdraw")
    print(" 4. Remittance")
    print(" 5. Quit/Exit")
    print("=================")
    choice = int(input("Select an option: "))
    
    if choice == 1: 
        account_number = input("Enter account number: ")
        account_password = input("Enter password: ")
        user_name = input("Enter user name: ")
        deposit = int(input("Enter initial deposit amount: "))
        res = db.Create(account_number, account_password, user_name, deposit)
        print(res['msg'])

    if choice == 2:
        account_number = input("Enter account number")
        res = db.FindIndexByAccountNumber(account_number)

        if res['status'] == 'success':
            account_password = input("Enter password: ")
            account = db.account_list[res['index']]
            if account.account_password == account_password:
                amt = int(input("Enter amount of deposit: "))
                if amt >= 0:
                  res = db.Update(account_number, amt)
                  print("입금이 완료되었습니다")
                else:
                  print("입금액은 0보다 커야합니다")
            else:
                print("비밀번호 불일치")
        else:
           print(res['msg'])
    
    if choice == 3:
        account_number = input("Enter account number")
        res = db.FindIndexByAccountNumber(account_number)

        if res['status'] == 'success':
          account_password = input("Enter password: ")
          if account_password == db.account_list[res['index']].account_password:
              amt = int(input("Enter withdrawal amount: "))
              if amt >= 0:
                res = db.Update(account_number,-amt)
                if res['status'] == 'success':
                  print("출금이 완료되었습니다")
                else:
                  print(res['msg'])
              else:
                print("출금액은 0보다 커야합니다")
          else:
              print("비밀번호 불일치")
        else:
          print("계좌 없음")
    
    if choice == 4:
        account_number = input("Enter account number")
        res = db.FindIndexByAccountNumber(account_number)
        
        if res['status'] == 'success':
          account_password = input("Enter password: ")
          if account_password == db.account_list[res['index']].account_password:
            rec_acc = input("Enter recipient account number: ")
            res = db.FindIndexByAccountNumber(rec_acc)
            if res['status'] == 'success':
              amt = int(input("Enter amount to remit: "))
              res = db.Update(account_number, -amt)
              if res['status'] == 'success':
               db.Update(rec_acc, amt)
              else :
                print(res['msg'])
          else:
            print("비밀번호 불일치")
        else:
          print(res['msg'])
            
    
    if choice == 5:
        break

    db.Show()