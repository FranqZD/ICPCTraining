Liston = input().split(" ")
#ListaClin[0] es el tamaño del golpe q tiene que pegar
#ListaClin[1] es el tiempo que tarda en golpear otra vez despues de pegar
ListaClin=[int(data) for data in Liston]
if ListaClin[0]%3 == 0 and ListaClin[1]==0:
    tercerapart = ListaClin[0]//3
    print(tercerapart+3)
elif ListaClin[0]<=ListaClin[1]:
    print(ListaClin[0])
#Aqui es en caso de que el tiempo que tarda es menor o igual a la mitad
else:
    print(ListaClin[0]//2+ListaClin[1]+1)
