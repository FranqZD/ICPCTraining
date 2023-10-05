Data = input()
Datos = [int(data) for data in Data.split() ]
if(Datos[0] > Datos[1]+1):
    print(Datos[0] + (Datos[0]-1))
elif(Datos[1]>Datos[0]+1):
    print(Datos[1] + (Datos[1]-1))
else:
    print(Datos[0]+Datos[1])