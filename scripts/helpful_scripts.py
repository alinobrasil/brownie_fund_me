from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 200000000000

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ['development', 'ganache-local']
FORKED_LOCAL_ENVIRONMENTS = ['mainnet-fork', 'mainnet-fork-dev']

def get_account():
    if (network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or
    network.show_active() in FORKED_LOCAL_ENVIRONMENTS    ):
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])


def deploy_mocks():
    account = get_account()
    if len(MockV3Aggregator) <=0:
        print("Deploying MockV3Aggregator...")
        mock_aggregator = MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, 
        {"from": account})
    else:
        print("Mock aggregator already deployed. Getting the latest deployed address.")