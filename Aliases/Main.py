Cases = int(input())
Diccionario = {}
for i in range(Cases):
    Iniciales = ""
    Name = input().split()
    for l in range(1,int(Name[0])+1,1):
        #print(l)
        Iniciales+=Name[l][0]
    if Iniciales not in Diccionario:
        Diccionario[Iniciales] = 1
    else:
        Diccionario[Iniciales]+=1
Contador = 0
for Key in Diccionario:
    if Diccionario[Key] < 2:
       Contador += 1
#print (Diccionario)
print (Contador)
    
        
    

    