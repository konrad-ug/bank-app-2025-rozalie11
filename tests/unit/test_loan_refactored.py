from src.personal_acc import PersonalAccount
import pytest

class TestLoanRefactored:
    @pytest.fixture
    def account(self):
        return PersonalAccount("Dylan", "Wang", "66010201023", promotion_code = "PROM_XYZ")
    
    @pytest.mark.parametrize("history, amount, expected_results, expected_balance", [
    ([100, 50, 300], 1000, True, 1050),
    ([100, 600, 10, 5, -100], 600, True, 650),
    ([10, 20, -5], 10, False, 50),
    ([100, 50, -10, 10], 50, False, 50),
    ([200, -100, 400, 500, -250], 1000, False, 50),
    ([200, -150, 500, -500, 600], 650, False, 50),
    ],
    ids=[
        "first condition true",
        "first and second condition true",
        "first condition false",
        "second condition less than 5 false",
        "loan bigger than transactions sum",
        "loan equal to transactions sum"
    ])
    def test_loan_refactored(self, account, history, amount, expected_results, expected_balance):
        account.history = history
        result = account.submit_for_loan(amount)
        assert result == expected_results
        assert account.balance == expected_balance