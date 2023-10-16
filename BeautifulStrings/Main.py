texto  = input()
Resultado = "Yes"
for letra in texto:
    resultado = texto.count(letra)
    if(resultado % 2 != 0):
        Resultado = "No"
        break
print(Resultado)
    