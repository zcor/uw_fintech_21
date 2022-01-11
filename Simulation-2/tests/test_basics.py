import brownie

def test_bob_can_mint(husky, minter, bob):
    assert husky.balanceOf(bob) == 0
    minter.mint({'from': bob, 'amount': 10000})
    assert minter.last_price() == 10000
    assert husky.balanceOf(bob) > 0

def test_bob_cannot_claim(husky, minter, bob):
    with brownie.reverts():
        minter.claim({'from': bob})

def test_alice_can_claim(husky, minter, alice, bob):
    init_bal = alice.balance()
    minter.mint({'from': bob, 'amount': 10 ** 18})
    minter.claim({'from': alice})
    assert alice.balance() > init_bal

def test_token_address(husky, minter):
    assert minter.token() == husky.address

def test_leaderboard_initially_empty(minter):
    assert minter.leader() == '0x0000000000000000000000000000000000000000'

def test_bob_leader(minter,bob):
    minter.mint({'from': bob, 'amount': 10 ** 18})
    assert minter.leader() == bob

def test_charlie_takes_leader(minter, bob, charlie, husky):
    minter.mint({'from': bob, 'amount': 10 ** 17})
    minter.mint({'from': charlie, 'amount': 10 ** 17 + 1})
    minter.mint({'from': charlie, 'amount': 10 ** 17 + 2})
    assert minter.leader() == charlie

def test_bob_cannot_lowball(minter, bob, charlie):
    minter.mint({'from': charlie, 'amount': 10 ** 18})
    with brownie.reverts():
        minter.mint({'from': bob, 'amount': 10 ** 17})

def test_alice_can_claim_lots(minter, alice, bob, charlie, husky):
    init = alice.balance()
    minter.mint({'from': bob, 'amount': 10 ** 17})
    minter.mint({'from': charlie, 'amount': 10 ** 17 + 1})
    minter.mint({'from': charlie, 'amount': 10 ** 17 + 2})
    minter.claim({'from': alice})
    assert alice.balance() > init

def test_alice_can_reset(minter, alice, bob, husky):
    minter.mint({'from': bob, 'amount': 10 ** 17})
    assert minter.leader() == bob
    minter.reset({'from': alice})
    assert minter.leader() != bob

def test_contract_externally_payable(minter, alice):
    init_bal = minter.balance()
    alice.transfer(minter, '1 ether')
    assert minter.balance() == init_bal + 1e18
