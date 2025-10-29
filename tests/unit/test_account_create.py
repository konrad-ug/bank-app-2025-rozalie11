from src.personal_acc import PersonalAccount

class TestPersonalAccount:
    # feature 1
    
    def test_account_creation(self):
        account = PersonalAccount("John", "Doe", "03460201023")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 0.0
        assert account.pesel == "03460201023"
        assert account.promotion_code == None

    #featyre 2 i 3

    def test_pesel_empty(self):
        account = PersonalAccount("Dylan", "Wang", "")
        assert account.pesel == "Invalid"

    def test_pesel_short(self):
        account = PersonalAccount("Dylan", "Wang", "034602")
        assert account.pesel == "Invalid"

    def test_pesel_long(self):
        account = PersonalAccount("Dylan", "Wang", "034602010231")
        assert account.pesel == "Invalid"

    def test_pesel_noString(self):
        account = PersonalAccount("Dylan", "Wang", 10346020102)
        assert account.pesel == "Invalid"

    def test_pesel_noDigits(self):
        account = PersonalAccount("Dylan", "Wang", "abcdeklsyfk")
        assert account.pesel == "Invalid"

    #feature 4 (czesc tez jest w sekcji feature 5 zeby nie powtarzac)

    def test_promotion_code_long(self):
        account = PersonalAccount("Dylan", "Wang", "03460201023", promotion_code = "PROM_WXYZ")
        assert account.balance == 0.0
        assert account.promotion_code == "Invalid"

    def test_promotion_code_short(self):
        account = PersonalAccount("Dylan", "Wang", "03460201023", promotion_code = "PROM_YZ")
        assert account.balance == 0.0
        assert account.promotion_code == "Invalid"

    def test_promotion_code_none(self):
        account = PersonalAccount("Dylan", "Wang", "03460201023", promotion_code = None)
        assert account.balance == 0.0
        assert account.promotion_code == None

    def test_promotion_code_not_string(self):
        account = PersonalAccount("Dylan", "Wang", "66010201023", promotion_code=12345)
        assert account.balance == 0.0
        assert account.promotion_code == "Invalid"

    #feature 5 

    def test_prom_after_1960(self): #prawidlowy kod i rok ur > 1960
        account = PersonalAccount("Dylan", "Wang", "66010201023", promotion_code = "PROM_XYZ")
        assert account.balance == 50.0
        assert account.promotion_code == "PROM_XYZ"

    def test_prom_after_1960_inv_code(self): #nieprawidlowy kod i rok ur > 1960
        account = PersonalAccount("Dylan", "Wang", "66010201023", promotion_code = "POM_XYZ")
        assert account.balance == 0.0
        assert account.promotion_code == "Invalid"

    def test_prom_1960(self):
        account = PersonalAccount("Dylan", "Wang", "60010201023", promotion_code = "PROM_XYZ")
        assert account.balance == 0.0
        assert account.promotion_code == "PROM_XYZ"

    def test_prom_before_1960(self):
        account = PersonalAccount("Dylan", "Wang", "59010201023", promotion_code = "PROM_XYZ")
        assert account.balance == 0.0
        assert account.promotion_code == "PROM_XYZ"

    def test_prom_after_1960_no_code(self):
        account = PersonalAccount("Dylan", "Wang", "66010201023")
        assert account.balance == 0.0
        assert account.promotion_code == None

    def test_prom_21_cent(self):
        account = PersonalAccount("Dylan", "Wang", "02250201023", promotion_code = "PROM_XYZ")
        assert account.balance == 50.0
        assert account.promotion_code == "PROM_XYZ"