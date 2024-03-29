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
    url(r'asnef/(?P<numexp>[0-9]+)/$', views.asnef, name='asnef'),
    url(r'coche/(?P<numexp>[0-9]+)/$', views.coche, name='coche'),
    url(r'hipotecario/(?P<numexp>[0-9]+)/$', views.hipotecario, name='hipotecario'),
    url(r'microcredito/(?P<numexp>[0-9]+)/$', views.microcredito, name='microcredito'),
    url(r'personal/(?P<numexp>[0-9]+)/$', views.personal, name='personal'),
    url(r'expediente/(?P<numexp>[0-9]+)/$', views.expediente, name='expediente'),
    url(r'enviado/$', views.send, name='enviado'),
]
