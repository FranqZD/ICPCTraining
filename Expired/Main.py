Data = input()
DatosInt = [int(data) for data in Data.split() ]
if(DatosInt[1]-DatosInt[2]>=0):
    print("delicious")
elif(DatosInt[0]>=(DatosInt[2]-DatosInt[1])):
    print("safe")
else:
    print("dangerous")