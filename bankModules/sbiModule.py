# sbi_module.py

from bankModules.finance_module import Finance
from bankModules.goldLoan_module import GoldLoanManagementSystem
from bankModules.atm_module import ATM
from time import sleep

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
        self.email=input('Enter Email:')
        print('Your OTP for PAN', self.kyc, 'is', self.otp)
        while True:
            verify=int(input('Enter OTP sent to the PAN registered mobile number:\n'))
            if verify == self.otp:
                print('Verified!')
                break
            else:
                print('Wrong OTP please try again.')
        

    def printdetails(self):
        print(f'Welcome to HDFC Bank {self.name}')


class SBIFinance(Finance):
    def __init__(self):
        Finance.__init__(self)
        Details.__init__(self)

    def generate_emi(self,time_period,loan_amount,interest_rate):
        interest = (loan_amount*time_period*interest_rate) / 100
        future_value = interest + loan_amount

        emi = future_value / (time_period*12)
        return emi


    def loan_approval(self):
        # Details.get_details(self)
        print("Initializing loan approval system..")
        sleep(1)
        credit_score = int(input("Enter your credit score: "))
        income = float(input("Enter your annual income: $"))
        loan_amount = float(input("Enter the loan amount you are requesting: $"))
        time_period=int(input("Enter time period (years): "))

        sbi_interest_rate = 9.0

        if self.check_credit_score(credit_score) and self.check_loan_amount(loan_amount, income):
            print("Loan Approved")
            print(f"Monthly EMI: ${self.generate_emi(time_period,loan_amount,sbi_interest_rate)}")
            decision = int(input("Confirm loan request?\n1)Yes\n2)No\n"))
            if decision == 1:
                print(f"${loan_amount} has been credited into your bank account with SBI Bank at {sbi_interest_rate}% interest rate.")
                return loan_amount
            else:
                return -1
        else:
            print("Loan Denied")
            return -1

class SBIGoldLoanManagementSystem(GoldLoanManagementSystem):
    def __init__(self):
        # super().__init__()
        GoldLoanManagementSystem.__init__(self)
        Details.__init__(self)

    def create_loan(self, customer_name, gold_weight, carat):
        # Details.get_details(self)
        sbi_interest_rate = 11.0
        super().create_loan(customer_name, gold_weight, carat, sbi_interest_rate)
