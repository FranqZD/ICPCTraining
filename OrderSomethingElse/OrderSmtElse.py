Datos = input()
Data = [int (datos) for datos in Datos.split() ]
Dishes = input()
DishesS = [int (num) for num in Dishes.split()]
DishesS.sort()
if DishesS[0]+Data[2]<Data[1]:
    print(DishesS[0]+Data[2])
else:   
    print (Data[1])