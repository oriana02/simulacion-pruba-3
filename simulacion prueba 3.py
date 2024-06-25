def menu():
    print("""1. Registrar pedido
             2. Listas de todos los pedidos
             3. Imprimir hoja de ruta
             4. Salir del programa""")

def registrar_pedido(nombre, apellido, comuna, detalle_pedido ):
    if nombre == "":
        nombre = input("Ingrese Nombre: ")
        apellido = input("Ingrese Apellido: ")
        comuna = input("Ingrese comuna")
        detalle_pedido =input("Detalle del pedido")
        
        
