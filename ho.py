a=0
while a<3:
    usuario=input("Dame tu usuario: ") 
    a=a+1 
    if (usuario)=="informatica":
        print("USUARIO CORRECTO")
        contra=input("Dame tu password: ") 
        if (contra)=="1234":
             print("Bienvenid@") 
             opc="s"
             while(opc=="s"):
                    i=0
                    while(i<=10):
                        print("Este es el ciclo: ",i)
                        i=i+1
                    opc=input("¿Deseas realizar la operacion s 0 n? ")
                    print("😘Hasta pronto😘")
             break 
        else:
            print("PASSWORD INCORRECTA") 
            if a==3:
                print("INTENTOS AGOTADOS") 
                break 
    else:
        print("USUARIO INCORRECTO") 
        if a==3:
            print("INTENTOS AGOTADOS")