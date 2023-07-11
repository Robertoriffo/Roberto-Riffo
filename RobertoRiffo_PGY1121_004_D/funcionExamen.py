import os
import numpy as np
listado=0
eleguir=0
pago=0
tipoA=0
tipoB=0
tipoC=0
tipoD=0
op=0
p=1
r=0
while(op!=6):
    os.system("cls")
    print("     casa feliz     ")
    print("     **********************     ")
    print(" 1.  comprar departamento ")
    print(" 2.  mostrar departamento disponible")
    print(" 3.  ver listado de compradores  ")
    print(" 4.  mostrar ganancias totales ")
    print(" 5.  salir ")
def llenar(matriz,otra):#esta funcion me llena las matrices
    p=1
    for i in range (10):
        for j in range (4):
            matriz[i,j]=p
            otra[i,j]=p
            p+=1
#opcion 1 comprar departamento            
def valiaOP():
    pp=0
    while(True):
        try:
            pp=int(input)("elija opcion")
            if(pp>=1 and pp<=6):
             break
            else:
                 print("debe ingresar una opcion entre 1 y 5")
        except ValueError:
            print("Debe ingresar un numero entero  ")
    return pp
def mostrarDepartamentos(otra):
    os.system("cls")
    for i in range (10):
        print("\n") #salto de linea o departamento
        for j in range (4):
            if(j==1 or j==4):
                print("\n",otra[i,j],end="     " )
            else:
                print("\n",otra[i,j],end="   ")
    print("\n\n")
#registar rut de la persona (Opcion 1)
def llenadomatriz(matriz):
    for i in range (10):
        p=1
    os.system("cls")
    for j in range(4):
        if(i==0):
         os.system("cls")
        print("ingresar rut del cliente",p)
        rut=""
        while(len(rut)<=0):
            rut=int(input("su rut debe tener minimo 8 caracteres"))
            if(len(rut.strip()<=8)):
                print("no se puede tener menos de 8 caracteres")
                rut=""
        matriz[i][j]=rut
        p+1
#comprar departamento,precio de los departamentos (OPCION 1)
def mostrarycomprardepartamento(matriz,otra,rut):
    pago
    if(tipoA=="3.800 UF"):
        pago= 3.800 
    if(tipoB=="3.000 UF"):
        pago= 3.000 
    if(tipoC=="2.800 UF"):
        pago= 2.800 
    if(tipoD=="3.500 UF"):
        pago = 3.500
    
    for i in range (10):
        for j in range(4):
            if(matriz==otra[i,j]):
                while (True):
                   while(True):
                    try:
                        ruts=int(input("Rut debe tener 8 digitos minimo"))
                        if(rut<9999999):
                            print("debe tener 8 digitos minimo")
                        else:
                            break
                    except ValueError:
                                print("debe ser numero entero")
                    if(len(ruts)>0):
                        sw=0
                        for y in range(len(ruts)):
                            if(rut)==ruts[y]:
                                sw=1
                        if(sw==1):
                           print("el rut ya existe y no se puede agregar el pasajero")
                        else:
                            ruts.append(rut)
                            break
                    else:
                        ruts.append(rut)
                        break
#eleguir departamento (OPCION 1)
def validoEleguir():
    os.system("cls")
    eleguir=""
    while(len(des)<=0):
        print("Tipo A")
        print("Tipo B")
        print("Tipo C")
        print("Tipo D")
        print()
        des=input(" Elija el tipo de departamento:").lower()
        if(eleguir!="Tipo A" and eleguir!="Tipo B" and eleguir!="Tipo C" and eleguir!="Tipó D")
           print("debe ingresar una opcion correcta")
           eleguir=""
    return eleguir
#eleguir piso (Opcion 1)
def validoPiso():
    piso=0
    while(True):
        try:
            piso=int(input("ingrese numero de piso entre 1 y el 4")
            if(piso>=1):
            break
            else:
                print("Error debe ingresar un piso entre 1 y el 4")
    except ValueError:
        print("debe ser un numero positvo y entero")
        return piso



#OPCION 2 Mostrar departamentos disponible
def disponible(matriz,otra):
    for i in range(10):
        for j in range(4):
            if(matriz==otra[i,j]):
                return True
        return False

#OPION 3 ver listado de compradores
def validolistado(r):
    r.sort()
    print("Listado de compradores de departamentos ordenados de menor a mayor")
    print("\t",r)
#OPCION 4 mostrar ventas totales
def totalventa(matriz):
    suma=0
    for i in range(10):
        for j in range(4):
            if(matriz[i,j]!=0) and matriz[i,j]>104:
        return suma
def mostrar_totalventa(matriz,otra):
    cant_A = 0
    cant_B = 0
    cant_C = 0
    cant_D = 0
    valorA = 3800
    valorB = 3000
    valorC = 2800
    valorD = 3500
    total_vendido = 0    
    for i in range(40):
        tipo_depto = matriz_otra[i][1]
        if( tipo_depto != None):
            if(tipo_depto == "A"):
                cant_A = cant_A + 1
                total_vendido = total_vendido + valorA
            elif(tipo_depto == "B"):
                cant_B = cant_B + 1
                total_vendido = total_vendido + valorB
            elif(tipo_depto == "C"):
                cant_C = cant_C + 1
                total_vendido = total_vendido + valorC
            elif(tipo_depto == "D"):
                cant_D = cant_D + 1
                total_vendido = total_vendido + valorD
    
    print("| Tipo de Departamento | Cantidad | Total ")
    print("| Tipo A 3.800 UF      |    ",cant_A,"   | ",(cant_A*valorA)," ")
    print("| Tipo B 3.800 UF      |    ",cant_B,"   | ",(cant_B*valorB)," ")
    print("| Tipo C 3.800 UF      |    ",cant_C,"   | ",(cant_C*valorC)," ")
    print("| Tipo D 3.800 UF      |    ",cant_D,"   | ",(cant_D*valorD)," ")
    print("| TOTAL                |    ",(cant_A+cant_B+cant_C+cant_D),"   | ",total_vendido,"")
    input("Presione enter para continuar...")
