from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    
    @abstractmethod
    def make_payment(self, amount):
        pass

class CreditCard(PaymentMethod):
    def __init__(self, card_number, card_holder, expiry_date, cvv):
        self.card_number = card_number
        self.card_holder = card_holder
        self.expiry_date = expiry_date
        self.cvv = cvv
    
    def make_payment(self, amount):
        print(f"Processing credit card payment of {amount:.2f} for {self.card_holder} using card {self.card_number}.")


class BankTransfer(PaymentMethod):
    def __init__(self, account_number, bank_name, swift_code):
        self.account_number = account_number
        self.bank_name = bank_name
        self.swift_code = swift_code
    
    def make_payment(self, amount):
        print(f"Processing bank transfer payment of {amount:.2f} from account {self.account_number} at {self.bank_name}.")

class EWallet(PaymentMethod):
    def __init__(self, wallet_id, wallet_provider):
        self.wallet_id = wallet_id
        self.wallet_provider = wallet_provider
    
    def make_payment(self, amount):
        print(f"Processing e-wallet payment of {amount:.2f} using wallet {self.wallet_id} from {self.wallet_provider}.")

class PaymentProcessor:
    def __init__(self):
        self.payment_methods = []
    
    def add_payment_method(self, payment_method):
        self.payment_methods.append(payment_method)
    
    def process_payment(self, payment_method, amount):
        if payment_method in self.payment_methods:
            payment_method.make_payment(amount)
        else:
            print("Payment method not available.")

credit_card = CreditCard("1234 5678 9101 1231", "David Rudenko", "12/26", "123")
bank_transfer = BankTransfer("9876543210", "Global Bank", "GB123456")
e_wallet = EWallet("wallet123", "PayPal")

payment_processor = PaymentProcessor()
payment_processor.add_payment_method(credit_card)
payment_processor.add_payment_method(bank_transfer)
payment_processor.add_payment_method(e_wallet)

payment_processor.process_payment(credit_card, 100.0)
payment_processor.process_payment(bank_transfer, 250.0)
payment_processor.process_payment(e_wallet, 50.0)
