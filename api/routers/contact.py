import os
import requests
from fastapi import APIRouter, HTTPException, Depends
from django.conf import settings
from landing.models import Contact

router = APIRouter()

def verify_hcaptcha(token: str) -> bool:
    hcaptcha_secret = settings.HCAPTCHA_SECRET
    
    payload = {
        "secret": hcaptcha_secret,
        "response": token
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    try:
        response = requests.post(
            "https://api.hcaptcha.com/siteverify", 
            data=payload,
            headers=headers,
            timeout=10
        )
        result = response.json()
            
        return result.get("success", False)
    except requests.RequestException as e:
        return False

from fastapi import APIRouter, HTTPException, Form
from pydantic import EmailStr

@router.post("/contact/")
def send_message(
    name: str = Form(..., max_length=50),
    email: EmailStr = Form(...),
    message: str = Form(..., max_length=1785),
    date: str = Form(...),
    h_captcha_response: str = Form(..., alias="h-captcha-response")
):
    if not verify_hcaptcha(h_captcha_response):
        raise HTTPException(status_code=400, detail="Invalid CAPTCHA.")
    
    Contact.objects.create(name=name, email=email, message=message)
    
    json_body = {
        "embeds": [{
            "title": f'{name} | {email}',
            "description": message,
            "color": 6370691,
            "timestamp": date
        }]
    }
    
    r = requests.post(settings.DISCORD_WEBHOOK, json=json_body)
    if r.status_code == 204:
        return {"Message": "Success"}
    raise HTTPException(status_code=r.status_code, detail="Webhook failed")
