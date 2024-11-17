class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance
    def __str__(self):
        return f'Номер счета: {self._account_number}. Текущий баланс составляет: {self._balance}'

    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError('Баланс должен быть положительным целым числом.')
        self._balance = value

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f'Поступило денежных средств: {amount}. Текущий баланс: {self._balance}.')
        else:
            print('Сумма для внесения денежных средств должна быть положительной!')
    def withdraw(self, amount):
        if amount < self._balance:
            self._balance -= amount
            print(f'Снятие денежных средств: {amount}. Текущий баланс: {self._balance}')
        else:
            print(f'Вы не сможете снять данное количество денежных средств: {amount}, '
                  f'так как текущий баланс: {self._balance}.')
    def calculate_interest(self, rate):
        if rate > 0:
            interest = self._balance * (rate / 100)
            self._balance += interest
            print(f'Процент составляет: {rate}%.')
            print(f'Начисленные проценты на остаток: {round(interest, 2)}. Текущий баланс составляет: {self._balance}.')
        else:
            print('Процентная ставка должна быть положительной!')

account = BankAccount('123456789', 1000)
print(account)
account.deposit(int(input('Внесите сумму: ')))
account.withdraw(int(input('Какую сумму необходимо снять: ')))
account.calculate_interest(13)
account.balance = int(input('Изменение баланса: '))
print(f'Баланс составляет: {account.balance}')