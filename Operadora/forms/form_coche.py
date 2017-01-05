from .forms import *

class formCoche(forms.Form):
    def __init__(self, *args, **kwargs):
        super(formCoche, self).__init__(*args, **kwargs)

    def validarDNI(value):
        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
        dig_ext = "XYZ"
        reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
        numeros = "1234567890"
        dni = value.upper()
        if len(dni) == 9:
            dig_control = dni[8]
            dni = dni[:8]
            if dni[0] in dig_ext:
                dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
            if not len(dni) == len([n for n in dni if n in numeros]) \
                    and tabla[int(dni) % 23] == dig_control:
                raise ValidationError(_(my_default_errors_DNI['invalido']))

    # PERSONALES
    name = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                           error_messages=my_default_errors_Name)
    dni = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                          error_messages=my_default_errors_DNI, validators=[validarDNI])
    direccion = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                error_messages=my_default_errors_direccion, required=False)
    email = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                            error_messages=my_default_errors_email, validators=[validate_email])
    telefono = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    movil = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                               error_messages=my_default_errors_movil)
    fechanacimiento = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}),
        error_messages=my_default_errors_fechanacimiento)
    nacionalidad = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                   error_messages=my_default_errors_nacionalidad)
    estadocivil = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                    choices=EstatsCivils, required=False)
    tipocasado = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                   choices=TipoCasado, required=False)
    numerohijos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    mayoresdeedad = forms.BooleanField(initial=False, required=False)
    cuantosacargo = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    ingresohijos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    anotacionespersonales = forms.CharField(widget=forms.Textarea(
        attrs={"max_length": 500, "rows": 5, "placeholder": "Anotaciones para los datos personales...",
               "class": "form-control"}), required=False)
    # EMPRESA
    cotizacion = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                   choices=Cotiza, required=False)
    tipotrabajo = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                    choices=TipWork, required=False)
    finalizacontrato = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}),
        required=False)
    nombreempresa1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                     required=False)
    cargoempresa1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                    required=False)
    actividadempresa1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                        required=False)
    ingresosempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    pagasempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    otrosingresosempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    antiguedadempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    nombreempresa2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                     required=False)
    cargoempresa2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                    required=False)
    actividadempresa2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                        required=False)
    ingresosempresa2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    pagasempresa2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    otrosingresosempresa2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    antiguedadempresa2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    nombreempresa3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                     required=False)
    cargoempresa3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                    required=False)
    actividadempresa3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                        required=False)
    ingresosempresa3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    pagasempresa3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    otrosingresosempresa3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    antiguedadempresa3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    importejuvilacion = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    numerodepagasjuvilacion = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                 required=False)
    iniciojuvilacion = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}),
        required=False)
    finjuvilacion = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}),
        required=False)
    parodesdecuando = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}),
        required=False)
    parocuantocobra = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    otrosingresos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    otrosgastos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    otrosingresostexto = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                         required=False)
    otrosgastostexto = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                       required=False)
    anotacionesingresos = forms.CharField(widget=forms.Textarea(
        attrs={"max_length": 500, "rows": 5, "placeholder": "Anotaciones para los ingresos...",
               "class": "form-control"}), required=False)
    # VIVIENDA 1
    viviendavalor1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendavalorhipoteca1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaestapagada1 = forms.BooleanField(initial=False, required=False)
    viviendalibredecargos1 = forms.BooleanField(initial=False, required=False)
    viviendacuotamensual1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaanos1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaentidad1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                       required=False)
    viviendametros1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaporciento1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendadireccion1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendapoblacion1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendaprovincia1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendacodigopostal1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendavalor2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendavalorhipoteca2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaestapagada2 = forms.BooleanField(initial=False, required=False)
    viviendalibredecargos2 = forms.BooleanField(initial=False, required=False)
    viviendacuotamensual2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaanos2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaentidad2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                       required=False)
    viviendametros2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaporciento2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendadireccion2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendapoblacion2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendaprovincia2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendacodigopostal2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendavalor3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendavalorhipoteca3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaestapagada3 = forms.BooleanField(initial=False, required=False)
    viviendalibredecargos3 = forms.BooleanField(initial=False, required=False)
    viviendacuotamensual3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaanos3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaentidad3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                       required=False)
    viviendametros3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaporciento3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendadireccion3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendapoblacion3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendaprovincia3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendacodigopostal3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    # VIVIENDA2
    viviendaalquiladavalor1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                 required=False)
    viviendaalquiladavalorhipoteca1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                         required=False)
    viviendaalquiladaestapagada1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladalibredecargos1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladacuotamensual1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                        required=False)
    viviendaalquiladaanos1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaalquiladaentidad1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladametros1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                  required=False)
    viviendaalquiladaporciento1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                     required=False)
    viviendaalquiladadireccion1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladapoblacion1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladaprovincia1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladacodigopostal1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                        required=False)
    viviendaalquiladacobraalquiler1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                         required=False)
    viviendaalquiladavalor2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                 required=False)
    viviendaalquiladavalorhipoteca2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                         required=False)
    viviendaalquiladaestapagada2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladalibredecargos2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladacuotamensual2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                        required=False)
    viviendaalquiladaanos2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaalquiladaentidad2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladametros2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                  required=False)
    viviendaalquiladaporciento2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                     required=False)
    viviendaalquiladadireccion2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladapoblacion2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladaprovincia2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladacodigopostal2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                        required=False)
    viviendaalquiladacobraalquiler2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                         required=False)
    viviendaalquiladavalor3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                 required=False)
    viviendaalquiladavalorhipoteca3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                         required=False)
    viviendaalquiladaestapagada3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladalibredecargos3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladacuotamensual3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                        required=False)
    viviendaalquiladaanos3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaalquiladaentidad3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladametros3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                  required=False)
    viviendaalquiladaporciento3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                     required=False)
    viviendaalquiladadireccion3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladapoblacion3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladaprovincia3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladacodigopostal3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                        required=False)
    viviendaalquiladacobraalquiler3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                         required=False)
    # VIVIENDA3
    alquilerpaga1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilermetros1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilerdireccion1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilerpoblacion1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilerprovincia1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilercodigopostal1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilerpaga2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilermetros2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilerdireccion2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilerpoblacion2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilerprovincia2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilercodigopostal2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilerpaga3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilermetros3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilerdireccion3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilerpoblacion3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilerprovincia3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilercodigopostal3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    # VIVIENDA4
    direccionpersonal = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                        required=False)
    poblacionpersonal = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                        required=False)
    provinciapersonal = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                        required=False)
    codigopostalpersonal = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    anotacionesviviendas = forms.CharField(widget=forms.Textarea(
        attrs={"max_length": 500, "rows": 5, "placeholder": "Anotaciones para las viviendas...",
               "class": "form-control"}), required=False)
    # CREDITOS
    creditotipo1 = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                     choices=CredTip, required=False)
    creditotantoporciento1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditoimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditocuota1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditoentidad1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                      required=False)
    creditotipo2 = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                     choices=CredTip, required=False)
    creditotantoporciento2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditoimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditocuota2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditoentidad2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                      required=False)
    creditotipo3 = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                     choices=CredTip, required=False)
    creditotantoporciento3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditoimporte3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditocuota3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditoentidad3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                      required=False)
    # TARJETAS
    tarjetacuota1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    tarjetaimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    tarjetaentidad1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                      required=False)
    tarjetacuota2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    tarjetaimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    tarjetaentidad2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                      required=False)
    tarjetacuota3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    tarjetaimporte3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    tarjetaentidad3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                      required=False)
    # RECIVOS
    recivosimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    recivosimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    recivosimporte3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    # MOROSOS
    morosoimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    morosoquien1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                   required=False)
    morosoimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    morosoquien2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                   required=False)
    morosoimporte3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    morosoquien3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                   required=False)
    anotacionesfinancieras = forms.CharField(widget=forms.Textarea(
        attrs={"max_length": 500, "rows": 5, "placeholder": "Anotaciones para los datos financieros...",
               "class": "form-control"}), required=False)
    # COCHE
    motor = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}))
    marca = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}))
    modelo = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}))
    antiguedad = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}))
    matricula = forms.CharField(widget=forms.TextInput(attrs={"max_length": 10, "class": "form-control"}))
    estadovehiculo = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}))
    anotacionescoche = forms.CharField(widget=forms.Textarea(
        attrs={"max_length": 500, "rows": 5, "placeholder": "Anotaciones para los datos del coche...",
               "class": "form-control"}), required=False)
    metodopago = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                   choices=RecibirMoney, required=False)
    anotacionesdestinado = forms.CharField(widget=forms.Textarea(
        attrs={"max_length": 500, "rows": 5, "placeholder": "Anotaciones para que va destinada la solicitud...",
               "class": "form-control"}), required=False)
    justificante = forms.BooleanField(initial=False, required=False)
    autorizacion = forms.BooleanField(initial=False, required=False)
    medio = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                              choices=Medios, required=False)
    anotacionesgenerales = forms.CharField(widget=forms.Textarea(
        attrs={"max_length": 500, "rows": 5, "placeholder": "Observaciones generales...",
               "class": "form-control"}), required=False)

    def clean(self):
        cleaned_data = super(formCoche, self).clean()
        name = cleaned_data.get("name")
        dni = cleaned_data.get("dni")
        direccion = cleaned_data.get("direccion")
        email = cleaned_data.get("email")
        telefono = cleaned_data.get("telefono")
        movil = cleaned_data.get("movil")
        fechanacimiento = cleaned_data.get("fechanacimiento")
        nacionalidad = cleaned_data.get("nacionalidad")
        estadocivil = cleaned_data.get("estadocivil")
        tipocasado = cleaned_data.get("tipocasado")
        numerohijos = cleaned_data.get("numerohijos")
        mayoresdeedad = cleaned_data.get("mayoresdeedad")
        cuantosacargo = cleaned_data.get("cuantosacargo")
        ingresohijos = cleaned_data.get("ingresohijos")
        anotacionespersonales = cleaned_data.get("anotacionespersonales")
        cotizacion = cleaned_data.get("cotizacion")
        tipotrabajo = cleaned_data.get("tipotrabajo")
        finalizacontrato = cleaned_data.get("finalizacontrato")
        nombreempresa1 = cleaned_data.get("nombreempresa1")
        cargoempresa1 = cleaned_data.get("cargoempresa1")
        actividadempresa1 = cleaned_data.get("actividadempresa1")
        ingresosempresa1 = cleaned_data.get("ingresosempresa1")
        pagasempresa1 = cleaned_data.get("pagasempresa1")
        otrosingresosempresa1 = cleaned_data.get("otrosingresosempresa1")
        antiguedadempresa1 = cleaned_data.get("antiguedadempresa1")
        nombreempresa2 = cleaned_data.get("nombreempresa2")
        cargoempresa2 = cleaned_data.get("cargoempresa2")
        actividadempresa2 = cleaned_data.get("actividadempresa2")
        ingresosempresa2 = cleaned_data.get("ingresosempresa2")
        pagasempresa2 = cleaned_data.get("pagasempresa2")
        otrosingresosempresa2 = cleaned_data.get("otrosingresosempresa2")
        antiguedadempresa2 = cleaned_data.get("antiguedadempresa2")
        nombreempresa3 = cleaned_data.get("nombreempresa3")
        cargoempresa3 = cleaned_data.get("cargoempresa3")
        actividadempresa3 = cleaned_data.get("actividadempresa3")
        ingresosempresa3 = cleaned_data.get("ingresosempresa3")
        pagasempresa3 = cleaned_data.get("pagasempresa3")
        otrosingresosempresa3 = cleaned_data.get("otrosingresosempresa3")
        antiguedadempresa3 = cleaned_data.get("antiguedadempresa3")
        importejuvilacion = cleaned_data.get("importejuvilacion")
        numerodepagasjuvilacion = cleaned_data.get("numerodepagasjuvilacion")
        iniciojuvilacion = cleaned_data.get("iniciojuvilacion")
        finjuvilacion = cleaned_data.get("finjuvilacion")
        parodesdecuando = cleaned_data.get("parodesdecuando")
        parocuantocobra = cleaned_data.get("parocuantocobra")
        otrosingresos = cleaned_data.get("otrosingresos")
        otrosgastos = cleaned_data.get("otrosgastos")
        otrosingresostexto = cleaned_data.get("otrosingresostexto")
        otrosgastostexto = cleaned_data.get("otrosgastostexto")
        anotacionesingresos = cleaned_data.get("anotacionesingresos")
        viviendavalor1 = cleaned_data.get("viviendavalor1")
        viviendavalorhipoteca1 = cleaned_data.get("viviendavalorhipoteca1")
        viviendaestapagada1 = cleaned_data.get("viviendaestapagada1")
        viviendalibredecargos1 = cleaned_data.get("viviendalibredecargos1")
        viviendacuotamensual1 = cleaned_data.get("viviendacuotamensual1")
        viviendaanos1 = cleaned_data.get("viviendaanos1")
        viviendaentidad1 = cleaned_data.get("viviendaentidad1")
        viviendametros1 = cleaned_data.get("viviendametros1")
        viviendaporciento1 = cleaned_data.get("viviendaporciento1")
        viviendadireccion1 = cleaned_data.get("viviendadireccion1")
        viviendapoblacion1 = cleaned_data.get("viviendapoblacion1")
        viviendaprovincia1 = cleaned_data.get("viviendaprovincia1")
        viviendacodigopostal1 = cleaned_data.get("viviendacodigopostal1")
        viviendavalor2 = cleaned_data.get("viviendavalor2")
        viviendavalorhipoteca2 = cleaned_data.get("viviendavalorhipoteca2")
        viviendaestapagada2 = cleaned_data.get("viviendaestapagada2")
        viviendalibredecargos2 = cleaned_data.get("viviendalibredecargos2")
        viviendacuotamensual2 = cleaned_data.get("viviendacuotamensual2")
        viviendaanos2 = cleaned_data.get("viviendaanos2")
        viviendaentidad2 = cleaned_data.get("viviendaentidad2")
        viviendametros2 = cleaned_data.get("viviendametros2")
        viviendaporciento2 = cleaned_data.get("viviendaporciento2")
        viviendadireccion2 = cleaned_data.get("viviendadireccion2")
        viviendapoblacion2 = cleaned_data.get("viviendapoblacion2")
        viviendaprovincia2 = cleaned_data.get("viviendaprovincia2")
        viviendacodigopostal2 = cleaned_data.get("viviendacodigopostal2")
        viviendavalor3 = cleaned_data.get("viviendavalor3")
        viviendavalorhipoteca3 = cleaned_data.get("viviendavalorhipoteca3")
        viviendaestapagada3 = cleaned_data.get("viviendaestapagada3")
        viviendalibredecargos3 = cleaned_data.get("viviendalibredecargos3")
        viviendacuotamensual3 = cleaned_data.get("viviendacuotamensual3")
        viviendaanos3 = cleaned_data.get("viviendaanos3")
        viviendaentidad3 = cleaned_data.get("viviendaentidad3")
        viviendametros3 = cleaned_data.get("viviendametros3")
        viviendaporciento3 = cleaned_data.get("viviendaporciento3")
        viviendadireccion3 = cleaned_data.get("viviendadireccion3")
        viviendapoblacion3 = cleaned_data.get("viviendapoblacion3")
        viviendaprovincia3 = cleaned_data.get("viviendaprovincia3")
        viviendacodigopostal3 = cleaned_data.get("viviendacodigopostal3")
        viviendaalquiladavalor1 = cleaned_data.get("viviendaalquiladavalor1")
        viviendaalquiladavalorhipoteca1 = cleaned_data.get("viviendaalquiladavalorhipoteca1")
        viviendaalquiladaestapagada1 = cleaned_data.get("viviendaalquiladaestapagada1")
        viviendaalquiladalibredecargos1 = cleaned_data.get("viviendaalquiladalibredecargos1")
        viviendaalquiladacuotamensual1 = cleaned_data.get("viviendaalquiladacuotamensual1")
        viviendaalquiladaanos1 = cleaned_data.get("viviendaalquiladaanos1")
        viviendaalquiladaentidad1 = cleaned_data.get("viviendaalquiladaentidad1")
        viviendaalquiladametros1 = cleaned_data.get("viviendaalquiladametros1")
        viviendaalquiladaporciento1 = cleaned_data.get("viviendaalquiladaporciento1")
        viviendaalquiladadireccion1 = cleaned_data.get("viviendaalquiladadireccion1")
        viviendaalquiladapoblacion1 = cleaned_data.get("viviendaalquiladapoblacion1")
        viviendaalquiladaprovincia1 = cleaned_data.get("viviendaalquiladaprovincia1")
        viviendaalquiladacodigopostal1 = cleaned_data.get("viviendaalquiladacodigopostal1")
        viviendaalquiladacobraalquiler1 = cleaned_data.get("viviendaalquiladacobraalquiler1")
        viviendaalquiladavalor2 = cleaned_data.get("viviendaalquiladavalor2")
        viviendaalquiladavalorhipoteca2 = cleaned_data.get("viviendaalquiladavalorhipoteca2")
        viviendaalquiladaestapagada2 = cleaned_data.get("viviendaalquiladaestapagada2")
        viviendaalquiladalibredecargos2 = cleaned_data.get("viviendaalquiladalibredecargos2")
        viviendaalquiladacuotamensual2 = cleaned_data.get("viviendaalquiladacuotamensual2")
        viviendaalquiladaanos2 = cleaned_data.get("viviendaalquiladaanos2")
        viviendaalquiladaentidad2 = cleaned_data.get("viviendaalquiladaentidad2")
        viviendaalquiladametros2 = cleaned_data.get("viviendaalquiladametros2")
        viviendaalquiladaporciento2 = cleaned_data.get("viviendaalquiladaporciento2")
        viviendaalquiladadireccion2 = cleaned_data.get("viviendaalquiladadireccion2")
        viviendaalquiladapoblacion2 = cleaned_data.get("viviendaalquiladapoblacion2")
        viviendaalquiladaprovincia2 = cleaned_data.get("viviendaalquiladaprovincia2")
        viviendaalquiladacodigopostal2 = cleaned_data.get("viviendaalquiladacodigopostal2")
        viviendaalquiladacobraalquiler2 = cleaned_data.get("viviendaalquiladacobraalquiler2")
        viviendaalquiladavalor3 = cleaned_data.get("viviendaalquiladavalor3")
        viviendaalquiladavalorhipoteca3 = cleaned_data.get("viviendaalquiladavalorhipoteca3")
        viviendaalquiladaestapagada3 = cleaned_data.get("viviendaalquiladaestapagada3")
        viviendaalquiladalibredecargos3 = cleaned_data.get("viviendaalquiladalibredecargos3")
        viviendaalquiladacuotamensual3 = cleaned_data.get("viviendaalquiladacuotamensual3")
        viviendaalquiladaanos3 = cleaned_data.get("viviendaalquiladaanos3")
        viviendaalquiladaentidad3 = cleaned_data.get("viviendaalquiladaentidad3")
        viviendaalquiladametros3 = cleaned_data.get("viviendaalquiladametros3")
        viviendaalquiladaporciento3 = cleaned_data.get("viviendaalquiladaporciento3")
        viviendaalquiladadireccion3 = cleaned_data.get("viviendaalquiladadireccion3")
        viviendaalquiladapoblacion3 = cleaned_data.get("viviendaalquiladapoblacion3")
        viviendaalquiladaprovincia3 = cleaned_data.get("viviendaalquiladaprovincia3")
        viviendaalquiladacodigopostal3 = cleaned_data.get("viviendaalquiladacodigopostal3")
        viviendaalquiladacobraalquiler3 = cleaned_data.get("viviendaalquiladacobraalquiler3")
        alquilerpaga1 = cleaned_data.get("alquilerpaga1")
        alquilermetros1 = cleaned_data.get("alquilermetros1")
        alquilerdireccion1 = cleaned_data.get("alquilerdireccion1")
        alquilerpoblacion1 = cleaned_data.get("alquilerpoblacion1")
        alquilerprovincia1 = cleaned_data.get("alquilerprovincia1")
        alquilercodigopostal1 = cleaned_data.get("alquilercodigopostal1")
        alquilerpaga2 = cleaned_data.get("alquilerpaga2")
        alquilermetros2 = cleaned_data.get("alquilermetros2")
        alquilerdireccion2 = cleaned_data.get("alquilerdireccion2")
        alquilerpoblacion2 = cleaned_data.get("alquilerpoblacion2")
        alquilerprovincia2 = cleaned_data.get("alquilerprovincia2")
        alquilercodigopostal2 = cleaned_data.get("alquilercodigopostal2")
        alquilerpaga3 = cleaned_data.get("alquilerpaga3")
        alquilermetros3 = cleaned_data.get("alquilermetros3")
        alquilerdireccion3 = cleaned_data.get("alquilerdireccion3")
        alquilerpoblacion3 = cleaned_data.get("alquilerpoblacion3")
        alquilerprovincia3 = cleaned_data.get("alquilerprovincia3")
        alquilercodigopostal3 = cleaned_data.get("alquilercodigopostal3")
        direccionpersonal = cleaned_data.get("direccionpersonal")
        poblacionpersonal = cleaned_data.get("poblacionpersonal")
        provinciapersonal = cleaned_data.get("provinciapersonal")
        codigopostalpersonal = cleaned_data.get("codigopostalpersonal")
        anotacionesviviendas = cleaned_data.get("anotacionesviviendas")
        creditotipo1 = cleaned_data.get("creditotipo1")
        creditotantoporciento1 = cleaned_data.get("creditotantoporciento1")
        creditoimporte1 = cleaned_data.get("creditoimporte1")
        creditocuota1 = cleaned_data.get("creditocuota1")
        creditoentidad1 = cleaned_data.get("creditoentidad1")
        creditotipo2 = cleaned_data.get("creditotipo2")
        creditotantoporciento2 = cleaned_data.get("creditotantoporciento2")
        creditoimporte2 = cleaned_data.get("creditoimporte2")
        creditocuota2 = cleaned_data.get("creditocuota2")
        creditoentidad2 = cleaned_data.get("creditoentidad2")
        creditotipo3 = cleaned_data.get("creditotipo3")
        creditotantoporciento3 = cleaned_data.get("creditotantoporciento3")
        creditoimporte3 = cleaned_data.get("creditoimporte3")
        creditocuota3 = cleaned_data.get("creditocuota3")
        creditoentidad3 = cleaned_data.get("creditoentidad3")
        tarjetacuota1 = cleaned_data.get("tarjetacuota1")
        tarjetaimporte1 = cleaned_data.get("tarjetaimporte1")
        tarjetaentidad1 = cleaned_data.get("tarjetaentidad1")
        tarjetacuota2 = cleaned_data.get("tarjetacuota2")
        tarjetaimporte2 = cleaned_data.get("tarjetaimporte2")
        tarjetaentidad2 = cleaned_data.get("tarjetaentidad2")
        tarjetacuota3 = cleaned_data.get("tarjetacuota3")
        tarjetaimporte3 = cleaned_data.get("tarjetaimporte3")
        tarjetaentidad3 = cleaned_data.get("tarjetaentidad3")
        recivosimporte1 = cleaned_data.get("recivosimporte1")
        recivosimporte2 = cleaned_data.get("recivosimporte2")
        recivosimporte3 = cleaned_data.get("recivosimporte3")
        morosoimporte1 = cleaned_data.get("morosoimporte1")
        morosoquien1 = cleaned_data.get("morosoquien1")
        morosoimporte2 = cleaned_data.get("morosoimporte2")
        morosoquien2 = cleaned_data.get("morosoquien2")
        morosoimporte3 = cleaned_data.get("morosoimporte3")
        morosoquien3 = cleaned_data.get("morosoquien3")
        anotacionesfinancieras = cleaned_data.get("anotacionesfinancieras")
        motor = cleaned_data.get("motor")
        marca = cleaned_data.get("marca")
        modelo = cleaned_data.get("modelo")
        antiguedad = cleaned_data.get("antiguedad")
        matricula = cleaned_data.get("matricula")
        estadovehiculo = cleaned_data.get("estadovehiculo")
        anotacionescoche = cleaned_data.get("anotacionescoche")
        metodopago = cleaned_data.get("metodopago")
        anotacionesdestinado = cleaned_data.get("anotacionesdestinado")
        justificante = cleaned_data.get("justificante")
        autorizacion = cleaned_data.get("autorizacion")
        medio = cleaned_data.get("medio")
        anotacionesgenerales = cleaned_data.get("anotacionesgenerales")
