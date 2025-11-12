class Account:
    def __init__(self, balance = 0.0, fee = 0.0):
        self.balance = balance
        self.fee = fee
        self.history = []

    def receiveMoneyTransfer(self, amount):
        if not isinstance(amount, (int, float)):
            return
        if amount<=0:
            return
        else:
            self.balance += amount
            self.history.append(float(amount))

    def sendMoneyTransfer(self, amount):
        if not isinstance(amount, (int, float)):
            return
        if amount <= 0:
            return
        elif amount > self.balance:
            return
        else:
            self.balance -= amount
            self.history.append(float(-amount))

    def sendExpressTransfer(self, amount):
        if not isinstance(amount, (int, float)):
            return
        if amount <= 0:
            return
        elif amount > self.balance:
            return
        else:
            total = self.fee + amount
            self.balance -= total
            self.history.append(float(-amount))
            self.history.append(float(-self.fee))