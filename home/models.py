from django.db import models

class ContactModel(models.Model):
    email = models.EmailField(verbose_name='ایمیل')
    subject = models.CharField(max_length=250, verbose_name='موضوع')
    message = models.TextField(verbose_name='متن پیام')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.email} | {self.subject}'