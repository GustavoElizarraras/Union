"""hackaton URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from usuarios import views as usuario_view
from optimizacion import views as optimizacion_view
from aportes import views as aportes_view

urlpatterns = [
    path('admin/', admin.site.urls),

    #Usuarios
    path('users/login/', usuario_view.login_view, name='login'),
    path('users/logout/', usuario_view.logout_view, name='logout'),
    path('users/signup/', usuario_view.signup_view, name='signup'),

    #Optimizacion
    path('', optimizacion_view.home, name='home'),
    #Aportes
]
