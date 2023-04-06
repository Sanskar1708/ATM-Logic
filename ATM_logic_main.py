class ATM(object):
    def __init__(self, atm_card_number, atm_pin_number):
        self.atm_card_number = atm_card_number
        self.atm_pin_number = atm_pin_number
    

    def CashWithdrawal(self,user,pin,card_num):
        if  user == 'user1' and pin == 0000 and card_num == 000000000: 
            x = int(input("Enter amount"))
            print(x)
            print("You withdrew $", x)
        elif user == 'user2' and pin == 1111 and card_num == 111111111:
            x = int(input("Enter amount"))
            print(x)
            print("You withdrew $", x)
        elif user == 'user3' and pin == 2222 and card_num == 222222222:
            x = int(input("Enter amount"))
            print(x)
            print("You withdrew $", x)
        elif user == 'user4' and pin == 3333 and card_num == 333333333:
            x = int(input("Enter amount"))
            print(x)
            print("You withdrew $", x)
        else:
            print("User not found in the data base")
        
    def BalanceEnquiry(self, user,pin,card_num):
        if user == 'user1' and pin == 0000 and card_num == 000000000: 
            print("amount: Balance")
        elif user == 'user2' and pin == 1111 and card_num == 111111111:
            print("amount: Balance")
        elif user == 'user3' and pin == 2222 and card_num == 222222222:
            print("amount: Balance")
        elif user == 'user4' and pin == 3333 and card_num == 333333333:
            print("amount: Balance")
        else:
            print("User not found in the data base")

    

def main():
    user1 = ATM(000000000,0000);
    user2 = ATM(111111111,1111);
    user3 = ATM(222222222,2222);
    user4 = ATM(333333333,3333);
    
    user = input("Enter your user number: \n")
    purpose = input('Enter "x" for Cash withdrawal or "y" for balance enquiry: \n')  
    card_num = int(input("Enter your card number: \n")) 
    pin = int(input("Enter your PIN: \n"))
    
   
    if user == 'user1' and pin == 0000 and card_num == 000000000: 
            print("User1 found in the data base")
            if  purpose == "x":
                user1.CashWithdrawal(user,pin,card_num)
            elif purpose == "y":
                user1.BalanceEnquiry(user,pin,card_num)
    elif user == 'user2' and pin == 1111 and card_num == 111111111:
            print("User2 found in the data base")
            if  purpose == "x":
                user2.CashWithdrawal(user,pin,card_num)
            elif purpose == "y":
                user2.BalanceEnquiry(user,pin,card_num)
    elif user == 'user3' and pin == 2222 and card_num == 222222222:
            print("User3 found in the data base")
            if  purpose == "x":
                user3.CashWithdrawal(user,pin,card_num)
            elif purpose == "y":
                user3.BalanceEnquiry(user,pin,card_num)
    elif user == 'user4' and pin == 3333 and card_num == 333333333:
            print("User4 found in the data base")
            if  purpose == "x":
                user4.CashWithdrawal(user,pin,card_num)
            elif purpose == "y":
                user4.BalanceEnquiry(user,pin,card_num)
    else:
            print("User not found in the data base")
    
    


if __name__ == "__main__":
    main()