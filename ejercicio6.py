import math
numero=int(input("ingrese un nuemro "))
lista=[]
meta=numero
while meta >=1:
    if numero==0:
        print(0)
        break
    elif numero==1:
        print(1)
        break
    elif meta==1:
        lista.append(meta)
        break
    
    else:
        resibo=math.trunc(meta%2)
        meta=math.trunc(meta/2)
        lista.append(resibo)


if numero==0 or numero==1:
    pass
else:
    lon=len(lista)
    banario=""
    for i in range(lon-1,-1,-1):
        banario+=str(lista[i])
    print (banario)