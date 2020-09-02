from django import forms
from .models import Cliente

class clienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields=['apellido','nombre','edad','email','sexo']