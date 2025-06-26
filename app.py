import Account
import AccountDB

from AccountDB import AccountDB

#TODO: Create menu, and print it infinitely
# 1. Create 
# 2. Deposit
# 3. Withdraw
# 4. Remittance
# 5. Quit/Exit

db = AccountDB

while True:
    print("===Bank Menu===")
    print(" 1. Create ")
    print(" 2. Deposit")
    print(" 3. Withdraw")
    print(" 4. Remittance")
    print(" 5. Quit/Exit")

    choice = int(input("Select an option: "))
    
    if choice == 1: 
        account_number = input("Enter account number: ")
        account_password = input("Enter password: ")
        user_name = input("Enter user name: ")
        deposit = int(input("Enter initial deposit amount: "))
        res = db.Create(account_number, account_password, user_name, deposit)
        print(res)

    if choice == 2:
        account_number = input("Enter account number")
        res = db.FindIndexByAccountNumber(account_number)
        if res['status'] == 'fail':
            print("계좌 없음")
        else:
            account_password = input("Enter password: ")
            account = db.account_list[res['index']]
            if account.account_password == account_password:
                amt = int(input("Enter amount of deposit: "))
                res = db.Update(account_number, amt)
                print(res)
            else:
                print("비밀번호 불일치")
    
    if choice == 3:
        account_number = input("Enter account number")
        res = db.FindIndexByAccountNumber(account_number)
        if res['status'] == 'fail':
            print("계좌 없음")
        else:
            account_password = input("Enter password: ")
            account = db.account_list[res['index']]
            if account.account_password == account_password:
                amt = int(input("Enter withdrawal amount: "))
                res = db.Update(account_number,-amt)
                print(res)
            else:
                print("비밀번호 불일치")
    
    if choice == 4:
        account_number = input("Enter account number")
        res = db.FindIndexByAccountNumber(account_number)
        if res['status'] == 'fail':
            print("계좌 없음")
        else:
            account_password = input("Enter password: ")
            account = db.account_list[res['index']]
            if account.account_password == account_password:
                rec_acc = input("Enter recipient account number: ")
                amt = int(input("Enter amount to remit: "))
                res = db.Update(account_number, -amt)
                if res['status'] == 'success':
                    res = db.Update(rec_acc, amt)
                    print("Remittance successful.")
                else:
                    print("Insuffient amount of credits to remit.")
            else:
                print("비밀번호 불일치")
    
    if choice == 5:
        break
        
