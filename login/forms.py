from django import forms

# signin
class SigninForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Enter your Email'}))
    
    password = forms.CharField(max_length=250, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Enter your Password'}))
    
# signup
class SignupForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Enter your Email'}))
        
    password = forms.CharField(max_length=250, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Enter your Password'}))
    
    password_2 = forms.CharField(max_length=250, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Enter again your Password'}))
    
    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")

        if password and password_2 and password != password_2:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

# register
class RegisterForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Enter your Email'}))
    
# otp
class OtpForm(forms.Form):
    code = forms.CharField(max_length=4, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Enter Code'}))