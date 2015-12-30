from django.contrib.auth.models import User
from django import forms
from DjangoApp1.models import Tapas

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
        
class TapaForm(forms.ModelForm):
    bar = forms.SlugField (max_length=20, label= "Bar al que pertenece")
    tapa = forms.SlugField (max_length=15, label= "Nombre de la tapa")
    
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Tapas
        fields = ('bar','tapa')