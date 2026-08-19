from django import forms

class SigninForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Enter your Email'}))
    
    password = forms.CharField(max_length=250, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Enter your Password'}))