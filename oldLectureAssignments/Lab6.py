class Cat:
    def __init__(self, name, owner, lives=9):
        self.is_alive = True
        self.name = name
        self.owner = owner
        self.lives = lives

    def talk(self):
        return self.name + ' says meow!'

    @classmethod
    def adopt_a_cat(cls, owner):
        cat_names = ["Felix", "Bugs", "Grumpy"]
        name = cat_names[len(owner) % len(cat_names)]
        lives = len(owner) + len(name)
        return cls(name, owner, lives)


class NoisyCat(Cat):
    def __init__(self, name, owner, lives=9):
        super().__init__(name, owner, lives - 1)

    def talk(self):
        return super().talk() + ' ' + super().talk()


# Testing the above class
# Question 2
my_cat = NoisyCat("Furball", "James")
print(my_cat.name)
print(my_cat.is_alive)
print(my_cat.lives)
print(my_cat.talk())

friend_cat = NoisyCat("Tabby", "James", 2)
print(friend_cat.talk())
print(friend_cat.lives)

# Question 3
cat1 = Cat.adopt_a_cat("Ifeoma")
print(isinstance(cat1, Cat))
print(cat1.owner)
print(cat1.name)
print(cat1.lives)

cat2 = Cat.adopt_a_cat("Ay")
print(cat2.owner)
print(cat2.name)
print(cat2.lives)


class Account:
    max_withdrawal = 10
    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        if amount > self.max_withdrawal:
            return "Cant withdraw that amount"
        self.balance = self.balance - amount
        return self.balance

    # Question 4
    def time_to_retire(self, amount):
        """Return the number of years until balance would grow to amount"""
        assert self.balance > 0 and amount > 0 and self.interest > 0
        balance = self.balance
        years = 0
        if amount == self.balance:
            return years
        while balance < amount:
            years = years + 1
            balance = balance + balance * self.interest

        return years


class FreeChecking(Account):
    withdraw_fee = 1
    free_withdrawals = 2

    def __init__(self, account_holder):
        super().__init__(account_holder)

    def withdraw(self, amount):
        if self.free_withdrawals > 0:
            self.free_withdrawals = self.free_withdrawals - 1
        elif self.balance - self.withdraw_fee - amount <= 0:
            return "Insufficient funds"
        else:
            self.balance = self.balance - self.withdraw_fee
        return super().withdraw(amount)


# Question 5
# Testing

ch = FreeChecking('Jack')
ch.balance = 20
print(ch.withdraw(100))  # First one free
print(ch.withdraw(3))  # and the second
print(ch.balance)
print(ch.withdraw(3))  # Not free
print(ch.withdraw(3))  # Not Free

ch2 = FreeChecking('John')
ch2.balance = 10
print(ch2.withdraw(3))
print(ch.withdraw(3)) # This is the first acc, still charges a fee
print(ch.withdraw(5)) # No tenough to cover fee + withdraw
