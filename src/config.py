from dotenv import load_dotenv
from os import getenv

load_dotenv()


class Config():
    TSUNAMI_API_KEY = getenv("TSUNAMI_API_KEY")
    TSUNAMI_API_URL="https://api.parsiq.net/tsunami/"
    NETS={
        "Ethereum Mainnet": "eip155-1",
        "Polygon Mainnet": "eip155-137",
        "BNB Chain Mainnet": "eip155-56",
        "Avalanche Mainnet": "eip155-43114",
        "Arbitrum Mainnet": "eip155-42161",
        "Ethereum Sepolia": "eip155-11155111",
        "Ethereum Görli": "eip155-5",
        "Polygon Mumbai": "eip155-80001"
    }
