from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('login')),
    path('login/', views.pagina_login, name='login'),
    path('cadastro/', views.pagina_cadastro, name='cadastro'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.sair, name='logout'),
]
