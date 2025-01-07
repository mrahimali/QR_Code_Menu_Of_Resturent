from django import forms

class QRCodeForm(forms.Form):
    resturent_name=forms.CharField(
        max_length=50, 
        label='Resturent Name', 
        widget= forms.TextInput(attrs={
            'class': 'form-control mx-auto',
            'placeholder':'Enter your resturent name'
        })
        )
    url = forms.URLField(
        max_length=200, 
        label='Menu Url',
        widget= forms.URLInput(
            attrs={
            'class':'form-control mb-4',
            'placeholder':'Enter url of your menu'
        }
        )
        )

