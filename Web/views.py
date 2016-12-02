import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import Context

from Web import forms
from Web import models


def index(request):
    return render(request, 'index.html')


def asnef(request):
    return render(request, 'asnef.html')


def coche(request):
    context = Context({})

    if request.method == 'POST':
        form = forms.formCoche(request.POST)
        if form.is_valid():
            # url
            target_url = form.cleaned_data['url']
            # direct connection
            target_dbms = form.cleaned_data['dbms']
            target_user = form.cleaned_data['user']
            target_password = form.cleaned_data['password']
            target_ip = form.cleaned_data['ip']
            target_port = form.cleaned_data['port']
            target_db_name = form.cleaned_data['db_name']
            # parameters
            c = form.cleaned_data['charset']
            v = form.cleaned_data['verbosity']
            l = form.cleaned_data['level']
            r = form.cleaned_data['risk']
            d = form.cleaned_data['depth']
            n = form.cleaned_data['name']
            m = form.cleaned_data['mail']
            mf = form.cleaned_data['mail_field']
            pc = form.cleaned_data['periodicity_checkbox']
            ed = form.cleaned_data['execute_date']
            pd = form.cleaned_data['periodicity']

            p = models.sqlmap_requests.objects.create(name=n, level=l, verbosity=v, risk=r,
                                                      depth=d,
                                                      charset=c, user=request.user,
                                                      mail=mf, execute_date=ed, periodicity=pd)
            return HttpResponseRedirect('/')
        else:
            print form.errors
    else:
        form = forms.formCoche()
        context.update({"form": form})
        lastNum = models.expediente.objects.all().order_by("numexp").reverse[0].values("numexp")
        fecha = datetime.now()
        if not lastNum:
            lastNum = 40000
        else:
            lastNum = 1
        context.update({"numexp": lastNum})
        context.update({"data": fecha.year+"-"+fecha.month+"-"+fecha.day})
        context.update({"hora": fecha.hour+":"+fecha.minute+":"+fecha.second})
        return render(request, 'coche.html', context)


def hipotecario(request):
    context = Context({})
    return render(request, 'hipotecario.html', context)


def microcredito(request):
    context = Context({})
    return render(request, 'microcredito.html', context)


def personal(request):
    context = Context({})
    return render(request, 'personal.html', context)
