#importando formularios predeterminados de Django
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


#FOrmulario ya creado y se hereda
class CustomUserCreationForm(UserCreationForm):
      error_class = "is_invalid"

      def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.fields["username"].widget.attrs.update({"class":"form-control"})
            self.fields["first_name"].widget.attrs.update({"class":"form-control"})
            self.fields["last_name"].widget.attrs.update({"class":"form-control"})
            self.fields["email"].widget.attrs.update({"class":"form-control"})
            self.fields["password1"].widget.attrs.update({"class":"form-control"})
            self.fields["password2"].widget.attrs.update({"class":"form-control"})

      class Meta: #es una metaclase ya solo se reutiliza
            model = User
            fields = ['username','first_name','last_name','email','password1','password2']

class CustomAuthenticationForm(AuthenticationForm):
      error_class = "is_invalid"
      class Meta:
            model = User
            fields = ['username', 'password']