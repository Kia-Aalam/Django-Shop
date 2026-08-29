from django.db import models
from django.utils import timezone
from datetime import timedelta

from account.models import User

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
    
class CheckoutModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="checkouts")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    city = models.CharField(max_length=100)
    post_code = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.user.email} | {self.post_code}"