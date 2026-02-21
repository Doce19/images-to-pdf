from dotenv import load_dotenv

load_dotenv()

import smtplib
import os
from email.message import EmailMessage


def send_simple_mail(to_email: str, pdf_path: str):
    msg = EmailMessage()
    msg["From"] = os.getenv("EMAIL_ADDRESS")
    msg["To"] = to_email
    msg["Subject"] = "Votre PDF"

    msg.set_content("Bonjour,\n\nVeuillez trouver votre PDF en pièce jointe.\n")

    with open(pdf_path, "rb") as f:
        file_data = f.read()
        msg.add_attachment(
            file_data,
            maintype="application",
            subtype="pdf",
            filename="document.pdf"
        )

    with smtplib.SMTP(
        os.getenv("SMTP_SERVER"),
        int(os.getenv("SMTP_PORT"))
    ) as server:
        server.starttls()
        server.login(
            os.getenv("EMAIL_ADDRESS"),
            os.getenv("EMAIL_PASSWORD")
        )
        server.send_message(msg)
    