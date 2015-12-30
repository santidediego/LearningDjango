from django.contrib.auth.models import User
from django import forms

class LoginForm(forms.ModelForm):
    username = forms.SlugField (max_length=8, 
	                             label='Usuario: ')
    password = forms.SlugField (max_length=8, 
	                        widget=forms.PasswordInput(),  
	                        label='Contraseña:',
	                        help_text='Hasta 8 letras')                       
    class Meta:
        model  = User
        fields = ('username',  'password')
        
class RegisterForm(forms.ModelForm):
	username = forms.SlugField (max_length=8, label='Usuario:')
	email    = forms.EmailField (label='Email:')
	password = forms.SlugField (max_length=8, 
	                   help_text="(números y letras hasta 8)", 
	                   widget=forms.PasswordInput(),  
	                   label='Contraseña:')
	class Meta:
		model  = User
		fields = ('username', 'email', 'password')