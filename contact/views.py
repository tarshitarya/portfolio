from django.shortcuts import render
from .models import Contact
from .forms import ContactForm

def contact(request):
    user_name = None

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            user_name = contact.name
            return render(request, 'contact/contact.html', {
                'form': ContactForm(),  # blank form
                'Contacts': Contact.objects.all(),
                'success': True,
                'user_name': user_name
            })
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {
        'form': form,
        'Contacts': Contact.objects.all()
    })
