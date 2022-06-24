print("Bienvenido al sistema de administración")
print("Por favor ingrese su nombre de usuario:")
usuario = input()
print("Por favor ingrese su contraseña:")
contraseña = input()
if usuario == "admin" and contraseña == "255075":
    print("Bienvenido administrador")
else:
    print("Nombre de usuario o contraseña incorrectos")
    print("Intente nuevamente")
    print("Por favor ingrese su nombre de usuario:")
    usuario = input()
    print("Por favor ingrese su contraseña:")
    contraseña = input()
    if usuario == "admin" and contraseña == "255075":
        print("Bienvenido administrador")
