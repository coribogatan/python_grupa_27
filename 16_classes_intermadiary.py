
#interiorul clasei
class BankAccount:
    bank = "ING"

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance # _ inseamna proprietate privata; __ cannot be accessed from the outside of the class
        self.number_of_deposits = 0


    # getter
    @property
    def balance(self):
        return self.__balance

    # setter
    @balance.setter
    def balance(self, value):
        if value > 0:
            self.number_of_deposits += 1
            self.__balance = value

    def __str__(self):
        return f"{self.owner} has {self.__balance} EURO"

    # def deposit(self, amount):
    #     self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Not enough funds!")
        else:
            self.__balance = self.__balance - amount

    @staticmethod
    def is_valid_amount(amount):
        if not isinstance(amount, bool) and isinstance(amount, (int, float)) and amount > 0: # check if amount is of type int or float
            return True
        else:
            return False

    @classmethod
    def construct_from_string(cls, account_data):
        #cls = BankAccount
        # account_data = "John:300"
        owner, amount = account_data.split(":") # # owner receives account_data.split(':')[0] and amount receives account_data.split(':')[1]
        obj1 = cls(owner, int(amount)) #obj1 = BankAccount() -> echivalent
        return obj1




# @staticmethod. O metoda care are legatura cu conturi bancare, dar nu cu un cont anume sau info dintr-un self anume
# @classmethod - O metoda care opereaza pe clasa si are o actiune la nivel de clasa





# exteriorul clasei
ing1 = BankAccount("adrian")
ing1._balance = 300
ing1.withdraw(10)
print(ing1.balance)

ing1.balance += 300
ing1.balance += 600
ing1.balance += 900

new_amount = 1
print(BankAccount.is_valid_amount(new_amount))

print(ing1.balance)
print(ing1.number_of_deposits)

print(BankAccount)












