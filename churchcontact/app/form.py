from django import forms 

class ContactForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField(max_length=100)
    phone_number = forms.CharField(widget=forms.NumberInput, max_length=11)

    