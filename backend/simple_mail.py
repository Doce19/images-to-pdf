from dotenv import load_dotenv
load_dotenv()

import os
import requests
import base64


def send_simple_mail(to_email: str, pdf_path: str):

    api_key = os.getenv("BREVO_API_KEY")

    if not api_key:
        raise Exception("BREVO_API_KEY not found")

    # Lire et encoder le PDF
    with open(pdf_path, "rb") as f:
        encoded_file = base64.b64encode(f.read()).decode()

    url = "https://api.brevo.com/v3/smtp/email"

    headers = {
        "accept": "application/json",
        "api-key": api_key,
        "content-type": "application/json"
    }

    data = {
        "sender": {
            "name": "Images to PDF",
            "email": "edtohoun@gmail.com"   # doit être validé dans Brevo
        },
        "to": [
            {"email": to_email}
        ],
        "subject": "Votre PDF est prêt",
        "htmlContent": "<p>Bonjour,<br><br>Votre fichier PDF est en pièce jointe.</p>",
        "attachment": [
            {
                "content": encoded_file,
                "name": "document.pdf"
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 201:
        raise Exception(f"Brevo error: {response.text}")