from django.shortcuts import render


# Create your views here.
def landing(request):
    return render(request, 'landing/index.html')


def services(request):
    return render(request, 'landing/services.html', {'name': 'Our Services'})


def contact(request):
    return render(request, 'landing/contact.html', {'name': 'Contact Us'})

