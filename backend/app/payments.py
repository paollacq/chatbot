import qrcode

def generate_payment_qr(wallet_address: str, amount: float, destination_tag: str = None):
    payment_uri = f"xrpl:{wallet_address}?amount={amount}"
    if destination_tag:
        payment_uri += f"&dt={destination_tag}"
    
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(payment_uri)
    qr.make(fit=True)
    qr_code_path = f"static/qr_codes/payment_{wallet_address}.png"
    qr.make_image(fill="black", back_color="white").save(qr_code_path)
    return qr_code_path
import requests

XRPL_API_URL = "https://s.altnet.rippletest.net:51234"

def confirm_payment(transaction_id: str):
    payload = {"method": "tx", "params": [{"transaction": transaction_id}]}
    response = requests.post(XRPL_API_URL, json=payload)
    return response.json()
