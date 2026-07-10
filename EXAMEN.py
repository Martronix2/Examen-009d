Veiculos = {
    "V001":["TOYOTA","Modelo","Sendán","B",True,"China"],
    "V002":["TOYOTA","Modelo","SUV","B",True,"China"],
    "V003":["TOYOTA","Modelo","Pickup","B",True,"China"],
}
Inventario={"V001":[1,4],"V002":[100000,4],"V003":[100000,4]}

opcion_menu=0
def menu_texto():
    print("=============================================")
    print("1.   Stock disponble")
    print("2.   Buscar Vehículo por rango de precio")
    print("3.   Actualizar precio")
    print("4.   Agregar Vehículo")
    print("5.   Eliminar Vehículo")
    print("6.   Salir")
    print("=============================================")

def leer_menu():
    a=True
    while a:
        try:
            entrada=int(input("Ingrese el menu: "))
            if entrada > 0 and entrada < 7:
                a=False
                return entrada
            else:
                print("Error: Tiene que ingresar una opcion del menu")
        except:
            print("Error: Tiene que ingresar un numero")

def stock_tipo(tipo):
    total=0
    existe=False
    for codigo in Veiculos:
        if Veiculos[codigo][2].lower()==tipo.lower():
            existe=True
            total=+Inventario[codigo][1]
    if existe:
        print(f"Hay un {total} vehículos con ese modelo")
    else:
        print("No se encontro ningun vehículo con ese modelo")

def buscar_precio(minimo,maximo):
    lista=[]
    hay=False
    for codigo in Inventario:
        if Inventario[codigo][1] >= minimo or maximo <= Inventario[codigo][1]:
            lista.append(Veiculos[codigo][1]+" "+Veiculos[codigo][2]+"--"+codigo)
            hay=True
    if hay:
        print("Se encontraron los siguientes vehiculos ",lista)
    else:
        print("No se encontro ningun vehiculo en ese rango")

while opcion_menu != 6:
    menu_texto()
    opcion_menu=leer_menu()
    match opcion_menu:
        case 1:
            #stock disponible
            try:
                tipo=input("Ingrese el tipo del vehículo: ")
                stock_tipo(tipo)
            except ValueError:
                print("Error: Volviendo al menu")
        case 2:
            #Buscar veículo por rango de precios}
            a=True
            while a:
                try:  
                    minimo=int(input("Ingrese el minimo: "))
                    maximo=int(input("Ingrese el maximo: "))
                    buscar_precio(minimo,maximo)
                    a=False
                except:
                    print("Error: Tiene que ingresar un numero")
        case 3:
            #actualizar precio
            print("HOLA")
        case 6:
            print("Terminando programa")