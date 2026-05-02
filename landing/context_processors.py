from django.conf import settings

def admin_media(request):
    return {'HCAPTCHA_SITEKEY': settings.HCAPTCHA_SITEKEY}
