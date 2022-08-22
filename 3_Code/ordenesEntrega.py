#Programa de ordenes de entrega 

import sqlite3
db_name = 'ordenesEntrega.db'
import PySimpleGUI as sg
sg.theme('SystemDefault1')
import random
import datetime

#Funcion para ejecutar consultas de base de datos
def run_query(query, parameters = ()):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, parameters)
        conn.commit()
    return result

#Definición de la interfaz gráfica con campos de texto y botón y etiquetas
layout = [
    [sg.Text('Código de orden', size=(15, 1)), sg.InputText(key='codigo'), sg.Button('Generar código')],
    [sg.Text('Cliente', size=(15, 1)), sg.InputText(key='cliente')],
    [sg.Text('Nombre del producto', size=(15, 1)), sg.InputText(key='nombreProducto')],
    [sg.Text('Fecha de entrega', size=(15,1)), sg.Input(key='fecha', size=(45,1)), sg.CalendarButton("Seleccionar Fecha", close_when_date_chosen=True,  target='fecha', no_titlebar=False, format=('%Y-%m-%d'))],
    [sg.Text('Dirección de entrega', size=(15, 1)), sg.InputText(key='direccion')],
    [sg.Button('Agregar'), sg.Button('Cancelar')] 
]

#Carga de la interfaz gráfica
window = sg.Window('Ordenes de entrega', layout)

#definición de la función agregarOrden
def agregarOrden():
    #Muestra una pregunta de confirmación para agregar la orden
    confirmacion = sg.popup_yes_no('¿Desea agregar la orden?')
    #Si se presiona la opción si
    if confirmacion == 'Yes':
        #Guarda los datos en la base de datos con la función run_query
        query = 'INSERT INTO ordenes (codigo, cliente, nombre, fecha, direccion) VALUES ("{}", "{}", "{}", "{}", "{}")'.format(values['codigo'], values['cliente'], values['nombreProducto'], values['fecha'], values['direccion'])
        parameters = ()
        run_query(query, parameters)
        #Muestra un mensaje de confirmación
        sg.popup('Orden agregada')
        #Limpia los campos de texto
        window['codigo'].update('')
        window['cliente'].update('')
        window['nombreProducto'].update('')
        window['fecha'].update('')
        window['direccion'].update('')
    #Si se presiona la opción no
    if confirmacion == 'No':
        #Limpia los campos de texto del menú principal
        window['codigo'].update('')
        window['cliente'].update('')
        window['nombreProducto'].update('')
        window['fecha'].update('')
        window['direccion'].update('')

#Funcion principal
def main():
    #Ciclo de ejecución de la interfaz gráfica
    while True:
        #Lee los datos de la interfaz gráfica
        event = window.read()
        #Si se presiona el botón agregar
        if event == 'Agregar':
            #Llama a la función agregarOrden
            agregarOrden()
        #Si se presiona el botón cancelar
        if event == 'Cancelar':
            #Cierra la ventana
            window.close()
            #Finaliza el programa
            exit()

#Funcion que genera el código de la orden aleatoriamente
def generarCodigo():
    #Se genera un código aleatorio de 4 dígitos
    codigo = str(random.randint(1000, 9999))
    #Se busca si el código ya existe en la base de datos
    query = 'SELECT codigo FROM ordenes WHERE codigo = "{}"'.format(codigo)
    parameters = ()
    result = run_query(query, parameters)
    #Si el código ya existe, se vuelve a generar un código aleatorio
    if result.fetchone() is not None:
        generarCodigo()
    #Si el código no existe, se retorna el código
    else:
        return codigo

#Funcion que ingresa el código de la orden en la interfaz gráfica
def ingresarCodigo():
    #Se genera un código aleatorio
    codigo = generarCodigo()
    #Se ingresa el código en la interfaz gráfica
    window['codigo'].update(codigo)

#Muestrar la interfaz gráfica
while True:
    event, values = window.read()
    #Llama a la función generarCodigo
    if event == 'Agregar':
        #Si se presiona el botón de agregar, se verifica que los campos no estén vacíos
        if values['codigo'] == '' or values['cliente'] == '' or values['nombreProducto'] == '' or values['fecha'] == '' or values['direccion'] == '':
            sg.popup_error("Error", "Por favor, ingrese todos los datos")
        elif any(char.isalpha() for char in values['codigo']):
            sg.popup_error("Error", "El código debe ser numérico. Por favor, utilice el generador de códigos")
        #La fecha no debe contener letras, muestra un mensaje de error si tiene letras
        elif any(char.isalpha() for char in values['fecha']):
            sg.popup_error("Error", "La fecha es inválida. (Recuerde que no debe contener letras)")
        #La fecha debe ser mayor a la fecha actual y debe estar en el formato aaaa-mm-dd, muestra un mensaje de error si no es así
        elif values['fecha'] < str(datetime.date.today()):
            sg.popup_error("Error", "La fecha es inválida. (Debe ser mayor a la fecha actual)")
        elif values['fecha'][4] != '-' or values['fecha'][7] != '-':
            sg.popup_error("Error", "La fecha es inválida. (Recuerde que debe estar en el formato aaaa-mm-dd)")
        #El numero para el mes debe ser entre 1 y 12, y el numero para el dia debe ser entre 1 y 31, muestra un mensaje de error si no es así
        elif int(values['fecha'][5:7]) < 1 or int(values['fecha'][5:7]) > 12 or int(values['fecha'][8:10]) < 1 or int(values['fecha'][8:10]) > 31:
            sg.popup_error("Error", "La fecha es inválida. (El mes y el dia deben ser válidos)")
        else:
            #Si los campos no están vacíos, se ejecuta la función agregarOrden
            agregarOrden()
    elif event == 'Cancelar':
        #Si se presiona el botón de cancelar, se cierra la ventana
        break
    elif event == 'Generar código':
        #Si se presiona el botón de generar código, se llama a la función ingresarCodigo
        ingresarCodigo()
    elif event == sg.WIN_CLOSED:
        break
window.close()
