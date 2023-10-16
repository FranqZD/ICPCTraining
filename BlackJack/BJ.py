Datos = input()
Data = [int (data) for data in Datos.split()]

if(Data[0]+Data[1]+Data[2]>= 22):
    print("bust")
else:
    print("win")

