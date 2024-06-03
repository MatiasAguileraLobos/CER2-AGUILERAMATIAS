from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import PropuestaProyecto

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class PropuestaProyectoForm(forms.ModelForm):
    class Meta:
        model = PropuestaProyecto
        fields = ['nombre_proyecto', 'tema']