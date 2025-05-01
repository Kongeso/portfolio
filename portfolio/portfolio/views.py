from django.core.mail import send_mail
from django.shortcuts import render, redirect


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            f'Contact from {name}',
            message,
            email,
            ['your-email@example.com'],
            fail_silently=False,
        )
        return redirect('contact_success')

    return render(request, 'contact.html')