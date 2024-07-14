with open("metamorfosis.txt","r") as archivo:
    read=archivo.read()

opcion=int(input("elelije una de las siguientes opciones \n 1 numero total del palabras \n 2 longitud media de las palabra \n 3 numero de oracines \n 4 plabra mas lagra"))

match opcion:
    case 1:
        texto=read.split(" ")
        lon=len(texto)
        print(f"la cantidad de palabra es {lon}")
    case 2:
        suma=0
        media=0
        texto=read.split(" ")
        lon=len(texto)
        for i in texto:
            suma+=len(i)
        media=suma/lon
        print(f"la media es  {media}")
    case 3:
        texto=read.split(".")
        lon=len(texto)
        print(f"la cantidad de oraciones es {lon}")
    case 4:
        con=0
        texto=read.split(" ")
        lon=len(texto)
        for i in texto:
            if len(i)>con:
                con=len(i)
                como=i
        print(f"la palabra mas larga es {como} con cantidada de lentra {con}")
