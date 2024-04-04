def listaManual():
    pass

def sumatoria():
    pass

def promedio():
    pass

def edadMayorNum():
    pass

def edadMenorNum():
    pass

def mostrarEdadLetras():
    pass

def ordenarEdadAscendente():
    pass

def ordenarEdadDescendente():
    pass

def diferenciaEdadYPromedio():
    pass

def archivo():
    pass

def main():
    print("MENU PRINCIPAL \n")
    print("1-Cargar lista de forma manual \n2- Calcular sumatoria \n3-Calcular promedio \n4- Mostrar edad mayor en número \n5- Mostrar edad menor en número \n6- Mostrar la edad en letras\n7- Ordenar Ascendente las Edades\n8- Ordenar Descendente las Edades\n9- Mostrar Diferencia entre cada edad y promedio\n10- Registrar datos en un archivo")
    n = int(input(":"))

    if n == 1:
        listaManual("parametros que nos pasen los grupos")
    elif n == 2:
        sumatoria()
    elif n == 3:
        promedio()
    elif n == 4:
        edadMayorNum()
    elif n == 5:
        edadMenorNum()
    elif n == 6:
        mostrarEdadLetras()
    elif n == 7:
        ordenarEdadAscendente()
    elif n == 8:
        ordenarEdadDescendente()
    elif n == 9:
        diferenciaEdadYPromedio()
    elif n == 10:
        archivo()
    

if _name_ == "_main_":
    main()