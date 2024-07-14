lista=[{"nombre":"balbasaur", "tipo": "planta"},{"nombre":"charmander", "tipo": "fuego"},{"nombre":"squirtle", "tipo": "agua"},{"nombre":"pikachu", "tipo": "eletrico"}]
pokemoA=int(input("escoja en el pokemon que va a ataquar \n 0 para balbasuar \n 1 para charmander\n 2  para squirtle \n 3  para pikachu "))
pokemoD=int(input("escoja en el pokemon que va a defeder \n 0 para balbasuar \n 1 para charmander\n 2  para squirtle \n 3 para pikachu "))

while 1<3:
    defase=int(input( " ingrese la defesa del el pokemon que va a recibir el ataka"))
    ataque=int(input("ingrese el ataque del el pokemon que va ataquer"))
    if ataque >=1 and ataque<=100 and defase >=1 and defase<=100:
        break
    else:
        print("la taque y la defesa tiene que esta en el rango 1 a 100")
        
    

if lista[pokemoA]["tipo"]=="planta":
    if lista[pokemoD]["tipo"]=="eletrico" or lista[pokemoD]["tipo"]=="planta":
        daño=50*(ataque/defase)*1
        print(f" el taque es nuutral daño es {daño} ")
    elif lista[pokemoD]["tipo"]=="fuego":
        daño=50*(ataque/defase)*0.5
        print(f" el taque es no eficas daño es {daño} ")
    elif lista[pokemoD]["tipo"]=="agua":
        daño=50*(ataque/defase)*2
        print(f" el taque es eficas  daño es {daño} ")
elif lista[pokemoA]["tipo"]=="fuego":
    if lista[pokemoD]["tipo"]=="eletrico" or lista[pokemoD]["tipo"]=="fuego":
        daño=50*(ataque/defase)*1
        print(f" el taque es nuutral daño es {daño} ")
    elif lista[pokemoD]["tipo"]=="agua":
        daño=50*(ataque/defase)*0.5
        print(f" el taque es no eficas daño es {daño} ")
    elif lista[pokemoD]["tipo"]=="planta":
        daño=50*(ataque/defase)*2
        print(f" el taque es eficas  daño es {daño} ")
elif lista[pokemoA]["tipo"]=="agua":
    if  lista[pokemoD]["tipo"]=="agua":
        daño=50*(ataque/defase)*1
        print(f" el taque es nuutral daño es {daño} ")
    elif lista[pokemoD]["tipo"]=="eletrico" or lista[pokemoD]["tipo"]=="planta":
        daño=50*(ataque/defase)*0.5
        print(f" el taque es no eficas daño es {daño} ")
    elif lista[pokemoD]["tipo"]=="fuego":
        daño=50*(ataque/defase)*2
        print(f" el taque es eficas  daño es {daño} ")
elif lista[pokemoA]["tipo"]=="eletrico":
    if lista[pokemoD]["tipo"]=="eletrico" or lista[pokemoD]["tipo"]=="fuego":
        daño=50*(ataque/defase)*1
        print(f" el taque es nuutral daño es {daño} ")
    elif lista[pokemoD]["tipo"]=="planta":
        daño=50*(ataque/defase)*0.5
        print(f" el taque es no eficas daño es {daño} ")
    elif lista[pokemoD]["tipo"]=="agua":
        daño=50*(ataque/defase)*2
        print(f" el taque es eficas  daño es {daño} ")


