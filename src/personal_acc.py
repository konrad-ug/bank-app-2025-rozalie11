from src.account import Account

class PersonalAccount(Account):
    def __init__(self, first_name, last_name, pesel, promotion_code = None):
        super().__init__(fee=1.0)
        self.first_name = first_name
        self.last_name = last_name
        self.pesel = pesel if self.is_pesel_valid(pesel) else "Invalid"
        self.promotion_code = promotion_code if self.is_promotion_code_valid(promotion_code) or promotion_code is None  else "Invalid"

        if self.is_promotion_code_valid(promotion_code) and self.get_year(pesel) > 1960:
            self.add_balance()

    def is_pesel_valid(self, pesel):
        if isinstance(pesel, str) and len(pesel) == 11 and pesel.isdigit():
            return True
        return False
    
    def is_promotion_code_valid(self, promotion_code):
        if isinstance(promotion_code, str) and promotion_code.startswith("PROM_") and len(promotion_code) == 8:
            return True
        return False
    
    def add_balance(self):
        self.balance += 50.0
        
    def get_year(self, pesel):
        if not self.is_pesel_valid(pesel):
            return 0
        
        year = int(pesel[0:2])
        month = int(pesel[2:4])

        if 1 <= month <= 12:
            year += 1900
        elif 21 <= month <= 32:
            year += 2000
        return year
    
    def submit_for_loan(self, amount):
        if len(self.history) >= 3:
            last_three = self.history[-3:] 
            only_positive = True  

            for transaction in last_three:
                if transaction <= 0:
                    only_positive = False
                    break 

            if only_positive:
                self.balance += amount
                return True

        if len(self.history) >= 5 and sum(self.history[-5:]) > amount:
            self.balance += amount
            return True
        return False
    