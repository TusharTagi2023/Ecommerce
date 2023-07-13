from django.conf import settings
from django.core.mail import send_mail

def send_actiavte_email(email,token):
    subject="Accounts verifications"
    email_from=settings.EMAIL_HOST_USER
    message=f"Click on link for account verification  http://127.0.0.1:8000/accounts/{token}"
    print(f"********************************************{email_from}")
    send_mail(subject, message, email_from, [email])

