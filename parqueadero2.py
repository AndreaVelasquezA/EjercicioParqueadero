import numpy as np
from datetime import datetime
carros=[]



dt = datetime.now()
min1=("minuts=",dt.minute)
min2=("minuts=",dt.minute)

def datos():
    a=str(input("digite la placa de el auto: "))
    x = datetime.now()
    h=(x.hour)*60
    m=x.minute
    total=h+m
    print("el vehiculo entró a las: ",x) 
    return[a,total,x]

def datos_s():
    x = datetime.now()
    h=(x.hour)*60
    m=x.minute
    total=h+m
    print("el vehiculo salió a las: ",x) 
    return total

vehiculos=0
ganancia=0
parqueos=0

while True:
    
    texto_menu = """ \n *** PARQUEADERO ***:  

                    1. Agregar vehículo  

                    2. Retirar vehículo 

                    3. Reporte de totales 

                    4. Salir 

                """

    print(texto_menu) 

    opcion = int(input("Digite su selección: ")) 

    if(opcion == 1):
        c=int(input("digite el numero de entrada al parqueadero del carro: "))
        carro=datos()
        carros.append(c)            
        print("recuerde que su auto es el numero",c)

    elif(opcion ==2):
        s=int(input("digite el numero del carro que va a salir: "))
        carrof=datos_s()   
        tp=(carrof-c[1])*80 
        print("el vehiculo de placa: ",carro[0])  
        print("que ingreso a la fecha: ",carro[2])   
        print("el total a pagar es: ",tp)   
            

    elif(opcion ==3):
        tp=(carrof-c[1])*80 
        ganancia=ganancia+tp
        print("la ganancia total hasta ahora es: ganancia: ",ganancia)  
        print("los parqueos hechos el dia de hoy son: ", parqueos)  
        vehiculos-=1
        print("los autos que se encuentran en el parqueadero son: ", vehiculos)
       
    
    if(opcion == 4):
            print("gracias por confiar en nosotros")
            break
