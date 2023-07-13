from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel1
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from base.emails import send_actiavte_email

class Profile(BaseModel1):
    use = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    is_verified=models.BooleanField(default=False)
    email_token=models.CharField(max_length=100, null=True, blank=True)
    profile_image=models.ImageField(upload_to="profile")


@receiver(post_save, sender=User)
def send_email_token(sender, instance, created, **kwargs):
    try:
        if created:
            email_token=str(uuid.uuid4())
            Profile.objects.create(use=instance,email_token=email_token)
            email=instance.email
            print("***********************************************worked")
            send_actiavte_email(email, email_token)
    except Exception as e:
        print(e)





