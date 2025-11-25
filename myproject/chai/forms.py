from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name',
            }
        ),
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
            }
        ),
    )

    message = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your message',
                'rows': 4,
            }
        ),
    )

    contactmethod = forms.ChoiceField(
        choices=[
            ('email', 'Email'),
            ('phone', 'Phone'),
            ('both', 'Both'),
        ],
        widget=forms.RadioSelect,
    )




class CalculatorForm(forms.Form):
    OPERATIONS = (
        ('add', 'Add (+)'),
        ('sub', 'Subtract (−)'),
        ('mul', 'Multiply (×)'),
        ('div', 'Divide (÷)'),
        ('mod', 'Modulus (%)'),
    )

    number1 = forms.FloatField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'First number',
                'step': 'any',
            }
        ),
        label='Number 1'
    )

    number2 = forms.FloatField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Second number',
                'step': 'any',
            }
        ),
        label='Number 2'
    )

    operation = forms.ChoiceField(
        choices=OPERATIONS,
        required=True,
        widget=forms.Select(
            attrs={
                'class': 'form-select',
            }
        ),
        label='Operation'
    )

 
class InputForm(forms.Form):
    name=forms.CharField(max_length=100)
    email=forms.EmailField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)

class Signup(forms.Form):
    username=forms.CharField(max_length=100)
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)

from .models import FormModel
class SignupForm1(forms.ModelForm):
    class Meta:
        model= FormModel
        fields= "__all__"

from .models import Blogpost
class BlogForm(forms.ModelForm):
    class Meta:
        model=Blogpost
        fields="__all__"