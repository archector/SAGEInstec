# -*- coding: utf-8 -*-

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum
from django.shortcuts import render, redirect
from decimal import Decimal
from estacionamientos.controller import *
from estacionamientos.forms import EstacionamientoExtendedForm,TarifaForm,\
    EstacionamientoNombre
from estacionamientos.forms import EstacionamientoForm
from estacionamientos.forms import EstacionamientoReserva
from estacionamientos.forms import EstacionamientoPago
from estacionamientos.forms import EstacionamientoRif
from estacionamientos.forms import EstacionamientoCi
from estacionamientos.models import Estacionamiento, ReservasModel , RecibosModel
from django.core.context_processors import request
from django.template import Context
import datetime
import json

listaReserva = []
FECHA_FIJA = datetime.datetime(datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day,0,0)

# Usamos esta vista para procesar todos los estacionamientos
def estacionamientos_all(request):
    global listaReserva
    listaReserva = []
    # Si se hace un POST a esta vista implica que se quiere agregar un nuevo
    # estacionamiento
    estacionamientos = Estacionamiento.objects.all()
    if request.method == 'POST':
            # Creamos un formulario con los datos que recibimos
            form = EstacionamientoForm(request.POST)

            # Parte de la entrega era limitar la cantidad maxima de
            # estacionamientos a 5
            if len(estacionamientos) >= 15:
                    return render(request, 'templateMensaje.html',
                                  {'color':'red', 'mensaje':'No se pueden agregar más estacionamientos'})

            # Si el formulario es valido, entonces creamos un objeto con
            # el constructor del modelo
            if form.is_valid():
                obj = Estacionamiento(
                        Propietario = form.cleaned_data['propietario'],
                        Nombre = form.cleaned_data['nombre'],
                        Direccion = form.cleaned_data['direccion'],
                        Rif = form.cleaned_data['rif'],
                        Telefono_1 = form.cleaned_data['telefono_1'],
                        Telefono_2 = form.cleaned_data['telefono_2'],
                        Telefono_3 = form.cleaned_data['telefono_3'],
                        Email_1 = form.cleaned_data['email_1'],
                        Email_2 = form.cleaned_data['email_2'],
                        Ingresos = 0,
                        monto_tarifa_pico = 0
                )
                obj.save()
                # Recargamos los estacionamientos ya que acabamos de agregar
                estacionamientos = Estacionamiento.objects.all()
    # Si no es un POST es un GET, y mandamos un formulario vacio
    else:
        form = EstacionamientoForm()

    return render(request, 'base.html', {'form': form, 'estacionamientos': estacionamientos})

def estacionamiento_detail(request, _id):
    _id = int(_id)
    # Verificamos que el objeto exista antes de continuar
    try:
        estacion = Estacionamiento.objects.get(id = _id)
    except ObjectDoesNotExist:
        return render(request, '404.html')

    global listaReserva
    listaReserva = []

    if request.method == 'POST':
            # Leemos el formulario
            form = EstacionamientoExtendedForm(request.POST)
            
            # Si el formulario
            if form.is_valid():
                hora_in = form.cleaned_data['horarioin']
                hora_out = form.cleaned_data['horarioout']
                reserva_in = form.cleaned_data['horario_reserin']
                reserva_out = form.cleaned_data['horario_reserout']
                ini_pico = form.cleaned_data['pico_inicio']
                fin_pico = form.cleaned_data['pico_fin']
                
                mount = form.cleaned_data['monto_pico']
                

                m_validado = HorarioEstacionamiento(hora_in, hora_out, reserva_in, reserva_out,ini_pico,fin_pico)
                if not m_validado[0]:
                    return render(request, 'estacionamiento.html', {'color':'red', 'mensaje': m_validado[1]})

                estacion.Tarifa = form.cleaned_data['tarifa']
                estacion.monto_tarifa = form.cleaned_data['monto_tarifa']
                estacion.Apertura = hora_in
                estacion.Cierre = hora_out
                estacion.Reservas_Inicio = reserva_in
                estacion.Reservas_Cierre = reserva_out
                estacion.NroPuesto = form.cleaned_data['puestos']
                
                if estacion.Tarifa.tipoTarifa == 'difHoras':
                    
                    estacion.Pico_Inicio = ini_pico
                    estacion.Pico_Final = fin_pico
                    if not mount:
                        estacion.monto_tarifa_pico = None
                    if mount:
                        estacion.monto_tarifa_pico = mount
                    
                else:
                    estacion.Pico_Inicio = None
                    estacion.Pico_Final = None
                    estacion.monto_tarifa_pico = None
                    
                    

                estacion.save()
    else:
        form = EstacionamientoExtendedForm()
      
    return render(request, 'estacionamiento.html', {'form': form, 'estacionamiento': estacion})


def estacionamiento_reserva(request, _id):
    _id = int(_id)
    # Verificamos que el objeto exista antes de continuar
    try:
        estacion = Estacionamiento.objects.get(id = _id)
    except ObjectDoesNotExist:
        return render(request, '404.html')

    global listaReserva

    # Antes de entrar en la reserva, si la lista esta vacia, agregamos los
    # valores predefinidos
    if len(listaReserva) < 1:

        Puestos = ReservasModel.objects.filter(Estacionamiento = estacion).values_list('InicioReserva', 'FinalReserva')

        for obj in Puestos:
            listaReserva.append((obj[0],obj[1]))

    # Si se hace un GET renderizamos los estacionamientos con su formulario
    if request.method == 'GET':
        form = EstacionamientoReserva()
        return render(request, 'estacionamientoReserva.html', {'form': form, 'estacionamiento': estacion})

    # Si es un POST estan mandando un request
    elif request.method == 'POST':
            form = EstacionamientoReserva(request.POST)
            # Verificamos si es valido con los validadores del formulario
            if form.is_valid():
                inicio_reserva = form.cleaned_data['inicio']
                final_reserva = form.cleaned_data['final']
                horaReserva = (inicio_reserva,final_reserva)

                # Validamos los horarios con los horario de salida y entrada
                m_validado = validarHorarioReserva(inicio_reserva, final_reserva, estacion.Reservas_Inicio, estacion.Reservas_Cierre)

                # Si no es valido devolvemos el request
                if not m_validado[0]:
                    return render(request, 'estacionamientoReserva.html', {'form': form, 'estacionamiento': estacion,'color':'red', 'mensaje': m_validado[1]})

                # Si esta en un rango valido, procedemos a buscar en la lista
                # el lugar a insertar
                reserva = algoritmo_Marzullo(listaReserva, horaReserva, estacion.NroPuesto)
                if reserva[0] :
                    listaReserva.append(horaReserva)
                    cobro = estacion.calcularCobro(inicio_reserva,final_reserva)
                    reservaFinal = ReservasModel(
                                        Estacionamiento = estacion,
                                        Puesto = reserva[1],
                                        InicioReserva = inicio_reserva,
                                        FinalReserva = final_reserva,
                                        Costo = cobro
                                    )
                    reservaFinal.save()
                    
                    form = EstacionamientoReserva()
                    return render(request, 'pagos.html', {'color':'green', 'mensaje':'Hay disponibilidad en el horario seleccionado','ini': inicio_reserva, 'fin':final_reserva,'monto':cobro,'nomb':estacion.Nombre,'puesto':reservaFinal.Puesto,'tarifa':estacion.monto_tarifa, 'num':reservaFinal.id})
                else:             
                    return render(request, 'estacionamientoReserva.html', {'color':'red', 'mensaje':'No hay un puesto disponible para ese horario','form': form, 'estacionamiento': estacion})
    else:
        form = EstacionamientoReserva()

    return render(request, 'estacionamientoReserva.html', {'form': form, 'estacionamiento': estacion})

def estacionamiento_pagos(request, _id):
    _id = int(_id)
    # Verificamos que el objeto exista antes de continuar
    try:
        reserv = ReservasModel.objects.latest("id")
    except ObjectDoesNotExist:
        return render(request, '404.html')
    
    recibos = RecibosModel.objects.all()

    form = EstacionamientoPago()

    return render(request, 'pagos.html',{'reserva': reserv,'form':form,'recibos':recibos})

def eliminar_reserva_view(request, _id):
    _id = int(_id)
    
    try:
        reserv = ReservasModel.objects.latest("id")
    except ObjectDoesNotExist:
        return render(request, '404.html')
    reserv.delete()
    
    return render(request, 'eliminandoreserva.html',{'reserva': reserv})

def pago_confirm(request, _id):
    _id = int(_id)
    # Verificamos que el objeto exista antes de continuar
    try:
        reserv = ReservasModel.objects.latest("id")
    except ObjectDoesNotExist:
        return render(request, '404.html')
    
    recibos = RecibosModel.objects.all()
    
    if request.method == 'POST':
            # Creamos un formulario con los datos que recibimos
            form = EstacionamientoPago(request.POST)

            # Si el formulario es valido, entonces creamos un objeto con
            # el constructor del modelo
            if form.is_valid():
                obj = RecibosModel(
                        NumeroTransaccion=reserv.id,
                        Cedula = form.cleaned_data['cedula'],
                        Nombre = form.cleaned_data['nombre'],
                        Apellido = form.cleaned_data['apellido'],
                        NumeroTarjeta = form.cleaned_data['num_tarjeta'],
                        FechaPago = datetime.datetime.now(),
                        InicioReserva = reserv.InicioReserva,
                        FinalReserva = reserv.FinalReserva,
                        Costo = Decimal(reserv.Costo),
                        RifEstacionamiento=reserv.Estacionamiento.Rif,
                        NombreEstacionamiento=reserv.Estacionamiento.Nombre,
                        TelEstacionamiento=reserv.Estacionamiento.Telefono_1,
                        
                )
                obj.save()
                e = Estacionamiento.objects.get(Rif=reserv.Estacionamiento.Rif,Nombre=reserv.Estacionamiento.Nombre)
                e.Ingresos =e.Ingresos+ Decimal(reserv.Costo)
                e.save(update_fields=['Ingresos'])
                # Recargamos los recibos ya que acabamos de agregar
                recibos = RecibosModel.objects.all()
                
    # Si no es un POST es un GET, y mandamos un formulario vacio
    else:
        form = EstacionamientoPago()

    return render(request, 'pagoconfirm.html',{'reserva': reserv,'form':form,'recibos':recibos})


def recibo_pago(request, _id):
    _id = int(_id)
    # Verificamos que el objeto exista antes de continuar
    try:
        recibo = RecibosModel.objects.latest("id")
    except ObjectDoesNotExist:
        return render(request, '404.html')
    
    form = EstacionamientoPago()
    
    return render(request, 'recibo.html',{'recibo': recibo,'form':form})

def form_pago(request, _id):
    _id = int(_id)
    # Verificamos que el objeto exista antes de continuar
    try:
        reserv = ReservasModel.objects.latest("id")
    except ObjectDoesNotExist:
        return render(request, '404.html')
    
    recibos = RecibosModel.objects.all()

    form = EstacionamientoPago()

    return render(request, 'pagosform.html',{'reserva': reserv,'form':form,'recibos':recibos})


# Redirecciona los request de / a /estacionamientos

def index(request):
    return redirect('/estacionamientos')

def reporte_ingresos(request):
    form = EstacionamientoRif() 
    n =0
    if request.method == 'POST':
            # Creamos un formulario con los datos que recibimos
            form = EstacionamientoRif(request.POST)
            
            # Si el formulario es valido, entonces creamos un objeto con
            # el constructor del modelo
            if form.is_valid():
                # Recargamos los recibos ya que acabamos de agregar
                
                rif = form.cleaned_data['rif']
                est = Estacionamiento.objects.filter(Rif=rif)
                total =est.aggregate(sum=Sum('Ingresos'))
                if (len(est) == 0):
                    n=1
                return render(request, 'reporteingresos.html',{'form':form,'rif':rif,'est':est,'total':total,'n':n})
    # Si no es un POST es un GET, y mandamos un formulario vacio
    else:
        form = EstacionamientoRif()
     
    return render(request, 'reporteingresos.html',{'form':form})

def reporte_reservas(request):
    form = EstacionamientoCi() 
    n =0
    nombre=""   
    if request.method == 'POST':
            # Creamos un formulario con los datos que recibimos
            form = EstacionamientoCi(request.POST)
            
            # Si el formulario es valido, entonces creamos un objeto con
            # el constructor del modelo
            if form.is_valid():
                # Recargamos los recibos ya que acabamos de agregar
                
                ci = form.cleaned_data['ci']
                recibos = RecibosModel.objects.filter(Cedula=ci).order_by('FechaPago')
                total =recibos.aggregate(sum=Sum('Costo'))
                
                numero = RecibosModel.objects.filter(Cedula=ci).count()
                if (len(recibos) == 0):
                    n=1
                else:
                    n=2
                    nombre=recibos[0].Nombre
                return render(request, 'reportereservas.html',{'form':form,'nombre':nombre,'num':numero,'ci':ci,'recibo':recibos,'total':total,'n':n})
    # Si no es un POST es un GET, y mandamos un formulario vacio
    else:
        form = EstacionamientoCi()
     
    return render(request, 'reportereservas.html',{'form':form})

def reporte_tasas(request):
    form = EstacionamientoNombre() 
    n =0
    
    global listaReserva

    if request.method == 'POST':
            # Creamos un formulario con los datos que recibimos
            form = EstacionamientoNombre(request.POST)
            
            # Si el formulario es valido, entonces creamos un objeto con
            # el constructor del modelo
            if form.is_valid():
                # Recargamos los recibos ya que acabamos de agregar
                
                nomb = form.cleaned_data['nombre']
                est = Estacionamiento.objects.filter(Nombre=nomb)
                try:
                    est2 = Estacionamiento.objects.get(Nombre=nomb)
                except:
                    return render(request, 'reportetasas.html',{'form':form,'nombre':nomb,'est':est,'n':1})
                if (len(est) == 0):
                    n=1
                    
                Puestos = ReservasModel.objects.filter(Estacionamiento = est).values_list('InicioReserva', 'FinalReserva')
                Inic1 = FECHA_FIJA + datetime.timedelta(hours=est2.Apertura.hour) + datetime.timedelta(minutes=est2.Apertura.minute) + datetime.timedelta(seconds=est2.Apertura.second) + datetime.timedelta(days=1)
                Fin1 = FECHA_FIJA + datetime.timedelta(hours=est2.Cierre.hour) + datetime.timedelta(minutes=est2.Cierre.minute) + datetime.timedelta(seconds=est2.Cierre.second) + datetime.timedelta(days=1)
                if (Fin1 == Inic1):
                    Fin1 = FECHA_FIJA + datetime.timedelta(days=1)
                cap = (Fin1-Inic1).seconds * est2.NroPuesto
                tasas = []
                tasas.append(['Dia', 'Porcentaje'])
                
                for i in range (1,8):
                    Inic = FECHA_FIJA + datetime.timedelta(hours=est2.Apertura.hour) + datetime.timedelta(minutes=est2.Apertura.minute) + datetime.timedelta(seconds=est2.Apertura.second) + datetime.timedelta(days=i)
                    Fin = FECHA_FIJA + datetime.timedelta(hours=est2.Cierre.hour) + datetime.timedelta(minutes=est2.Cierre.minute) + datetime.timedelta(seconds=est2.Cierre.second) + datetime.timedelta(days=i)
                    if (Fin == Inic):
                        Fin = FECHA_FIJA + datetime.timedelta(days=1)
                    tasa = 0
                    
                    for obj in Puestos:
                        objI = obj[0].replace(tzinfo=None)
                        objF = obj[1].replace(tzinfo=None)
                        if (objI < Inic and objF < Fin and objF > Inic):
                            t_reserva = (objF-Inic).seconds
                            tasa = tasa + t_reserva
                        elif (objI > Inic and objF < Fin and objI < Fin):
                            t_reserva = (objF-objI).seconds
                            tasa = tasa + t_reserva
                        elif (objI > Inic and objF > Fin and objI < Fin):
                            t_reserva = (Fin - objI).seconds
                            tasa = tasa + t_reserva
                        elif (objF >  Fin and objI < Inic):
                            t_reserva = (Fin - Inic).seconds
                            tasa = tasa + t_reserva
                    tasa = tasa*100/cap
                    tasas.append(['dia ' + str(i), tasa])
                
                        
                
                return render(request, 'reportetasas.html',{'form':form,'nombre':nomb,'est':est,'n':n, 'dataZ': json.dumps(tasas)})
    # Si no es un POST es un GET, y mandamos un formulario vacio
    else:
        form = EstacionamientoNombre()
     
    return render(request, 'reportetasas.html',{'form':form})








