user = input("Enter your user number: \n")
purpose = input('Enter "x" for Cash withdrawal or "y" for balance enquiry: \n')  
card_num = int(input("Enter your card number: \n")) 
pin = int(input("Enter your PIN: \n"))

class ATM(object):
    def __init__(self, atm_card_number, atm_pin_number):
        self.atm_card_number = atm_card_number
        self.atm_pin_number = atm_pin_number

    def CashWithdrawal(self):
        if user == user1 and pin == user1.atm_pin_number and card_num == user1.atm_card_number: 
            x = int(input("Enter amount"))
            print(x)
            print("You have withdrew $", x)
        elif user == user2 and pin == user2.atm_pin_number and card_num == user2.atm_card_number:
            x = int(input("Enter amount"))
            print(x)
            print("You have withdrew $", x)
        elif user == user3 and pin == user3.atm_pin_number and card_num == user3.atm_card_number:
            x = int(input("Enter amount"))
            print(x)
            print("You have withdrew $", x)
        elif user == user4 and pin == user4.atm_pin_number and card_num == user4.atm_card_number:
            x = int(input("Enter amount"))
            print(x)
            print("You have withdrew $", x)
        else:
            print("User not found in the data base")
        
    def BalanceEnquiry(self):
        if user == user1 and pin == user1.atm_pin_number and card_num == user1.atm_card_number: 
            print("amount: Balance")
        elif user == user2 and pin == user2.atm_pin_number and card_num == user2.atm_card_number:
            print("amount: Balance")
        elif user == user3 and pin == user3.atm_pin_number and card_num == user3.atm_card_number:
            print("amount: Balance")
        elif user == user4 and pin == user4.atm_pin_number and card_num == user4.atm_card_number:
            print("amount: Balance")
        else:
            print("User not found in the data base")

    if  purpose == "x":
        CashWithdrawal()
    elif purpose == "y":
        BalanceEnquiry()

user1 = ATM(000000000, 0000)
user2 = ATM(111111111, 1111)
user3 = ATM(222222222, 2222)
user4 = ATM(333333333, 3333)
user5 = ATM(444444444, 4444)

user1.CashWithdrawal()
user1.BalanceEnquiry()

user2.CashWithdrawal()
user2.BalanceEnquiry()

user3.CashWithdrawal()
user3.BalanceEnquiry()

user4.CashWithdrawal()
user4.BalanceEnquiry()
