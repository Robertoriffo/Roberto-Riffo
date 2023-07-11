#programa principal
import os 
import numpy as np
import funcionExamen as fn 
from funcionExamen import disponible,validoPiso,mostrarycomprardepartamento,llenadomatriz,valiaOP, llenar,mostrarDepartamentos, validoEleguir,llenarmatriz

1#ingresar datos a la matriz
2#comprar departamento
3#ver list
#definir menu
rut=0
ruts=0
matriz=np.empty([10,4]),type(int(int))
otra=np.empty([10,4]),type(int(int))
fn.llenar(matriz,otra)

#poner las opciones 
# OPCION 1  
while(True):
    try:
       op=int(input("ingrese la opcion deseada:"))
       if (op>0 and op<6):
         break
       else:
        print ("debe escojer una opcion entre 1 y 5")
    except ValueError:
        print("debe ingresar una opcion")
#  Comprar departamento
if(op==1):
    l=1
    fn.mostrarDepartamentos(matriz)
    print(matriz)
    input("pulsas cualquier tecla")
    dd=fn.piso()
    fn.mostrarDepartamentos(matriz)
    cc=fn.disponible(matriz,otra)
    if(cc): #si cc es verdadero el departamento esta disponible o no lo esta
        print("el departamento esta disponible")
        pagar=fn.comprardepartamento(matriz,otra)
        print("\usted debera cancelar un total de: $", pagar)
        os.system("pulse cualquier tecla")
    fn.validoEleguir(matriz,otra)


#OPCION 2 
if (op==2):
    dd=fn.disponible()
if(l==1):
      fn.mostrar(matriz)
os.system("cls")
#OPCION 3 mostar listado
if(op==3):
fn.listado(ruts)
os.system("pulse cualquier tecla")
#opcion 4 
if(op==4):
    suma=0
    suma=fn.totalventa(otra)
    if(suma==0):
        print("\t No se han vendido pasajes aun")
    else:
        print("\t El total vendido hasta ahora es de : $",suma)
    os.system("pause")
#Opcion 5       
if(op==5):
    ("adios,buen dia")
    os.system