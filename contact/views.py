from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def send_massege(request):
    myinfo= Info.objects.first()
    pass
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')


        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,  
            [email],
        )


    context = {
        'myinfo': myinfo,
    }
    return render(request, 'contact.html', context)