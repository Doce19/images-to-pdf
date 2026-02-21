import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env", override=True)

print("SMTP_PORT =", os.getenv("SMTP_PORT"))
print("SMTP_SERVER =", os.getenv("SMTP_SERVER"))
print("EMAIL_ADDRESS =", os.getenv("EMAIL_ADDRESS"))


from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import List
from PIL import Image
import uuid
from simple_mail import send_simple_mail


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OUTPUT_DIR = "generated"
os.makedirs(OUTPUT_DIR, exist_ok=True)


@app.post("/convert")
async def convert_images_to_pdf(
    email: str = Form(...),
    files: List[UploadFile] = File(...)
):
    if not files:
        return {"error": "No files received"}

    pdf_name = f"{uuid.uuid4()}.pdf"
    pdf_path = os.path.join(OUTPUT_DIR, pdf_name)

    images = []
    for file in files:
        image = Image.open(file.file).convert("RGB")
        images.append(image)

    images[0].save(
        pdf_path,
        save_all=True,
        append_images=images[1:]
    )

    # Envoi du mail
    send_simple_mail(email, pdf_path)

    return JSONResponse(
        content={"message": "PDF généré et envoyé par email"}
    )
    
