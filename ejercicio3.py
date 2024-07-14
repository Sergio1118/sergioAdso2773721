i=0
while i<3:
    opcion=int(input("opcion 1 calcular el area del cuadrado \n opcion 2 calcular el area del triangulo \n opcion 3 calcular el area del rectangulo \n opcion 4 calcular el area del circulo\n utliliza cualquier numero entra 5 acia delete para salidaser"))
    resutadol=0
    match opcion:
        case 1:
            lado=int(input("calcular el area del cuadrado \n ingrese e lado del el cuadrado"))
            resutadol=lado*lado
            print(f"el area del el cuadrado es:{resutadol}")
        case 2:
            base=int(input("calcular el area del el triangulo \n ingrese la basa del el triangulo"))
            altura=int(input("ingrese la altura del el triangulo"))
            resutadol=(base*altura)/2
            print(f"el area del el triangulo es:{resutadol}")
        case 3:
            altol=int(input("calcular el area del rectangulo  \n ingrese e altira del el rectangulo"))
            ancho=int(input("ingrese el ancho del el rectagunlo"))
            resutadol=altol*ancho
            print(f"el area del el rectagunlo es:{resutadol}")
        case 4:
            radio=(int(input("calcular el area del circulo \n ingrese el radio del el circulo")))
            resutadol=3.14*(radio**2)
            print(f"el area del el circulo es:{resutadol}")
        case _:
            print("salidad")
            break
        

