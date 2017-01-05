from .views import *


def group_check(user):
    return user.groups.filter(name__in=['Operadoras'])


@login_required(login_url="/")
@user_passes_test(group_check)
def asnef(request, numexp):
    context = {}
    if request.method == 'POST':
        form = forms.formAsnef(request.POST)
        if form.is_valid():

            return HttpResponseRedirect('/formularios/enviado')
        else:
            context.update({'form': form})
    else:
        form = forms.formAsnef()
        models.expediente.objects.update(tipo="ASNEF")
        context.update({'form': form})
        context.update({"numexp": numexp})
    return render(request, 'form_asnef.html', context)
