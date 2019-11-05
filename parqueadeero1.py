from datetime import datetime
def datos():
    a=str(input("digite la placa de el auto"))
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
    print("hola bienvenido a Original ParkingLot")
    a=int(input("digite 1 cuando ingrese un vehiculo o digite 2 si va a salir un vehiculo. si quiere salir del programa entre una tecla: "))

    if a==1:

        if vehiculos<10:
            vehiculos+=1
            parqueos+=1
            if vehiculos==1:
                carro1=datos()            
                print("recuerde que su auto es el numero 1")


            elif vehiculos==2:
                carro2=datos()            
                print("recuerde que su auto es el numero 2")


            elif vehiculos==3:         
                carro3=datos()            
                print("recuerde que su auto es el numero 3")


            elif vehiculos==4:
                carro4=datos()            
                print("recuerde que su auto es el numero 4")


            elif vehiculos==5:
                carro5=datos()            
                print("recuerde que su auto es el numero 5")


            elif vehiculos==6:
                carro6=datos()            
                print("recuerde que su auto es el numero 6")


            elif vehiculos==7:
                carro7=datos()            
                print("recuerde que su auto es el numero 7")

        
            elif vehiculos==8:
                carro8=datos()            
                print("recuerde que su auto es el numero 8")


            elif vehiculos==9:
                carro9=datos()  
                print("recuerde que su auto es el numero 9")          


            elif vehiculos==10:
                carro10=datos()   
                print("recuerde que su auto es el numero 10")         


        else:
         print("lo siento no hay espacio disponible para otro vehiculo")

    elif  a==2:
        s=int(input("digite el numero del carro que va a salir: "))
        if s==1:
            carrof=datos_s()   
            tp=(carrof-carro1[1])*80 
            print("el vehiculo de placa: ",carro1[0])  
            print("que ingreso a la fecha: ",carro1[2])   
            print("el total a pagar es: ",tp)   
            print("")
            print("") 
            ganancia=ganancia+tp
            print("la ganancia total hasta ahora es: ganancia: ",ganancia)  
            print("los parqueos hechos el dia de hoy son: ", parqueos)  
            vehiculos-=1
            print("los autos que se encuentran ahorita son: ", vehiculos)

        elif s==2:
            carrof=datos_s()   
            tp=(carrof-carro2[1])*80  
            print("el vehiculo de placa: ",carro2[0])  
            print("que ingreso a la fecha: ",carro2[2]) 
            print("el total a pagar es: ",tp)    
            print("")
            print("")   
            ganancia=ganancia+tp
            print("la ganancia total hasta ahora es: ganancia: ",ganancia)      
            print("los parqueos hechos el dia de hoy son: ", parqueos)  
            vehiculos-=1
            print("los autos que se encuentran ahorita son: ", vehiculos)

        elif s==3:         
            carrof=datos_s()   
            tp=(carrof-carro3[1])*80  
            print("el vehiculo de placa: ",carro3[0])  
            print("que ingreso a la fecha: ",carro3[2]) 
            print("el total a pagar es: ",tp)
            print("")
            print("")         
            ganancia=ganancia+tp
            print("la ganancia total hasta ahora es: ganancia: ",ganancia)    
            print("los parqueos hechos el dia de hoy son: ", parqueos)  
            vehiculos-=1
            print("los autos que se encuentran ahorita son: ", vehiculos)

        elif s==4:
            carrof=datos_s()   
            tp=(carrof-carro4[1])*80 
            print("el vehiculo de placa: ",carro4[0])  
            print("que ingreso a la fecha: ",carro4[2]) 
            print("el total a pagar es: ",tp)  
            print("")
            print("")    
            ganancia=ganancia+tp
            print("la ganancia total hasta ahora es: ganancia: ",ganancia)       
            print("los parqueos hechos el dia de hoy son: ", parqueos)  
            vehiculos-=1
            print("los autos que se encuentran ahorita son: ", vehiculos)

        elif s==5:
            carrof=datos_s()   
            tp=(carrof-carro5[1])*80 
            print("el vehiculo de placa: ",carro5[0])  
            print("que ingreso a la fecha: ",carro5[2])  
            print("el total a pagar es: ",tp)   
            print("")
            print("")    
            ganancia=ganancia+tp
            print("la ganancia total hasta ahora es: ganancia: ",ganancia)      
            print("los parqueos hechos el dia de hoy son: ", parqueos)  
            vehiculos-=1
            print("los autos que se encuentran ahorita son: ", vehiculos)

        elif s==6:
            carrof=datos_s()   
            tp=(carrof-carro6[1])*80    
            print("el vehiculo de placa: ",carro6[0])  
            print("que ingreso a la fecha: ",carro6[2]) 
            print("el total a pagar es: ",tp) 
            print("")
            print("")  
            ganancia=ganancia+tp
            print("la ganancia total hasta ahora es: ganancia: ",ganancia)       
            print("los parqueos hechos el dia de hoy son: ", parqueos)  
            vehiculos-=1
            print("los autos que se encuentran ahorita son: ", vehiculos)

        elif s==7:
            carrof=datos_s()   
            tp=(carrof-carro7[1])*80 
            print("el vehiculo de placa: ",carro7[0])  
            print("que ingreso a la fecha: ",carro7[2]) 
            print("el total a pagar es: ",tp)    
            print("")
            print("")
            ganancia=ganancia+tp
            print("la ganancia total hasta ahora es: ganancia: ",ganancia)           
            print("los parqueos hechos el dia de hoy son: ", parqueos)  
            vehiculos-=1
            print("los autos que se encuentran ahorita son: ", vehiculos)
        
        elif s==8:
            carrof=datos_s()
            tp=(carrof-carro8[1])*80 
            print("el vehiculo de placa: ",carro8[0])  
            print("que ingreso a la fecha: ",carro8[2])     
            print("el total a pagar es: ",tp) 
            print("")
            print("")         
            ganancia=ganancia+tp
            print("la ganancia total hasta ahora es: ganancia: ",ganancia)   
            print("los parqueos hechos el dia de hoy son: ", parqueos)  
            vehiculos-=1
            print("los autos que se encuentran ahorita son: ", vehiculos)

        elif s==9:
            carrof=datos_s() 
            tp=(carrof-carro9[1])*80  
            print("el vehiculo de placa: ",carro9[0])  
            print("que ingreso a la fecha: ",carro9[2])  
            print("el total a pagar es: ",tp) 
            print("")
            print("")      
            ganancia=ganancia+tp
            print("la ganancia total hasta ahora es: ganancia: ",ganancia)                    
            print("los parqueos hechos el dia de hoy son: ", parqueos)  
            vehiculos-=1
            print("los autos que se encuentran ahorita son: ", vehiculos)

        elif s==10:
            carrof=datos_s() 
            tp=(carrof-carro10[1])*80 
            print("el vehiculo de placa: ",carro10[0])  
            print("que ingreso a la fecha: ",carro10[2]) 
            print("el total a pagar es: ",tp) 
            print("")
            print("")    
            ganancia=ganancia+tp
            print("la ganancia total hasta ahora es: ganancia: ",ganancia)   
            print("los parqueos hechos el dia de hoy son: ", parqueos)  
            vehiculos-=1
            print("los autos que se encuentran ahorita son: ", vehiculos)
    else:
        print("chau")
        break
