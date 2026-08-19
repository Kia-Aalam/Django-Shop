from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactModel

def index(request):
    return render(request, 'index.html')

def contact(request):
        
    if request.method == "POST":
            form = ContactForm(request.POST)
                
            if form.is_valid():
                ContactModel.objects.create(
                    email=form.cleaned_data['email'],
                    subject=form.cleaned_data['subject'],
                    message=form.cleaned_data['message']
                )   
                return redirect('home')
    else:
        form = ContactForm()
        
    return render(request, 'contact.html', {'form':form})