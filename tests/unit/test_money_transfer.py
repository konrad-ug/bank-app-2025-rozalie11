from src.account import Account

class TestMoneyTransfer:

    #feature 6

    def testReceivingTransferSuccess(self):
        account = Account("Dylan", "Wang", "66010201023", promotion_code = "PROM_XYZ")
        account.receiveMoneyTransfer(20)
        assert account.balance == 70.0

    def testReceivingTransferZero(self):
        account = Account("Dylan", "Wang", "66010201023", promotion_code = "PROM_XYZ")
        account.receiveMoneyTransfer(0)
        assert account.balance == 50.0

    def testReceivingTransferFailure(self): #dostaje ujemna liczbe
        account = Account("Dylan", "Wang", "66010201023", promotion_code = "PROM_XYZ")
        account.receiveMoneyTransfer(-50)
        assert account.balance == 50.0

    def testReceivingTransferNoNumbers(self): #podana kwota nie jest liczbą
        account = Account("Dylan", "Wang", "66010201023", promotion_code = "PROM_XYZ")
        account.receiveMoneyTransfer("kotek")
        assert account.balance == 50.0

    def testSendingTransferSuccess(self):
        account = Account("Dylan", "Wang", "66010201023", promotion_code = "PROM_XYZ")
        account.sendMoneyTransfer(30, "50256377101")
        assert account.balance == 20.0
    
    def testSendingTransferZero(self):
        account = Account("Dylan", "Wang", "66010201023", promotion_code = "PROM_XYZ")
        account.sendMoneyTransfer(0, "50256377101")
        assert account.balance == 50.0

    def testSendingTransferFailure(self): #wysyla wiecej niz poisada na koncie
        account = Account("Dylan", "Wang", "66010201023", promotion_code = "PROM_XYZ")
        account.sendMoneyTransfer(60, "50256377101")
        assert account.balance == 50.0

    def testSendingTransferInvalidPesel(self):
        account = Account("Dylan", "Wang", "66010201023", promotion_code = "PROM_XYZ")
        account.sendMoneyTransfer(60, "377101")
        assert account.balance == 50.0

    def testSendingTransferNoNumbers(self): #podana kwota nie jest liczbą
        account = Account("Dylan", "Wang", "66010201023", promotion_code = "PROM_XYZ")
        account.sendMoneyTransfer("kotek", "39976450101")
        assert account.balance == 50.0

    #feature 7