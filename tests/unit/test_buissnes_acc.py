from src.buissnes_acc import BuissnesAccount

# feature 7
class TestBuissnessAccount:
    def test_nip_valid(self):
        account = BuissnesAccount("AiIndustry", "0235618769")
        assert account.nip == "0235618769"

    def test_nip_invalid(self):
        account = BuissnesAccount("AiIndustry", "18769")
        assert account.nip == "Invalid"

    def testReceiveTransfer(self):
        account = BuissnesAccount("iIndustry", "0235618769")
        account.receiveMoneyTransfer(100)
        assert account.balance == 100.0

    def testSendTransferSuccess(self):
        account = BuissnesAccount("iIndustry", "0235618769")
        account.receiveMoneyTransfer(100)
        account.sendMoneyTransfer(50, "6211654321")
        assert account.balance == 50.0

    def testSendTransferInvalidNIP(self):
        account = BuissnesAccount("iIndustry", "0235618769")
        account.receiveMoneyTransfer(100)
        account.sendMoneyTransfer(50, "654321")
        assert account.balance == 100.0