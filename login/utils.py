from django.core.mail import send_mail
from django.conf import settings

def send_otp_email(email, otp_code):
    subject = 'MultiShop | مولتی شاپ'
    message = f'کد تایید شما: {otp_code}\nاین کد 3 دقیقه اعتبار دارد.'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]
    
    send_mail(subject, message, from_email, recipient_list)