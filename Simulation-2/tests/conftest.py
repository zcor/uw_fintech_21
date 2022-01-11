#!/usr/bin/python3

import pytest
from brownie import HuskyToken, HuskyTokenMinter

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

@pytest.fixture(scope="module")
def alice(accounts):
    return accounts[0]

@pytest.fixture(scope="module")
def bob(accounts):
    return accounts[1]

@pytest.fixture(scope="module")
def charlie(accounts):
    return accounts[2]



@pytest.fixture(scope="module")
def husky(alice):
    husky_token = HuskyToken.deploy("Husky", "HUSKY", 0, {'from': alice})
    return husky_token

@pytest.fixture(scope="module")
def minter(alice, husky):
    husky_token = husky
    husky_token_minter = HuskyTokenMinter.deploy(husky_token, alice, {'from': alice})
    husky_token.addMinter(husky_token_minter, {'from': alice});
    husky_token.renounceMinter({'from': alice});
    return  husky_token_minter
