from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Enter your Email'}))
    
    subject = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Subject'}))
    
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Enter your Message'}))