from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

from rest_framework.decorators import api_view

# Create your views here.
@api_view(['POST'])
def contact(request): 

        email = request.data.get('email')
        name = request.data.get('name')
        phone_number = request.data.get('phone_number')

        send_mail(
            subject=f'Test Email to {name}', 
            message='Some Message for you', 
            from_email=settings.EMAIL_HOST_USER, 
            recipient_list=[email]
        )

        return HttpResponse(f"<p>Email was successfully sent to this : <p style='font-weight: bold;'> { email } </p></p>")
        
