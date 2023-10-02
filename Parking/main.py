Data = input()
Datos = [int(datos) for datos in Data.split()]

if(Datos[0]*Datos[1]>Datos[2]):
    print(Datos[2])
else:
    print(Datos[0]*Datos[1])