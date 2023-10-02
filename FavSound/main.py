Data = input()
Datos = [int(datos) for datos in Data.split()]
if(Datos[0]*Datos[2]<= Datos[1]):
    print(Datos[2])
else:
    print(int(Datos[1]/Datos[0]))