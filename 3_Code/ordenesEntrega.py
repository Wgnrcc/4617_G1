#Programa de ordenes de entrega 

import sqlite3
db_name = 'ordenesEntrega.db'
import PySimpleGUI as sg
sg.theme('SystemDefault1')

#Funcion para ejecutar consultas de base de datos
def run_query(query, parameters = ()):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, parameters)
        conn.commit()
    return result
    
#Funcion que valida la fecha
#def validarFecha(fecha):
    #

#Definición de la interfaz gráfica con campos de texto y botón y etiquetas
layout = [
    [sg.Text('Código de orden', size=(15, 1)), sg.InputText(key='codigo')],
    [sg.Text('Cliente', size=(15, 1)), sg.InputText(key='cliente')],
    [sg.Text('Nombre del producto', size=(15, 1)), sg.InputText(key='nombreProducto')],
    [sg.Text('Fecha de entrega', size=(15, 1)), sg.InputText(key='fecha')],
    #Entrada para seleccionar fecha
    #[sg.CalendarButton(button_text='Fecha de entrega', target='fecha')],
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
            #Llama a la función validarFecha
            #if validarFecha(values['fecha']):
                #Llama a la función agregarOrden
            agregarOrden()
            #Si la fecha no es correcta
            #else:
                #Muestra un mensaje de error
                #sg.popup('Fecha no válida')
        #Si se presiona el botón cancelar
        if event == 'Cancelar':
            #Cierra la ventana
            window.close()
            #Finaliza el programa
            exit()

#Muestrar la interfaz gráfica
while True:
    event, values = window.read()
    if event == 'Agregar':
        #Si se presiona el botón de agregar, se verifica que los campos no estén vacíos
        if values['codigo'] == '' or values['cliente'] == '' or values['nombreProducto'] == '' or values['fecha'] == '' or values['direccion'] == '':
            sg.popup_error("Error", "Por favor, ingrese todos los datos")
        else:
            #Si los campos no están vacíos, se ejecuta la función agregarOrden
            agregarOrden()
    elif event == 'Cancelar':
        #Si se presiona el botón de cancelar, se cierra la ventana
        break
    elif event == sg.WIN_CLOSED:
        break
window.close()


