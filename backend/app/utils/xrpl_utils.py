import requests

XRPL_API_URL = "https://s.altnet.rippletest.net:51234"  # URL da rede teste

def create_payment_request(transaction_id):
    payload = {
        "method": "tx",
        "params": [{"transaction": transaction_id}]
    }
    response = requests.post(XRPL_API_URL, json=payload)
    return response.json()
