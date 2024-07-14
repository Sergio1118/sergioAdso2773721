with open("metamorfosis.txt","r") as archivo:
    read=archivo.read()
texto=read.split(" ")
for i in texto:
    cuo=texto.count(i)
    mesaje= f"esta palabra se repita es {i} {str(cuo)}\n "
    with open("repatidos.txt","a") as archivo:
        archivo.write(mesaje)

