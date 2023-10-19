fila = int(input())
if fila == 1:
    print("1 1")
elif fila == 0:
    print("1")
else:
    ListaPascal = [1,1]
    ListaResultado = []
    i=1
    for i in range(fila):
        ListaResultado.append(1)
        for l in range(1,i):
            ListaResultado.append(ListaPascal[l]+ListaPascal[l-1]) 
            print(ListaPascal[l],ListaPascal[l-1])
            
        ListaResultado.append(1)    
        ListaPascal = list(ListaResultado)
        ListaResultado.clear()
        
    print("RESULTADO BUENO",ListaPascal)
        