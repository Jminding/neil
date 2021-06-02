import pickle

class BankAccount:
    """
    Represents a bank account which contains a name, balance, and pin number
    """

    def __init__(self, name, bal, pin):
        """
        Initializes a new bank account
        :param name: The name of the user
        :param bal: Balance of the bank account
        :param pin: The pin of the user
        """

        self.name = name
        self.bal = bal
        self.pin = pin

    def deposit(self, amt):
        """
        Deposits money into the bank account
        :param amt: The amount to be deposited
        :return: None
        """

        self.bal += amt

    def withdraw(self, amt):
        """
        Withdraw money from the bank account
        :param amt: The amount to be withdrawn
        :return: None
        """

        self.bal -= amt


def get_account(name):
    """
    Retrieve the account under a given name
    :param name: Name of the user
    :return: The BankAccount of the user if it exists.  If it does not exist,
    returns None
    """
    try:
        with open(name, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None


def create_account(name):
    """
    Prompt the user to create a new bank account
    :param name: The name of the user
    :return: A new BankAccount object
    """
    bal = int(input("Please enter your initial balance: "))
    pin = input("Please enter a secure pin number: ")
    return BankAccount(name, bal, pin)


def main():
    print("Welcome to my bank!")
    name = input("Please enter your name to get started: ")
    acct = get_account(name)
    if acct is None:
        acct = create_account(name)

    print(f"Your current balance is {acct.bal}")

    w_or_d = input("Would you like to withdraw (w) or deposit (d)? ").lower()

    if w_or_d == "w":
        amt = int(input("Amount: "))
        acct.withdraw(amt)
    elif w_or_d == "d":
        amt = int(input("Amount: "))
        acct.deposit(amt)
    else:
        raise ValueError("Invalid value")

    print(f"Thank you, your balance is {acct.bal}")

    with open(name, "wb") as f:
        pickle.dump(acct, f)


if __name__ == "__main__":
    main()