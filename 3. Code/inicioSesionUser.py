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
