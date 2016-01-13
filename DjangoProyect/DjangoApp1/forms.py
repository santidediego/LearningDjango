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
    nombre = forms.CharField (max_length=15, label= "Nombre de la tapa")
    
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Tapas
        exclude = ('bar',)
        fields = ('nombre',)
    
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # If url is not empty and doesn't start with 'http://', prepend 'http://'.
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

        return cleaned_data