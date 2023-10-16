casos = int(input())
for i in range(casos):
    Datos = [int(data) for data in input().split(" ")]
    contador = 0
    Resta = 0
    
    while Datos[0]!=Datos[1]:
        Resta = abs(Datos[0]-Datos[1])
        contador+=1

        if Resta>Datos[2]:
            
            if(Datos[0]>Datos[1]):
                Datos[1]+=Datos[2]
                Datos[0]-=Datos[2]
                
            else:
                Datos[0]+=Datos[2]
                Datos[1]-=Datos[2]
        else:
            
            if(Datos[1]<Datos[0]):
                Datos[1]+=((Resta)/2)
                Datos[0]-=((Resta)/2)
                
            else:
                Datos[1]-=((Resta)/2)
                Datos[0]+=((Resta)/2)
                
    print(contador)