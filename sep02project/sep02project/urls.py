"""
URL configuration for sep02project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from sep02app.views import *
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name="home"),
    path('samsung/',samsung, name="samsung"),
    path('vivo/',vivo, name="vivo"),
    path('redmi/',redmi, name="redmi"),
    path('oppo/', oppo, name="oppo"),
    path('hp/',hp, name="hp"),
    path('honor/', honor,name="honor"),
    path('asus/', asus,name="asus"),
    path('dell/', dell,name="dell"),
    path('msi/', msi,name="msi"),
    path('lenovo/', lenovo,name="lenovo"),
    path('acer/', acer,name="acer"),
    path('infinix/', infinix,name="infinix"),
    path('products/',products ,name="products"),
    path("",login_user,name="login"),
    path("register/",register,name="register"),
    path("logout/",logout_user,name="logout"),
    path("contact/",contact,name="contact"),
    
]
