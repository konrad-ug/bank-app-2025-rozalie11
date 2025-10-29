from src.personal_acc import PersonalAccount
from src.buissnes_acc import BuissnesAccount

class TestExpressTransfer:
    def test_express_transfer_pers_acc(self):
        account = PersonalAccount("Dylan", "Wang", "66010201023", promotion_code = "PROM_XYZ")
        account.sendExpressTransfer(20.0)
        assert account.balance == 29.0

    def test_express_transfer_pers_acc_too_much(self):
        account = PersonalAccount("Dylan", "Wang", "66010201023", promotion_code = "PROM_XYZ")
        account.sendExpressTransfer(60.0)
        assert account.balance == 50.0

    def test_express_transfer_pers_acc_minus_amount(self):
        account = PersonalAccount("Dylan", "Wang", "66010201023", promotion_code = "PROM_XYZ")
        account.sendExpressTransfer(-20.0)
        assert account.balance == 50.0

    def test_express_transfer_pers_acc_amount_equal_to_balance(self):
        account = PersonalAccount("Dylan", "Wang", "66010201023", promotion_code = "PROM_XYZ")
        account.sendExpressTransfer(50.0)
        assert account.balance == -1.0

    def test_express_transfer_pers_acc_no_numbers(self): #podana kwota nie jest liczbą
        account = PersonalAccount("Dylan", "Wang", "66010201023", promotion_code = "PROM_XYZ")
        account.sendExpressTransfer("kotek")
        assert account.balance == 50.0

    def test_express_transfer_buiss_acc(self):
        account = BuissnesAccount("AiIndustry", "0450101037")
        account.receiveMoneyTransfer(100.0)
        account.sendExpressTransfer(20.0)
        assert account.balance == 75.0

    def test_express_transfer_buiss_acc_too_much(self):
        account = BuissnesAccount("AiIndustry", "0450101037")
        account.receiveMoneyTransfer(100.0)
        account.sendExpressTransfer(200.0)
        assert account.balance == 100.0

    def test_express_transfer_buiss_acc_minus_amount(self):
        account = BuissnesAccount("AiIndustry", "0450101037")
        account.receiveMoneyTransfer(100.0)
        account.sendExpressTransfer(-20.0)
        assert account.balance == 100.0

    def test_express_transfer_buiss_acc_amount_equal_to_balance(self):
        account = BuissnesAccount("AiIndustry", "0450101037")
        account.receiveMoneyTransfer(100.0)
        account.sendExpressTransfer(100.0)
        assert account.balance == -5.0

    def test_express_transfer_buiss_acc_no_numb(self):
        account = BuissnesAccount("iIndustry", "0235618769")
        account.receiveMoneyTransfer(100)
        account.sendExpressTransfer("lisek")
        assert account.balance == 100.0