Cant = input()
Numeros = input()
Numero = [int (num) for num in Numeros.split()]
Numero.sort()
print(Numero)

if(sum(Numero)-Numero[len(Numero)-1] <= Numero[len(Numero)-1]):
    print("Yes")
else:
    print("False")