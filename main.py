# main.py
import os
from sys import platform
from colorama import Fore, Style
from bankModules.hdfcModule import *
from bankModules.sbiModule import *
from bankModules.atm_module import *
from time import sleep

class TextColors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'


print(TextColors.GREEN+"Choose your bank:"+TextColors.RESET)
print("1. HDFC Bank")
print("2. SBI Bank")
bank_choice = int(input("> "))

if bank_choice == 1:
    class HDFCBankCustomer(HDFCFinance, HDFCGoldLoanManagementSystem, ATM,Details):
        def __init__(self):
            HDFCFinance.__init__(self)
            HDFCGoldLoanManagementSystem.__init__(self)
            ATM.__init__(self)
            Details.__init__(self)

elif bank_choice == 2:
    class SBIBankCustomer(SBIFinance, SBIGoldLoanManagementSystem, ATM,Details):
        def __init__(self):
            SBIFinance.__init__(self)
            SBIGoldLoanManagementSystem.__init__(self)
            ATM.__init__(self)
            Details.__init__(self)

def clear_terminal():
    os.system('clear')

def main():
    if bank_choice == 1:
        bank_customer = HDFCBankCustomer()
        print(TextColors.YELLOW+"------🙏🏼Welcome to HDFC Bank🙏🏼------"+TextColors.RESET)
    elif bank_choice == 2:
        bank_customer = SBIBankCustomer()
        print(TextColors.YELLOW+"------🙏🏼Welcome to SBI Bank🙏🏼------"+TextColors.RESET)
    else:
        print(TextColors.RED+"Invalid choice. Exiting."+TextColors.RESET)
        return

    bank_customer.get_details()


    while True:
        print(TextColors.GREEN+"\nMenu:"+TextColors.RESET)
        print("1. Investment")
        print("2. Loan Approval")
        print("3. Gold Loans")
        print("4. Display Loan Details")
        print("5. ATM Services")
        print("6. Exit")

        choice = int(input(TextColors.PURPLE+"Enter your choice: "+TextColors.RESET))

        if choice == 1:
            clear_terminal()
            print(TextColors.GREEN+"INVESTMENT PLANNER."+TextColors.RESET,end="")
            sleep(0.3)
            print(".",end="")
            sleep(0.3)
            print(".")
            bank_customer.investment()
        elif choice == 2:
            clear_terminal()
            approved_loan_amount = bank_customer.loan_approval()
            if approved_loan_amount != -1:
                bank_customer.balance_in_acc += approved_loan_amount
        elif choice == 3:
            clear_terminal()
            decision = int(input(TextColors.YELLOW+"1)Request loan\n2)Return payment\n"+TextColors.RESET))
            if decision == 1:
                if len(bank_customer.loans)==0:
                    gold_weight = float(input("Enter gold weight(g): "))
                    carat = int(input("Enter carat: "))
                    bank_customer.create_loan(bank_customer.name, gold_weight, carat)
                else:
                    print(TextColors.YELLOW+"Loan unavailable. Please repay existing loans."+TextColors.RESET)
            elif decision == 2:
                bank_customer.make_payment(bank_customer.name)
        elif choice == 4:
            clear_terminal()
            bank_customer.display_loan_details(bank_customer.name)
        elif choice == 5:
            clear_terminal()
            while True:
                print("\nATM Services:")
                print("1. Generate Green Pin")
                print("2. Change CARD password")
                print("3. Account Details (withdraw, deposit, check balance)")
                print(TextColors.RED+"4. Exit ATM Services"+TextColors.RESET)

                atm_choice = int(input("Enter your choice: "))

                if atm_choice == 1:
                    bank_customer.green_pin()
                elif atm_choice == 2:
                    bank_customer.change_pin()
                elif atm_choice == 3:
                    print(TextColors.GREEN+"Account..."+TextColors.RESET)
                    sleep(0.8)
                    while True:
                        print("1. Check Balance")
                        print("2. Deposit Amount")
                        print("3. Withdraw Amount")
                        print("4. Exit ATM Services")
                        
                        atm_options = int(input("Enter your choice: "))

                        if atm_options == 1:
                            bank_customer.balance_inquiry()
                        elif atm_options == 2:
                            bank_customer.deposit_in_acc()
                        elif atm_options == 3:
                            bank_customer.withdraw()
                        elif atm_options == 4:
                            print(TextColors.RED+"Exiting ATM Services."+TextColors.RESET)
                            clear_terminal()
                            break
                        else:
                            print(TextColors.RED+"Invalid! Please choose between the given numbers!"+TextColors.RESET)
                elif atm_choice == 4:
                    print(TextColors.RED+"Exiting ATM Services."+TextColors.RESET)
                    clear_terminal()
                    break
                else:
                    print(TextColors.RED+"Invalid choice! Please choose again."+TextColors.RESET)
        elif choice == 6:
            print(TextColors.RED+"Exiting program. Goodbye!"+TextColors.RESET)
            break
        else:
            print(TextColors.RED+"Invalid choice. Please choose again."+TextColors.RESET)


if __name__ == "__main__":
    main()
