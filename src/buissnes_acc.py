class BuissnesAccount:
    def __init__(self, company_name, nip):
        self.company_name = company_name
        self.nip = nip if self.is_nip_valid(nip) else "Invalid"
        self.balance = 0.0

    def is_nip_valid(self, nip):
        if isinstance(nip, str) and len(nip) == 10 and nip.isdigit():
            return True
        return False
    
    def receiveMoneyTransfer(self, amount):
        if not isinstance(amount, (int, float)):
            return
        if amount<=0:
            return
        else:
            self.balance += amount

    def sendMoneyTransfer(self, amount, receiverNIP):
        if not isinstance(amount, (int, float)):
            return
        if amount <= 0:
            return
        elif amount > self.balance:
            return
        elif not self.is_nip_valid(receiverNIP):
            return
        else:
            self.balance -= amount