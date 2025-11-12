from src.personal_acc import PersonalAccount
import pytest

class TestLoan:
    #feature 12

    @pytest.fixture
    def account(self):
        account = PersonalAccount("Dylan", "Wang", "66010201023", promotion_code = "PROM_XYZ")
        return account
    
    def testLoanTrueFirstCondition(self, account):
        account.history = [100, 50, 300]
        result = account.submit_for_loan(1000)
        assert result
        assert account.balance == 1050.0

    def testLoanTrueSecondCondition(self, account):
        account.history = [100, 600, 10, 5, -100]
        result = account.submit_for_loan(600)
        assert result
        assert account.balance == 650.0

    def testLoanFalseFirstCondition(self, account):
        account.history = [10, 20, -5]
        result = account.submit_for_loan(10)
        assert not result
        assert account.balance == 50.0

    def testLoanFalseSecondConditionLessThanFive(self, account):
        account.history = [100, 50, -10, 10]
        result = account.submit_for_loan(50)
        assert not result
        assert account.balance == 50.0

    def testLoanFalseSecondConditionMoreThanSum(self, account):
        account.history = [200, -100, 400, 500, -250]
        result = account.submit_for_loan(1000)
        assert not result
        assert account.balance == 50.0

    def testLoanFalseSecondConditionEqualToSum(self, account):
        account.history = [200, -150, 500, -500, 600]
        result = account.submit_for_loan(650)
        assert not result
        assert account.balance == 50.0

    