"""PrestamoAsegurado URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^servicios/$', views.servicios, name='servicios'),
    url(r'^empresa/$', views.empresa, name='empresa'),
    url(r'^politica/$', views.politica, name='politica'),
    url(r'^aviso/$', views.aviso, name='aviso'),
    url(r'^gastos/$', views.gastos, name='gastos'),
    url(r'^cookies/$', views.cookies, name='cookies'),
]
