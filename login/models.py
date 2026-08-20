from django.db import models

class SignupModel(models.Model):
    email = models.EmailField(verbose_name='ایمیل')
    password = models.CharField(max_length=250, verbose_name='گذرواژه')
    password_2 = models.CharField(max_length=250, verbose_name='تکرار گذرواژه')