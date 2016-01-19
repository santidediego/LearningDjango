from django.shortcuts import render  #For render templates
from DjangoApp1.models import Bares, Tapas
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from DjangoApp1.forms import LoginForm, RegisterForm, TapaForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

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
    bar.num_visitas=bar.num_visitas+1
    bar.save()
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
			return HttpResponseRedirect('/DjangoApp1/')
		else:
			context['mensaje'] =  u'No usuario  o contraseña incorrecta'

	return render (request, 'DjangoApp1/login.html', context)

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/DjangoApp1/')

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
def add_tapa(request, bar_name_slug):

    try:
        bar = Bares.objects.get(slug=bar_name_slug)
    except Bares.DoesNotExist:
                bar = None

    if request.method == 'POST':
        form = TapaForm(request.POST)
        if form.is_valid():
            if bar:
                tapa = form.save(commit=False)
                tapa.bar = bar
                tapa.votos = 0
                tapa.save()
                # probably better to use a redirect here.
                return redirect('add_tapa',bar_name_slug)
        else:
            print (form.errors)
    else:
        form = TapaForm()

    context_dict = {'form':form, 'bar': bar}

    return render(request, 'DjangoApp1/add_tapa.html', context_dict)



def reclama_datos(request):
	lista_bares = Bares.objects.order_by('nombre')
	datos={}
	datos[0]=list()
	datos[1]=list()
	for bar in lista_bares:
		datos[0].append(bar.nombre)
		datos[1].append(bar.num_visitas)
	return JsonResponse(datos, safe=False)
