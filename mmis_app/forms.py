from django import forms
from django.forms import SelectDateWidget

from .models import User, MercuryAddedProducts, EnergyConsumptionAndFuelProduction, ContactInformation
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class NewRegistration(UserCreationForm):
    email = forms.EmailField(max_length=50, required=True,
                             help_text='Required: 50 characters or fewer')
    organization = forms.CharField(max_length=150, required=True,
                                   help_text='Required: 150 characters or fewer')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',
                  'sector', 'gender', 'role')


class MapForm(forms.ModelForm):
    class Meta:
        model = MercuryAddedProducts
        fields = ('mercury_compound', 'item', 'imported', 'consumption_or_production', 'year', )
        labels = {
            'mercury_compound': 'Mercury Compound',
            'item': 'Item',
            'imported': 'Produced/Imported',
            'consumption_or_production': 'Annual Consumption / Production',
            'year': 'Year'
        }
        widgets = {
        'item': forms.TextInput({'placeholder': 'Mercury containing product/item'}),
        'imported': forms.TextInput({'placeholder': 'If imported state the country of import'}),
        'consumption_or_production': forms.TextInput({'placeholder': 't/y'}),
        'year': forms.TextInput({'placeholder': 'yyyy-mm-dd'}),

        }

    def __init__(self, *args, **kwargs):
        super(MapForm, self).__init__(*args, **kwargs)
        self.fields['mercury_compound'].choices = [("", "select category"),
                                                   ] + list(self.fields['mercury_compound'].choices)[0:]
        self.fields['item'].required = True
        self.fields['mercury_compound'].required = True
        self.fields['consumption_or_production'].required = True
        self.fields['year'].required = True


class EnergyFuelForm(forms.ModelForm):
    class Meta:
        model = EnergyConsumptionAndFuelProduction
        fields = ('energy_fuel', 'imported', 'consumption_or_production', 'year', )
        labels = {
            'energy_fuel': 'Energy Consumption/Fuel Production',
            'imported': 'Produced/Imported',
            'consumption_or_production': 'Annual Consumption / Production',
            'year': 'Year'
        }
        widgets = {
        'imported': forms.TextInput({'placeholder': 'If imported state the country of import'}),
        'consumption_or_production': forms.TextInput({'placeholder': 't/y'}),
        'year': forms.TextInput({'placeholder': 'yyyy-mm-dd'}),

        }

    def __init__(self, *args, **kwargs):
        super(EnergyFuelForm, self).__init__(*args, **kwargs)
        self.fields['energy_fuel'].choices = [("", "select category"),
                                                   ] + list(self.fields['energy_fuel'].choices)[0:]
        self.fields['energy_fuel'].required = True
        self.fields['consumption_or_production'].required = True
        self.fields['year'].required = True
