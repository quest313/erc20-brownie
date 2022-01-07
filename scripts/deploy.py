from brownie import PezzToken, network, config
from scripts.util import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS


def deploy_my_token():
    account = get_account()
    initial_supply = 1000000
    # TO DO change to to represent value of wei (eth20 contract follows ethereum for decimal places)

    publish_source = config["networks"][network.show_active()]["verify"]
    our_token = PezzToken.deploy(
        initial_supply, {"from": account}, publish_source=publish_source
    )
    print(f"Contract deployed to {our_token.address}")
    return our_token


def show_balance():
    account = get_account()
    account1 = get_account(id="chump")
    balance = PezzToken[-1].balanceOf(account.address)
    balance1 = PezzToken[-1].balanceOf(account1.address)
    print(f"balance of account 0 is {balance} pezz")
    print(f"balance of account 1 is {balance1} pezz")


def transfer():
    account = get_account(id="chump")
    PezzToken[-1].transfer(account.address, 100)


def main():
    deploy_my_token()
    show_balance()
    # transfer()
    # show_balance()
