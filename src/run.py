import requests
import json
from config import Config


def test():
    chain_id = f'{Config.NETS["Ethereum Mainnet"]}/'
    version = 'v1/'
    category = 'blocks/'
    data = '0x0c195cccdaf1c289879187a819ae8caed341fd5568e32d98b584c37dc09c59e7'
    url = f'{Config.TSUNAMI_API_URL}{chain_id}{version}{category}{data}'
    headers = {
        "Authorization": f"Bearer {Config.TSUNAMI_API_KEY}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(response.json())
    else:
        print("Request failed with status code:", response.status_code)


def get_data(
    call,
    chain_id=f'{Config.NETS["Ethereum Mainnet"]}', 
    version="v1"):

    url = f'{Config.TSUNAMI_API_URL}{chain_id}/{version}/{call}/{data}'


if __name__ == "__main__":

    url = "https://api.parsiq.net/tsunami/chainId/v1/address/address/txs?limit=100"

    headers = {
        "accept": "application/json",
        "authorization": "Bearer Vk0B4hylLtb3tdAJMPtbFBNzOkmLLATC"
    }

    response = requests.get(url, headers=headers)

    print(response.text)
