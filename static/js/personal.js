/**** Calcular Cuotas ****/
$(document).ready(function() {
    $("#importe_select").change(function() { /*Si importe_select canvia*/
        calculamensualidades();
        lele();
    });
    $("#importe_select2").change(function() { /*Si importe_select2 canvia*/
        calculacuota();
    });
    $("#estadocivil").change(function() { /*Si estadovicil canvia*/
        tipoestadocivil();
    });
    $("#ayudaimporte").change(function() { /*Si importe_select canvia*/
        calculhelp();
    });
    $("#ayudapagas").change(function() { /*Si importe_select canvia*/
        calculhelp();
    });
    $("#empresatipo").change(function() { /*Si importe_select canvia*/
        tipoempresa();
    });
    $("#empresaajena").change(function() { /*Si importe_select canvia*/
        empresatiempo();
    });
    $("#viviendapagada").change(function() { /*Si importe_select canvia*/
        viviendaestapagada();
    });
    $("#viviendapagada2").change(function() { /*Si importe_select canvia*/
        viviendaestapagada2();
    });
    $("#viviendapagada3").change(function() { /*Si importe_select canvia*/
        viviendaestapagada3();
    });
    $("#viviendapagadaa").change(function() { /*Si importe_select canvia*/
        viviendaestapagadaa();
    });
    $("#viviendapagadaa2").change(function() { /*Si importe_select canvia*/
        viviendaestapagadaa2();
    });
    $("#viviendapagadaa3").change(function() { /*Si importe_select canvia*/
        viviendaestapagadaa3();
    });
    $("#credtipo1").change(function() { /*Si estadovicil canvia*/
        credtip1();
    });

     $("#credtipo2").change(function() { /*Si estadovicil canvia*/
        credtip2();
    });

     $("#credtipo3").change(function() { /*Si estadovicil canvia*/
        credtip3();
    });

    function lele() {
        

    };

    function credtip1() {
        var credaval = $("#credtipo1").val();
        if (credaval == "avalista") {
            div = document.getElementById('creditoaval1');
            div.style.display = "block";
        } else {
            div = document.getElementById('creditoaval1');
            div.style.display = "none";
        }

    };

    function credtip2() {
        var credaval = $("#credtipo2").val();
        if (credaval == "avalista") {
            div = document.getElementById('creditoaval2');
            div.style.display = "block";
        } else {
            div = document.getElementById('creditoaval2');
            div.style.display = "none";
        }

    };

    function credtip3() {
        var credaval = $("#credtipo3").val();
        if (credaval == "avalista") {
            div = document.getElementById('creditoaval3');
            div.style.display = "block";
        } else {
            div = document.getElementById('creditoaval3');
            div.style.display = "none";
        }

    };

    function viviendaestapagada() {
        var viviendapagada = $("#viviendapagada").val();
        if (viviendapagada == '0') {
            div = document.getElementById('viviendapagada11');
            div.style.display = "block";
        } else {
            div = document.getElementById('viviendapagada11');
            div.style.display = "none";
        }

    };

    function viviendaestapagada2() {
        var viviendapagada = $("#viviendapagada2").val();
        if (viviendapagada == '0') {
            div = document.getElementById('viviendapagada22');
            div.style.display = "block";
        } else {
            div = document.getElementById('viviendapagada22');
            div.style.display = "none";
        }

    };

     function viviendaestapagada3() {
        var viviendapagada = $("#viviendapagada3").val();
        if (viviendapagada == '0') {
            div = document.getElementById('viviendapagada33');
            div.style.display = "block";
        } else {
            div = document.getElementById('viviendapagada33');
            div.style.display = "none";
        }

    };

    function viviendaestapagadaa() {
        var viviendapagada = $("#viviendapagadaa").val();
        if (viviendapagada == '0') {
            div = document.getElementById('viviendapagadaa11');
            div.style.display = "block";
        } else {
            div = document.getElementById('viviendapagadaa11');
            div.style.display = "none";
        }

    };

    function viviendaestapagadaa2() {
        var viviendapagada = $("#viviendapagadaa2").val();
        if (viviendapagada == '0') {
            div = document.getElementById('viviendapagadaa22');
            div.style.display = "block";
        } else {
            div = document.getElementById('viviendapagadaa22');
            div.style.display = "none";
        }

    };

     function viviendaestapagadaa3() {
        var viviendapagada = $("#viviendapagadaa3").val();
        if (viviendapagada == '0') {
            div = document.getElementById('viviendapagadaa33');
            div.style.display = "block";
        } else {
            div = document.getElementById('viviendapagadaa33');
            div.style.display = "none";
        }

    };



    function calculhelp() {
        var a = $('#ayudaimporte').val();
        var b = $('#ayudapagas').val();
        if (a != null && b != null) {
            $("#ayudatotal").val(a * b);
        };

    };


    function empresatiempo() {
        var empresaajena = $("#empresaajena").val();
        if (empresaajena == 'temporal') {
            div = document.getElementById('tempsi');
            div.style.display = "block";
        } else {
            div = document.getElementById('tempsi');
            div.style.display = "none";
            $("#empresatiempo").val(0);
        }


    };

    function tipoempresa() {
        var empresatipo = $("#empresatipo").val();
        if (empresatipo == 'ajena') {
            div = document.getElementById('ajenasi');
            div.style.display = "block";
            div2 = document.getElementById('ajenano');
            div2.style.display = "none";
            $("#empresaajena").append('<option value="fijo">   Fijo</option>');
            $("#empresaajena").append('<option value="indefinido">   Indefinido</option>');
            $("#empresaajena").append('<option value="temporal">   Temporal</option>');
        } else {
            div = document.getElementById('ajenasi');
            div.style.display = "none";
            div2 = document.getElementById('ajenano');
            div2.style.display = "block";
            $('#empresaajena').children('option:not(:first)').remove();
            div = document.getElementById('tempsi');
            div.style.display = "none";
            $("#empresatiempo").val(0);
        }

    };


    function tipoestadocivil() {
        var estadocivil = $("#estadocivil").val();
        if (estadocivil == 'casado') {
            div = document.getElementById('plsshw');
            div.style.display = "block";
            div2 = document.getElementById('plsshw2');
            div2.style.display = "none";
            $("#tipoestadocivil").append('<option value="separacion">Separación de bienes</option>');
            $("#tipoestadocivil").append('<option value="gananciales">Bienes gananciales</option>');
        } else {
            div = document.getElementById('plsshw');
            div.style.display = "none";
            div2 = document.getElementById('plsshw2');
            div2.style.display = "block";
            $('#tipoestadocivil').children('option:not(:first)').remove();
        }

    };

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

function quitarempresa3 (){
	$('#empresa3').hide();
	$('#botonempresa3out').hide();
	$('#botonempresa3').show();
	$('#empresanombre3').val(undefined);
	$('#empresacargo3').val(undefined);
	$('#empresaactividad3').val(undefined);
	$('#empresaingresos3').val(undefined);
	$('#empresapagas3').val(undefined);
	$('#empresaotros3').val(undefined);
	$('#empresaantiguedad3').val(undefined);
}

function quitarempresa2 () {
	$('#empresa2').hide();
	$('#botonempresa3').hide();
	$('#botonempresa2').show();
	$('#empresanombre2').val(undefined);
	$('#empresacargo2').val(undefined);
	$('#empresaactividad2').val(undefined);
	$('#empresaingresos2').val(undefined);
	$('#empresapagas2').val(undefined);
	$('#empresaotros2').val(undefined);
	$('#empresaantiguedad2').val(undefined);
}
function quitarviviendap3 (){
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
function quitarviviendap2 () {
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
function quitarviviendapa3 (){
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
function quitarviviendapa2 () {
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
function quitaralquiler2 (){
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
function quitaralquiler3 () {
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

function quitarcredito2 (){
    $('#credito2').hide();
    $('#botoncredito3').hide();
    $('#botoncredito2').show();
    $('#credtipo2').val(undefined);
    $('#credaval2').val(undefined);
    $('#credimp2').val(undefined);
    $('#credcuota2').val(undefined);
    $('#credent2').val(undefined);
    div = document.getElementById('creditoaval2');
    div.style.display = "none";
}
function quitarcredito3 () {
    $('#credito3').hide();
    $('#botoncredito3out').hide();
    $('#botoncredito3').show();
    $('#credtipo3').val(undefined);
    $('#credaval3').val(undefined);
    $('#credimp3').val(undefined);
    $('#credcuota3').val(undefined);
    $('#credent3').val(undefined);
    div = document.getElementById('creditoaval3');
    div.style.display = "none";
}

function quitartarg2 (){
    $('#targ2').hide();
    $('#botontarg3').hide();
    $('#botontarg2').show();
    $('#targcuota2').val(undefined);
    $('#targimp2').val(undefined);
    $('#targent2').val(undefined);
}
function quitartarg3 () {
    $('#targ3').hide();
    $('#botontarg3out').hide();
    $('#botontarg3').show();
    $('#targcuota3').val(undefined);
    $('#targimp3').val(undefined);
    $('#targent3').val(undefined);
}
function quitarrec2 (){
    $('#rec2').hide();
    $('#botonrec3').hide();
    $('#botonrec2').show();
    $('#recimp2').val(undefined);
}
function quitarrec3 () {
    $('#rec3').hide();
    $('#botonrec3out').hide();
    $('#botonrec3').show();
    $('#recimp3').val(undefined);
}
function quitarmor2 (){
    $('#mor2').hide();
    $('#botonmor3').hide();
    $('#botonmor2').show();
    $('#morimp2').val(undefined);
    $('#morwho2').val(undefined);
}
function quitarmor3 () {
    $('#mor3').hide();
    $('#botonmor3out').hide();
    $('#botonmor3').show();
    $('#morimp3').val(undefined);
    $('#morwho3').val(undefined);
}