# hdfc_module.py
from colorama import Fore, Style
from bankModules.finance_module import Finance
from bankModules.goldLoan_module import GoldLoanManagementSystem
from bankModules.atm_module import ATM
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

class Details:
    def get_details(self):
        import random
        print("Fetching user details..")
        sleep(1.5)
        self.name=input('Enter your name: ')
        self.id=random.randint(100,1000)
        self.kyc=input('Enter PAN number: ')
        self.otp=random.randint(1000,9999)
        while True:
            self.num=input('Enter Phone number:')
            if len(self.num)==10:
                break
            else:
                print('Invalid phone number try again.')
        print('Your OTP for PAN', self.kyc, 'is', self.otp)
        while True:
            verify=int(input('Enter OTP sent to the PAN registered mobile number:\n'))
            if verify == self.otp:
                print('Verified!')
                break
            else:
                print('Wrong OTP please try again.')
        self.email=input('Enter Email:')


    def printdetails(self):
        print(f'Welcome to HDFC Bank {self.name}')


class HDFCFinance(Finance):
    def __init__(self):
        # super().__init__()
        Finance.__init__(self)
        Details.__init__(self)


    def generate_emi(self,time_period,loan_amount,interest_rate):
        interest = (loan_amount*time_period*interest_rate) / 100
        future_value = interest + loan_amount

        emi = future_value / (time_period*12)
        return emi
    

    def loan_approval(self):
        # Details.get_details(self)
        print(TextColors.GREEN+"Initializing loan approval system.."+TextColors.RESET)
        sleep(1)
        credit_score = int(input("Enter your credit score: "))
        income = float(input("Enter your annual income: $"))
        loan_amount = float(input("Enter the loan amount you are requesting: $"))
        time_period=int(input("Enter time period (years): "))

        hdfc_interest_rate = 8.5

        if self.check_credit_score(credit_score) and self.check_loan_amount(loan_amount, income):
            print(TextColors.BLUE+"Loan Approved"+TextColors.RESET)
            print(f"Monthly EMI: ${self.generate_emi(time_period,loan_amount,hdfc_interest_rate)}")
            decision = int(input("Confirm loan request?\n1)Yes\n2)No\n"))
            if decision == 1:
                print(TextColors.YELLOW+f"${loan_amount}"+TextColors.RESET+ f" has been credited into your bank account with HDFC Bank at {hdfc_interest_rate}% interest rate.")
                return loan_amount
            else:
                return -1
        else:
            print("Loan Denied")
            return -1
        

class HDFCGoldLoanManagementSystem(GoldLoanManagementSystem):
    def __init__(self):
        # super().__init__()
        GoldLoanManagementSystem.__init__(self)
        Details.__init__(self)

    def create_loan(self, customer_name, gold_weight, carat):
        # Details.get_details(self)
        hdfc_interest_rate = 10.0
        super().create_loan(customer_name, gold_weight, carat, hdfc_interest_rate)
