import django
import os

from django.test import Client
from django.urls import reverse
from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "churchcontact.settings")
django.setup()


# Create your tests here.
c = Client()

def test_contactform(): 
    data = {'email': 'test@email.com', 'name': 'Bob Junior', 'phone_number': '********'}
    response = c.post(reverse('contact-form'), data=data)

    assert response.status_code == 200
