import os
import requests
from fastapi import FastAPI, HTTPException, Depends, Form
from pydantic import BaseModel
from django.conf import settings

from myapp.models import Contact

app = FastAPI()

class ContactRequest(BaseModel):
    name: str = Form(...)
    message: str = Form(...)
    date: str = Form(...)
    h_captcha_response: str = Form(..., alias="h-captcha-response")

def verify_hcaptcha(token: str) -> bool:
    hcaptcha_secret = getattr(settings, "HCAPTCHA_SECRET_KEY", os.environ.get("HCAPTCHA_SECRET_KEY"))
    try:
        response = requests.post(
            "https://api.hcaptcha.com/siteverify", 
            data={"secret": hcaptcha_secret, "response": token}
        )
        return response.json().get("success", False)
    except requests.RequestException:
        return False

@app.post("/api/contact")
def send_message(payload: ContactRequest = Depends()):
    
    if not verify_hcaptcha(payload.h_captcha_response):
        raise HTTPException(status_code=400, detail="Invalid CAPTCHA. Please prove you are human.")
    
    try:
        Contact.objects.create(
            name=payload.name,
            message=payload.message
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to save to database.")

    json_body = {
        "embeds": [
            {
                "title": payload.name,
                "description": payload.message,
                "color": 6370691,
                "timestamp": payload.date
            }
        ],
        "allowed_mentions": {
            "parse": ["everyone", "roles", "users"]
        }
    }
    
    r = requests.post(settings.DISCORD_WEBHOOK, json=json_body)
    
    if r.status_code == 204:
        return {"Message": "Success", "status_code": r.status_code}
    
    raise HTTPException(status_code=r.status_code, detail="Saved to DB, but failed to send Discord message")
