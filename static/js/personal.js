$(document).ready(function() {
  $(window).keydown(function(event){
    if(event.keyCode == 13) {
      event.preventDefault();
      return false;
    }
  });
});
/**** Calcular Cuotas ****/
$(document).ready(function () {

    /* FORM 1*/

    $("#id_estadocivil").change(function () { //ESTADO CIVIL CASADO
        var estadocivil = $("#id_estadocivil").val();
        if (estadocivil == 'Casado') {
            div = document.getElementById('plsshw');
            div.style.display = "block";
            div2 = document.getElementById('plsshw2');
            div2.style.display = "none";
        } else {
            div = document.getElementById('plsshw');
            div.style.display = "none";
            div2 = document.getElementById('plsshw2');
            div2.style.display = "block";
        }
    });
    $("#id_numerohijos").change(function () { //AFEGEIX OPCIONS HIJOS
        var sons = $("#id_numerohijos").val();
        console.log(sons);
        if (sons >= 1) {
            div = document.getElementById('123hijos');
            div.style.display = "block";
        } else {
            div = document.getElementById('123hijos');
            div.style.display = "none";
        }
    });
    $("#id_cotizacion").change(function () { /*TIPO DE EMPRESA*/
        var empresatipo = $("#id_cotizacion").val();
        if (empresatipo == 'Ajena') {
            div = document.getElementById('ajenasi');
            div.style.display = "block";
            div2 = document.getElementById('ajenano');
            div2.style.display = "none";
        } else {
            div = document.getElementById('ajenasi');
            div.style.display = "none";
            div2 = document.getElementById('ajenano');
            div2.style.display = "block";
            $('#id_tipotrabajo').val(0);
            div = document.getElementById('tempsi');
            div.style.display = "none";
            $("#id_finalizacontrato").val(0);
        }
    });
    $("#id_tipotrabajo").change(function () { /*TIPO DE TRABAJO*/
        var empresaajena = $("#id_tipotrabajo").val();
        if (empresaajena == 'Temporal') {
            div = document.getElementById('tempsi');
            div.style.display = "block";
        } else {
            div = document.getElementById('tempsi');
            div.style.display = "none";
            $("#id_finalizacontrato").val(0);
        }
    });

    $("#id_importejuvilacion").change(function () { //1 de 2
        calculhelp();
    });
    $("#id_numerodepagasjuvilacion").change(function () { //2 de 2
        calculhelp();
    });
    function calculhelp() { //CALCULA 1 * 2
        var a = $('#id_importejuvilacion').val();
        var b = $('#id_numerodepagasjuvilacion').val();
        if (a != null && b != null) {
            $("#ayudatotal").val(a * b);
        }
        ;

    };
    $("#id_creditotipo1").change(function () { /*Afegeix Tantpercent*/
        var credaval = $("#id_creditotipo1").val();
        if (credaval == "Avalista") {
            div = document.getElementById('creditoaval1');
            div.style.display = "block";
        } else {
            div = document.getElementById('creditoaval1');
            div.style.display = "none";
        }
    });

    $("#id_creditotipo2").change(function () { /*Afegeix Tantpercent*/
        var credaval = $("#id_creditotipo2").val();
        if (credaval == "Avalista") {
            div = document.getElementById('creditoaval2');
            div.style.display = "block";
        } else {
            div = document.getElementById('creditoaval2');
            div.style.display = "none";
        }
    });

    $("#id_creditotipo3").change(function () { /*Afegeix Tantpercent*/
        var credaval = $("#id_creditotipo3").val();
        if (credaval == "Avalista") {
            div = document.getElementById('creditoaval3');
            div.style.display = "block";
        } else {
            div = document.getElementById('creditoaval3');
            div.style.display = "none";
        }
    });


    $("#id_viviendaestapagada1").change(function () { /*Si importe_select canvia*/
        if (("#id_viviendaestapagada1").prop("checked")) {
            div = document.getElementById('viviendapagada11');
            div.style.display = "none";
        } else {
            div = document.getElementById('viviendapagada11');
            div.style.display = "block";
        }
    });
    $("#id_viviendaestapagada2").change(function () { /*Si importe_select canvia*/
        if (("#id_viviendaestapagada2").is("checked")) {
            div = document.getElementById('viviendapagada22');
            div.style.display = "none";
        } else {
            div = document.getElementById('viviendapagada22');
            div.style.display = "block";
        }
    });
    $("#id_viviendaestapagada3").change(function () { /*Si importe_select canvia*/
        if (("#id_viviendaestapagada3").is("checked")) {
            div = document.getElementById('viviendapagada33');
            div.style.display = "none";
        } else {
            div = document.getElementById('viviendapagada33');
            div.style.display = "block";
        }
    });
    $("#viviendaalquiladaestapagada1").change(function () { /*Si importe_select canvia*/
        if (("#viviendaalquiladaestapagada1").is("checked")) {
            div = document.getElementById('viviendapagadaa11');
            div.style.display = "none";
        } else {
            div = document.getElementById('viviendapagadaa11');
            div.style.display = "block";
        }
    });
    $("#viviendaalquiladaestapagada2").change(function () { /*Si importe_select canvia*/
        if (("#viviendaalquiladaestapagada2").is("checked")) {
            div = document.getElementById('viviendapagadaa22');
            div.style.display = "none";
        } else {
            div = document.getElementById('viviendapagadaa22');
            div.style.display = "block";
        }
    });
    $("#viviendaalquiladaestapagada3").change(function () { /*Si importe_select canvia*/
        if (("#viviendaalquiladaestapagada3").is("checked")) {
            div = document.getElementById('viviendapagadaa33');
            div.style.display = "none";
        } else {
            div = document.getElementById('viviendapagadaa33');
            div.style.display = "block";
        }
    });


    /*FORM 2 AVALISTA*/
    $("#id_avalistastadocivil").change(function () { //ESTADO CIVIL CASADO
        var estadocivil = $("#id_avalistastadocivil").val();
        if (estadocivil == 'Casado') {
            div = document.getElementById('avalplsshw');
            div.style.display = "block";
            div2 = document.getElementById('avalplsshw2');
            div2.style.display = "none";
        } else {
            div = document.getElementById('avalplsshw');
            div.style.display = "none";
            div2 = document.getElementById('avalplsshw2');
            div2.style.display = "block";
        }
    });
    $("#id_avalistaumerohijos").change(function () { //AFEGEIX OPCIONS HIJOS
        var sons = $("#id_avalistaumerohijos").val();
        console.log(sons);
        if (sons >= 1) {
            div = document.getElementById('aval123hijos');
            div.style.display = "block";
        } else {
            div = document.getElementById('aval123hijos');
            div.style.display = "none";
        }
    });
    $("#id_avalistaotizacion").change(function () { /*TIPO DE EMPRESA*/
        var empresatipo = $("#id_avalistaotizacion").val();
        if (empresatipo == 'Ajena') {
            div = document.getElementById('avalajenasi');
            div.style.display = "block";
            div2 = document.getElementById('avalajenano');
            div2.style.display = "none";
        } else {
            div = document.getElementById('avalajenasi');
            div.style.display = "none";
            div2 = document.getElementById('avalajenano');
            div2.style.display = "block";
            $('#id_avalistaipotrabajo').val(0);
            div = document.getElementById('avaltempsi');
            div.style.display = "none";
            $("#id_avalistainalizacontrato").val(0);
        }
    });
    $("#id_avalistaipotrabajo").change(function () { /*TIPO DE TRABAJO*/
        var empresaajena = $("#id_avalistaipotrabajo").val();
        if (empresaajena == 'Temporal') {
            div = document.getElementById('avaltempsi');
            div.style.display = "block";
        } else {
            div = document.getElementById('avaltempsi');
            div.style.display = "none";
            $("#id_avalistainalizacontrato").val(0);
        }
    });

    $("#id_avalistamportejuvilacion").change(function () { //1 de 2
        calculhelp2();
    });
    $("#id_avalistaumerodepagasjuvilacion").change(function () { //2 de 2
        calculhelp2();
    });
    function calculhelp2() { //CALCULA 1 * 2
        var a = $('#id_avalistamportejuvilacion').val();
        var b = $('#id_avalistaumerodepagasjuvilacion').val();
        if (a != null && b != null) {
            $("#ayudatotalaval").val(a * b);
        }
        ;

    };
    $("#id_avalistareditotipo1").change(function () { /*Afegeix Tantpercent*/
        var credaval = $("#id_avalistareditotipo1").val();
        if (credaval == "Avalista") {
            div = document.getElementById('avalcreditoaval1');
            div.style.display = "block";
        } else {
            div = document.getElementById('avalcreditoaval1');
            div.style.display = "none";
        }
    });
    $("#id_avalistareditotipo2").change(function () { /*Afegeix Tantpercent*/
        var credaval = $("#id_avalistareditotipo2").val();
        if (credaval == "Avalista") {
            div = document.getElementById('avalcreditoaval2');
            div.style.display = "block";
        } else {
            div = document.getElementById('avalcreditoaval2');
            div.style.display = "none";
        }
    });


    /*FORM 2 MICRO*/
    $("#importe_select").change(function () { /*Si importe_select canvia*/
        calculamensualidades();
        lele();
    });
    $("#importe_select2").change(function () { /*Si importe_select2 canvia*/
        calculacuota();
    });


    function calculamensualidades() {
        var importe = $("#importe_select").val();
        if (importe == 0) {
            $('#importe_select2').children('option:not(:first)').remove();
            $("#cuotamensual").val(0);
        } else if (importe == 500) {
            $('#importe_select2').children('option:not(:first)').remove();
            $("#importe_select2").append('<option value="12">12</option>');
            $("#importe_select2").append('<option value="16">16</option>');
            $("#importe_select2").append('<option value="18">18</option>');
            $("#importe_select2").append('<option value="20">20</option>');
            $("#importe_select2").append('<option value="24">24</option>');
            $("#cuotamensual").val(0);
        } else if (importe == 1000) {
            $('#importe_select2').children('option:not(:first)').remove();
            $("#importe_select2").append('<option value="12">12</option>');
            $("#importe_select2").append('<option value="16">16</option>');
            $("#importe_select2").append('<option value="18">18</option>');
            $("#importe_select2").append('<option value="20">20</option>');
            $("#importe_select2").append('<option value="24">24</option>');
            $("#cuotamensual").val(0);
        } else if (importe == 2000) {
            $('#importe_select2').children('option:not(:first)').remove();
            $("#importe_select2").append('<option value="12">12</option>');
            $("#importe_select2").append('<option value="24">24</option>');
            $("#importe_select2").append('<option value="36">36</option>');
            $("#importe_select2").append('<option value="48">48</option>');
            $("#importe_select2").append('<option value="60">60</option>');
            $("#cuotamensual").val(0);
        } else if (importe == 3000) {
            $('#importe_select2').children('option:not(:first)').remove();
            $("#importe_select2").append('<option value="12">12</option>');
            $("#importe_select2").append('<option value="24">24</option>');
            $("#importe_select2").append('<option value="36">36</option>');
            $("#importe_select2").append('<option value="48">48</option>');
            $("#importe_select2").append('<option value="60">60</option>');
            $("#cuotamensual").val(0);
        } else if (importe == 4000) {
            $('#importe_select2').children('option:not(:first)').remove();
            $("#importe_select2").append('<option value="12">12</option>');
            $("#importe_select2").append('<option value="24">24</option>');
            $("#importe_select2").append('<option value="36">36</option>');
            $("#importe_select2").append('<option value="48">48</option>');
            $("#importe_select2").append('<option value="60">60</option>');
            $("#cuotamensual").val(0);
        } else if (importe == 5000) {
            $('#importe_select2').children('option:not(:first)').remove();
            $("#importe_select2").append('<option value="12">12</option>');
            $("#importe_select2").append('<option value="24">24</option>');
            $("#importe_select2").append('<option value="36">36</option>');
            $("#importe_select2").append('<option value="48">48</option>');
            $("#importe_select2").append('<option value="60">60</option>');
            $("#cuotamensual").val(0);
        } else if (importe == 6000) {
            $('#importe_select2').children('option:not(:first)').remove();
            $("#importe_select2").append('<option value="12">12</option>');
            $("#importe_select2").append('<option value="24">24</option>');
            $("#importe_select2").append('<option value="36">36</option>');
            $("#importe_select2").append('<option value="48">48</option>');
            $("#importe_select2").append('<option value="60">60</option>');
            $("#cuotamensual").val(0);
        } else if (importe == 8000) {
            $('#importe_select2').children('option:not(:first)').remove();
            $("#importe_select2").append('<option value="12">12</option>');
            $("#importe_select2").append('<option value="24">24</option>');
            $("#importe_select2").append('<option value="36">36</option>');
            $("#importe_select2").append('<option value="48">48</option>');
            $("#importe_select2").append('<option value="60">60</option>');
            $("#importe_select2").append('<option value="72">72</option>');
            $("#importe_select2").append('<option value="84">84</option>');
            $("#importe_select2").append('<option value="96">96</option>');
            $("#cuotamensual").val(0);
        } else if (importe == 10000) {
            $('#importe_select2').children('option:not(:first)').remove();
            $("#importe_select2").append('<option value="12">12</option>');
            $("#importe_select2").append('<option value="24">24</option>');
            $("#importe_select2").append('<option value="36">36</option>');
            $("#importe_select2").append('<option value="48">48</option>');
            $("#importe_select2").append('<option value="60">60</option>');
            $("#importe_select2").append('<option value="72">72</option>');
            $("#importe_select2").append('<option value="84">84</option>');
            $("#importe_select2").append('<option value="96">96</option>');
            $("#cuotamensual").val(0);
        } else if (importe == 12000) {
            $('#importe_select2').children('option:not(:first)').remove();
            $("#importe_select2").append('<option value="12">12</option>');
            $("#importe_select2").append('<option value="24">24</option>');
            $("#importe_select2").append('<option value="36">36</option>');
            $("#importe_select2").append('<option value="48">48</option>');
            $("#importe_select2").append('<option value="60">60</option>');
            $("#importe_select2").append('<option value="72">72</option>');
            $("#importe_select2").append('<option value="84">84</option>');
            $("#importe_select2").append('<option value="96">96</option>');
            $("#cuotamensual").val(0);
        } else if (importe == 15000) {
            $('#importe_select2').children('option:not(:first)').remove();
            $("#importe_select2").append('<option value="12">12</option>');
            $("#importe_select2").append('<option value="24">24</option>');
            $("#importe_select2").append('<option value="36">36</option>');
            $("#importe_select2").append('<option value="48">48</option>');
            $("#importe_select2").append('<option value="60">60</option>');
            $("#importe_select2").append('<option value="72">72</option>');
            $("#importe_select2").append('<option value="84">84</option>');
            $("#importe_select2").append('<option value="96">96</option>');
            $("#cuotamensual").val(0);
        } else if (importe == 20000) {
            $('#importe_select2').children('option:not(:first)').remove();
            $("#importe_select2").append('<option value="24">24</option>');
            $("#importe_select2").append('<option value="36">36</option>');
            $("#importe_select2").append('<option value="48">48</option>');
            $("#importe_select2").append('<option value="60">60</option>');
            $("#importe_select2").append('<option value="72">72</option>');
            $("#importe_select2").append('<option value="84">84</option>');
            $("#importe_select2").append('<option value="96">96</option>');
            $("#cuotamensual").val(0);
        } else if (importe == 25000) {
            $('#importe_select2').children('option:not(:first)').remove();
            $("#importe_select2").append('<option value="24">24</option>');
            $("#importe_select2").append('<option value="36">36</option>');
            $("#importe_select2").append('<option value="48">48</option>');
            $("#importe_select2").append('<option value="60">60</option>');
            $("#importe_select2").append('<option value="72">72</option>');
            $("#importe_select2").append('<option value="84">84</option>');
            $("#importe_select2").append('<option value="96">96</option>');
            $("#cuotamensual").val(0);
        } else if (importe == 30000) {
            $('#importe_select2').children('option:not(:first)').remove();
            $("#importe_select2").append('<option value="24">24</option>');
            $("#importe_select2").append('<option value="36">36</option>');
            $("#importe_select2").append('<option value="48">48</option>');
            $("#importe_select2").append('<option value="60">60</option>');
            $("#importe_select2").append('<option value="72">72</option>');
            $("#importe_select2").append('<option value="84">84</option>');
            $("#importe_select2").append('<option value="96">96</option>');
            $("#cuotamensual").val(0);
        } else if (importe == 40000) {
            $('#importe_select2').children('option:not(:first)').remove();
            $("#importe_select2").append('<option value="36">36</option>');
            $("#importe_select2").append('<option value="48">48</option>');
            $("#importe_select2").append('<option value="60">60</option>');
            $("#importe_select2").append('<option value="72">72</option>');
            $("#importe_select2").append('<option value="84">84</option>');
            $("#importe_select2").append('<option value="96">96</option>');
            $("#cuotamensual").val(0);
        } else if (importe == 50000) {
            $('#importe_select2').children('option:not(:first)').remove();
            $("#importe_select2").append('<option value="48">48</option>');
            $("#importe_select2").append('<option value="60">60</option>');
            $("#importe_select2").append('<option value="72">72</option>');
            $("#importe_select2").append('<option value="84">84</option>');
            $("#importe_select2").append('<option value="96">96</option>');
            $("#cuotamensual").val(0);
        } else if (importe == 60000) {
            $('#importe_select2').children('option:not(:first)').remove();
            $("#importe_select2").append('<option value="48">48</option>');
            $("#importe_select2").append('<option value="60">60</option>');
            $("#importe_select2").append('<option value="72">72</option>');
            $("#importe_select2").append('<option value="84">84</option>');
            $("#importe_select2").append('<option value="96">96</option>');
            $("#cuotamensual").val(0);
        }
    };
    function calculacuota() {

        var importe = $("#importe_select").val();
        var mensualidades = $("#importe_select2").val();

        if (importe == 500) {
            if (mensualidades == 12) $("#cuotamensual").val(46);
            else if (mensualidades == 16) $("#cuotamensual").val(40).attr('selected', 'selected');
            else if (mensualidades == 18) $("#cuotamensual").val(35);
            else if (mensualidades == 20) $("#cuotamensual").val(30);
            else if (mensualidades == 24) $("#cuotamensual").val(25);
        } else if (importe == 1000) {
            if (mensualidades == 12) $("#cuotamensual").val(96);
            else if (mensualidades == 16) $("#cuotamensual").val(80);
            else if (mensualidades == 18) $("#cuotamensual").val(65);
            else if (mensualidades == 20) $("#cuotamensual").val(55);
            else if (mensualidades == 24) $("#cuotamensual").val(48);
        } else if (importe == 2000) {
            if (mensualidades == 12) $("#cuotamensual").val(180);
            else if (mensualidades == 24) $("#cuotamensual").val(96);
            else if (mensualidades == 36) $("#cuotamensual").val(68);
            else if (mensualidades == 48) $("#cuotamensual").val(55);
            else if (mensualidades == 60) $("#cuotamensual").val(45);
        } else if (importe == 3000) {
            if (mensualidades == 12) $("#cuotamensual").val(270);
            else if (mensualidades == 24) $("#cuotamensual").val(144);
            else if (mensualidades == 36) $("#cuotamensual").val(103);
            else if (mensualidades == 48) $("#cuotamensual").val(82);
            else if (mensualidades == 60) $("#cuotamensual").val(70);
        } else if (importe == 4000) {
            if (mensualidades == 12) $("#cuotamensual").val(360);
            else if (mensualidades == 24) $("#cuotamensual").val(192);
            else if (mensualidades == 36) $("#cuotamensual").val(137);
            else if (mensualidades == 48) $("#cuotamensual").val(109);
            else if (mensualidades == 60) $("#cuotamensual").val(93);
        } else if (importe == 5000) {
            if (mensualidades == 12) $("#cuotamensual").val(450);
            else if (mensualidades == 24) $("#cuotamensual").val(240);
            else if (mensualidades == 36) $("#cuotamensual").val(171);
            else if (mensualidades == 48) $("#cuotamensual").val(137);
            else if (mensualidades == 60) $("#cuotamensual").val(117);
        } else if (importe == 6000) {
            if (mensualidades == 12) $("#cuotamensual").val(540);
            else if (mensualidades == 24) $("#cuotamensual").val(289);
            else if (mensualidades == 36) $("#cuotamensual").val(205);
            else if (mensualidades == 48) $("#cuotamensual").val(164);
            else if (mensualidades == 60) $("#cuotamensual").val(140);
        } else if (importe == 8000) {
            if (mensualidades == 12) $("#cuotamensual").val(712);
            else if (mensualidades == 24) $("#cuotamensual").val(377);
            else if (mensualidades == 36) $("#cuotamensual").val(266);
            else if (mensualidades == 48) $("#cuotamensual").val(211);
            else if (mensualidades == 60) $("#cuotamensual").val(178);
            else if (mensualidades == 72) $("#cuotamensual").val(157);
            else if (mensualidades == 84) $("#cuotamensual").val(141);
            else if (mensualidades == 96) $("#cuotamensual").val(130);
        } else if (importe == 10000) {
            if (mensualidades == 12) $("#cuotamensual").val(890);
            else if (mensualidades == 24) $("#cuotamensual").val(471);
            else if (mensualidades == 36) $("#cuotamensual").val(333);
            else if (mensualidades == 48) $("#cuotamensual").val(264);
            else if (mensualidades == 60) $("#cuotamensual").val(223);
            else if (mensualidades == 72) $("#cuotamensual").val(196);
            else if (mensualidades == 84) $("#cuotamensual").val(177);
            else if (mensualidades == 96) $("#cuotamensual").val(163);
        } else if (importe == 12000) {
            if (mensualidades == 12) $("#cuotamensual").val(1067);
            else if (mensualidades == 24) $("#cuotamensual").val(566);
            else if (mensualidades == 36) $("#cuotamensual").val(399);
            else if (mensualidades == 48) $("#cuotamensual").val(316);
            else if (mensualidades == 60) $("#cuotamensual").val(267);
            else if (mensualidades == 72) $("#cuotamensual").val(235);
            else if (mensualidades == 84) $("#cuotamensual").val(212);
            else if (mensualidades == 96) $("#cuotamensual").val(195);
        } else if (importe == 15000) {
            if (mensualidades == 12) $("#cuotamensual").val(1334);
            else if (mensualidades == 24) $("#cuotamensual").val(707);
            else if (mensualidades == 36) $("#cuotamensual").val(499);
            else if (mensualidades == 48) $("#cuotamensual").val(395);
            else if (mensualidades == 60) $("#cuotamensual").val(334);
            else if (mensualidades == 72) $("#cuotamensual").val(294);
            else if (mensualidades == 84) $("#cuotamensual").val(265);
            else if (mensualidades == 96) $("#cuotamensual").val(244);
        } else if (importe == 20000) {
            if (mensualidades == 24) $("#cuotamensual").val(924);
            else if (mensualidades == 36) $("#cuotamensual").val(646);
            else if (mensualidades == 48) $("#cuotamensual").val(508);
            else if (mensualidades == 60) $("#cuotamensual").val(425);
            else if (mensualidades == 72) $("#cuotamensual").val(371);
            else if (mensualidades == 84) $("#cuotamensual").val(332);
            else if (mensualidades == 96) $("#cuotamensual").val(304);
        } else if (importe == 25000) {
            if (mensualidades == 24) $("#cuotamensual").val(1155);
            else if (mensualidades == 36) $("#cuotamensual").val(807);
            else if (mensualidades == 48) $("#cuotamensual").val(635);
            else if (mensualidades == 60) $("#cuotamensual").val(532);
            else if (mensualidades == 72) $("#cuotamensual").val(464);
            else if (mensualidades == 84) $("#cuotamensual").val(415);
            else if (mensualidades == 96) $("#cuotamensual").val(380);
        } else if (importe == 30000) {
            if (mensualidades == 24) $("#cuotamensual").val(1385);
            else if (mensualidades == 36) $("#cuotamensual").val(969);
            else if (mensualidades == 48) $("#cuotamensual").val(762);
            else if (mensualidades == 60) $("#cuotamensual").val(638);
            else if (mensualidades == 72) $("#cuotamensual").val(556);
            else if (mensualidades == 84) $("#cuotamensual").val(498);
            else if (mensualidades == 96) $("#cuotamensual").val(456);
        } else if (importe == 40000) {
            if (mensualidades == 36) $("#cuotamensual").val(1254);
            else if (mensualidades == 48) $("#cuotamensual").val(977);
            else if (mensualidades == 60) $("#cuotamensual").val(811);
            else if (mensualidades == 72) $("#cuotamensual").val(702);
            else if (mensualidades == 84) $("#cuotamensual").val(624);
            else if (mensualidades == 96) $("#cuotamensual").val(566);
        } else if (importe == 50000) {
            if (mensualidades == 48) $("#cuotamensual").val(1221);
            else if (mensualidades == 60) $("#cuotamensual").val(1014);
            else if (mensualidades == 72) $("#cuotamensual").val(877);
            else if (mensualidades == 84) $("#cuotamensual").val(780);
            else if (mensualidades == 96) $("#cuotamensual").val(707);
        } else if (importe == 60000) {
            if (mensualidades == 48) $("#cuotamensual").val(1466);
            else if (mensualidades == 60) $("#cuotamensual").val(1217);
            else if (mensualidades == 72) $("#cuotamensual").val(1053);
            else if (mensualidades == 84) $("#cuotamensual").val(936);
            else if (mensualidades == 96) $("#cuotamensual").val(894);
        }
    }
});


function quitarcredito2() {
    $('#credito2').hide();
    $('#botoncredito3').hide();
    $('#botoncredito2').show();
    $('#id_creditotipo2').val(undefined);
    $('#id_creditotantoporciento2').val(undefined);
    $('#id_creditoimporte2').val(undefined);
    $('#id_creditocuota2').val(undefined);
    $('#id_creditoentidad2').val(undefined);
    div = document.getElementById('creditoaval2');
    div.style.display = "none";
}

function quitarcredito3() {
    $('#credito3').hide();
    $('#botoncredito3out').hide();
    $('#botoncredito3').show();
    $('#id_creditotipo3').val(undefined);
    $('#id_creditotantoporciento3').val(undefined);
    $('#id_creditoimporte3').val(undefined);
    $('#id_creditocuota3').val(undefined);
    $('#id_creditoentidad3').val(undefined);
    div = document.getElementById('creditoaval3');
    div.style.display = "none";
}

function quitartarg2() {
    $('#targ2').hide();
    $('#botontarg3').hide();
    $('#botontarg2').show();
    $('#id_tarjetacuota2').val(undefined);
    $('#id_tarjetaimporte2').val(undefined);
    $('#id_tarjetaentidad2').val(undefined);
}

function quitartarg3() {
    $('#targ3').hide();
    $('#botontarg3out').hide();
    $('#botontarg3').show();
    $('#id_tarjetacuota3').val(undefined);
    $('#id_tarjetaimporte3').val(undefined);
    $('#id_tarjetaentidad3').val(undefined);
}

function quitarrec2() {
    $('#rec2').hide();
    $('#botonrec3').hide();
    $('#botonrec2').show();
    $('#id_recivosimporte2').val(undefined);
}

function quitarrec3() {
    $('#rec3').hide();
    $('#botonrec3out').hide();
    $('#botonrec3').show();
    $('#id_recivosimporte3').val(undefined);
}

function quitarmor2() {
    $('#mor2').hide();
    $('#botonmor3').hide();
    $('#botonmor2').show();
    $('#id_morosoimporte2').val(undefined);
    $('#id_morosoquien2').val(undefined);
}

function quitarmor3() {
    $('#mor3').hide();
    $('#botonmor3out').hide();
    $('#botonmor3').show();
    $('#id_morosoimporte3').val(undefined);
    $('#id_morosoquien3').val(undefined);
}

function avalquitarcredito2() {
    $('#avalcredito2').hide();
    $('#avalbotoncredito3').hide();
    $('#avalbotoncredito2').show();
    $('#id_avalistareditotipo2').val(undefined);
    $('#id_avalistareditotantoporciento2').val(undefined);
    $('#id_avalistareditoimporte2').val(undefined);
    $('#id_avalistareditocuota2').val(undefined);
    $('#id_avalistareditoentidad2').val(undefined);
    div = document.getElementById('creditoaval2');
    div.style.display = "none";
}

function avalquitartarg2() {
    $('#avaltarg2').hide();
    $('#avalbotontarg3').hide();
    $('#avalbotontarg2').show();
    $('#id_avalistaarjetacuota2').val(undefined);
    $('#id_avalistaarjetaimporte2').val(undefined);
    $('#id_avalistaarjetaentidad2').val(undefined);
}

function avalquitarrec2() {
    $('#avalrec2').hide();
    $('#avalbotonrec3').hide();
    $('#avalbotonrec2').show();
    $('#id_avalistaecivosimporte2').val(undefined);
}

function avalquitarmor2() {
    $('#avalmor2').hide();
    $('#avalbotonmor3').hide();
    $('#avalbotonmor2').show();
    $('#id_avalistaorosoimporte2').val(undefined);
    $('#id_avalistaorosoquien2').val(undefined);
}

function quitarempresa3() {
    $('#empresa3').hide();
    $('#botonempresa3out').hide();
    $('#botonempresa3').show();
    $('#id_nombreempresa3').val(undefined);
    $('#id_cargoempresa3').val(undefined);
    $('#id_actividadempresa3').val(undefined);
    $('#id_ingresosempresa3').val(undefined);
    $('#id_pagasempresa3').val(undefined);
    $('#id_otrosingresosempresa3').val(undefined);
    $('#id_antiguedadempresa3').val(undefined);
}

function quitarempresa2() {
    $('#empresa2').hide();
    $('#botonempresa3').hide();
    $('#botonempresa2').show();
    $('#id_nombreempresa2').val(undefined);
    $('#id_cargoempresa2').val(undefined);
    $('#id_actividadempresa2').val(undefined);
    $('#id_ingresosempresa2').val(undefined);
    $('#id_pagasempresa2').val(undefined);
    $('#id_otrosingresosempresa2').val(undefined);
    $('#id_antiguedadempresa2').val(undefined);
}


////VIVIENDAAAS

function quitarviviendap3() {
    $('#viviendap3').hide();
    $('#botonviviendap3out').hide();
    $('#botonviviendap3').show();
    $('#viviendavalor3').val(undefined);
    $('#viviendahipotecavalor3').val(undefined);
    $('#viviendapagada3').val(undefined);
    $('#viviendacuotahip3').val(undefined);
    $('#viviendaanoship3').val(undefined);
    $('#viviendaentidadhip3').val(undefined);
    $('#viviendam3').val(undefined);
    $('#viviendaporciento3').val(undefined);
    $('#viviendadireccion3').val(undefined);
    $('#viviendapoblacion3').val(undefined);
    $('#viviendaprovincia3').val(undefined);
    $('#viviendacp3').val(undefined);
    div = document.getElementById('viviendapagada33');
    div.style.display = "none";
}

function quitarviviendap2() {
    $('#viviendap2').hide();
    $('#botonviviendap3').hide();
    $('#botonviviendap2').show();
    $('#viviendavalor2').val(undefined);
    $('#viviendahipotecavalor2').val(undefined);
    $('#viviendapagada2').val(undefined);
    $('#viviendacuotahip2').val(undefined);
    $('#viviendaanoship2').val(undefined);
    $('#viviendaentidadhip2').val(undefined);
    $('#viviendam2').val(undefined);
    $('#viviendaporciento2').val(undefined);
    $('#viviendadireccion2').val(undefined);
    $('#viviendapoblacion2').val(undefined);
    $('#viviendaprovincia2').val(undefined);
    $('#viviendacp2').val(undefined);
    div = document.getElementById('viviendapagada22');
    div.style.display = "none";

}

function quitarviviendapa3() {
    $('#viviendapa3').hide();
    $('#botonviviendapa3out').hide();
    $('#botonviviendapa3').show();
    $('#viviendavalora3').val(undefined);
    $('#viviendahipotecavalora3').val(undefined);
    $('#viviendapagadaa3').val(undefined);
    $('#viviendacuotahipa3').val(undefined);
    $('#viviendaanoshipa3').val(undefined);
    $('#viviendaentidadhipa3').val(undefined);
    $('#viviendama3').val(undefined);
    $('#viviendaporcientoa3').val(undefined);
    $('#viviendadirecciona3').val(undefined);
    $('#viviendapoblaciona3').val(undefined);
    $('#viviendaprovinciaa3').val(undefined);
    $('#viviendacpa3').val(undefined);
    $('#viviendacobraa3').val(undefined);
    div = document.getElementById('viviendapagadaa33');
    div.style.display = "none";
}

function quitarviviendapa2() {
    $('#viviendapa2').hide();
    $('#botonviviendapa3').hide();
    $('#botonviviendapa2').show();
    $('#viviendavalora2').val(undefined);
    $('#viviendahipotecavalora2').val(undefined);
    $('#viviendapagadaa2').val(undefined);
    $('#viviendacuotahipa2').val(undefined);
    $('#viviendaanoshipa2').val(undefined);
    $('#viviendaentidadhipa2').val(undefined);
    $('#viviendama2').val(undefined);
    $('#viviendaporcientoa2').val(undefined);
    $('#viviendadirecciona2').val(undefined);
    $('#viviendapoblaciona2').val(undefined);
    $('#viviendaprovinciaa2').val(undefined);
    $('#viviendacpa2').val(undefined);
    $('#viviendacobraa2').val(undefined);
    div = document.getElementById('viviendapagadaa22');
    div.style.display = "none";

}

function quitaralquiler2() {
    $('#alquiler2').hide();
    $('#botonalquiler3').hide();
    $('#botonalquiler2').show();
    $('#alquilerpaga2').val(undefined);
    $('#alquilerm2').val(undefined);
    $('#alquilerdireccion2').val(undefined);
    $('#alquilerpoblacion2').val(undefined);
    $('#alquilerprovincia2').val(undefined);
    $('#alquilercp2').val(undefined);
}

function quitaralquiler3() {
    $('#alquiler3').hide();
    $('#botonalquiler3out').hide();
    $('#botonalquiler3').show();
    $('#alquilerpaga3').val(undefined);
    $('#alquilerm3').val(undefined);
    $('#alquilerdireccion3').val(undefined);
    $('#alquilerpoblacion3').val(undefined);
    $('#alquilerprovincia3').val(undefined);
    $('#alquilercp3').val(undefined);
}
