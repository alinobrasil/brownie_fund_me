from brownie import FundMe, MockV3Aggregator,network, config
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS

def deploy_fund_me():
    account = get_account()

    activeNetwork = network.show_active()
    print(f"Active network: {activeNetwork}")

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        priceFeedAddress = config['networks'][network.show_active()]['eth_usd_price_feed']
    else:
        deploy_mocks()
        priceFeedAddress = MockV3Aggregator[-1].address

    
    fund_me = FundMe.deploy(
        priceFeedAddress,
        {"from": account}, 
        publish_source=config['networks'][activeNetwork].get('verify'))
    print(f"FundMe Contract deployed to {fund_me.address}")

    return fund_me 

def main():
    deploy_fund_me()