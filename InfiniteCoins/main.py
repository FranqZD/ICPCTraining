N = int(input())
A = int(input())

if(N%500 == 0):
    print("Yes")
else:
    Resto = int(N%500)
    if(Resto>A):
        print("No")
    else:
        print("Yes")