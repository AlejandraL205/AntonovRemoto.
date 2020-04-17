carga=0
distancia= float (input("distancia vuelo en kilometros "))
print ("Nacional (2)- Internacional (4)")

while carga<=337250:
    p=int(input("cantidad de peso"))
    if peso < 10 :
        c = carga + peso 
        if c <= 355000:
            if p > 100 and vuelo==1:
                valort=(p*4500+distancia*4000)*0.85
                print("valor del paquete:"valort)
            elif peso < 400 and distancia > 8000 and vuelo == 2:
                valort=(peso*4500+distancia*4000)*0.p
                print("valor del paquete: ", valort)   
        else:
            print("no puede abordar el avion")
    else :
        print("no se acepta el peso")       
else:
    print("no se puede enviar el paquete")  
