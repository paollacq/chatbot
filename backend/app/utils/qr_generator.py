import qrcode

def generate_payment_qr(wallet_address, amount, destination_tag=None):
    payment_uri = f"xrpl:{wallet_address}?amount={amount}"
    if destination_tag:
        payment_uri += f"&dt={destination_tag}"
    
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(payment_uri)
    qr.make(fit=True)
    qr_code_path = f"static/qr_codes/payment_{wallet_address}.png"
    qr.make_image(fill="black", back_color="white").save(qr_code_path)
    return qr_code_path
