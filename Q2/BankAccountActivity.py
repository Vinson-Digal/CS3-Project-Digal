

class BankAccount:
    def __init__(self, account_number, balance):
        # Safe defaults first, then let the setters validate the real values
        self.__account_number = None
        self.__balance = 0.0
        self.set_account_number(account_number)
        self.set_balance(balance)

    # ---------- setters ----------
    def set_account_number(self, account_number):
        if isinstance(account_number, int) and account_number > 0:
            self.__account_number = account_number
        else:
            print("The account number must be a positive integer.")

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = float(balance)
        else:
            print("The balance must not be a negative number.")

    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance


def show(account):
    print(f"Account Number: {account.account_number}")
    print(f"Balance: {account.balance:.2f}")


if __name__ == "__main__":
    a1 = BankAccount(12345, 1000)

    print("Account 1")
    show(a1)

    print("\nUpdate balance to -100")
    a1.set_balance(-100)          
    show(a1)

    print("\nUpdate balance to 2500.5")
    a1.set_balance(2500.5)
    show(a1)

    print("\nUpdate account number to 67890")
    a1.set_account_number(67890)
    show(a1)

    try:
        print(a1.__balance)
    except AttributeError:
        print("\nDirect access to __balance is blocked (AttributeError).")
