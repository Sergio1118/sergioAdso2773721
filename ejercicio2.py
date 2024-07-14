palabra=input("ingrese una palabra")
lon=len(palabra)
j=-1
comtedor=0;
for i in range(0,lon):
    if palabra[i]==palabra[j]:
        comtedor+=1
    j=j-1

if comtedor==lon:
    print("es una palabra palidroma")
else:
    print("no es una palabra palidroma")