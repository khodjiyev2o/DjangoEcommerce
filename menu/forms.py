from .models import Customer
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email"]

    def save(self, commit=True):
        customer = super().save(commit=False)

        customer.email = self.cleaned_data['email']

        if commit:
            customer.save()
            return customer


class UserprofileForm(ModelForm):
    class Meta:
        model = Customer
        fields = ('phone', 'image')


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=75, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
        help_texts = {
            'username': None,
            'first_name':None,
            'last_name':None,
        }
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'


class UpdationForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['customer']
        help_texts = {
            'image': None,
        }
        widgets = {
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control'
            }),

        }