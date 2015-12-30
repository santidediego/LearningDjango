from django.shortcuts import render  #For render templates
from DjangoApp1.models import Bares, Tapas
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from DjangoApp1.forms import LoginForm, RegisterForm, TapaForm
from django.contrib.auth.decorators import login_required

''' Basic index
def index(request):
    return HttpResponse("Hello world!")
'''

#Now we show an index with templates

def index(request):
    #Ordenamos los bares en orden descendente por nombre
    bares_list = Bares.objects.order_by('-nombre')
    context_dict = {'bares': bares_list}

    # Render the response and send it back!
    return render(request, 'DjangoApp1/index.html', context_dict)

def bares(request, bar_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:

        bar = Bares.objects.get(slug=bar_name_slug)
        context_dict['bar_nombre'] = bar.nombre


        tapas = Tapas.objects.filter(bar=bar)

        context_dict['tapas'] = tapas

        context_dict['bar'] = bar
    except Bares.DoesNotExist:

        pass

    # Go render the response and return it to the client.
    return render(request, 'DjangoApp1/bar.html', context_dict)



def login_view(request):	# no se llama 'login'
	form = LoginForm()
	context = { 'form': form, 'mensaje':'Logeandose'}

	if request.method == 'POST':		
		form = LoginForm(request.POST)		
		usuario = request.POST.get('username')
		contrase = request.POST.get('password')
		# Hacer el login
		user = authenticate(username=usuario, password=contrase)
		if user is not None and user.is_active:
			login(request, user)
			context['mensaje'] =  u'Logeado como  %s, contraseña %s' % (usuario, contrase)
		else:
			context['mensaje'] =  u'No usuario  o contraseña incorrecta'
	   	
	return render (request, 'DjangoApp1/login.html', context)

def register(request):	
	form = RegisterForm()
	context = { 'mensaje': 'Estamos en  Registro', 'form': form,}

	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():		
			# Save the user's form data to the database.
			user = form.save()
                       # Now we hash the password with the set_password method.
                       # Once hashed, we can update the user object.
			user.set_password(user.password)
			user.save()						
			context['mensaje'] =  u'Registrado como  %s' % (user.username)		
		else:
			context['form'] = form
	   	
	return render (request, 'DjangoApp1/registro.html', context)
    
@login_required
def add_tapa(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = TapaForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = TapaForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'DjangoApp1/add_tapa.html', {'form': form})