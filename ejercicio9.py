batera=0
numero= int(input("ingrese un numero "))
if numero%2==0:
    print(f"es un numero par {numero}")
else:
    for i in range(2,numero):
        if numero%i==0:
            batera=1
    if batera==0:
        print(f"es un numero primo {numero}") 
    else:
        print(f"no es un numero {numero}")



