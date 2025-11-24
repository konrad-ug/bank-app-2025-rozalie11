from src.buissnes_acc import BuissnesAccount
import pytest

class TestBusinessLoan:
    @pytest.fixture
    def account(self):
        return BuissnesAccount("AiIndustry", "0235618769")
    
    @pytest.mark.parametrize("history, balance, amount, expected_results, expected_balance", [
    ([-1775], 5000, 2500, True, 7500),
    ([1000, -1775, -500, 5000], 5000, 2500, True, 7500),
    ([50, 100, -20], 5000, 2500, False, 5000.0),
    ([400, -1775, 50], 5000, 3000, False, 5000.0),
    ([1000, -200, 300], 5000, 3000, False, 5000.0),
    ],
    ids=[
        "sufficiant balance and ZUS payment",
        "sufficiant balance and ZUS payment with multiple transactions",
        "sufficiant balance but no ZUS payment",
        "insufficiant balance with ZUS payment",
        "insufficiant balance without ZUS payment"
    ])
    def test_business_loan(self, account, history, balance, amount, expected_results, expected_balance):
        account.history = history
        account.balance = balance
        result = account.take_loan(amount)
        assert result == expected_results
        assert account.balance == expected_balance