from django.contrib import admin
from django.urls import path, include
from onlyflans.views import (
    landing, 
    acerca, 
    bienvenido, 
    contacto, 
    exito, 
    lista_reviews,
    add_review,
    flan_reviews,
    view_reviews,
    cerrarsesion,
    index,
    )

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name="landing"),
    path('acerca/', acerca, name="acerca"),
    path('bienvenido/', bienvenido, name="bienvenido"),
    path('contacto/', contacto, name="contacto"),
    path('exito/', exito, name='exito'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('reviews/', lista_reviews, name='lista_reviews'),
    path('flan/<slug:slug>/reviews/', flan_reviews, name='flan_reviews'), 
    path('flan/<slug:slug>/add_review/', add_review, name='add_review'),
    path('flan/<slug:flan_slug>/reseñas/', view_reviews, name='view_reviews'),
    path('cerrarsesion/', cerrarsesion, name="cerrarsesion"), 
    path('index/', index, name="index"),
]
