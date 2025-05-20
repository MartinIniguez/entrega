
from cliente import Cliente

clientes = []

def registrar_cliente():
    print("Registro de nuevo cliente \n")
    try:
        nombre = input("Ingresa nombre: ")
        email = input("Ingresa email: ")
        direccion = input("Ingresa dirección: ")
        telefono = input("Ingresa teléfono: ")

        if nombre == "" or email == "" or direccion == "" or telefono == "":
            print("Todos los campos son obligatorios.")
            return

        nuevo = Cliente(nombre, email, direccion, telefono)
        clientes.append(nuevo)
        print("Cliente registrado con éxito.\n")
    except:
        print("Ocurrió un error al registrar al cliente.")

def mostrar_clientes():
    print("Clientes guardados:")
    if len(clientes) == 0:
        print("No hay clientes registrados.\n")
    else:
        for c in clientes:
            print(c)
            c.mostrar_info()

def cambiar_telefono():
    print("Cambiar numero de telefono de cliente.")
    nombre = input("Nombre del cliente: ")

    for cliente in clientes:
        if cliente.nombre == nombre:
            nuevo_telefono = input ("Nuevo telefono: ")
            cliente.cambiar_telefono (nuevo_telefono)
            return
        
            

def main():
    while True:
        print("---MENU---")
        print("1. Registrar cliente")
        print("2. Ver clientes")
        print("3. Salir")
        print("4. Cambiar telefono \n")
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            mostrar_clientes()
        elif opcion == "3":
            print("Hasta la vista baby!")
            break
        elif opcion == "4":
            cambiar_telefono()
            input("Ingresa telefono nuevo: ")
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()

