t=0
while t<3:
    with open("maqiena.txt","r") as archivo:
        read=archivo.read()
    print(f"las opciones son {read}")
    texto=read.split(" ")
    dinero=int(input("ingrese el dinero "))
    opcion=input("escoje la opcion de compra ")
    print(f"su creido es {dinero}")
    if opcion==texto[0]:
        prrecico=int(texto[2])
        if dinero<prrecico:
            print("te falta mas creito")
        else:
            redsudato=dinero-prrecico
            if redsudato==0:
                print("difrute  su coprre")
            else:
                print(f"su cambi es {redsudato}")
        
    elif opcion==texto[3]:
        prrecico=int(texto[5])
        if dinero<prrecico:
            print("te falta mas creito")
        else:
            redsudato=dinero-prrecico
            if redsudato==0:
                print("difrute  su coprre")
            else:
                print(f"su cambi es {redsudato}")
    elif opcion==texto[6]:

        prrecico=int(texto[8])
        if dinero<prrecico:
            print("te falta mas creito")
        else:
            redsudato=dinero-prrecico
            if redsudato==0:
                print("difrute  su coprre")
            else:
                print(f"su cambi es {redsudato}")
    else:
        break

