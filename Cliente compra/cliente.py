
class Cliente:
    def __init__(self, nombre, email, direccion, telefono):
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"Cliente: {self.nombre}"

    def mostrar_info(self):
        print("Información del Cliente:\n")
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")
        print(f"Dirección: {self.direccion}")
        print(f"Teléfono: {self.telefono}")

    def cambiar_telefono(self, nuevo):
        self.telefono = nuevo
        print("Teléfono actualizado.")
        

