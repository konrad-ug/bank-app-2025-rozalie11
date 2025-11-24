from src.account_registry import AccountRegistry
from src.personal_acc import PersonalAccount
import pytest

class TestAccountRegistry:
    @pytest.fixture
    def registry(self):
        return AccountRegistry()
    
    def test_add_account(self, registry):
        account = PersonalAccount("Dylan", "Wang", "02250201023")
        registry.add_account(account)
        assert registry.get_account_count() == 1
        assert registry.get_all_accounts()[0] == account

    def test_get_account_by_pesel(self, registry):
        account1 = PersonalAccount("Dylan", "Wang", "02250201023")
        account2 = PersonalAccount("Jane", "Doe", "12345678901")
        registry.add_account(account1)
        registry.add_account(account2)
        found_account = registry.get_account_by_pesel("12345678901")
        assert found_account == account2
        
    def test_get_account_by_pesel_not_found(self, registry):
        account1 = PersonalAccount("Dylan", "Wang", "02250201023")
        registry.add_account(account1)
        found_account = registry.get_account_by_pesel("99999999999")
        assert found_account is None

    def test_get_all_accounts(self, registry):
        account1 = PersonalAccount("Dylan", "Wang", "02250201023")
        account2 = PersonalAccount("Jane", "Doe", "12345678901")
        registry.add_account(account1)
        registry.add_account(account2)
        all_accounts = registry.get_all_accounts()
        assert all_accounts == [account1, account2]

    def test_get_account_count(self, registry):
        account1 = PersonalAccount("Dylan", "Wang", "02250201023")
        account2 = PersonalAccount("Jane", "Doe", "12345678901")
        registry.add_account(account1)
        registry.add_account(account2)
        assert registry.get_account_count() == 2

    