from django import forms
from .models import Rol
import re

class RolForm(forms.ModelForm):
     STATUS = {
         "True":"Activo",
         "False":"Inactivo"
    }
     
     error_css_class= "is_invalid"

     status = forms.ChoiceField(
         choices= list(STATUS.items()) ,
         widget= forms.Select(attrs={"class":"form-control"}) ,
         required=True
    )

     #constructor por defecto de Python()
     def __init__(self,*args,**kwargs): 
        super().__init__(*args,**kwargs)
        #Aqui agregamos clases de bootpstrap
        self.fields["nombre"].widget.attrs.update({"class":"form-control"})
        self.fields["descripcion"].widget.attrs.update({"class":"form-control"})
        
     
     class Meta:
          model= Rol 
          fields = ['nombre','descripcion','status']


     def clean_nombre(self):
         nombre = self.cleaned_data.get("nombre")
         if not nombre:
             raise forms.ValidationError("Este campo no puede estar vacio")
         if not re.match(r"^[a-zA-Z]$",nombre):
             raise forms.ValidationError("Este campo solo acepta letras") 
          
          
         
         return nombre
     
     def clean_descripcion(self):
         descripcion = self.cleaned_data.get("descripcion")
         if not descripcion:
             raise forms.ValidationError("Este campo no puede estar vacio")
         
         return descripcion


class RolForm2(forms.Form):
    
    STATUS = {
         "True":"Activo",
         "False":"Inactivo"
    }
     
    nombre = forms.CharField(max_length=50,label="Nombre")
    descripcion = forms.CharField(max_length=250,label="Descripcion")
    descripcion.widget.attrs.update({"class":"form-control"})
    status = forms.ChoiceField(
         choices= list(STATUS.items()) ,
         widget= forms.Select(attrs={"class":"form-control"}) ,
         required=True
    )

    correo= forms.EmailField(label="Correo Electronico")

    correo.widget.attrs.update({"class":"form-control"})
    #max_length=10,label="Telefono",min_length=10,
    telefono= forms.CharField(                             widget=forms.TextInput(attrs={'type':'tel'})
                              )
    telefono.widget.attrs.update({"class":"form-control"})

    password= forms.CharField(widget=forms.PasswordInput() )
    password.widget.attrs.update({"class":"form-control"})

    def clean_nombre(self):
         nombre = self.cleaned_data.get("nombre")
         if not nombre:
             raise forms.ValidationError("Este campo no puede estar vacio")
         if not re.match(r"^[a-zA-Z]$",nombre):
             raise forms.ValidationError("Este campo solo acepta letras") 
          
          
         
         return nombre
     
    def clean_descripcion(self):
         descripcion = self.cleaned_data.get("descripcion")
         if not descripcion:
             raise forms.ValidationError("Este campo no puede estar vacio")
         
         return descripcion
    
    def clean_telefono(self):
         telefono = self.cleaned_data.get("telefono")
         if not telefono:
             raise forms.ValidationError("Este campo no puede estar vacio")
         if not re.match(r"^\d{10}+$",telefono):
             raise forms.ValidationError("Este campo solo acepta numeros y debe contener solo 10 digitos ")
         
         return telefono
    
    
    def clean_correo(self):
         correo = self.cleaned_data.get("correo")
         if not correo:
             raise forms.ValidationError("Este campo no puede estar vacio")
         if not re.match(r"\A\w*@gmail.com",correo):
             raise forms.ValidationError("Verifique que su correo electronico este bien escrito y sea de gmail ")
         
         return correo