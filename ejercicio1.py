figura="  "
contetor=2
for i in range(6,0,-1):
    batero=1
    for j in range(0,i):
        if(i<6):
            if(batero==1):
                figura=contetor*" "
                figura+="*" 
                batero=0
            else:
                figura+=" "
                figura+="*"   
        else:
            figura+="*"
            figura+=" "
    print(figura)
    figura=" " 
    contetor+=1

figura="  "
contetor=6
batera=1
for i in range(2,7):
    batero=1
    for j in range(0,i):
        if(i<6):
            if(batero==1):
                figura=contetor*" "
                figura+="*" 
                batero=0
            else:
                figura+=" "
                figura+="*"   
        else:
            if(batera==1):
                figura+=" "
                figura+="*"
                figura+=" " 
                batera=0
            else:
                figura+="*"
                figura+=" " 
    print(figura)
    figura=" " 
    contetor-=1


