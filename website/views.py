from django.shortcuts import render
from website.forms import ContactForm
from django.contrib import messages

def home_page(request):
    return render(request, 'home/home.html')    

def about_page(request):
    return render(request, 'about/about.html')

def contact_page(request):
    if request.method == 'POST':
        print("we are here")
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.add_message(request, messages.SUCCESS, 'Your ticket has been submitted')
            form.save()
        else:
            messages.add_message(request, messages.ERROR, "Your ticket has not been submitted")
    form = ContactForm()
    return render(request, 'home/home.html', {'form': form})
