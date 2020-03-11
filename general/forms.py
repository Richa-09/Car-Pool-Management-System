from django import forms


class  DateInput(forms.DateInput):
    input_type = 'date'

class  TimeInput(forms.TimeInput):
    input_type = 'time'

class OfferForm(forms.Form):
    destination1 = forms.CharField(label="From", widget = forms.TextInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Enter start of journey...',
            'label' : 'From'
        }
    ))
    destination2 = forms.CharField(label="To", widget = forms.TextInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Enter end of journey...',
            'label' : 'To'
        }
    ))
    date = forms.DateField(label="Date of Journey", widget = DateInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Enter date of journey',
            'label' : 'Date of Journey'
        }
    ))
    time = forms.TimeField(label="Time of Journey",widget= TimeInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Enter start of journey...',
            'label' : 'Time of Journey'
        }
    ))
    carModel = forms.CharField(label="Model of vehicle", widget=forms.TextInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Specify car model',
            'label' : 'From'
        }
    ))
    seatsAvailable = forms.IntegerField(label="Number of seats available", widget=forms.TextInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Specify total extra seats',
            'label' : 'From'
        }
    ))
    cost = forms.IntegerField(label="Cost per Person", widget=forms.TextInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Total charge in Rupees',
            'label' : 'From'
        }
    ))

  