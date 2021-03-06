from django.conf.urls import patterns, url
from DjangoApp1 import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        #url(r'^about/$', views.about, name='about'),
        url(r'^bar/(?P<bar_name_slug>[\w\-]+)/$', views.bares, name='bar'),# New!
        url(r'^login/$', views.login_view, name='login'),
        url(r'^register/$', views.register, name='register'), # ADD NEW PATTERN!
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^add_tapa/(?P<bar_name_slug>[\w\-]+)/$', views.add_tapa, name='add_tapa'), # NEW MAPPING!
        url(r'^reclama_datos/$', views.reclama_datos, name='reclama_datos'),
        ) 


'''
El caracter r antes de la cadena de texto indica que es una cadena de caracteres en crudo. Esto permite que no tengamos que poner constantemente sentencias de escape para caracteres propios de expresiones regulares.
El caracter ^ indica el comienzo de nuestra expresión.
El caracter $ indica el fin de nuestra expresión.

'''
