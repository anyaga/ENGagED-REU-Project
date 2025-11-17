from django import forms


class download_form(forms.Form):
    email = forms.EmailField(label="Your Email",max_length=254)