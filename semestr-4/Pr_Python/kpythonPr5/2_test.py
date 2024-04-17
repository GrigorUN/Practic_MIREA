import pytest
from bank_account import BankAccount

@pytest.fixture
def new_account():
    return BankAccount("12345")

@pytest.fixture
def funded_account():
    return BankAccount("67890", balance=1000)

def test_deposit(new_account):
    assert new_account.balance == 0
    new_account.deposit(500)
    assert new_account.balance == 500

def test_withdraw(funded_account):
    assert funded_account.balance == 1000
    funded_account.withdraw(500)
    assert funded_account.balance == 500

@pytest.mark.parametrize("initial_balance, amount, expected_balance", [
    (1000, 500, 1500),
    (2000, 1000, 3000),
])
def test_deposit_with_parametrization(initial_balance, amount, expected_balance):
    account = BankAccount("54321", balance=initial_balance)
    account.deposit(amount)
    assert account.balance == expected_balance
