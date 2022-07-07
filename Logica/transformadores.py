from datetime import datetime, date
import numpy as np

def dias_demora(fecha_a, fecha_b): ### el primer metodo que se aplica
    if fecha_b == None:
        fecha_b = '1900-01-01' 
    
    fecha1 = datetime.strptime(fecha_a, '%Y-%m-%d')
    fecha2 = datetime.strptime(fecha_b, '%Y-%m-%d')

    return (fecha1-fecha2).days

def estado_tiempo(fechaVen,fechaRes):

    
    hoy = str(date.today())
    diasRetraso = dias_demora(fechaVen,fechaRes) 
    diasHoy =  dias_demora(hoy,fechaVen)

    if diasRetraso >= 0 and diasRetraso < 40000:
        return 'A tiempo'
    elif (diasHoy < 0):
        return 'A tiempo'
    else:
        return 'Fuera de tiempo'
        
def estado_respuesta(estado):
    if estado == "4" or estado == "5":
        return 'Resuelto'
    else:
        return 'No Resuelto'       

#def caracterizacion_tipo(lista_atrr):
    #if None in lista_atrr:


    

