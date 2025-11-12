from src.personal_acc import PersonalAccount
from src.buissnes_acc import BuissnesAccount

class TestAccountHistory:
    def test_receive_transfer_history(self):
        account = PersonalAccount("Dylan", "Wang", "02250201023", promotion_code = "PROM_XYZ")
        account.receiveMoneyTransfer(500)
        assert account.history == [500.0]

    def test_receive_transfer_history_minus(self):
        account = PersonalAccount("Dylan", "Wang", "02250201023", promotion_code = "PROM_XYZ")
        account.receiveMoneyTransfer(-500)
        assert account.history == []

    def test_receive_transfer_history_word(self):
        account = PersonalAccount("Dylan", "Wang", "02250201023", promotion_code = "PROM_XYZ")
        account.receiveMoneyTransfer("kotek")
        assert account.history == []

    def test_send_transfer_history(self):
        account = PersonalAccount("Dylan", "Wang", "02250201023", promotion_code = "PROM_XYZ")
        account.receiveMoneyTransfer(500)
        account.sendMoneyTransfer(200)
        assert account.history == [500.0, -200.0]

    def test_send_transfer_history_toomuch(self):
        account = PersonalAccount("Dylan", "Wang", "02250201023", promotion_code = "PROM_XYZ")
        account.receiveMoneyTransfer(500)
        account.sendMoneyTransfer(700)
        assert account.history == [500.0]

    def test_express_transfer_personal(self):
        account = PersonalAccount("Dylan", "Wang", "02250201023", promotion_code = "PROM_XYZ")
        account.receiveMoneyTransfer(500)
        account.sendExpressTransfer(300)
        assert account.history == [500.0, -300.0, -1.0]

    def test_express_transfer_buissness(self):
        account = BuissnesAccount("AiIndustry", "0235618769")
        account.receiveMoneyTransfer(1000)
        account.sendExpressTransfer(200)
        assert account.history == [1000.0, -200.0, -5.0]