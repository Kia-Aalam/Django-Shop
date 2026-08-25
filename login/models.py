from django.db import models
from django.utils import timezone
from datetime import timedelta

class SignupModel(models.Model):
    email = models.EmailField(verbose_name='ایمیل')
    password = models.CharField(max_length=250, verbose_name='گذرواژه')
    password_2 = models.CharField(max_length=250, verbose_name='تکرار گذرواژه')
    
class Otp(models.Model):
    email = models.EmailField()
    code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def is_expired(self):
        # OTP expires after 3 minutes
        expiration_time = self.created_at + timedelta(minutes=3)
        return timezone.now() > expiration_time
    
    def __str__(self):
        return self.email