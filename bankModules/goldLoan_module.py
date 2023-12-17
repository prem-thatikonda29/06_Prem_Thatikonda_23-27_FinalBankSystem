# gold Loan module

class Loan:
    def __init__(self, customer_name, gold_weight, carat, loan_amount, interest_rate):
        self.customer_name = customer_name
        self.gold_weight = gold_weight
        self.carat = carat
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.total_amount_due = loan_amount + (loan_amount * interest_rate / 100)
        self.is_closed = False

    def calculate_loan_amount(self):
        carat_scale = int(input("\n1)22k\n2)24k\nEnter carat: "))
        if carat_scale == 22:
            purity_factor = self.carat / 22
        elif carat_scale == 24:
            purity_factor = self.carat / 24

        return self.gold_weight * purity_factor * 100

    def make_payment(self, amount):
        if not self.is_closed:
            self.total_amount_due -= amount
            if self.total_amount_due <= 0:
                self.is_closed = True
                print("Loan fully repaid. Closed.")
                # self.loans.pop()

    def display_details(self):
        print(f"Customer: {self.customer_name}")
        print(f"Gold Weight: {self.gold_weight} grams")
        print(f"Carat: {self.carat}")
        print(f"Loan Amount: ${self.loan_amount}")
        print(f"Interest Rate: {self.interest_rate}%")
        print(f"Total Amount Due: ${self.total_amount_due}")
        print("Status: Closed" if self.is_closed else "Status: Open")


class GoldLoan(Loan):
    def __init__(self, customer_name, gold_weight, carat, loan_amount, interest_rate):
        super().__init__(customer_name, gold_weight, carat, loan_amount, interest_rate)
        self.total_amount_due = loan_amount + (loan_amount * interest_rate / 100)

    def calculate_loan_amount(self):
        carat_scale = int(input("1)18k\n2)22k\n3)24k\nEnter carat: "))
        if carat_scale == 18:
            purity_factor = self.carat / 18
        elif carat_scale == 22:
            purity_factor = self.carat / 22
        elif carat_scale == 24:
            purity_factor = self.carat / 24

        self.total_amount_due = self.loan_amount + (self.loan_amount * self.interest_rate / 100)
        return self.gold_weight * purity_factor * 100


class GoldLoanManagementSystem:
    def __init__(self):
        self.loans = []

    # def create_loan(self, customer_name, gold_weight, carat, loan_amount, interest_rate):
    def create_loan(self, customer_name, gold_weight, carat, interest_rate):
        loan_amount_calculated = self.calculate_loan_amount(gold_weight, carat)
        loan = GoldLoan(customer_name, gold_weight, carat, loan_amount_calculated, interest_rate)
        self.loans.append(loan)
        print(f"${loan_amount_calculated} loan requested successfully.")


    def calculate_loan_amount(self, gold_weight, carat):
        purity_factor = carat / 24
        return (gold_weight * purity_factor * 100) * 0.75


    def make_payment(self, customer_name):
        payment = float(input("Enter return payment: "))
        for loan in self.loans:
            if loan.customer_name == customer_name:
                loan.make_payment(payment)
                print(f"${payment} paid back")
                self.loans.remove(loan)
                return
        print("Customer not found or no active loan for the customer.")

    def display_loan_details(self, customer_name):
        for loan in self.loans:
            if loan.customer_name == customer_name:
                loan.display_details()
                return
        print("Customer not found or no active loan for the customer.")