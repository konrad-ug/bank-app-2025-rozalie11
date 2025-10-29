from src.personal_acc import PersonalAccount

class TestMoneyTransfer:

    #feature 6

    def testReceivingTransferSuccess(self):
        account = PersonalAccount("Dylan", "Wang", "66010201023", promotion_code = "PROM_XYZ")
        account.receiveMoneyTransfer(20)
        assert account.balance == 70.0

    def testReceivingTransferZero(self):
        account = PersonalAccount("Dylan", "Wang", "66010201023", promotion_code = "PROM_XYZ")
        account.receiveMoneyTransfer(0)
        assert account.balance == 50.0

    def testReceivingTransferFailure(self): #dostaje ujemna liczbe
        account = PersonalAccount("Dylan", "Wang", "66010201023", promotion_code = "PROM_XYZ")
        account.receiveMoneyTransfer(-50)
        assert account.balance == 50.0

    def testReceivingTransferNoNumbers(self): #podana kwota nie jest liczbą
        account = PersonalAccount("Dylan", "Wang", "66010201023", promotion_code = "PROM_XYZ")
        account.receiveMoneyTransfer("kotek")
        assert account.balance == 50.0

    def testSendingTransferSuccess(self):
        account = PersonalAccount("Dylan", "Wang", "66010201023", promotion_code = "PROM_XYZ")
        account.sendMoneyTransfer(30)
        assert account.balance == 20.0
    
    def testSendingTransferZero(self):
        account = PersonalAccount("Dylan", "Wang", "66010201023", promotion_code = "PROM_XYZ")
        account.sendMoneyTransfer(0)
        assert account.balance == 50.0

    def testSendingTransferFailure(self): #wysyla wiecej niz poisada na koncie
        account = PersonalAccount("Dylan", "Wang", "66010201023", promotion_code = "PROM_XYZ")
        account.sendMoneyTransfer(60)
        assert account.balance == 50.0

    def testSendingTransferNoNumbers(self): #podana kwota nie jest liczbą
        account = PersonalAccount("Dylan", "Wang", "66010201023", promotion_code = "PROM_XYZ")
        account.sendMoneyTransfer("kotek")
        assert account.balance == 50.0

    #feature 7 w osobnym pliku