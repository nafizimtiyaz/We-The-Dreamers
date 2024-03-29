from django.shortcuts import render,redirect
from Contact.models import Contact
from Home.models import Category


def ContactUs(request):
    cat = Category.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        Email = request.POST['Email']
        message = request.POST['message']
        subject = request.POST['subject']

        contact_form = Contact(name=name, Email=Email, message=message, subject=subject)
        contact_form.save()

        return redirect('/contact')

    else:
        return render(request, 'contact.html',{'cat': cat,})
