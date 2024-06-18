class Bank:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def get_balance(self):
        return self.balance

    def set_balance(self, new_balance):
        self.balance = new_balance


class ExtendedBank(Bank):
    def __init__(self, name, account_number, balance):
        super().__init__(name, account_number, balance)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, new_account_number):
        self._account_number = new_account_number


class CustomExtendedBank(ExtendedBank):
    def __init__(self, name, account_number, balance):
        super().__init__(name, account_number, balance)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, new_account_number):
        self._account_number = new_account_number

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        self._balance = new_balance


bank = CustomExtendedBank("John Doe", "123456789", 1000.0)


bank.name = "Jane Doe"
bank.account_number = "987654321"
bank.balance = 1500.0


print(f"Name: {bank.name}")
print(f"Account Number: {bank.account_number}")
print(f"Balance: {bank.balance}")