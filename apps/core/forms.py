from django import forms
#importando formularios predeterminados de Django
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#FOrmulario ya creado y se hereda
class CustomUserCreationForm(UserCreationForm):
        class Meta: #es una metaclase ya solo se reutiliza
                model = User
                fields = ['username','first_name','last_name','email','password1','password2']



