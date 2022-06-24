print ("Bienvenido al sistema de venta/compra de productos tecnologicos")
print ("Desea iniciar sesion o registrarse")
print ("1. Iniciar sesion")
print ("2. Registrarse")
opcion = input()
if opcion == "1":
 print ("Por favor ingrese su nombre de usuario:")
    usuario = input()
    print ("Por favor ingrese su contraseña:")
    contraseña = input()
    if usuario == "admin" and contraseña == "255075":
        print ("Bienvenido administrador")
 if opcion == "2":
    print ("Por favor ingrese su nombre de usuario:")
    usuario = input()
    print ("Por favor ingrese su contraseña:")
    contraseña = input()
    #crea un archivo de texto con el nombre de usuario y contraseña ingresados
    archivo = open("usuarios.txt", "a")
    archivo.write(usuario + " " + contraseña + "\n")
    archivo.close()
    print ("Usuario registrado")
